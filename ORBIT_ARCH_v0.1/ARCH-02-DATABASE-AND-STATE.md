# ORBIT · ARCH-02 · DATABASE AND STATE

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Memberi skema fisik dan aturan perubahan state yang cukup konkret untuk mencegah kehilangan histori, pencampuran scope, dan stale write.

**Scope:** 17 tabel SQLite lokal; hanya entitas P0; lifecycle, optimistic concurrency, export/reset dan histori actual.  
**Non-goals:** ORM, event sourcing, DB multiuser/production, migrasi BRP penuh, restore akun atau import ekspor melalui UI.

**Sumber:** PRO-FR-001–005; MAP-FR-001/006/007/011/012 dan MAP-BR-001/007/008; GRD-FR-001/010/011; AUTH-FR-014/015; CORE-BR-003/005/006. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. State canon dan kepemilikan

| Istilah | Makna operasional | Bukan |
| --- | --- | --- |
| actual | Input skor atau hasil final yang dilaporkan eksplisit; final tetap entitas berbeda dari komponen | Hasil prediksi, verifikasi kampus, atau angka nyata pada demo |
| predicted | Output numerik model dari input/asumsi yang dinyatakan | ActualFinalGrade |
| what-if | Output dengan overlay scenario dan banner; output model tanpa kelulusan resmi | Update GradeEntry atau attempt aktual |
| unknown | Entitas/input ada atau diharapkan, tetapi nilainya/aturannya belum diketahui | Angka 0 atau otomatis unmet |
| missing | Record yang diperlukan tidak ditemukan, misalnya belum ada BRP | Unknown yang disimpan sebagai string numerik |
| not_applicable | Aturan/metrik tidak berlaku pada konteks, dengan reason eksplisit | Jalan pintas mengabaikan input invalid |
| stale | Output/preview/scenario memakai epoch/revision sumber yang berbeda | Error data hilang atau current |

State ini orthogonal: nilai bisa unknown dan scenario-nya stale. Setiap read model membawa `dataset_mode=synthetic`, provenance, validity/freshness, dan alasan. Semua tabel berada dalam satu owner scope lokal; ini isolasi namespace, bukan klaim authorization multiuser. Skor/hasil user-reported dalam demo tetap `is_synthetic=true`.

## 3. Relasi konseptual dan aliases

Workspace → Profile; Profile memilih AcademicTerm/CurriculumSnapshot. CurriculumSnapshot × Course → CurriculumCourse; Offering mengacu term dan pasangan curriculum/course atau personal fallback. Enrollment → Offering; Enrollment → BRPVersion → AssessmentNode → Score. Enrollment → ActualFinalRevision (banyak revisi) dan CourseTarget (maksimum satu). Workspace → Scenario (maksimum satu). ChangeLog dan OperationReceipt mendukung perubahan atomik, bukan broker.

`CurriculumVersion` PRD dipetakan ke `curriculum_snapshot`; `GradeEntry` ke `assessment_score`; `ActualFinalGrade` adalah revisi terbaru per enrollment dalam `actual_final_revision`; `SimulationScenario/TargetScenario/AcademicPlanScenario` ditampung satu aggregate `scenario` dengan tiga overlay berbeda. Nama fisik tidak mengganti identitas requirement. Course ID stabil; SKS/nama tampilan berada pada CurriculumCourse versi tertentu.

## 4. Skema fisik normatif rancangan

Ini **spesifikasi schema**, belum SQL migrasi yang dieksekusi. Semua kolom NOT NULL kecuali diberi `?`. `T=TEXT`, `I=INTEGER`. IDs TEXT UUID/fixture ID nonkosong. Timestamp TEXT RFC3339 UTC, UI Asia/Jakarta. `J=TEXT JSON` divalidasi Python (tidak mewajibkan SQLite JSON extension). `D=TEXT decimal kanonik` dari parser ARCH-04, tidak REAL. PK/UNIQUE membuat indeks otomatis. FK memakai RESTRICT secara default; reset menghapus berurutan dalam satu transaksi, tidak mengandalkan cascade global. Kolom JSON tak punya FK internal: service wajib memvalidasi seluruh ID terhadap snapshot dalam transaksi.

| Tabel | Kolom, tipe dan kunci | CHECK / UNIQUE / relasi wajib |
| --- | --- | --- |
| workspace | singleton I PK; owner_scope T UNIQUE; epoch T; state_revision I; source_revision I; schema_version I; last_reset_receipt J? | singleton=1; revision≥0; source_revision≤state_revision; schema_version=1; owner stabil sepanjang reset/restart |
| profile | owner_scope T PK/FK workspace(owner_scope); program T?; cohort T?; curriculum_id T? FK curriculum_snapshot; active_term_id T? FK academic_term; checkpoint T; timezone T | checkpoint dalam scope/term/enrollment/done; timezone default Asia/Jakarta; unknown disimpan NULL, bukan program rekaan |
| academic_term | term_id T PK; academic_year T; part T; sequence_no I UNIQUE; label T; starts_on T?; ends_on T? | part ganjil/genap/other; sequence_no≥1; urutan eksplisit, tidak dihitung dari angkatan; tanggal ISO bila ada, ends≥starts divalidasi service |
| course | course_id T PK; code T UNIQUE | Identitas stabil; alias/nama tidak dipakai untuk equivalence |
| curriculum_snapshot | curriculum_id T PK; program T; version T; applicability J; source J; rule_version T; content_hash T; status T | status active/superseded; UNIQUE(program,version); immutable setelah aktivasi; hanya dataset valid masuk tabel |
| curriculum_course | curriculum_id T FK; course_id T FK; label T; sks I; category T; recommended_sequence I?; prerequisite J; availability J; source J; rule_version T | PK(curriculum_id,course_id); sks>0 dan typeof integer; recommended_sequence NULL atau≥1; composite FK untuk referensi pasangan dari offering; AST dan scope diverifikasi Python |
| grade_policy | policy_id T PK; version T; applicability J; thresholds J; source J; content_hash T | Immutable; threshold decimal string, rentang tidak overlap/gap; scope offering/kelas/term explicit; tidak ada policy official default |
| offering | offering_id T PK; owner_scope T FK workspace; term_id T FK academic_term; curriculum_id T?; course_id T?; personal_label T; class_label T?; source J | Kedua curriculum/course NULL atau keduanya terisi; composite FK ke curriculum_course; UNIQUE(owner_scope,offering_id); personal offering tidak ditebak mapping dari nama |
| enrollment | enrollment_id T PK; owner_scope T; offering_id T; attempt_no I; attempt_key T; status T; source J | FK(owner_scope,offering_id)→offering; UNIQUE(owner_scope,offering_id); UNIQUE(owner_scope,attempt_key); attempt_no≥1; status active/completed; key kanonik [curriculum,course,term,attempt] atau [personal_offering,attempt] |
| brp_version | brp_id T PK; enrollment_id T FK enrollment; version_no I; status T; locked I; source J; rule_version T; unsupported_rules J | version_no≥1; locked 0/1; status active/superseded; UNIQUE(enrollment_id,version_no); partial UNIQUE(enrollment_id) WHERE status='active' |
| assessment_node | node_id T PK; brp_id T FK brp_version; parent_id T?; kind T; label T; weight_bp I; max_score D?; granularity D?; position I | UNIQUE(brp_id,node_id); composite FK(brp_id,parent_id)→assessment_node; kind group/leaf; weight_bp 0..10000; position≥0; group max/granularity NULL, leaf keduanya wajib; partial UNIQUE(brp_id) WHERE parent_id IS NULL |
| assessment_score | node_id T PK/FK assessment_node; earned D?; source J; saved_revision I | earned=NULL atau valid 0..max di Python; hanya leaf BRP aktif; saved_revision≥1; satu nilai current per leaf, histori final terpisah |
| actual_final_revision | final_revision_id T PK; enrollment_id T FK; revision_no I; supersedes_id T? UNIQUE FK ke tabel ini; numeric_value D?; letter_value T?; policy_id T? FK grade_policy; outcome T; source J; correction_reason T?; committed_revision I; occurred_at T | UNIQUE(enrollment_id,revision_no); revision_no≥1; outcome passed/failed/unresolved; revision_no 1→supersedes NULL, >1→supersedes dan reason wajib; angka 0..100; revision chain satu enrollment diperiksa service |
| course_target | enrollment_id T PK/FK enrollment; numeric_target D?; letter_target T?; policy_id T? FK grade_policy; source J; saved_revision I | Tepat satu target numeric/letter; numeric 0..100; letter tanpa policy tetap unresolved, tidak dikonversi diam-diam; tidak menyimpan target global IPK |
| scenario | singleton I PK; scenario_id T UNIQUE; owner_scope T UNIQUE FK workspace; base_epoch T; base_source_revision I; scenario_revision I; plan J; score_overlay J; target_overlay J; assumptions J | singleton=1; revision≥0; satu overlay aktif; plan/score/target tidak mengandung actual final; semua foreign IDs/type/range diverifikasi service |
| change_log | event_id T PK; owner_scope T FK; epoch T; state_revision I; source_revision I; entity_type T; entity_id T; scenario_id T?; event_type T; source_ref T?; occurred_at T; details J | Satu event ringkas per operasi; UNIQUE(epoch,state_revision); details hanya changed fields/IDs, bukan skor mentah; tak dipakai merekonstruksi histori final |
| operation_receipt | epoch T; operation_id T; request_hash T; result J; committed_state_revision I; occurred_at T | PK(epoch,operation_id); hanya receipt sukses; result menyimpan IDs/revision/status tanpa token/secrets; payload hash dari jenis operasi+input kanonik+expected token |

### 4.1 Indeks tambahan dan invariant yang bukan SQL CHECK

Indeks `offering(term_id)`, `assessment_node(brp_id,parent_id,position)`, `actual_final_revision(enrollment_id,revision_no DESC)` (UNIQUE prefix sudah dapat memenuhi pencarian; jangan duplikasi bila query plan cukup), dan `change_log(epoch,state_revision)` melalui UNIQUE. Untuk 6–12 course tidak perlu indeks semua kolom atau cache hasil.

Service menegakkan: tepat satu root BRP group dengan weight 10000; setiap group punya ≥1 anak dan total 10000; leaf tanpa anak; tree reachable penuh, tanpa cycle; sumber BRP cocok enrollment/term/kelas atau labelled personal draft; offering/attempt scope tidak dicampur; history duplicate attempt ditolak walau offering_id berbeda untuk course/term/attempt sama. FK course tidak cukup untuk prerequisite JSON, sehingga validator AST wajib sebelum aktivasi. Profil berubah tidak menulis ulang binding attempt historis.

## 5. Revision dan unit of work

Token form/command: `{epoch, state_revision}`. Setiap write sukses menaikkan state_revision tepat 1. Perubahan sumber (profil akademik, katalog aktif, enrollment, BRP, skor, target course, actual final) juga menaikkan source_revision tepat 1; perubahan overlay hanya menaikkan scenario_revision. Memasukkan target course konservatif membuat scenario stale; ini biaya sederhana dibanding dependency tracking per field.

`scenario.stale := base_epoch != workspace.epoch OR base_source_revision != workspace.source_revision`. Skenario stale boleh dibaca dengan banner, tetapi tidak dihitung ulang seolah current atau diedit sebelum reset/pilih ulang. Tidak ada rebase otomatis P0. Read model memuat token input; halaman lama tetap bertanggal/revision lama dan server menolak submit usang. P0 tidak menjanjikan live push antar tab.

Urutan write konseptual:

1. Parse input dan verifikasi request/CSRF di adapter. Ambil owner dari server, bukan input pengguna.
2. Buka connection, foreign_keys ON, BEGIN IMMEDIATE. Cek receipt epoch/op_id **sebelum** stale token: hash sama → kembalikan hasil tersimpan tanpa write; beda → OPERATION_ID_REUSED.
3. Cek epoch/state_revision sama. Baca ulang aggregate, source binding dan semua invariant; preview aktual harus mengikat payload serta token yang sama.
4. Tulis semua record, increment revision, append change_log dan receipt dalam transaksi yang sama. Hanya confirm aktual menambah actual_final_revision.
5. COMMIT. Baru UI menyatakan saved. Error/lock timeout → ROLLBACK keseluruhan; input form tetap, retry memakai op_id/payload sama. Jika respons hilang setelah commit, receipt membuat retry tidak menggandakan write.

Connection memakai mode explicit transaction tanpa implicit BEGIN; pilihan parameter sqlite3 harus cocok versi Python yang telah diuji. Gunakan SQL BEGIN/COMMIT/ROLLBACK secara konsisten, jangan mencampur autocommit otomatis dan explicit BEGIN.

READ: satu read transaction menyalin seluruh input ke DTO immutable pada satu revision; tutup transaksi, hitung kedua engine dari snapshot itu. Tidak melakukan dua read bebas yang mencampur revision. SQLite tidak mendukung dua BEGIN bertingkat; service komposit menggunakan satu unit of work, subservice tidak commit sendiri.

## 6. Lifecycle khusus

| Operasi | Precondition / input | Postcondition / error | Bukti test |
| --- | --- | --- | --- |
| Aktivasi dataset | Dataset kandidat tervalidasi seluruh graph/scope; expected token | Insert immutable snapshot secara atomik, pilihan baru eksplisit; invalid meninggalkan aktif lama utuh. Tidak migrasi historical attempts | MAP-T-007/012, DDP-T-02 |
| Simpan BRP sebelum skor | Tree valid, locked=0 | Versi baru disimpan; versi lama superseded, tetap ada. Setelah ada row skor (termasuk clear/null yang disimpan), lock permanen sampai workspace reset | GRD-T-001/002, DDP-T-06 |
| Konfirmasi/koreksi final | Preview signed atas input final eksplisit, provenance, token; koreksi punya reason | Append revisi N+1 menunjuk N; current=revision_no terbesar; no DELETE/UPDATE histori; MAP/Dashboard recompute, scenario stale | GRD-T-010, INT-T-013 |
| Reset scenario | Token current; stale scenario boleh reset | plan/score/target overlay kosong, assumptions kosong, base_source_revision terbaru; scenario_revision+1; actual/source_revision tetap | MAP-T-006/011, INT-T-003 |
| Export | Satu read snapshot; local request tervalidasi | JSON schema_version, dataset_mode, owner/epoch/revisions, input dan histori final, source, scenario plus stale flag; decimals string; tidak export cookie/secret/token/receipts/logs | AUTH-T-015, INT-T-014 |
| Preview/cancel workspace reset | Read-only count/dampak dan expected token | Preview/cancel nol write dan nol increment revision | DDP-T-09 |
| Confirm workspace reset | Explicit confirmation + token/hash preview + op_id | Hapus semua record domain termasuk catalog runtime, profile, grades, targets, overlays, histori, logs/receipts; pertahankan owner/schema, epoch baru, kedua revision=0. Seed file tidak diubah; workspace kosong, load fixture harus eksplisit lagi | AUTH-T-015, INT-T-014 |

Workspace menyimpan satu `last_reset_receipt` minimal `{old_epoch,op_id,request_hash,new_epoch}` agar retry reset yang sama dikenali selama new_epoch masih current. Ini metadata operasi, bukan data akademik. Semua form/receipt lama selain reset tersebut menghasilkan STALE_EPOCH. Reset berikutnya mengganti tombstone ini. Reset tidak menghapus ekspor yang sudah diunduh pengguna; UI menyatakan batas itu. Riwayat final append-only selama workspace hidup, dengan pengecualian destructive reset yang dikonfirmasi.

Backup operasional file DB setelah proses berhenti, dan pemulihan manual, ada di ARCH-09; bukan import transkrip P0. SQLite corruption/versi schema tidak cocok harus menghentikan start dengan panduan pemulihan, bukan diam-diam overwrite database.

## 7. Trade-off

JSON dipakai hanya untuk AST/overlay kecil yang alami berbentuk tree/map; relasi akademik utama tetap tabel dan FK. Ini menghindari puluhan tabel clause/operand tanpa mengurangi validasi Python. Satu revision global menolak write independen dari tab lama sekalipun mungkin bisa digabung; keputusan konservatif ini dapat dijelaskan tim. Histori penuh score entry tidak diwajibkan baseline; histori final aktual wajib dan tidak boleh diganti dengan logging ringkas.

## Risiko, dependensi, dan bukti terbuka

Schema cukup besar untuk tim pemula: 17 tabel tidak berarti 17 service/repository class. Gunakan satu repository kecil dengan query berkelompok. FK/JSON validation, transaksi dan reset perlu temp-file tests. Pembatasan synthetic saja tidak membuktikan keamanan data nyata.

**Traceability:** PRO-AC/T-001–005/103; MAP-AC/T-006/007/011/012/103; GRD-AC/T-001/010/011/103; AUTH-AC/T-014/015/103; INT-T-001/003/013/014. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** OD-02 fixture/binding, OD-04 review skema dan reset; RV-02–04 tetap open untuk aturan institusi; tanpa itu output hanya demo. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
