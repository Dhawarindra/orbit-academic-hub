# ORBIT — Glossary & Decision Log

Versi: **v0.2.1 DDP1 Errata** · Tanggal: **18 November 2026 (Asia/Jakarta)** · Owner: **Product Lead** · Status: untuk review manusia.


## Aturan canon

PRD-00 memiliki definisi produk lintas modul; dokumen ini register istilah pendukungnya. Bila domain menyimpang, perbaiki canon dan seluruh konsumen sebelum publish baseline. Kepemilikan di sini berarti domain yang menerima write, bukan pilihan service/database. Semua ID internal immutable; display name, kode dan label tidak dipakai mengganti identitas record.

## Entitas dan ownership

| Istilah | Owner canon | Identitas / relasi | Definisi dan batas |
| --- | --- | --- | --- |
| User / local owner_scope | AUTH | user_id internal immutable; local owner_scope stabil pada demo | P0 identitas workspace sintetis, bukan autentikasi; akun multiuser P2 tidak otomatis mahasiswa terverifikasi |
| AcademicProfile | PRO | profile_id; satu per user | program, cohort self-reported, curriculum version, active term; tanpa credential |
| Program / cohort | MAP taxonomy / PRO pilihan | program_id; entry_year | Angkatan tidak menentukan kurikulum secara otomatis |
| CurriculumVersion | MAP | curriculum_version_id | Applicability program/angkatan/transition dan sumber; dapat superseded |
| Course | MAP | course_id | Identitas stabil; nama atau kode tampilan dapat punya alias |
| CurriculumCourse | MAP | curriculum_version_id + course_id | SKS, kelompok, semester rekomendasi, prerequisite rule sesuai versi |
| AcademicTerm | MAP katalog / PRO pilihan | term_id | Periode akademik; berbeda dari semester_index personal |
| CourseOffering | MAP | offering_id | Course + term + kelas + metadata pengajar opsional; manual user-defined boleh privat |
| Enrollment / attempt | PRO | enrollment_id / attempt_id | User mengambil offering; pengulangan tetap record baru |
| BRPVersion | GRD | brp_version_id | Struktur dan rule penilaian per offering/class/period; tidak universal |
| Assessment | GRD | assessment_id | Parent/leaf, bobot lokal, max_score, topic dan due_at; SCH mengedit deadline canon ini |
| GradeEntry | GRD | entry_id | Skor komponen yang diketahui atau unknown, dengan provenance |
| ActualFinalGrade | GRD | final_id | Hasil akhir yang dinyatakan aktual; manual tetap user_reported; bukan Prediction |
| GradePrediction | GRD | prediction_id | Hasil turunan matematis dengan inputs/rule/scenario; tidak final |
| Target | PRO profil / GRD course | target_id | Keinginan pribadi; tidak sama dengan rule kelulusan |
| SimulationScenario | MAP (course plan); GRD memakai overlay | scenario_id | Satu container berisi base_revision dan overlay course/score; tidak clone actual |
| Meeting / PreparationBlock | SCH | meeting_id / block_id | Jadwal kelas vs alokasi kerja; deadline tetap pada Assessment |
| WorkEstimate / Capacity | SCH | owner+assessment / owner+week | Sisa jam dan jam tersedia; unknown ≠ nol |
| Topic | MAP curated taxonomy | topic_id | Konsep untuk mapping assessment, tips dan resource; nama bebas bukan mapping terverifikasi |
| Contribution | SNR atau VLT menurut purpose | contribution_id | Copy data dipilih dengan consent; tidak auto-sync workspace |
| Resource | VLT | resource_id | Metadata link Drive; file tetap milik sumber eksternal |
| ContributorProfile | VLT | contributor_id | Link internal ke user dibatasi; public credit opt-in terpisah |
| Competency / mapping | CAR | competency_id / mapping_id | Hubungan kurasi course-kompetensi; tidak bukti skill pengguna |
| GuidanceItem / Closeout | GDE | item_id / closeout_id | Alasan+CTA hasil turunan; snapshot finalisasi pengguna |
| Bookmark / Feedback | SUP | bookmark_id / feedback_id | Bookmark unik owner+resource; feedback privat |
| Consent / IntegrationGrant | AUTH | consent_id / grant_id | Tujuan dan izin akses terpisah dari login/atribusi |

**Offering personal:** bila katalog offering resmi belum ada, pengguna membuat user-defined offering scoped owner dengan course_ref opsional dan term. Tidak dipromosikan sebagai offering bersama tanpa kurasi. Struktur ini memungkinkan grade/schedule bekerja saat kurikulum belum lengkap. Setelah mapping resmi tersedia, lakukan preview mapping, jangan merge berdasar nama.

**Target ownership:** PRO memiliki target profil umum, GRD target course/grade, MAP target rencana semester. Semua menggunakan identitas Target dan atribut scope yang sama; satu record hanya punya satu writer sesuai scope. Tidak ada target duplikat untuk dashboard.

## Status dan provenance

| Sumbu | Nilai canon | Makna |
| --- | --- | --- |
| Evidence confidence | VERIFIED_OFFICIAL / VERIFIED_SECONDARY / PRODUCT_ASSUMPTION / NEEDS_VALIDATION | Tingkat sumber klaim, bukan mutu mahasiswa |
| Grade component state | unknown / actual_input | Diketahui dari input pengguna; actual_input tidak berarti sumber kampus terverifikasi |
| Final provenance | actual_user_reported / official_verified | Hasil dinyatakan aktual oleh pengguna vs diambil/divalidasi melalui sumber sah; official_verified belum tersedia P0 |
| Derived result | prediction / scenario | Kalkulasi dari data vs hasil overlay skenario |
| Actual progress | not_started / active / passed / failed / unresolved | Diturunkan dari riwayat aktual dan policy cocok; bukan proyeksi |
| Eligibility | met / unmet / unknown | Hasil prasyarat berdasarkan scope dan sumber; bukan IRS disetujui |
| Plan flag | planned / unplanned | Preferensi skenario; bisa bersamaan dengan active/passed |
| Freshness | current / stale / unavailable | Sesuai input_revision/rule_version atau belum dapat dihitung |
| Content visibility | draft / pending / published / hidden / withdrawn / rejected | Public read hanya published; draft personal tetap owner-only |
| Data sensitivity | Public / Private / Restricted | Published metadata / workspace / credential-linkage-consent-raw contribution |

Source confidence pada official document hanya membuktikan isi yang diperiksa. Policy binding perlu applicability yang tepat; source official lama atau berbeda scope dapat tetap tidak aktif. User menekan “saya yakin” tidak mengubah status menjadi VERIFIED_OFFICIAL.

## Kontrak lintas modul

Perubahan sumber membawa `event_id`, `entity_id`, `revision`, `occurred_at`, `owner_scope`, `source_ref` dan `scenario_id` nullable. Hasil turunan mencatat daftar `input_revisions`, `rule_version`, `calculated_at`, `uncertainty` dan `quality_flags`. Penamaan ini kontrak konsep, bukan endpoint final.

| Perubahan | Pemilik write | Konsumen | Invariant |
| --- | --- | --- | --- |
| ProfileChanged / CurriculumBindingChanged | PRO | MAP, GRD, SCH, CAR | Preview migrasi; historic credits/rules tidak ditimpa |
| AssessmentDueChanged | GRD; editor dapat berasal SCH | SCH, GDE | Satu assessment_id, tidak ada deadline clone |
| GradeEntryChanged | GRD | Prediction, GDE, UX | Tidak mengubah actual final/passed |
| ActualFinalGradeChanged | GRD; konfirmasi per course P0 atau closeout P2 | MAP, GPA, GDE, UX | Provenance terlihat; scenario tidak memicu event ini |
| WorkEstimateChanged | SCH | Workload, GDE | Nilai/skor tidak ikut diubah |
| ResourceVisibilityChanged | VLT | SUP, GDE, PUB bila credit | Read memeriksa visibility meskipun index stale |
| ConsentRevoked / DeletionRequested | AUTH | SNR, VLT, semua data owner | Blok projection/akses dulu, purge kemudian |

MVP dapat merealisasikan kontrak dengan pemanggilan lokal atau refresh saat dibuka. Tidak perlu message broker. Repeated event dengan revision yang sama tidak membuat duplicate; revision lebih lama tidak menimpa terbaru. Konflik concurrent write meminta review diff, bukan last-write-wins diam-diam pada nilai/closeout. Error konsumen membuat result stale; sumber tersimpan tetap dapat dibuka.

## Siklus dan batas nilai

BRP draft dapat disimpan walau belum valid; hanya valid linear tree yang dihitung. Unknown tidak sama dengan nol. Final actual membutuhkan konfirmasi sendiri. Skenario terpisah dengan base_revision; reset tidak menghapus actual. Closeout final adalah catatan pengguna, bukan persetujuan akademik. Semester dengan unresolved tetap menampilkannya dan tidak memberi status lulus otomatis.

## Keputusan

Baris D-01–D-15 mempertahankan keputusan historis v0.1. Prioritas rilis dan mode operasionalnya disupersesi secara eksplisit oleh D-16–D-21 di bawah; detail algoritma, privasi dan identitas yang tidak berubah tetap berlaku.

| ID | Topik | Keputusan / rationale | Status | Dampak |
| --- | --- | --- | --- | --- |
| D-01 | Scope dan bahasa | Orbit independen; Fasilkom UI sebagai target awal; branding belum final; dokumen Indonesia | Ditetapkan brief | Semua PRD |
| D-02 | Academic source binding | Verified source content ≠ active policy untuk semua user; ikat program/cohort/version/term; unknown jika tidak cocok | PRODUCT_ASSUMPTION konservatif | PRO/MAP/GRD |
| D-03 | MVP modular | Baseline P0 manual; P1 kating analytics/self-submit/career; P2 integrasi; Tiny perlu change log | Usulan menunggu rubrik | CORE + indeks |
| D-04 | Provenance dan actual | unknown, actual_input, actual_user_reported, official_verified dan scenario berbeda; official_verified belum tersedia P0 | Ditetapkan pemisahan dari brief | PRO/MAP/GRD/GDE |
| D-05 | Perhitungan linear | Basis point bobot; leaf-only; full precision sebelum rounding; model non-linear ditahan; GPA policy-bound | PRODUCT_ASSUMPTION | GRD |
| D-06 | Beban akademik | Jam tersisa/capacity dan coverage; bobot assessment sebagai salience terpisah; threshold 0,8/1 adalah usulan | PRODUCT_ASSUMPTION | SCH/GDE |
| D-07 | Privasi agregat | P1 gate k=10 donor, fixed cells, n-band, rounding, no drill-down, review dan withdrawal; bukan jaminan anonimitas | Usulan memerlukan Privacy Reviewer | SNR/AUTH |
| D-08 | Vault link-only | Curated P0; submit P1; manual access checks; anonymous credit default; no hosting Drive | Ditetapkan prinsip brief, detail usulan | VLT/PUB/SUP |
| D-09 | Navigator | P1 mapping kurasi, reason eksplisit, rank deterministik; tidak menyimpulkan kompetensi atau outcome pekerjaan | PRODUCT_ASSUMPTION | CAR/GDE |
| D-10 | Guidance dan closeout | Max 3 tindakan, no side effect until apply, versioned closeout, no compulsory donation | PRODUCT_ASSUMPTION | GDE/GRD/MAP |
| D-11 | UI | P0 tema terang konsisten; dark P1; Figma arah visual; data ilustrasi bukan seed akademik | PRODUCT_ASSUMPTION berdasarkan observasi | UX/seluruh domain |
| D-12 | Auth dan lifecycle | Akun Orbit lokal; recovery code; retention aktif delete≤7d, backup≤30d, audit minimal90d, export≤24h; integrasi off | Usulan sebelum deployment; bukan legal claim | AUTH/SNR/VLT |
| D-13 | Search/support | Metadata-only search; query tanpa histori personal; bookmark owner tunggal; feedback in-app; digest P2 | PRODUCT_ASSUMPTION | SUP/PUB |
| D-14 | Quality targets | Latency/usability target adalah target uji prototipe, bukan hasil atau jaminan kapasitas produksi | PRODUCT_ASSUMPTION | Seluruh NFR |
| D-15 | Tanpa integrasi tersembunyi | Tidak ada scraping tanpa izin, password proxy, API akademik diasumsikan, ML wajib atau data komunitas rekaan | Ditetapkan brief | CORE/AUTH/GRD/SNR |

Semua keputusan v0.1 bertanggal 18 November 2026 (Asia/Jakarta), owner Product Lead kecuali domain reviewer disebut. “Ditetapkan brief” berarti bersumber dari instruksi pengguna, bukan otoritas UI. Keputusan berstatus usulan belum disetujui manusia. Perubahan berikutnya menambahkan tanggal, opsi yang dipilih, alasan, owner role dan requirement terdampak; tidak menghapus jejak keputusan lama.

## Pertanyaan terbuka utama

RV-01 aturan tugas CLOSED; RV-14 kapasitas aktual dan RV-15 konsep baru serta RV-16 validasi masalah open; RV-02 curriculum applicability; RV-03 BRP nyata; RV-04 policy GPA/retake/special grade; RV-05/06 izin SSO/SLCM; RV-07 privacy publication gate; RV-08 rights resource; RV-09 career mapping; RV-10 hosting/retention; RV-11 team identities; RV-12 usability/contrast; RV-13 source changes. Lihat [Research Register](RESEARCH-AND-VALIDATION-REGISTER.md) untuk owner, dampak, default dan bukti penutup.

## Keputusan revisi DDP1 —18 November 2026

Semua keputusan berikut merupakan rekomendasi analisis pada audit ini, bukan approval Asdos atau bukti aplikasi sudah dibangun. Owner Product Lead dengan reviewer domain; review kapasitas 18–19 Nov.

| ID | Keputusan dan dasar | Supersesi terbatas | Dampak |
| --- | --- | --- | --- |
| D-16 | Panduan resmi SRC-11 menjadi sumber aturan tugas; deadline 10 Des 2026 23.59 WIB dan enam bobot rubrik dicatat | Menutup bagian ketidakpastian rubrik pada D-03/RV-01 | Semua PRD/governance; kapasitas aktual tetap RV-14 |
| D-17 | P0 Roadmap+Grade Rescue+Dashboard dengan profil/guard minimum; P1 opsional; P2 semua fitur yang ditunda, bukan dibuang | Prioritas D-03, D-07/08/09/10/13 dan dark theme D-11 | Daftar FR di MVP Scope/RTM; identitas UI dan algoritma lama tetap |
| D-18 | Python utama; rekomendasi monolit Flask/Jinja, SQLite, unittest; versi runtime dipilih setelah smoke check tim | Mengisi keputusan teknologi yang sebelumnya belum tersedia | Python memiliki semua perhitungan/validasi/state, HTML/CSS/JS hanya presentasi |
| D-19 | Demo lokal satu owner_scope sintetis dengan export/reset; akun multiuser menjadi P2 | Mode rilis D-12, bukan penghapusan kontrol keamanan akun | AUTH-FR-014/015 baru; seluruh fitur akun/consent tetap disimpan sebelum penggunaan data nyata |
| D-20 | Dashboard membaca MAP/GRD langsung; konfirmasi aktual per course tidak membutuhkan semester closeout | Jalur dependency pada D-10, tanpa mengubah semantik aktual/simulasi D-04 | CORE-FR-002/005, GRD-FR-010/BR-010, UX-FR-002, interface semua konsumen |
| D-21 | Satu skenario, dataset kecil dan struktur BRP dikunci setelah skor; stale memakai reset/pilih ulang | Menunda subkemampuan rebase/migrasi; invariants D-02/D-05 tetap | MAP-FR-006; GRD-FR-001/020; daftar/list sebagai UI dasar |

Aturan tugas bukan kebijakan akademik mata kuliah. SRC-11 tidak menutup RV-02/03/04, tidak mengizinkan SSO/SLCM, dan tidak mewajibkan fitur tertentu, framework, deployment publik, jumlah commit atau angka nilai tertentu.

## D-22 — Errata capability dan handoff, 18 November 2026

Review independen menemukan empat label prioritas bisnis yang belum mengikuti FR: UX-BR-001/002, PUB-BR-006 dan SUP-BR-001. Label tersebut dikoreksi, bukan reprioritisasi FR: dark mode dan Career Navigator tetap P2, contact/feedback P2, search P1. Navigasi mengikuti capability manifest; fitur nonaktif tidak memperoleh aksi aktif hanya karena muncul dalam desain atau journey lengkap. Scope awal tetap 48 FR P0 dan gate terkait; aktivasi P1/P2 memerlukan keputusan scope eksplisit yang tercatat. D-01–D-21 tetap sebagai riwayat, dengan supersesi yang sudah dijelaskan.

Owner: Product Lead/tim. Dasar: SRC-16 review independen dan pengecekan langsung terhadap v0.2. Keputusan ini menutup kontradiksi dokumentasi; tidak menutup RV-14/15 atau membuktikan kesiapan runtime. Status tetap CONDITIONAL GO untuk desain arsitektur. Lihat [errata](PRD-v0.2.1-ERRATA.md).
