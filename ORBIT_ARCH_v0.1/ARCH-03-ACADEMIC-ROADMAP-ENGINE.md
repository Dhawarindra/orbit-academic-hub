# ORBIT · ARCH-03 · ACADEMIC ROADMAP ENGINE

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Menentukan perilaku algoritma graf yang dapat diuji terpisah dari UI/SQLite dan tidak mengubah simulasi menjadi kelayakan aktual.

**Scope:** catalog validation, prerequisite expression, actual eligibility, SKS, satu overlay dan dampak penundaan.  
**Non-goals:** solver optimal, IRS submission, equivalence nama, full rebase, izin khusus/corequisite otomatis, serta UI admin.

**Sumber:** PRD-02 MAP-FR-001–009/011/012 dan MAP-BR-001–008; PRO-FR-002/004/005; GRD-FR-010/011; CORE-FR-003/004. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. Input dan output domain

Domain menerima DTO immutable, bukan row SQLite atau Flask request. Identitas course selalu `(curriculum_id, course_id)`; `term.sequence_no` urutan term eksplisit, sedangkan recommended personal semester adalah petunjuk sumber yang tidak diambil dari cohort.

| DTO | Schema konseptual | Validasi / pemilik |
| --- | --- | --- |
| CatalogInput | curriculum_id, program, applicability, rule_version, source, courses[{course_id,code,label,sks,prerequisite,availability}] | MAP validator; source synthetic dan batas demo terlihat |
| Expression | `{id,op:'and'/'or',children:[Expression...]}`; leaf `{id,op:'passed',course_id}`; `{id,op:'none',source_ref}`; `{id,op:'unsupported',raw,reason,refs:[]}` | Group nonempty; node IDs unik; unsupported raw dipertahankan sebagai data, tidak dieksekusi |
| ActualEvidence | enrollment_id, course binding, attempt, latest_final_revision_id, outcome passed/failed/unresolved, source | Hanya actual_final_revision terbaru per attempt; no score projection |
| PlanOverlay | selected course IDs→term sequence; personal_sks_cap nullable; chosen_or_branch expression_id→child_id; assumed_pass IDs; requested_delay | Satu scenario, source token current, semua refs sesuai curriculum |
| EligibilityResult | course_id, progress, planned, eligibility, reasons[{leaf_id,status,source_ref,attempt_ids}], rule_version, input_revisions, quality_flags | Tiga sumbu status berbeda; keluaran tidak menulis data |
| PlanResult | course totals by term, cap_kind, violations[], earliest_by_course, affected_courses[], assumptions[], unresolved[], input_revisions | Waktu bersyarat; bukan optimal plan / tanggal kelulusan |

`none` hanya boleh dibuat jika source secara eksplisit menyatakan tidak ada prasyarat. Missing expression menjadi `unknown/missing_rule`, bukan `none`. Profile unknown boleh memakai Grade personal; eligibility kurikulum nyata tidak dihitung. Jika pengguna memilih dataset demo yang cocok scope sintetis, hasil ditulis **kelayakan pada contoh sintetis**, tidak VERIFIED_OFFICIAL.

## 3. validate_catalog dan graph

Kontrak `validate_catalog(candidate) -> ValidatedCatalog | ValidationErrors`:

1. Validasi schema, IDs, SKS positif, metadata source/version/applicability, urutan term/availability.
2. Validasi tiap AST: node reachable, group tidak kosong, leaf dikenal atau unsupported yang dinyatakan; graph AST sendiri tidak cycle/shared node identity. Referensi course yang eksplisit wajib ada dalam curriculum yang sama.
3. Bentuk adjacency **prerequisite→dependent**, indegree dan reverse map dari seluruh leaf yang dikenal; edge course berulang dideduplikasi. DFS warna atau Kahn mendeteksi cycle; laporkan ID cycle/path dari DFS, bukan semua node yang hanya terblokir di belakang cycle.
4. Disconnected DAG sah. Self-loop ditolak. Cycle pada salah satu alternatif OR juga membuat dataset ditolak: validator struktur konservatif, bukan pemecah constraint OR.
5. Jika invalid, kembalikan field path/course IDs yang rusak. Service tidak mengaktifkan sebagian kandidat dan tidak mengganti katalog aktif. Unsupported semantic rule sah disimpan, tetapi eligibility/waktu yang bergantung padanya unknown.

Contoh error: `GRAPH_CYCLE [A,B,A]`; `DANGLING_REFERENCE course D leaf Z`; `SCOPE_MISMATCH curriculum c2 leaf(A,c1)`. Source tanpa bukti resmi diberi NEEDS_VALIDATION, bukan sekadar menambahkan kata resmi pada UI. FK tidak dapat menggantikan langkah validasi AST.

## 4. evaluate_eligibility dan actual evidence

| A | B | AND(A,B) | OR(A,B) |
| --- | --- | --- | --- |
| met | met | met | met |
| met | unmet | unmet | met |
| met | unknown | unknown | met |
| unmet | met | unmet | met |
| unmet | unmet | unmet | unmet |
| unmet | unknown | unmet | unknown |
| unknown | met | unknown | met |
| unknown | unmet | unmet | unknown |
| unknown | unknown | unknown | unknown |

Evaluasi semua leaf untuk alasan lengkap meskipun nilai operator bisa short-circuit. Leaf passed: applicable explicit actual passed→met, applicable failed→unmet, belum ada actual/hasil unresolved/binding ambigu→unknown. Enrollment aktif dan skor komponen yang lengkap sekalipun tidak menjadi final otomatis. `AND(A met,OR(B unmet,C unknown))=unknown`, dengan alasan per leaf.

Riwayat repeat tetap semua attempt. P0 tidak memilih highest/latest antar attempt untuk menebak aturan. Bila beberapa attempt relevan memiliki konflik dan tidak ada rule agregasi applicable, leaf unknown dengan reason `attempt_policy_unresolved`. Fixture boleh memiliki aturan sintetis eksplisit seperti “salah satu attempt confirmed passed memenuhi leaf”; aturan itu diberi version/source dan hanya berlaku fixture. Revisi dalam **attempt yang sama** memakai record terbaru, bukan mempertahankan pass yang telah dikoreksi failed.

Progress course dan eligibility tidak digabung: not_started bila belum ada pengambilan; active bila enrollment berjalan; passed/failed hanya dari actual yang applicable. Konflik attempt memberi progress label “perlu verifikasi” pada view model (nilai progress konservatif + quality flag), tidak memilih passed. Planned adalah flag overlay terpisah. Lihat juga keterbatasan repeat di OD-02.

## 5. SKS dan simulate_delay

`summarize_credits(snapshot,plan) -> {completed,active,planned_by_term,excluded,coverage,cap_warnings}`: completed hanya course passed applicable, sekali per course; active menghitung pengambilan aktif unik, planned menghitung selected course unik per term. Ketiga metrik **tidak dijumlahkan menjadi total kelulusan** karena himpunan bisa overlap. Repeat/personal offering tanpa SKS terikat masuk excluded, bukan 0 SKS. SKS course berasal dari binding curriculum attempt; mengganti profil tidak menulis ulang history.

`validate_plan` mempertahankan pilihan yang konflik dan memberi alasan. A3+B4=7, personal cap 6→warning personal. Tidak ada cap resmi jika policy tidak tersedia. Cap tidak otomatis menggeser course, dan simulasi tidak mengklaim memenuhi semua constraints.

Kontrak `simulate_delay(catalog, actual, overlay, horizon) -> PlanResult`:

1. Pastikan graph valid dan scenario current. Baseline plan serta delay hanya overlay; academic_term dan enrollment tidak diedit.
2. Untuk setiap OR yang diperlukan untuk menghitung waktu, gunakan **chosen child** eksplisit. Pilihan ini harus arg milik OR tersebut. Tanpa pilihan, earliest cabang terdampak unknown; jangan memperlakukan OR sebagai AND atau memilih paling mudah diam-diam.
3. Susun dependent closure dan traversal topological. AND menunggu maksimum earliest semua child; OR menunggu chosen child. Leaf actual passed dapat memenuhi prerequisite sebelum rencana term mendatang; course yang belum passed hanya diperlakukan assumed_pass jika ditandai eksplisit pada scenario.
4. Untuk edge prasyarat terpilih pada fixture tanpa corequisite: earliest anak ≥term lulus asumsi parent+1. Actual pass tanpa tanggal term yang jelas dapat memenuhi eligibility, tetapi tidak dipakai mengarang tanggal historis; earliest masa depan dibatasi start term yang dipilih pengguna.
5. Availability `every_term` sintetis dapat langsung memakai earliest; `known_terms`/ganjil-genap sintetis mencari slot dalam horizon eksplisit. Unknown availability memberi unknown dan alasan. Tidak menemukan slot dalam horizon berarti `no_slot_in_horizon`, **bukan mustahil selamanya**.
6. Kembalikan pergeseran dan cap warnings, assumed passes/chosen branches/availability source. Plan yang melampaui cap tidak “diperbaiki” oleh solver tersembunyi.

Golden: A3→B4→C3, baseline A1/B2/C3, assumed pass tiap term dan availability setiap term. Delay A→2 menghasilkan B3/C4. Jika availability B unknown, waktu B dan C unknown; eligibility aktual tetap dapat dievaluasi secara terpisah. D membutuhkan OR(A,E); bila chosen=A, waktu mengikuti A dengan label asumsi; tanpa chosen, waktu D unknown walau struktur graf valid.

## 6. Service boundary dan lifecycle scenario

| Operasi | Precondition / input | Postcondition / output | Error / test |
| --- | --- | --- | --- |
| activate_catalog | Candidate lengkap, expected token, op_id | Immutable catalog baru hanya setelah semua valid; record lama utuh | GRAPH_INVALID/SCOPE_MISMATCH; MAP-T-007/012, DDP-T-02 |
| read_roadmap | Scope/demo catalog dipilih atau unknown | List seluruh course/edge/reason; unknown scope menghasilkan empty action, tidak leak dataset lain | MAP-T-001/002/003/008/009 |
| save_plan | Current scenario, overlay refs valid, expected token | Overlay tersimpan, actual tetap; warnings tersimpan sebagai hasil hitung saat read | STALE_SCENARIO/INVALID_INPUT; MAP-T-004/005 |
| read_stale_plan | base_source_revision lama | Banner + daftar change_log fields/IDs sejak base, nilai lama tidak current | MAP-T-006 |
| reset_scenario | Token workspace current; confirm tindakan reset overlay | Seluruh plan, target dan score overlay kosong; base terbaru; actual utuh | MAP-T-011, INT-T-003 |

Reset scenario berbeda dari reset workspace. Pilih ulang memakai baseline baru dan form kosong; tidak mempertahankan pilihan lama melalui full rebase. Change_log dipakai menjelaskan bahwa sumber berubah, bukan menyimpan snapshot grade mentah di log. Service stale hanya mengembalikan pilihan draft lama, token dan alasan perubahan. Karena snapshot hasil derived tidak disimpan, service tidak merekonstruksi angka lama dari input baru; hasil hitung ditahan sampai reset/pilih ulang. Halaman yang sudah terbuka boleh menampilkan hasil lamanya dengan revision asal, tetapi tidak dianggap current setelah perubahan diketahui.

## 7. Kompleksitas dan batas

V=course, E=edge unik, X=seluruh node AST (termasuk operator), H=jumlah term dalam horizon, A=attempt. Dengan dictionary lookup rata-rata O(1): validasi O(V+E+X), ruang O(V+E+X); cycle DFS O(V+E). Satu read eligibility seluruh katalog O(A+X+V), dengan evidence dipetakan sekali, bukan query per leaf. Credit totals O(A+V). Simulation satu pilihan OR per node O(V+E+X) untuk every_term; pencarian availability terbatasi menambah O(VH). Ruang O(V+E+X+H) bila term lookup bersama; hasil per-course/per-term paling banyak O(V+H) untuk satu term penempatan per course.

O(X) tidak disederhanakan menjadi jumlah leaf bila AST punya chain operator satu anak. Angka biaya mengasumsikan panjang ID/data terbatas dan bukan enumerasi seluruh kombinasi OR. Batas fixture P0 6–12 course; benchmark 100 node/300 edge adalah dataset uji terpisah.

Alternatif optimasi kombinatorial, auto-mapping alias dan graph renderer sebagai business engine ditolak karena menambah asumsi yang tidak dijamin sumber. Python harus mengimplementasikan validasi/evaluasi dan dapat menjelaskan traversal.

## Risiko, dependensi, dan bukti terbuka

Dua jenis unknown—data aktual belum ada dan aturan unsupported—harus punya reason berbeda. Retake/applicability perlu fixture review; tanpa itu engine mengembalikan unknown. Tidak ada dependency GDE/closeout.

**Traceability:** MAP-AC/T-001–009/011/012/101–103; DDP-T-01/02/13; INT-T-003/010/013; PRO-T-005. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** OD-02 menyepakati isi fixture, horizon dan repeat rule sintetis; RV-02 tetap open untuk katalog nyata, tidak memblokir rancangan demo. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
