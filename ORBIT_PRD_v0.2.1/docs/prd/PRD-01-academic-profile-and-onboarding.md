# PRD-01 — Academic Profile & Onboarding

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-01 / v0.2 DDP1 Draft |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Product Owner Profil |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | P0 memakai workspace lokal sintetis AUTH-FR-014; username/password Orbit menjadi P2; prodi/angkatan diinput pengguna, bukan klaim terverifikasi. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). |

## 2. Executive Summary & Problem

Onboarding mengumpulkan konteks minimum untuk mengarahkan mahasiswa ke semester yang benar tanpa meminta seluruh riwayat sekaligus. Profil, kredensial dan atribusi publik dipisahkan. Mahasiswa yang belum tahu versi kurikulum dapat mulai mencatat offering personal, tetapi roadmap tidak memberi keputusan resmi.

## 3. Goals, Non-Goals & Success Metrics

Pengguna dapat mencapai tindakan berguna pertama dengan satu offering dan melanjutkan pengisian profil kapan saja.

**Non-goals:** Membuktikan status mahasiswa melalui pengakuan sendiri, mengambil riwayat otomatis, atau menetapkan kurikulum hanya dari tahun masuk.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Waktu ke offering pertama | Uji 5 peserta dengan katalog siap; dari login hingga offering tersimpan | Usulan median ≤5 menit |
| Resume onboarding | Checkpoint tampil kembali setelah restart lokal; logout/login hanya mode akun P2 | 100% skenario P0 |
| Pengumpulan minimum | Field wajib untuk akun/profil sesuai kontrak | Nol permintaan identitas kampus yang tidak diperlukan |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Mahasiswa baru dengan riwayat kosong; mahasiswa lanjut yang membawa riwayat; alumni yang ingin berkontribusi tanpa SSO.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Guest | Mulai registrasi atau membaca demo | Menyimpan data personal tanpa akun |
| Student/senior/alumni | CRUD profil dan riwayat sendiri | Mengubah profil orang lain |
| Curator | Menerbitkan opsi program/kurikulum | Menetapkan profil pengguna tanpa persetujuan |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Profil bertahap, semester, enrollment dan riwayat manual satu per satu | Preferensi personal sederhana | Migrasi kurikulum, import tabel dan import resmi berizin |

**Slice rilis:** Workspace lokal → isi program/angkatan atau unknown → pilih term → tambah offering → dashboard. Identitas owner_scope menggantikan precondition login pada P0; tidak membuktikan afiliasi.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Workspace lokal → isi program/angkatan atau unknown → pilih term → tambah offering → dashboard. Identitas owner_scope menggantikan precondition login pada P0; tidak membuktikan afiliasi. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Landing → daftar lokal (AUTH) → formulir program/angkatan/kurikulum → pilih semester → tambah matkul. Jika kurikulum belum pasti, simpan sebagai unknown dan tampilkan keterbatasan. Kembali ke dashboard menampilkan langkah berikut yang relevan.

**J2.** Pengaturan → riwayat akademik → tambah course, periode, SKS dan hasil aktual yang dilaporkan → preview → simpan. Duplikat course+term+attempt diarahkan ke edit; pengulangan berbeda term menjadi attempt terpisah.

**J3.** Pengaturan → ubah kurikulum → lihat matkul cocok, berubah, tidak terpetakan → setujui migrasi. Batalkan mengembalikan versi lama tanpa mengubah nilai historis.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| PRO-US-001 | As a student, I want mengisi profil secara bertahap, so that saya bisa mulai dengan data minimum. | P0 | PRO-FR-001, PRO-FR-002, PRO-FR-003 |
| PRO-US-002 | As a student, I want mencatat hasil lama dan matkul aktif, so that roadmap mengenali riwayat saya. | P0 | PRO-FR-004, PRO-FR-005 |
| PRO-US-003 | As a student, I want meninjau perubahan kurikulum, so that riwayat tidak hilang. | P1 / P2 (per FR) | PRO-FR-006, PRO-FR-007, PRO-FR-008 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRO-FR-001 | P0 | Simpan langkah profil | Workspace lokal aktif; akun aktif hanya untuk mode multiuser P2 | program/cohort/kurikulum nullable | Simpan field yang valid dan checkpoint tanpa memaksa field opsional | Status incomplete bila scope kurikulum belum lengkap | PRO-AC-001 |
| PRO-FR-002 | P0 | Lanjut onboarding | Kurikulum belum diketahui | Pilihan belum tahu | Izinkan masuk workspace personal dengan badge scope unknown | Offering manual dapat dibuat; eligibility resmi tidak dihitung | PRO-AC-002 |
| PRO-FR-003 | P0 | Buka kembali workspace lokal atau masuk akun P2 | Checkpoint profil tersimpan | owner_scope stabil | Buka langkah terakhir yang belum lengkap; berikan Lewati dulu | Field tersimpan tidak perlu diketik ulang | PRO-AC-003 |
| PRO-FR-004 | P0 | Tambah matkul aktif | Term aktif dipilih | course_id/offering_id atau offering personal | Buat enrollment unik pada offering milik scope yang tepat | Satu enrollment dan pintasan konfigurasi BRP tersedia | PRO-AC-004 |
| PRO-FR-005 | P0 | Simpan riwayat | Pemilik workspace; fixture sintetis pada rilis DDP1 | course, term, attempt, final grade, provenance | Validasi identitas attempt sebelum menyimpan hasil yang dilaporkan | Duplikat attempt ditolak; term berbeda diterima sebagai pengulangan | PRO-AC-005 |
| PRO-FR-006 | P2 | Ganti versi kurikulum | Profil dan riwayat sudah ada | curriculum_version_id baru | Tampilkan diff mapping sebelum commit | Cancel mempertahankan versi lama dan semua nilai | PRO-AC-006 |
| PRO-FR-007 | P1 | Simpan preferensi | Pemilik workspace lokal atau akun P2 | zona waktu, nama sapaan, target opsional | Simpan preferensi personal tanpa mengubah nama publik | Nama sapaan/zona waktu lokal berubah; bila kredit kontributor P2 aktif, identitas publik tetap mengikuti consent terpisah | PRO-AC-007 |
| PRO-FR-008 | P2 | Konfirmasi migrasi | Diff sudah ditinjau | mapping yang disetujui | Buat revisi profil dan tandai skenario lama stale | Nilai historis tetap ber-SKS/source lama; skenario perlu rebase | PRO-AC-008 |
| PRO-FR-009 | P2 | Import tabel riwayat | Format kolom dipetakan | 5 baris, 1 duplikat, 1 invalid | Preview tiap baris dan minta konfirmasi subset valid | 3 baris valid dapat diimpor; 2 bermasalah tidak ditulis | PRO-AC-009 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| PRO-BR-001 | Akun baru memiliki profile=incomplete. Ready untuk roadmap memerlukan program, curriculum version terverifikasi sesuai scope; ready untuk grade cukup offering personal. | PRO-FR-001, PRO-FR-002 |
| PRO-BR-002 | Semester akademik adalah term berlabel tahun ajar/ganjil/genap dengan tanggal opsional. Nomor semester personal bukan hasil otomatis dari angkatan. | PRO-FR-004 |
| PRO-BR-003 | Riwayat berisi ActualFinalGrade dengan provenance user_reported; import tidak membuktikan kebenaran kampus. | PRO-FR-005, PRO-FR-009 |
| PRO-BR-004 | Perubahan profil tidak menulis ulang SKS atau aturan pada attempt historis. Mapping ambigu tidak dicocokkan hanya dari nama. | PRO-FR-006, PRO-FR-008 |
| PRO-BR-005 | Target personal boleh kosong; target bukan batas minimum kelulusan kampus. Zona waktu default Asia/Jakarta dapat diganti. | PRO-FR-007 |
| PRO-BR-006 | Curriculum selection tanpa sumber cocok tidak menjadi VERIFIED_OFFICIAL melalui konfirmasi user. | PRO-FR-002, PRO-FR-008 |

**Skenario sintetis:** mahasiswa mengisi angkatan 2026 tetapi tidak tahu versi kurikulum. Sistem menyimpan 2026 sebagai self-reported dan meminta pilihan versi hanya saat roadmap membutuhkan aturan. Satu offering MAT-DEMO tetap dapat dibuat untuk BRP. Ketika profil pindah versi V1 → V2, course A setara eksplisit dapat dipetakan; course B tanpa equivalence tetap perlu ditinjau. Tidak ada penghapusan nilai B.

Urutan validasi: kepemilikan → format → keberadaan ID → kecocokan scope → duplikasi → preview → commit revisi. Gagal pada satu langkah tidak menandai checkpoint selesai.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| AcademicProfile / profile_id | user_id 1:1; program, cohort, curriculum_version, active_term, completion_flags | Student melalui PRO | incomplete → usable → ready; revisions | Private |
| Enrollment / enrollment_id | user_id + offering_id + attempt_id; status aktif/withdrawn/completed | Student; course dari MAP | Riwayat tidak hard overwrite | Private |
| AcademicTerm / term_id | label, start/end nullable, timezone; berbeda dari semester_index pengguna | Curator atau personal berlabel | Tanggal dikoreksi dengan audit | Public template / Private personal |
| ProfilePreference / user_id | nama sapaan, timezone, locale, target refs | Student | Revisi; export/delete AUTH | Private |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Stepper ringkas: Konteks → Semester → Matkul → Selesai. Tampilkan field wajib berdasarkan langkah yang dipilih, tombol Simpan dan lanjut serta Lewati dulu yang setara terbaca. Pilihan kurikulum menampilkan program, applicability dan sumber. Riwayat berupa tabel dengan edit satu baris; tampilkan total hanya untuk baris valid. Dialog migrasi menampilkan jumlah terpetakan/perlu review dan tombol Batal yang tidak kehilangan profil. Mobile menggunakan satu kolom; label tetap terlihat ketika field terisi.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| First use | Penjelasan manfaat tiap input | Tidak tampil 0 IPK sebagai nilai nyata |
| No curriculum | Belum tahu tersedia | Fitur personal tetap berjalan |
| Semester tidak cocok | Minta tinjau rentang tanggal | Jangan infer status cuti |
| Duplicate attempt | Tawarkan buka record | Jangan gandakan SKS |
| Migrasi ambigu | Daftar perlu ditinjau | Tidak auto-merge course |
| Offline/unauthorized | Input belum tersimpan / login ulang | Tidak restore data milik user lain |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** P0 menerima owner_scope dari AUTH-FR-014, bukan AccountCreated. Jalur AUTH-FR-001, PRO-FR-006/008 dan migrasi hanya P2. PRO-FR-007 → SCH-FR-002 opsional P1; default Asia/Jakarta tidak memerlukan preferences UI. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| AUTH-FR-001 → PRO-FR-001 | AccountCreated memberi user_id, bukan prodi/angkatan | Akun valid tetap dapat incomplete |
| PRO-FR-004 → MAP-FR-001/GRD-FR-001 | EnrollmentChanged dengan offering/term scope | BRP manual jika template belum ada |
| PRO-FR-008 → MAP-FR-006 | ProfileRevisionChanged memicu stale scenario | Manual rebase; data historis read-only |
| PRO-FR-007 → SCH-FR-002 | TimezoneChanged mengubah tampilan waktu | Timestamp sumber tidak diinterpretasi ulang diam-diam |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Akun tidak membutuhkan NPM atau dokumen identitas. Program dan cohort adalah data privat kecuali consent khusus kontribusi agregat. Nama sapaan tidak pernah menjadi display_name komunitas secara otomatis. Field kelengkapan tidak boleh digunakan sebagai gamifikasi yang memaksa pengungkapan.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| PRO-NFR-001 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | PRO-AC-101 |
| PRO-NFR-002 | P0 | Tampilan utama p95 ≤2 detik setelah data tersedia pada beban uji dasar. | PRO-AC-102 |
| PRO-NFR-003 | P0 | Kegagalan simpan tidak menghapus input; retry dengan identitas operasi sama tidak menghasilkan duplikasi. | PRO-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| PRO-AC-001 | Given Workspace lokal aktif; akun aktif hanya untuk mode multiuser P2; program/cohort/kurikulum nullable | When Simpan langkah profil | Then Status incomplete bila scope kurikulum belum lengkap | PRO-FR-001 |
| PRO-AC-002 | Given Kurikulum belum diketahui; Pilihan belum tahu | When Lanjut onboarding | Then Offering manual dapat dibuat; eligibility resmi tidak dihitung | PRO-FR-002 |
| PRO-AC-003 | Given Checkpoint profil tersimpan; owner_scope stabil | When Buka kembali workspace lokal atau masuk akun P2 | Then Field tersimpan tidak perlu diketik ulang | PRO-FR-003 |
| PRO-AC-004 | Given Term aktif dipilih; course_id/offering_id atau offering personal | When Tambah matkul aktif | Then Satu enrollment dan pintasan konfigurasi BRP tersedia | PRO-FR-004 |
| PRO-AC-005 | Given Pemilik workspace; fixture sintetis pada rilis DDP1; course, term, attempt, final grade, provenance | When Simpan riwayat | Then Duplikat attempt ditolak; term berbeda diterima sebagai pengulangan | PRO-FR-005 |
| PRO-AC-006 | Given Profil dan riwayat sudah ada; curriculum_version_id baru | When Ganti versi kurikulum | Then Cancel mempertahankan versi lama dan semua nilai | PRO-FR-006 |
| PRO-AC-007 | Given Pemilik workspace lokal atau akun P2; zona waktu, nama sapaan, target opsional | When Simpan preferensi | Then Nama sapaan/zona waktu lokal berubah; bila kredit kontributor P2 aktif, identitas publik tetap mengikuti consent terpisah | PRO-FR-007 |
| PRO-AC-008 | Given Diff sudah ditinjau; mapping yang disetujui | When Konfirmasi migrasi | Then Nilai historis tetap ber-SKS/source lama; skenario perlu rebase | PRO-FR-008 |
| PRO-AC-009 | Given Format kolom dipetakan; 5 baris, 1 duplikat, 1 invalid | When Import tabel riwayat | Then 3 baris valid dapat diimpor; 2 bermasalah tidak ditulis | PRO-FR-009 |
| PRO-AC-101 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | PRO-NFR-001 |
| PRO-AC-102 | Given Beban uji dasar dan data telah tersedia | When Buka tampilan utama 30 kali | Then p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | PRO-NFR-002 |
| PRO-AC-103 | Given Form valid dan gangguan koneksi sebelum konfirmasi simpan | When Simpan, pulihkan koneksi, lalu retry | Then Input tetap terlihat; tepat satu revisi tersimpan dan indikator sukses hanya setelah konfirmasi | PRO-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| PRO-T-001 | fungsional | Workspace lokal aktif; akun aktif hanya untuk mode multiuser P2; program/cohort/kurikulum nullable | Simpan langkah profil | Status incomplete bila scope kurikulum belum lengkap | P0 | PRO-FR-001 / PRO-AC-001 |
| PRO-T-002 | edge | Kurikulum belum diketahui; Pilihan belum tahu | Lanjut onboarding | Offering manual dapat dibuat; eligibility resmi tidak dihitung | P0 | PRO-FR-002 / PRO-AC-002 |
| PRO-T-003 | fungsional | Checkpoint profil tersimpan; owner_scope stabil | Buka kembali workspace lokal atau masuk akun P2 | Field tersimpan tidak perlu diketik ulang | P0 | PRO-FR-003 / PRO-AC-003 |
| PRO-T-004 | fungsional | Term aktif dipilih; course_id/offering_id atau offering personal | Tambah matkul aktif | Satu enrollment dan pintasan konfigurasi BRP tersedia | P0 | PRO-FR-004 / PRO-AC-004 |
| PRO-T-005 | boundary | Pemilik workspace; fixture sintetis pada rilis DDP1; course, term, attempt, final grade, provenance | Simpan riwayat | Duplikat attempt ditolak; term berbeda diterima sebagai pengulangan | P0 | PRO-FR-005 / PRO-AC-005 |
| PRO-T-006 | negatif | Profil dan riwayat sudah ada; curriculum_version_id baru | Ganti versi kurikulum | Cancel mempertahankan versi lama dan semua nilai | P2 | PRO-FR-006 / PRO-AC-006 |
| PRO-T-007 | privasi | Pemilik workspace lokal atau akun P2; zona waktu, nama sapaan, target opsional | Simpan preferensi | Nama sapaan/zona waktu lokal berubah; bila kredit kontributor P2 aktif, identitas publik tetap mengikuti consent terpisah | P1 | PRO-FR-007 / PRO-AC-007 |
| PRO-T-008 | integrasi | Diff sudah ditinjau; mapping yang disetujui | Konfirmasi migrasi | Nilai historis tetap ber-SKS/source lama; skenario perlu rebase | P2 | PRO-FR-008 / PRO-AC-008 |
| PRO-T-009 | negatif | Format kolom dipetakan; 5 baris, 1 duplikat, 1 invalid | Import tabel riwayat | 3 baris valid dapat diimpor; 2 bermasalah tidak ditulis | P2 | PRO-FR-009 / PRO-AC-009 |
| PRO-T-101 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | PRO-NFR-001 / PRO-AC-101 |
| PRO-T-102 | nonfungsional | Beban uji dasar dan data telah tersedia | Buka tampilan utama 30 kali | p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | P0 | PRO-NFR-002 / PRO-AC-102 |
| PRO-T-103 | nonfungsional | Form valid dan gangguan koneksi sebelum konfirmasi simpan | Simpan, pulihkan koneksi, lalu retry | Input tetap terlihat; tepat satu revisi tersimpan dan indikator sukses hanya setelah konfirmasi | P0 | PRO-NFR-003 / PRO-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| PRO-Q1 | Daftar program/versi berlaku belum lengkap | Salah roadmap | Curator validasi applicability; default unknown |
| PRO-Q2 | Volume riwayat mahasiswa lanjut | Input berulang | P2 import setelah parser preview tersedia |
| PRO-Q3 | Panduan tidak menetapkan database tertentu; runtime tim belum diuji | Persistensi perlu verifikasi | SQLite direkomendasikan; uji restart dan export/reset sebelum rilis |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Tidak ada auto-import nilai atau verifikasi afiliasi melalui email domain saja. Integrasi kampus baru boleh menggantikan input manual setelah kontrak akses sah tersedia.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: PRO-FR-006, PRO-FR-008, PRO-FR-009. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-01 brief; SRC-02/03 mengonfirmasi konteks program tetapi tidak mengikat angkatan pengguna ke versi kurikulum. D-01, D-02 dan D-04 adalah keputusan produk.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-04 pada audit untuk alasan revisi.

