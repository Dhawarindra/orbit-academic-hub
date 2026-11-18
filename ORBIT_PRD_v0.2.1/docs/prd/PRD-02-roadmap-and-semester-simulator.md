# PRD-02 — Academic Roadmap & Semester Simulator

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-02 / v0.2 DDP1 Draft |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Product Owner Roadmap / Academic Curator |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | Katalog production hanya aktif setelah kurikulum target diverifikasi; contoh A/B/C adalah fixture sintetis. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). |

## 2. Executive Summary & Problem

Roadmap memperlihatkan hubungan antar mata kuliah dan dampak pilihan semester. Status pengambilan, kelayakan, dan rencana pengguna adalah sumbu yang berbeda. Simulator membantu membandingkan alternatif dengan asumsi jelas; ia tidak mengirim IRS atau menyatakan persetujuan akademik.

## 3. Goals, Non-Goals & Success Metrics

Pengguna dapat menemukan prasyarat penghambat, menyusun satu rencana, serta melihat akibat penundaan tanpa mengubah riwayat aktual.

**Non-goals:** Optimasi jadwal global, jaminan lulus tepat waktu, atau menganggap offering selalu tersedia setiap semester.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Ketepatan alasan eligibility | Fixture AND/OR, unknown, retake dan cycle | 100% cocok oracle sebelum rilis |
| Pemahaman rencana bersyarat | Uji pengguna membedakan lulus aktual vs diasumsikan lulus | Usulan 4/5 peserta |
| Aksesibilitas jalur | Semua informasi graf tersedia pada list | 100% course, edge dan alasan |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Mahasiswa memilih semester depan; mahasiswa yang menunda satu course; curator yang memperbaiki katalog.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Guest | Katalog published dan sumber | Riwayat atau skenario personal |
| Student | Skenario sendiri dan status dari riwayat sendiri | Mengubah katalog bersama |
| Curator/admin | Draft, verifikasi dan publish katalog | Mengganti final grade mahasiswa |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Katalog kecil, AND/OR tiga nilai, SKS, dampak penundaan, satu skenario, validasi graf, daftar accessible | Tidak ada tambahan wajib | Perbandingan multiskenario dan rebase yang mempertahankan pilihan; katalog luas/izin khusus |

**Slice rilis:** Fixture A→B→C dan AND/OR → evaluasi aktual → tunda A → tampilkan dampak bersyarat → reset. Editor graf drag-and-drop dan dashboard kurator bukan syarat.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Fixture A→B→C dan AND/OR → evaluasi aktual → tunda A → tampilkan dampak bersyarat → reset. Editor graf drag-and-drop dan dashboard kurator bukan syarat. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Dashboard → Roadmap → lihat versi/sumber → pilih course → panel prasyarat dan eligibility → Tambah ke rencana. Jika unknown, rencana boleh tersimpan sebagai perlu verifikasi. Kembali ke list mempertahankan filter semester.

**J2.** Simulator → salin baseline → pilih course A ditunda → lihat descendants terdampak dan asumsi ketersediaan → bandingkan before/after → simpan atau reset. Hanya skenario berubah.

**J3.** Curator mengubah prerequisite graph → validasi siklus dan referensi → terbitkan versi baru. Pengguna lama tetap terikat versi lama sampai migrasi eksplisit.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| MAP-US-001 | As a student, I want melihat prasyarat dan status, so that saya memahami alasan course terkunci. | P0 | MAP-FR-001, MAP-FR-002, MAP-FR-003 |
| MAP-US-002 | As a student, I want mencoba kombinasi dan penundaan, so that pilihan semester dapat dibandingkan. | P0 | MAP-FR-004, MAP-FR-005, MAP-FR-006 |
| MAP-US-003 | As a curator, I want memvalidasi graf sebelum publish, so that aturan rusak tidak tersebar. | P0 | MAP-FR-007, MAP-FR-008, MAP-FR-009 |
| MAP-US-004 | As a student, I want mereset eksperimen, so that data akademik asli tetap aman. | P0 | MAP-FR-011 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MAP-FR-001 | P0 | Buka roadmap | Scope profil terpilih | curriculum_version_id | Tampilkan course dan SKS dari CurriculumCourse versi itu beserta source status | Course antar versi tidak tercampur | MAP-AC-001 |
| MAP-FR-002 | P0 | Nilai eligibility | Graf rule valid | ActualFinalGrade dan provenance | Evaluasi prasyarat memakai hasil aktual saja dalam mode real | Prediksi 90 pada A tidak membuka B yang mensyaratkan lulus A | MAP-AC-002 |
| MAP-FR-003 | P0 | Buka detail prasyarat | Ekspresi rule tersedia | AND(A,OR(B,C)); A lulus, B gagal, C unknown | Kembalikan met/unmet/unknown dengan alasan per leaf | Hasil unknown; A terpenuhi, OR belum pasti | MAP-AC-003 |
| MAP-FR-004 | P0 | Validasi rencana | Skenario draft | course terpilih dan batas SKS | Jumlahkan SKS dan tampilkan pelanggaran terhadap rule aktif atau cap personal | A=3,B=4 total 7; cap personal 6 memberi warning personal | MAP-AC-004 |
| MAP-FR-005 | P0 | Tunda course | Skenario dengan A→B→C | A bergeser dari semester 1 ke 2; semua tersedia tiap term pada fixture | Traversal downstream tanpa mengubah katalog atau enrollment | Earliest fixture B=3,C=4; dampak bertanda asumsi, bukan tanggal lulus | MAP-AC-005 |
| MAP-FR-006 | P0 | Buka skenario setelah nilai berubah | base_revision lama | ActualFinalGradeChanged | Tandai stale dan tampilkan perubahan baseline; pada P0 tawarkan reset lalu pilih ulang, rebase yang mempertahankan pilihan merupakan P2 | Revision r1 tidak tampil current setelah sumber r2; reset memuat r2, actual tidak berubah; mode P2 mempertahankan pilihan valid setelah review diff | MAP-AC-006 |
| MAP-FR-007 | P0 | Validasi aktivasi dataset graf | Kurator menyiapkan fixture/file konfigurasi; tidak perlu UI admin | A→B dan B→A | Tolak cycle dengan daftar ID yang terlibat | Dataset cycle tidak diaktifkan; cycle A/B terlihat; versi lama tetap aktif | MAP-AC-007 |
| MAP-FR-008 | P0 | Buka roadmap dalam mode daftar | Katalog dan rule tersedia; tampilan graf opsional | Mode list | Sediakan informasi course, edge, semester dan alasan tanpa drag/hover | Seluruh prasyarat dapat dibaca melalui keyboard tanpa memerlukan renderer graf interaktif | MAP-AC-008 |
| MAP-FR-009 | P0 | Simpan rule tidak dikenal | Curator | Jenis requirement belum didukung | Pertahankan catatan rule dan beri status unsupported | Eligibility unknown, tidak dianggap otomatis terpenuhi | MAP-AC-009 |
| MAP-FR-010 | P2 | Bandingkan alternatif | Dua scenario tersimpan | scenario A dan B | Tampilkan delta SKS, course tertunda dan asumsi berbeda | Perbedaan terlihat tanpa menulis hasil real | MAP-AC-010 |
| MAP-FR-011 | P0 | Reset scenario | Scenario sudah mengubah plan dan grade overlay | scenario_id | Hapus overlay dan baca baseline source terbaru dengan badge revisi | Actual enrollment/final grade tidak berubah; skenario bersih | MAP-AC-011 |
| MAP-FR-012 | P0 | Validasi aktivasi katalog referensi rusak | Kurator menyiapkan fixture/file konfigurasi; tidak perlu UI admin | Prerequisite menunjuk course_id tidak ada atau versi berbeda | Tolak publish hingga semua referensi memiliki mapping scope sah | Dataset ditolak dan tidak mengganti versi aktif; daftar missing/mismatch course terlihat | MAP-AC-012 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| MAP-BR-001 | Course punya ID tetap; nama, SKS dan prasyarat terikat CurriculumCourse pada CurriculumVersion. Alias nama bukan equivalence. | MAP-FR-001 |
| MAP-BR-002 | Status course terdiri dari progress (not_started/active/passed/failed), planned flag, dan eligibility (met/unmet/unknown). Planned tidak menggantikan passed. | MAP-FR-002, MAP-FR-004 |
| MAP-BR-003 | AND: satu unmet → unmet, semua met → met, selain itu unknown. OR: satu met → met, semua unmet → unmet, selain itu unknown. Rule kosong hanya met bila sumber menyatakan tidak ada prasyarat. | MAP-FR-003, MAP-FR-009 |
| MAP-BR-004 | Only actual records memberi input mode real, tetap dilabeli user_reported jika belum diverifikasi kampus. Mode simulasi boleh memakai assumed_pass dengan banner bersyarat. | MAP-FR-002, MAP-FR-005 |
| MAP-BR-005 | Earliest term dihitung topological pada graf yang didukung: AND menunggu semua prasyarat, sementara OR memakai jalur alternatif yang dipilih eksplisit pada skenario dan dilabeli asumsi. P0 tidak mengoptimalkan semua kombinasi OR. Bila jalur OR belum dipilih, availability belum diketahui atau ada corequisite/izin khusus unsupported, hasil waktu tetap unknown/bersyarat. Fixture setiap-term memberi term anak lebih besar dari term prasyarat terpilih. | MAP-FR-003, MAP-FR-005, MAP-FR-007, MAP-FR-009 |
| MAP-BR-006 | Validasi SKS personal dan aturan resmi ditampilkan terpisah. Tidak mengarang batas resmi saat policy binding belum ada. | MAP-FR-004 |
| MAP-BR-007 | Reset menghapus overlay skenario saja dan membaca baseline terbaru. P0 memakai stale → review perubahan → reset/pilih ulang. Rebase yang mempertahankan pilihan valid dan meminta tinjau konflik disimpan sebagai kemampuan P2 pada MAP-FR-006; tidak dihapus. | MAP-FR-006, MAP-FR-011 |
| MAP-BR-008 | Siklus, dangling course ID dan scope mismatch memblokir publish. Data draft tidak menggantikan katalog aktif. | MAP-FR-007, MAP-FR-001, MAP-FR-012 |

**Graf sintetis:** A (3 SKS) → B (4 SKS) → C (3 SKS); D (2 SKS) memerlukan A atau E. Jika A aktual lulus, B eligible menurut catatan pengguna; C tetap belum eligible sampai B aktual lulus. Memasukkan B predicted=95 tidak mengubah C.

**Penundaan:** skenario S memiliki A di semester 1, B 2, C 3. Dengan asumsi tiap course ditawarkan setiap term dan tidak ada batas lain, A ke semester 2 menggeser paling awal B ke 3 dan C ke 4. Jika B hanya tersedia pada term genap, traversal mencari term tersedia berikutnya. Jika availability belum diketahui, tampilkan “waktu penawaran perlu dikonfirmasi”.

**Pseudocode konseptual:** validasi graf → baca actual snapshot dan rule version → evaluasi leaf tiga nilai → evaluasi expression → kumpulkan alasan → terapkan overlay hanya pada scenario → hitung totals dan constraints → tampilkan sumber serta uncertainty.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| CurriculumVersion / curriculum_version_id | program, applicability, verification status, effective date, source refs | Academic Curator | draft → verified/published → superseded | Public published |
| Course / course_id | Kode identitas stabil dan alias; tidak menyimpan SKS universal | Curator | Retired ID tetap bisa dirujuk history | Public |
| CurriculumCourse / version+course | SKS, category, recommended term, prerequisite expression, rule_version | Curator dari sumber resmi | Immutable per published revision | Public |
| CourseOffering / offering_id | course, term, class, teacher label optional; availability source | Curator / user personal | Confirmed vs user-defined | Public template / Private personal |
| SimulationScenario / scenario_id | owner, base_revision, curriculum, terms, assumed outcomes | Student | draft/saved/stale/rebased/deleted | Private |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Desktop menawarkan Peta jalur dan Daftar matkul, filter semester/kategori dan pencarian. Klik course membuka panel kanan berisi prerequisite, apa yang dibuka, provenance dan CTA rencana. Mobile default list dengan kelompok semester; graf opsional pan/zoom dan tombol setara keyboard. Pada setiap halaman simulator tampil banner “Simulasi — tidak mengubah riwayat atau IRS”. Status memakai teks/ikon, bukan warna saja. Frame Roadmap v2 11:183 diamati: sidebar ikon, tab list/graf, filter semester, kolom semester, legenda dan area ajakan simulasi. Nama/edge pada frame bersifat ilustratif dan tidak diimpor sebagai rule.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| No verified catalog | Jelajah contoh berlabel demo atau pilih versi | Tidak klaim kelayakan resmi |
| Unknown prerequisite | Alasan data/rule belum tersedia | Simpan rencana perlu tinjau |
| Impossible combination | Konflik dan course penyebab | Tidak menghapus pilihan diam-diam |
| Cycle/dangling | Publish ditolak | Perbaiki draft curator |
| Stale scenario | Tawarkan rebase/reset | Aktual tetap terlindungi |
| Missing offering | Waktu penawaran belum diketahui | Alternatif bersyarat |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** P0 membaca actual dari GRD-FR-010 secara langsung; GDE/closeout tidak menjadi precondition. Aktivasi katalog berupa validasi dataset/file oleh Python; UI admin P2. MAP-FR-006 stale/reset P0; rebase mempertahankan pilihan P2. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| PRO-FR-008 → MAP-FR-001 | Profile scope menentukan catalog revision | Migrasi eksplisit; mismatch menahan eligibility |
| GRD-FR-010 → MAP-FR-002 | ActualFinalGradeChanged per attempt | PredictionChanged tidak membuka prasyarat |
| MAP-FR-004 → GDE-FR-002 | ConstraintResult berisi reason dan source | Unknown diperlakukan kebutuhan data |
| MAP-FR-001 → CAR-FR-004 | Course dan prerequisite IDs | Mapping karier yang tidak cocok versi dikecualikan |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Rencana serta riwayat tidak tampil pada katalog publik. Source metadata terlihat tanpa membuka dokumen privat yang diunggah orang lain. Label “eligible berdasarkan catatanmu” tidak boleh berubah menjadi “IRS disetujui”.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| MAP-NFR-001 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | MAP-AC-101 |
| MAP-NFR-002 | P0 | Validasi graf 100 node/300 edge p95 ≤300 ms setelah input tersedia. | MAP-AC-102 |
| MAP-NFR-003 | P0 | Kegagalan simpan tidak menghapus input; retry dengan identitas operasi sama tidak menghasilkan duplikasi. | MAP-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| MAP-AC-001 | Given Scope profil terpilih; curriculum_version_id | When Buka roadmap | Then Course antar versi tidak tercampur | MAP-FR-001 |
| MAP-AC-002 | Given Graf rule valid; ActualFinalGrade dan provenance | When Nilai eligibility | Then Prediksi 90 pada A tidak membuka B yang mensyaratkan lulus A | MAP-FR-002 |
| MAP-AC-003 | Given Ekspresi rule tersedia; AND(A,OR(B,C)); A lulus, B gagal, C unknown | When Buka detail prasyarat | Then Hasil unknown; A terpenuhi, OR belum pasti | MAP-FR-003 |
| MAP-AC-004 | Given Skenario draft; course terpilih dan batas SKS | When Validasi rencana | Then A=3,B=4 total 7; cap personal 6 memberi warning personal | MAP-FR-004 |
| MAP-AC-005 | Given Skenario dengan A→B→C; A bergeser dari semester 1 ke 2; semua tersedia tiap term pada fixture | When Tunda course | Then Earliest fixture B=3,C=4; dampak bertanda asumsi, bukan tanggal lulus | MAP-FR-005 |
| MAP-AC-006 | Given base_revision lama; ActualFinalGradeChanged | When Buka skenario setelah nilai berubah | Then Revision r1 tidak tampil current setelah sumber r2; reset memuat r2, actual tidak berubah; mode P2 mempertahankan pilihan valid setelah review diff | MAP-FR-006 |
| MAP-AC-007 | Given Kurator menyiapkan fixture/file konfigurasi; tidak perlu UI admin; A→B dan B→A | When Validasi aktivasi dataset graf | Then Dataset cycle tidak diaktifkan; cycle A/B terlihat; versi lama tetap aktif | MAP-FR-007 |
| MAP-AC-008 | Given Katalog dan rule tersedia; tampilan graf opsional; Mode list | When Buka roadmap dalam mode daftar | Then Seluruh prasyarat dapat dibaca melalui keyboard tanpa memerlukan renderer graf interaktif | MAP-FR-008 |
| MAP-AC-009 | Given Curator; Jenis requirement belum didukung | When Simpan rule tidak dikenal | Then Eligibility unknown, tidak dianggap otomatis terpenuhi | MAP-FR-009 |
| MAP-AC-010 | Given Dua scenario tersimpan; scenario A dan B | When Bandingkan alternatif | Then Perbedaan terlihat tanpa menulis hasil real | MAP-FR-010 |
| MAP-AC-011 | Given Scenario sudah mengubah plan dan grade overlay; scenario_id | When Reset scenario | Then Actual enrollment/final grade tidak berubah; skenario bersih | MAP-FR-011 |
| MAP-AC-012 | Given Kurator menyiapkan fixture/file konfigurasi; tidak perlu UI admin; Prerequisite menunjuk course_id tidak ada atau versi berbeda | When Validasi aktivasi katalog referensi rusak | Then Dataset ditolak dan tidak mengganti versi aktif; daftar missing/mismatch course terlihat | MAP-FR-012 |
| MAP-AC-101 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | MAP-NFR-001 |
| MAP-AC-102 | Given Fixture acyclic dan cyclic 100/300 | When Evaluasi 30 kali | Then Terminasi dan p95 ≤300 ms; tidak rekursi tak berakhir | MAP-NFR-002 |
| MAP-AC-103 | Given Form valid dan gangguan koneksi sebelum konfirmasi simpan | When Simpan, pulihkan koneksi, lalu retry | Then Input tetap terlihat; tepat satu revisi tersimpan dan indikator sukses hanya setelah konfirmasi | MAP-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| MAP-T-001 | fungsional | Scope profil terpilih; curriculum_version_id | Buka roadmap | Course antar versi tidak tercampur | P0 | MAP-FR-001 / MAP-AC-001 |
| MAP-T-002 | negatif | Graf rule valid; ActualFinalGrade dan provenance | Nilai eligibility | Prediksi 90 pada A tidak membuka B yang mensyaratkan lulus A | P0 | MAP-FR-002 / MAP-AC-002 |
| MAP-T-003 | boundary | Ekspresi rule tersedia; AND(A,OR(B,C)); A lulus, B gagal, C unknown | Buka detail prasyarat | Hasil unknown; A terpenuhi, OR belum pasti | P0 | MAP-FR-003 / MAP-AC-003 |
| MAP-T-004 | numerik | Skenario draft; course terpilih dan batas SKS | Validasi rencana | A=3,B=4 total 7; cap personal 6 memberi warning personal | P0 | MAP-FR-004 / MAP-AC-004 |
| MAP-T-005 | integrasi | Skenario dengan A→B→C; A bergeser dari semester 1 ke 2; semua tersedia tiap term pada fixture | Tunda course | Earliest fixture B=3,C=4; dampak bertanda asumsi, bukan tanggal lulus | P0 | MAP-FR-005 / MAP-AC-005 |
| MAP-T-006 | edge | base_revision lama; ActualFinalGradeChanged | Buka skenario setelah nilai berubah | Revision r1 tidak tampil current setelah sumber r2; reset memuat r2, actual tidak berubah; mode P2 mempertahankan pilihan valid setelah review diff | P0 | MAP-FR-006 / MAP-AC-006 |
| MAP-T-007 | negatif | Kurator menyiapkan fixture/file konfigurasi; tidak perlu UI admin; A→B dan B→A | Validasi aktivasi dataset graf | Dataset cycle tidak diaktifkan; cycle A/B terlihat; versi lama tetap aktif | P0 | MAP-FR-007 / MAP-AC-007 |
| MAP-T-008 | aksesibilitas | Katalog dan rule tersedia; tampilan graf opsional; Mode list | Buka roadmap dalam mode daftar | Seluruh prasyarat dapat dibaca melalui keyboard tanpa memerlukan renderer graf interaktif | P0 | MAP-FR-008 / MAP-AC-008 |
| MAP-T-009 | edge | Curator; Jenis requirement belum didukung | Simpan rule tidak dikenal | Eligibility unknown, tidak dianggap otomatis terpenuhi | P0 | MAP-FR-009 / MAP-AC-009 |
| MAP-T-010 | fungsional | Dua scenario tersimpan; scenario A dan B | Bandingkan alternatif | Perbedaan terlihat tanpa menulis hasil real | P2 | MAP-FR-010 / MAP-AC-010 |
| MAP-T-011 | integrasi | Scenario sudah mengubah plan dan grade overlay; scenario_id | Reset scenario | Actual enrollment/final grade tidak berubah; skenario bersih | P0 | MAP-FR-011 / MAP-AC-011 |
| MAP-T-012 | negatif | Kurator menyiapkan fixture/file konfigurasi; tidak perlu UI admin; Prerequisite menunjuk course_id tidak ada atau versi berbeda | Validasi aktivasi katalog referensi rusak | Dataset ditolak dan tidak mengganti versi aktif; daftar missing/mismatch course terlihat | P0 | MAP-FR-012 / MAP-AC-012 |
| MAP-T-101 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | MAP-NFR-001 / MAP-AC-101 |
| MAP-T-102 | nonfungsional | Fixture acyclic dan cyclic 100/300 | Evaluasi 30 kali | Terminasi dan p95 ≤300 ms; tidak rekursi tak berakhir | P0 | MAP-NFR-002 / MAP-AC-102 |
| MAP-T-103 | nonfungsional | Form valid dan gangguan koneksi sebelum konfirmasi simpan | Simpan, pulihkan koneksi, lalu retry | Input tetap terlihat; tepat satu revisi tersimpan dan indikator sukses hanya setelah konfirmasi | P0 | MAP-NFR-003 / MAP-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| MAP-Q1 | Applicability dan equivalence antar kurikulum belum disahkan | Salah hasil dependency | Kurator verifikasi; rule unknown |
| MAP-Q2 | Penawaran per term berubah | Simulasi terlalu pasti | Tandai availability assumption |
| MAP-Q3 | Prasyarat khusus tidak terstruktur | False eligible | Simpan source text; jangan auto-pass |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Multi-scenario UI P2; optimasi penjadwalan, corequisite kompleks dan integrasi IRS P2. Tidak ada scraping SLCM.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: MAP-FR-010. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-05 course.csui.dev diperiksa sebagai referensi navigasi sekunder; SRC-02/03 konteks resmi; SRC-04 pedoman umum bukan katalog lengkap; SRC-07 Roadmap v2 diamati sebagai desain ilustratif.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-05 pada audit untuk alasan revisi.

