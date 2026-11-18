# PRD-10 — Authentication, Privacy & Integrations

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-10 / v0.2 DDP1 Draft |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Security & Privacy Owner |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | Local authentication berarti kredensial Orbit yang dikelola aplikasi, bukan password UI. Integrasi resmi belum memiliki kontrak akses terverifikasi. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). |

## 2. Executive Summary & Problem

AUTH memisahkan pembuktian akun, hak akses record, pengambilan data, verifikasi afiliasi dan atribusi publik. Slice DDP1 memakai workspace lokal sintetis; akun Orbit multiuser tetap terdokumentasi sebagai P2. Integrasi campus adalah adapter future yang tidak dibutuhkan untuk fungsi inti.

## 3. Goals, Non-Goals & Success Metrics

Akun tidak saling membuka data, pengguna mengendalikan consent/export/delete, dan gangguan integrasi tidak mengunci workspace.

**Non-goals:** Mengumpulkan password SSO, menyimpulkan prodi/nilai dari login, mengklaim kepatuhan hukum yang belum direview, atau membuat protokol keamanan sendiri.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Isolasi owner | Read/write/export semua entitas dengan akun A/B | Nol kebocoran pada acceptance tests |
| Control lifecycle | Consent off/withdraw/export/delete | 100% aksi memiliki hasil teramati |
| Integrasi tidak wajib | Campus adapters disabled | Semua alur P0 tetap berjalan |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Student/senior/alumni berakun lokal; moderator mengkurasi komunitas; admin mengelola konfigurasi; guest membaca publik.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Guest | Konten published | Private workspace dan moderation queue |
| Student/senior/alumni | CRUD/export/delete milik sendiri; opt-in contribution | Nilai orang lain atau role escalation |
| Moderator | Review approved community payload/text/reports | Raw grade workspace, credential dan identity-link data |
| Admin | Assign role/config/audit minimal dengan re-auth | UI untuk membaca nilai privat by default |
| Integration adapter | Resource scopes yang disetujui | Akses data di luar grant |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Integrasi unavailable; mode demo lokal dan export/reset lokal AUTH-FR-014/015 | Tidak ada layanan akun tambahan | Akun Orbit multiuser, recovery, role, consent/deletion lifecycle, SSO UI, SLCM |

**Slice rilis:** Satu owner_scope lokal, loopback dan data sintetis. Source repo publik tidak berarti aplikasi di-host publik. Sebelum multiuser/data nyata/deployment, paket keamanan akun dan RV-10 harus diverifikasi.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Satu owner_scope lokal, loopback dan data sintetis. Source repo publik tidak berarti aplikasi di-host publik. Sebelum multiuser/data nyata/deployment, paket keamanan akun dan RV-10 harus diverifikasi. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Guest → daftar → tentukan username/password Orbit → simpan recovery code sekali → login → profil. Tidak diminta password SSO. Kehilangan recovery code dan password tidak boleh dipulihkan hanya dari nama/NPM.

**J2.** Settings → Privasi → lihat izin per purpose → export atau withdraw → konfirmasi hasil. Export privacy dasar berbeda dari laporan akademik rapi P2.

**J3.** Settings → Hapus akun → re-auth → preview dampak (profil, nilai, kontribusi, kredit) → confirm → sesi dicabut dan purge dimulai. Halaman status menjelaskan tenggat yang disetujui; tidak menampilkan data personal setelah pencabutan.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| AUTH-US-001 | As a student, I want mengakses akun Orbit dengan aman, so that saya tidak perlu menyerahkan password kampus. | P2 | AUTH-FR-001, AUTH-FR-002, AUTH-FR-003 |
| AUTH-US-002 | As a student, I want mengendalikan data dan izin, so that data hanya dipakai sesuai pilihan. | P2 | AUTH-FR-004, AUTH-FR-005, AUTH-FR-006, AUTH-FR-007 |
| AUTH-US-003 | As a future integrator, I want menautkan akun dan jadwal dengan izin, so that integrasi tidak melampaui scope. | P0 / P2 (per FR) | AUTH-FR-008, AUTH-FR-009, AUTH-FR-010 |
| AUTH-US-004 | As a student, I want mengakhiri sesi kedaluwarsa dan membatasi serangan login, so that akun saya lebih terlindungi. | P2 | AUTH-FR-012, AUTH-FR-013 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AUTH-FR-001 | P2 | Daftar akun lokal | Guest | username unik dan password Orbit | Validasi kredensial dan simpan password hanya sebagai hash adaptif salted melalui primitive teruji | Akun tercipta tanpa password plaintext atau klaim afiliasi UI | AUTH-AC-001 |
| AUTH-FR-002 | P2 | Login/logout | Akun aktif | Kredensial atau sesi | Buat sesi baru saat auth; cabut sesi pada logout; generic error saat gagal | Sesi dicabut tidak dapat mengakses workspace | AUTH-AC-002 |
| AUTH-FR-003 | P2 | Pulihkan akun | User punya recovery code sekali pakai | Code valid lalu code yang sama lagi | Reset credential melalui re-auth setara, rotasi sessions dan kode | Pemakaian pertama berhasil; penggunaan ulang ditolak | AUTH-AC-003 |
| AUTH-FR-004 | P2 | Akses record user lain | Akun A login | grade/export/closeout milik B | Periksa owner dan action pada setiap akses; deny by default | Tidak ada payload B atau indikasi sensitif yang terungkap | AUTH-AC-004 |
| AUTH-FR-005 | P2 | Ekspor data sendiri | Re-auth baru dan owner valid | Pilihan semua data personal | Buat snapshot portable JSON/CSV dengan provenance/consent; tanpa secrets | Hanya data pemilik; tidak termasuk hash/token/recovery code | AUTH-AC-005 |
| AUTH-FR-006 | P2 | Ubah/cabut consent | Consent purpose aktif | purpose dan version | Catat perubahan serta invalidasi publikasi terkait sebelum pembacaan berikutnya | SNR/VLT tidak memakai izin lama; layanan personal tetap tersedia | AUTH-AC-006 |
| AUTH-FR-007 | P2 | Hapus akun | Re-auth dan preview disetujui | delete operation_id | Cabut akses segera dan antrekan purge sesuai retention | Sesi ditolak segera; data aktif terhapus ≤7 hari; backup ≤30 hari | AUTH-AC-007 |
| AUTH-FR-008 | P2 | Link identitas SSO | Provider resmi disetujui dan sesi lokal re-auth | Grant provider dan subject stabil | Tautkan dengan bukti kendali kedua akun; jangan merge hanya karena email sama | Bentrok subject meminta resolusi; no silent account takeover | AUTH-AC-008 |
| AUTH-FR-009 | P2 | Sync jadwal | Grant authorized schedule dan adapter enabled | Jadwal dari sumber resmi | Preview perubahan dan konflik dengan edit manual | Tanpa grant tidak ada sync; kegagalan menyisakan jadwal manual | AUTH-AC-009 |
| AUTH-FR-010 | P0 | Buka integrasi belum tersedia | Tidak ada izin/provider contract | SSO/SLCM control | Tampilkan status belum tersedia dan alternatif input manual di workspace lokal; akun Orbit hanya jika mode P2 diaktifkan | Tidak meminta password kampus atau mencoba scraping | AUTH-AC-010 |
| AUTH-FR-011 | P2 | Ubah role admin/moderator | Admin re-auth | user_id, role, alasan | Validasi hak perubahan role dan audit; user tidak boleh self-elevate | Student gagal menaikkan role sendiri | AUTH-AC-011 |
| AUTH-FR-012 | P2 | Batasi login/recovery gagal | Akun/source mencapai 5 kegagalan dalam 15 menit | Percobaan keenam pada window sama | Terapkan progressive delay dan pesan generik menurut rule aktif | Percobaan tidak diproses tanpa batas; tidak lockout permanen | AUTH-AC-012 |
| AUTH-FR-013 | P2 | Validasi masa sesi | Sesi usia 13 jam, atau idle 31 menit pada fixture default | Akses workspace | Tolak sesi expired sesuai absolute/idle timeout | Re-auth diperlukan; response tidak memuat data privat | AUTH-AC-013 |
| AUTH-FR-014 | P0 | Jalankan demo DDP1 | Mode local-demo; fixture sintetis | Konfigurasi bind, owner_scope dan capability manifest | Gunakan satu owner_scope lokal stabil, bind loopback, nonaktifkan debug pada demo, akun publik dan semua adapter kampus; nyatakan batas data sintetis pada UI/README | Aplikasi dapat berjalan di localhost tanpa login; konfigurasi akses jaringan publik ditolak pada mode ini; tidak ada data nyata/kredensial pada fixture atau repository | AUTH-AC-014 |
| AUTH-FR-015 | P0 | Ekspor atau reset workspace demo | Workspace lokal; pengguna mengonfirmasi reset | Data, provenance, revisions dan pilihan cancel/confirm | Ekspor JSON lokal tanpa secrets; reset hanya setelah preview/konfirmasi; simpan data di luar berkas seed dan tandai database/export runtime tidak dilacak Git | Restart mempertahankan input dan owner_scope; cancel reset tidak mengubah data; confirm mengosongkan data lokal, seed tetap; ekspor memuat versi dan provenance tanpa secrets | AUTH-AC-015 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| AUTH-BR-001 | Authentication membuktikan kendali akun; authorization memeriksa action+ownership; data access memerlukan scope sumber; verification afiliasi memerlukan bukti. Keempatnya tidak saling mengimplikasikan. | AUTH-FR-001, AUTH-FR-004, AUTH-FR-008, AUTH-FR-009 |
| AUTH-BR-002 | Usulan mode akun P2 tanpa MFA: password minimal 15 karakter, maksimum yang didukung sekurangnya 64; izinkan paste/password manager. Jangan mewajibkan pergantian berkala tanpa alasan risiko. Hash/token tidak dicatat di log. | AUTH-FR-001, AUTH-FR-003 |
| AUTH-BR-003 | Session defaults usulan: idle 30 menit, absolute 12 jam; rotasi setelah login/reset/privilege change. Transport terenkripsi; token dilindungi dari akses script dan pengiriman lintas situs yang tidak sah sesuai mekanisme stack yang dipilih nanti. | AUTH-FR-002, AUTH-FR-011, AUTH-FR-013 |
| AUTH-BR-004 | Retention produk usulan: data aktif sampai user menghapus; delete/withdraw raw ≤7 hari; backup bergulir ≤30 hari dan tombstone diterapkan saat restore; security/consent audit minimal 90 hari tanpa nilai/kredensial mentah. Ini usulan operasional, bukan klaim kewajiban hukum. | AUTH-FR-006, AUTH-FR-007 |
| AUTH-BR-005 | Consent mencatat purpose, selected fields, text version, granted_at/revoked_at dan projection status. Atribusi publik terpisah dari linkage identitas dan izin skor/topik. | AUTH-FR-006 |
| AUTH-BR-006 | Recovery code high-entropy, sekali tampil, hanya hash yang disimpan, single-use. Tanpa faktor pemulihan yang sah, admin tidak boleh reset berdasarkan klaim identitas informal; ekspor/backup pengguna dapat mengurangi kehilangan. | AUTH-FR-003, AUTH-FR-005 |
| AUTH-BR-007 | Rate limiting login/recovery diterapkan per akun dan sumber untuk menahan brute force; angka default usulan 5 kegagalan/15 menit lalu progressive delay, bukan lockout permanen yang mudah disalahgunakan. | AUTH-FR-002, AUTH-FR-003, AUTH-FR-012 |
| AUTH-BR-008 | Integrasi off secara default. Login SSO hanya memasok claims yang benar-benar diberikan; tidak menjamin prodi, angkatan, jadwal atau nilai. Protokol/endpoints belum dipilih. | AUTH-FR-008, AUTH-FR-009, AUTH-FR-010 |
| AUTH-BR-009 | Saat sync future, field yang diedit manual setelah last_sync tidak ditimpa; preview diff menampilkan sumber dan pilihan. Cabut grant memutus sync tanpa menghapus jadwal manual. | AUTH-FR-009 |
| AUTH-BR-010 | Export/download hanya pemilik dengan re-auth; artefak sementara dihapus usulan ≤24 jam, tidak memiliki tautan publik permanen. Laporan akademik berformat rapi berbeda scope. | AUTH-FR-005 |

### Threat model ringkas

| Ancaman | Aset / kontrol produk | Verifikasi |
| --- | --- | --- |
| ID record ditebak | Owner authorization pada setiap read/write/export | AUTH-T-004 |
| Credential stuffing / takeover | Hash teruji, rate limit, session rotation, re-auth | AUTH-T-001/002/003 |
| XSS di tips/feedback | Plain-text atau sanitasi aman, no executable embed; session protected | VLT-T-009 dan SUP-T-005 ditambah security review Prompt 2 |
| CSRF pada perubahan | Validasi request state-changing sesuai mekanisme auth | Security review dan AUTH-AC-103 |
| URL resource berbahaya / SSRF | HTTPS allowlist; tidak server-fetch pada P0 | VLT-T-002/010 |
| Small-cell reidentification | Fixed cells, suppression, consent dan no raw export | SNR-T-004/007 |
| Backup menghidupkan akun terhapus | Deletion tombstone diterapkan sebelum layanan restore | AUTH-AC-102 |

**Skenario:** akun alumni lokal tetap dapat berkontribusi tanpa UI SSO. Jika suatu hari SSO tersedia, subject provider yang sama tidak boleh ditautkan ke dua akun aktif. Email cocok saja tidak cukup. SLCM unavailable → jadwal manual tetap berfungsi.

**Batas operasional:** keamanan multiuser tidak boleh diganti password plaintext demi rubrik. Jika platform yang diizinkan belum mampu memenuhi kontrol mode akun P2, demo harus memakai data sintetis dan akses terbatas sampai arsitektur aman disetujui; jangan mengumpulkan nilai nyata.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| Account / user_id | username normalized, account_status; tidak memakai NPM sebagai ID | AUTH | active/locked/deletion_requested/deleted | Restricted |
| Credential / credential_id | password hash, recovery code hash; no plaintext | AUTH primitive teruji | rotated/revoked | Restricted |
| Session / session_id | owner, issued/last_seen/expires, privilege revision | AUTH | active/revoked/expired | Restricted |
| Consent / consent_id | user,purpose,field set,version,granted/revoked | User/AUTH | Append changes; purge per policy | Restricted |
| PublicIdentityPreference | display name opt-in; identity verified separately | User | Projection updated/revoked | Private control / Public approved projection |
| IntegrationGrant / grant_id | provider subject, scopes, expires, connection status | User + authorized provider | linked/revoked/expired | Restricted |
| DeletionRequest / request_id | owner,scope,operation_id,progress,tombstone | User/AUTH | requested/access_revoked/purged | Restricted minimal audit |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Form menyebut “Password akun Orbit”, tidak “password UI”. Recovery code diberi langkah unduh/catat dengan penjelasan hanya muncul sekali. Settings memisahkan akun, privasi, data, kredit publik dan integrasi. Integrasi yang belum ada bukan tombol login aktif. Delete flow menampilkan konsekuensi pada kontribusi dan file Drive (tidak dihapus). Export menampilkan data yang termasuk dan provenance. Error auth generik; jangan mengungkap apakah username tertentu terdaftar.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| Expired session | Login ulang tanpa data akun lain | Simpan draft hanya untuk owner aman |
| Repeated failures | Delay dan recovery sah | Tidak lockout permanen |
| Missing recovery | Jelaskan akun tidak dapat dipulihkan informal | Tidak meminta password kampus |
| Grant revoked | Sync berhenti | Manual data tetap |
| Delete pending | Akses sudah dicabut | Purge idempotent |
| Permission denied | Pesan umum | Jangan mengungkap metadata target |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** P0 menyediakan owner_scope lokal via AUTH-FR-014, bukan token login. AUTH-FR-015 mengatur export/reset lokal. Kontrak akun, permission banyak pengguna, consent, publication dan deletion terjadwal pada tabel berikut berlaku P2; source repository tetap publik. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| AUTH-FR-001 → PRO-FR-001 | AccountCreated user_id only | No academic claims inferred |
| AUTH-FR-006 → SNR-FR-007/VLT-FR-006 | ConsentRevoked versioned | Hide public projection before background cleanup |
| AUTH-FR-007 → semua domain | DeletionRequested/tombstone scope | Retries idempotent; restore respects deletion |
| AUTH-FR-009 → SCH-FR-002 | Future authorized schedule changes | Manual conflict preview, no password proxy |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Privacy by default berlaku sejak akun baru. Admin operasional mungkin punya tanggung jawab infrastruktur, tetapi tidak diberi akses isi nilai melalui fitur admin; akses darurat bila kelak dibutuhkan memerlukan tujuan, otorisasi dan audit terpisah. Penilaian kepatuhan hukum dan lokasi penyimpanan ditunda sampai operator/deployment diketahui; tidak ada klaim compliance otomatis.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| AUTH-NFR-001 | P0 | Semua entitas privat lulus pengujian owner A/B pada read, edit, list dan export. | AUTH-AC-101 |
| AUTH-NFR-002 | P0 | Restore tidak menghidupkan data yang sudah diminta dihapus. | AUTH-AC-102 |
| AUTH-NFR-003 | P0 | Mutasi workspace lokal, sesi atau akun memerlukan validasi request terhadap pemalsuan; secret dan nilai mentah tidak bocor di log. | AUTH-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata. AUTH-NFR-001/002 dan AUTH-T-101/102 ditunda bersama layanan akun P2; AUTH-NFR-003 tetap berlaku untuk mutasi lokal (validasi request/origin dan tanpa secret di log), bukan bukti autentikasi multiuser.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| AUTH-AC-001 | Given Guest; username unik dan password Orbit | When Daftar akun lokal | Then Akun tercipta tanpa password plaintext atau klaim afiliasi UI | AUTH-FR-001 |
| AUTH-AC-002 | Given Akun aktif; Kredensial atau sesi | When Login/logout | Then Sesi dicabut tidak dapat mengakses workspace | AUTH-FR-002 |
| AUTH-AC-003 | Given User punya recovery code sekali pakai; Code valid lalu code yang sama lagi | When Pulihkan akun | Then Pemakaian pertama berhasil; penggunaan ulang ditolak | AUTH-FR-003 |
| AUTH-AC-004 | Given Akun A login; grade/export/closeout milik B | When Akses record user lain | Then Tidak ada payload B atau indikasi sensitif yang terungkap | AUTH-FR-004 |
| AUTH-AC-005 | Given Re-auth baru dan owner valid; Pilihan semua data personal | When Ekspor data sendiri | Then Hanya data pemilik; tidak termasuk hash/token/recovery code | AUTH-FR-005 |
| AUTH-AC-006 | Given Consent purpose aktif; purpose dan version | When Ubah/cabut consent | Then SNR/VLT tidak memakai izin lama; layanan personal tetap tersedia | AUTH-FR-006 |
| AUTH-AC-007 | Given Re-auth dan preview disetujui; delete operation_id | When Hapus akun | Then Sesi ditolak segera; data aktif terhapus ≤7 hari; backup ≤30 hari | AUTH-FR-007 |
| AUTH-AC-008 | Given Provider resmi disetujui dan sesi lokal re-auth; Grant provider dan subject stabil | When Link identitas SSO | Then Bentrok subject meminta resolusi; no silent account takeover | AUTH-FR-008 |
| AUTH-AC-009 | Given Grant authorized schedule dan adapter enabled; Jadwal dari sumber resmi | When Sync jadwal | Then Tanpa grant tidak ada sync; kegagalan menyisakan jadwal manual | AUTH-FR-009 |
| AUTH-AC-010 | Given Tidak ada izin/provider contract; SSO/SLCM control | When Buka integrasi belum tersedia | Then Tidak meminta password kampus atau mencoba scraping | AUTH-FR-010 |
| AUTH-AC-011 | Given Admin re-auth; user_id,role,alasan | When Ubah role admin/moderator | Then Student gagal menaikkan role sendiri | AUTH-FR-011 |
| AUTH-AC-012 | Given Akun/source mencapai5 kegagalan dalam15 menit; Percobaan keenam pada window sama | When Batasi login/recovery gagal | Then Percobaan tidak diproses tanpa batas; tidak lockout permanen | AUTH-FR-012 |
| AUTH-AC-013 | Given Sesi usia13 jam, atau idle31 menit pada fixture default; Akses workspace | When Validasi masa sesi | Then Re-auth diperlukan; response tidak memuat data privat | AUTH-FR-013 |
| AUTH-AC-101 | Given Dua akun dengan data berbeda | When Coba akses silang langsung dan lewat search | Then Nol data/metadata privat keluar; deny konsisten | AUTH-NFR-001 |
| AUTH-AC-102 | Given Backup sebelum delete, tombstone setelah delete | When Restore ke lingkungan uji | Then Tombstone diterapkan sebelum akses pengguna; data terhapus tetap tidak terbaca | AUTH-NFR-002 |
| AUTH-AC-103 | Given workspace lokal aktif (atau sesi akun P2), request lintas origin dan log capture | When uji mutasi palsu serta export/reset lokal; login/reset akun hanya bila P2 aktif | Then request mutasi palsu ditolak; log tidak memuat secrets atau nilai mentah; export sah tidak memuat secret | AUTH-NFR-003 |
| AUTH-AC-014 | Given Mode local-demo; fixture sintetis; Konfigurasi bind, owner_scope dan capability manifest | When Jalankan demo DDP1 | Then Aplikasi dapat berjalan di localhost tanpa login; konfigurasi akses jaringan publik ditolak pada mode ini; tidak ada data nyata/kredensial pada fixture atau repository | AUTH-FR-014 |
| AUTH-AC-015 | Given Workspace lokal; pengguna mengonfirmasi reset; Data, provenance, revisions dan pilihan cancel/confirm | When Ekspor atau reset workspace demo | Then Restart mempertahankan input dan owner_scope; cancel reset tidak mengubah data; confirm mengosongkan data lokal, seed tetap; ekspor memuat versi dan provenance tanpa secrets | AUTH-FR-015 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| AUTH-T-001 | fungsional | Guest; username unik dan password Orbit | Daftar akun lokal | Akun tercipta tanpa password plaintext atau klaim afiliasi UI | P2 | AUTH-FR-001 / AUTH-AC-001 |
| AUTH-T-002 | keamanan | Akun aktif; Kredensial atau sesi | Login/logout | Sesi dicabut tidak dapat mengakses workspace | P2 | AUTH-FR-002 / AUTH-AC-002 |
| AUTH-T-003 | boundary | User punya recovery code sekali pakai; Code valid lalu code yang sama lagi | Pulihkan akun | Pemakaian pertama berhasil; penggunaan ulang ditolak | P2 | AUTH-FR-003 / AUTH-AC-003 |
| AUTH-T-004 | keamanan | Akun A login; grade/export/closeout milik B | Akses record user lain | Tidak ada payload B atau indikasi sensitif yang terungkap | P2 | AUTH-FR-004 / AUTH-AC-004 |
| AUTH-T-005 | privasi | Re-auth baru dan owner valid; Pilihan semua data personal | Ekspor data sendiri | Hanya data pemilik; tidak termasuk hash/token/recovery code | P2 | AUTH-FR-005 / AUTH-AC-005 |
| AUTH-T-006 | integrasi | Consent purpose aktif; purpose dan version | Ubah/cabut consent | SNR/VLT tidak memakai izin lama; layanan personal tetap tersedia | P2 | AUTH-FR-006 / AUTH-AC-006 |
| AUTH-T-007 | privasi | Re-auth dan preview disetujui; delete operation_id | Hapus akun | Sesi ditolak segera; data aktif terhapus ≤7 hari; backup ≤30 hari | P2 | AUTH-FR-007 / AUTH-AC-007 |
| AUTH-T-008 | keamanan | Provider resmi disetujui dan sesi lokal re-auth; Grant provider dan subject stabil | Link identitas SSO | Bentrok subject meminta resolusi; no silent account takeover | P2 | AUTH-FR-008 / AUTH-AC-008 |
| AUTH-T-009 | fungsional | Grant authorized schedule dan adapter enabled; Jadwal dari sumber resmi | Sync jadwal | Tanpa grant tidak ada sync; kegagalan menyisakan jadwal manual | P2 | AUTH-FR-009 / AUTH-AC-009 |
| AUTH-T-010 | negatif | Tidak ada izin/provider contract; SSO/SLCM control | Buka integrasi belum tersedia | Tidak meminta password kampus atau mencoba scraping | P0 | AUTH-FR-010 / AUTH-AC-010 |
| AUTH-T-011 | keamanan | Admin re-auth; user_id, role, alasan | Ubah role admin/moderator | Student gagal menaikkan role sendiri | P2 | AUTH-FR-011 / AUTH-AC-011 |
| AUTH-T-012 | keamanan | Akun/source mencapai 5 kegagalan dalam 15 menit; Percobaan keenam pada window sama | Batasi login/recovery gagal | Percobaan tidak diproses tanpa batas; tidak lockout permanen | P2 | AUTH-FR-012 / AUTH-AC-012 |
| AUTH-T-013 | boundary | Sesi usia 13 jam, atau idle 31 menit pada fixture default; Akses workspace | Validasi masa sesi | Re-auth diperlukan; response tidak memuat data privat | P2 | AUTH-FR-013 / AUTH-AC-013 |
| AUTH-T-101 | nonfungsional | Dua akun dengan data berbeda | Coba akses silang langsung dan lewat search | Nol data/metadata privat keluar; deny konsisten | P0 | AUTH-NFR-001 / AUTH-AC-101 |
| AUTH-T-102 | nonfungsional | Backup sebelum delete, tombstone setelah delete | Restore ke lingkungan uji | Tombstone diterapkan sebelum akses pengguna; data terhapus tetap tidak terbaca | P0 | AUTH-NFR-002 / AUTH-AC-102 |
| AUTH-T-103 | nonfungsional | Workspace lokal atau sesi P2; request lintas origin; log capture | Kirim mutasi palsu, lalu export/reset sah; login/reset akun hanya bila P2 aktif | Mutasi palsu ditolak; log tanpa secret/nilai mentah dan export tanpa secret | P0 | AUTH-NFR-003 / AUTH-AC-103 |
| AUTH-T-014 | integrasi/negatif | Mode local-demo; fixture sintetis; Konfigurasi bind, owner_scope dan capability manifest | Jalankan demo DDP1 | Aplikasi dapat berjalan di localhost tanpa login; konfigurasi akses jaringan publik ditolak pada mode ini; tidak ada data nyata/kredensial pada fixture atau repository | P0 | AUTH-FR-014 / AUTH-AC-014 |
| AUTH-T-015 | integrasi/negatif | Workspace lokal; pengguna mengonfirmasi reset; Data, provenance, revisions dan pilihan cancel/confirm | Ekspor atau reset workspace demo | Restart mempertahankan input dan owner_scope; cancel reset tidak mengubah data; confirm mengosongkan data lokal, seed tetap; ekspor memuat versi dan provenance tanpa secrets | P0 | AUTH-FR-015 / AUTH-AC-015 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| AUTH-Q1 | Python utama telah ditetapkan panduan; pilihan runtime/version belum diuji tim | Implementasi keamanan masih perlu verifikasi | Flask lokal direkomendasikan; tidak membuka layanan multiuser sebelum gate terkait |
| AUTH-Q2 | Kontrak SSO/SLCM tidak ada | Integrasi tak dapat dijanjikan | Off; izin resmi dan dokumentasi diperlukan |
| AUTH-Q3 | Operator, hosting, retention belum disetujui | Risiko privasi operasional | Data sintetis hingga review deployment |
| AUTH-Q4 | Recovery akun hanya relevan pada mode multiuser P2 | Akun hilang jika kode hilang | Pertahankan recovery code dan export akun; P0 memakai export/reset lokal |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

SSO UI, account linking dan SLCM adalah P2 gated external approval. Tidak ada scraping tanpa otorisasi, password proxy, raw grade analytics atau credential sharing.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: AUTH-FR-001, AUTH-FR-002, AUTH-FR-003, AUTH-FR-004, AUTH-FR-005, AUTH-FR-006, AUTH-FR-007, AUTH-FR-008, AUTH-FR-009, AUTH-FR-011, AUTH-FR-012, AUTH-FR-013. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-09 OWASP Authentication dan SRC-10 Authorization diperiksa untuk prinsip kontrol; angka session/rate/retention adalah PRODUCT_ASSUMPTION D-12, bukan kutipan standar. SRC-01 membatasi integrasi kampus.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-04/AUD-13 pada audit untuk alasan revisi.

