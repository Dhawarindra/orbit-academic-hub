# PRD-12 — Search, Feedback & Supporting Features

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-12 / v0.2.1 DDP1 Errata |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Supporting Features Product Owner |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | P1 memakai pencarian metadata sederhana; tidak perlu full-text Drive, ML ranking, email atau push. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). v0.2.1: errata prioritas/journey dari review independen; FR dan ID tetap. |

## 2. Executive Summary & Problem

Fitur pendukung membantu menemukan course/resource, menyimpan bookmark dan melaporkan masalah tanpa menambah ketergantungan berat. Search menghormati izin sebelum hasil, snippet maupun jumlah ditampilkan.

## 3. Goals, Non-Goals & Success Metrics

Pengguna menemukan objek relevan, mempertahankan konteks kembali, dan mendapat nomor pelacakan feedback tanpa mengungkap nilai privat.

**Non-goals:** Mencari seluruh isi Drive, mengindeks grade personal ke pencarian publik, menjanjikan helpdesk 24/7 atau mengirim digest tanpa opt-in.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Relevansi exact match | Query kode course yang ada | Hasil exact code di posisi pertama |
| Isolasi hasil | Guest vs owner vs moderator | Nol hasil/snippet/count dari data tanpa izin |
| Keandalan feedback | Retry setelah timeout | Tepat satu report dengan tracking ID |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Guest mencari course, mahasiswa menyimpan materi, moderator memilah laporan, dan pengguna melaporkan bug tanpa mengunggah data sensitif.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Guest | Cari metadata public; baca help; kirim feedback terbatas | Private bookmarks/drafts |
| Student | Search public dan bookmarks sendiri | Draft/resource/feedback orang lain |
| Moderator | Queue report sesuai tugas | Menelusuri raw grade melalui search |
| Admin/editor | Changelog dan preferences schema | Private query history sebagai analytics mentah |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Tidak ada fitur pendukung terpisah yang menghalangi P0 | Search metadata/filter, help dan changelog dalam aplikasi | Bookmark, feedback/tracking/moderation, preferences/digest dan laporan akademik rapi |

**Slice rilis:** Jika Vault P1 diaktifkan: exact/prefix/token search serta filter hanya metadata published; tanpa email, crawler atau layanan pencarian eksternal. Changelog repository tetap diperlukan sebagai rekomendasi kualitas meski UI changelog ditunda.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Jika Vault P1 diaktifkan: exact/prefix/token search serta filter hanya metadata published; tanpa email, crawler atau layanan pencarian eksternal. Changelog repository tetap diperlukan sebagai rekomendasi kualitas meski UI changelog ditunda. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Header search → input query → enter → hasil berkelompok course/topic/resource → filter → pilih → kembali mempertahankan query. Query kosong menampilkan prompt, bukan semua data privat.

**J2.** Resource → bookmark → daftar tersimpan → resource ditarik → tampil tidak tersedia dengan hapus bookmark. Tidak membocorkan metadata resource yang telah hidden.

**J3.** Bantuan → Laporkan masalah → pilih kategori, tulis langkah reproduksi tanpa nilai/password → preview → submit → tracking ID. Bila network timeout, retry memakai operasi sama dan menampilkan report existing.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| SUP-US-001 | As a student, I want mencari course dan materi, so that saya mencapai sumber relevan. | P1 | SUP-FR-001, SUP-FR-002, SUP-FR-003 |
| SUP-US-002 | As a student, I want menyimpan resource dan mengatur preferensi, so that penggunaan berikutnya lebih mudah. | P2 | SUP-FR-004, SUP-FR-007 |
| SUP-US-003 | As a user, I want melaporkan masalah dan membaca perubahan, so that saya mengerti status aplikasi. | P1 / P2 (per FR) | SUP-FR-005, SUP-FR-006, SUP-FR-008 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SUP-FR-001 | P1 | Submit search | User/guest sesuai izin | Query code/name/topic/resource metadata | Filter authorization dan visibility sebelum ranking/snippet/count | Hidden/draft tidak muncul atau memengaruhi count | SUP-AC-001 |
| SUP-FR-002 | P1 | Urutkan hasil | Ada exact dan partial match | Query DEMO-A | Prioritaskan exact code lalu prefix title lalu token match | DEMO-A exact tampil sebelum teks yang hanya menyebutnya | SUP-AC-002 |
| SUP-FR-003 | P1 | Pakai filter | Query aktif | course/topic/year/type | Gabungkan filter dengan AND dan pertahankan saat kembali | Zero result memberi reset filter; bukan error | SUP-AC-003 |
| SUP-FR-004 | P2 | Bookmark/unbookmark | Akun aktif | resource_id sama dua kali | Terapkan unique owner+resource; deleted/hidden jadi tombstone | Tidak duplikat; hidden tidak menampilkan metadata lama | SUP-AC-004 |
| SUP-FR-005 | P2 | Submit feedback | Form valid | category, description, steps optional; operation_id | Simpan teks aman dan tracking ID; tidak meminta data nilai/password | Retry operation_id sama mengembalikan report sama | SUP-AC-005 |
| SUP-FR-006 | P1 | Baca help | Guest/user | Topik bobot/kurikulum/akses resource | Tampilkan artikel sesuai versi UI dan tautan terkait | User menemukan penjelasan dan kembali ke layar asal | SUP-AC-006 |
| SUP-FR-007 | P2 | Simpan preferences | Akun aktif | timezone/theme/locale supported | Delegasikan ke owner PRO/UX; jangan buat profil duplikat | Perubahan konsisten pada halaman terkait | SUP-AC-007 |
| SUP-FR-008 | P1 | Buka changelog | Release content published | version, date, changes, known limits | Tampilkan perubahan yang benar-benar dirilis dan batasnya | Fitur future tetap labeled planned | SUP-AC-008 |
| SUP-FR-009 | P2 | Aktifkan weekly digest | Infrastruktur tersedia dan opt-in eksplisit | frequency,channel,quiet preferences | Preview isi/rentang data dan simpan consent notifikasi tersendiri | Tanpa opt-in tidak ada kiriman; opt-out menghentikan berikutnya | SUP-AC-009 |
| SUP-FR-010 | P2 | Ekspor laporan akademik rapi | Owner dan re-auth | Term dan jenis hasil selected | Beri label actual/projection/scenario, policy dan as-of | Laporan tidak disebut transkrip resmi; ekspor lokal AUTH-FR-015 P0 tetap tersedia, ekspor akun AUTH-FR-005 mengikuti mode multiuser P2 | SUP-AC-010 |
| SUP-FR-011 | P2 | Render feedback tersimpan | Moderator membuka report | Description berisi tag script dan link berbahaya sebagai teks | Tampilkan plain text tanpa eksekusi atau auto-fetch link | Tidak menjalankan script dan tidak memanggil URL dari isi report | SUP-AC-011 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| SUP-BR-001 | Saat search aktif (P1), corpus terdiri dari published Course/CurriculumCourse, Topic dan Resource metadata. Tidak ada grade, nama pemilik akun, contribution raw, feedback atau isi Drive dalam global search. | SUP-FR-001 |
| SUP-BR-002 | Normalisasi whitespace/case dan alias terkurasi; query literal tidak dieksekusi sebagai markup. Query 1–100 karakter; debounce usulan 300ms jika live, Enter selalu tersedia. | SUP-FR-001, SUP-FR-002 |
| SUP-BR-003 | Ranking deterministik exact code → title prefix → token title/topic → description; tie tipe course sebelum topic sebelum resource, lalu title dan stable ID. | SUP-FR-002 |
| SUP-BR-004 | Filter AND; per-page 20 hasil usulan. Scope izin diterapkan sebelum totals/pagination agar count tidak membocorkan draft. | SUP-FR-001, SUP-FR-003 |
| SUP-BR-005 | Bookmark milik SUP dengan owner+resource unique; VLT menyediakan aksi. Withdrawal resource mengubah view menjadi tombstone tanpa mempertahankan metadata terlarang di UI. | SUP-FR-004 |
| SUP-BR-006 | Feedback P2 plain text, kategori bug/content/accessibility/idea, description 10–2.000 karakter; steps optional. Attachment tidak termasuk scope feedback awal. Guest diberi receipt secret berentropi untuk mengecek laporan sendiri bila status view diaktifkan. | SUP-FR-005, SUP-FR-011 |
| SUP-BR-007 | Status report: received → triaged → in_progress/resolved/closed; receipt bukan janji SLA. Abuse control usulan 5 submit/10 menit per akun/sumber dengan jalur retry, tidak mengirim email otomatis. | SUP-FR-005 |
| SUP-BR-008 | Preferensi punya owner tunggal PRO/UX; help/changelog PUB/SUP editorial. Ekspor workspace lokal AUTH-FR-015 P0 tidak ditunda oleh laporan akademik rapi P2; ekspor akun AUTH-FR-005 berlaku dalam mode multiuser P2. | SUP-FR-006, SUP-FR-007, SUP-FR-008, SUP-FR-010 |
| SUP-BR-009 | Notifikasi/digest P2 memiliki consent channel terpisah, unsubscribe dan isi minimum; tidak mengirim grade ke kanal eksternal secara default. | SUP-FR-009 |

**Search fixture:** course code DEMO-A berjudul Algoritma Dasar, resource berjudul Latihan DEMO-A, dan draft resource berjudul DEMO-A Rahasia. Query DEMO-A menampilkan course lebih dahulu lalu resource published; draft tidak tampil dan tidak menambah jumlah hasil. Filter tipe catatan yang tidak cocok menghasilkan 0 hasil dengan tombol Reset filter.

**Feedback fixture:** satu submit sukses di penyimpanan tetapi respons timeout. Retry id operasi yang sama mengembalikan report awal, bukan dua tiket. Teks seperti tag script ditampilkan literal/tersanitasi, tidak dieksekusi.

**Export:** data portabel lokal P0 diatur AUTH-FR-015; export akun multiuser tetap AUTH-FR-005 P2. Laporan yang dirancang untuk presentasi/unduh sebagai rapor pribadi adalah P2; tetap bukan dokumen akademik resmi.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| SearchProjection / source_id+revision | type,title,tokens,scope,status,course/topic refs | Source domain owns; SUP indexes | Recompute/hide on source events | Public eligible metadata |
| Bookmark / bookmark_id | owner,resource_id,created_at | SUP | active/tombstone/deleted | Private |
| Feedback / feedback_id | owner optional,receipt hash,category,description,status,operation_id | User/moderator | received/triaged/resolved/closed | Private |
| HelpArticle & ChangelogEntry | content_id,UI version,published_at,reviewer | Editor | draft/published/retired | Public |
| DigestPreference / preference_id | owner,channel,frequency,consent ref | User future | off/opted_in/revoked | Private |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Header menyediakan search berlabel dan shortcut opsional, bukan satu-satunya cara menemukan fitur. Hasil dikelompokkan dengan badge tipe, source status, filters dan jumlah hasil yang telah difilter izin. Saved resources memakai list ringkas. Feedback form menampilkan pengingat singkat agar tidak memasukkan password/nilai/transkrip dan kategori yang mudah dipilih. Hasil submit menampilkan tracking ID serta langkah berikut tanpa janji waktu. Changelog menampilkan versi/tanggal dan known limitations.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| Query empty | Petunjuk search | Tidak enumerasi private objects |
| No results | Reset filter atau ubah kata | Tidak mengarang rekomendasi |
| Source hidden during search | Hilangkan pada open/refetch | Tidak tampil stale sensitive snippet |
| Duplicate bookmark | Tampilkan tersimpan | Tidak duplicate |
| Feedback timeout | Retry aman | Tracking ID tetap sama |
| Digest unavailable | Kontrol tidak aktif dengan penjelasan | Tidak opt-in semu |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** Search/help/changelog opsional P1; bookmark/feedback/preferences P2. Search P1 memakai metadata published yang dikurasi; tidak membutuhkan akun publik. Export lokal minimum dimiliki AUTH-FR-015, bukan SUP-FR-010. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| MAP-FR-001/VLT-FR-001 → SUP-FR-001 | Published metadata changed | Search rechecks visibility at read, even stale index |
| VLT-FR-004/007 → SUP-FR-004 | Bookmark intent / withdrawal | Tombstone and permission filter |
| PUB-FR-008 → SUP-FR-005 | Feedback context minimal | No email send side effect |
| SUP-FR-007 → PRO-FR-007/UX-FR-010 | Preference write to canonical owner | Unknown theme rejected; no duplicate state |
| SUP-FR-010 → AUTH-FR-005 | Owner export gate | P2 formatting does not block P0 privacy export |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Search query tidak disimpan sebagai histori identitas pada search P1; observability hanya latency/error tanpa query mentah. Feedback privat dan tidak muncul di global search. Credit publik tidak memberikan izin mengindeks akun pribadi. Notifikasi tidak memiliki consent implied dari registrasi.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| SUP-NFR-001 | P0 | Search metadata 1.000 resource +100 course p95 ≤500 ms setelah corpus tersedia. | SUP-AC-101 |
| SUP-NFR-002 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | SUP-AC-102 |
| SUP-NFR-003 | P0 | Kegagalan simpan tidak menghapus input; retry dengan identitas operasi sama tidak menghasilkan duplikasi. | SUP-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| SUP-AC-001 | Given User/guest sesuai izin; Query code/name/topic/resource metadata | When Submit search | Then Hidden/draft tidak muncul atau memengaruhi count | SUP-FR-001 |
| SUP-AC-002 | Given Ada exact dan partial match; Query DEMO-A | When Urutkan hasil | Then DEMO-A exact tampil sebelum teks yang hanya menyebutnya | SUP-FR-002 |
| SUP-AC-003 | Given Query aktif; course/topic/year/type | When Pakai filter | Then Zero result memberi reset filter; bukan error | SUP-FR-003 |
| SUP-AC-004 | Given Akun aktif; resource_id sama dua kali | When Bookmark/unbookmark | Then Tidak duplikat; hidden tidak menampilkan metadata lama | SUP-FR-004 |
| SUP-AC-005 | Given Form valid; category,description,steps optional; operation_id | When Submit feedback | Then Retry operation_id sama mengembalikan report sama | SUP-FR-005 |
| SUP-AC-006 | Given Guest/user; Topik bobot/kurikulum/akses resource | When Baca help | Then User menemukan penjelasan dan kembali ke layar asal | SUP-FR-006 |
| SUP-AC-007 | Given Akun aktif; timezone/theme/locale supported | When Simpan preferences | Then Perubahan konsisten pada halaman terkait | SUP-FR-007 |
| SUP-AC-008 | Given Release content published; version,date,changes,known limits | When Buka changelog | Then Fitur future tetap labeled planned | SUP-FR-008 |
| SUP-AC-009 | Given Infrastruktur tersedia dan opt-in eksplisit; frequency,channel,quiet preferences | When Aktifkan weekly digest | Then Tanpa opt-in tidak ada kiriman; opt-out menghentikan berikutnya | SUP-FR-009 |
| SUP-AC-010 | Given Owner dan re-auth; Term dan jenis hasil selected | When Ekspor laporan akademik rapi | Then Laporan tidak disebut transkrip resmi; ekspor lokal AUTH-FR-015 P0 tetap tersedia, ekspor akun AUTH-FR-005 mengikuti mode multiuser P2 | SUP-FR-010 |
| SUP-AC-011 | Given Moderator membuka report; Description berisi tag script dan link berbahaya sebagai teks | When Render feedback tersimpan | Then Tidak menjalankan script dan tidak memanggil URL dari isi report | SUP-FR-011 |
| SUP-AC-101 | Given Query exact,zero-result dan filtered | When Jalankan masing-masing 30 kali | Then p95 ≤500 ms; tidak bypass permission demi performa | SUP-NFR-001 |
| SUP-AC-102 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | SUP-NFR-002 |
| SUP-AC-103 | Given Form valid dan gangguan koneksi sebelum konfirmasi simpan | When Simpan, pulihkan koneksi, lalu retry | Then Input tetap terlihat; tepat satu revisi tersimpan dan indikator sukses hanya setelah konfirmasi | SUP-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| SUP-T-001 | privasi | User/guest sesuai izin; Query code/name/topic/resource metadata | Submit search | Hidden/draft tidak muncul atau memengaruhi count | P1 | SUP-FR-001 / SUP-AC-001 |
| SUP-T-002 | fungsional | Ada exact dan partial match; Query DEMO-A | Urutkan hasil | DEMO-A exact tampil sebelum teks yang hanya menyebutnya | P1 | SUP-FR-002 / SUP-AC-002 |
| SUP-T-003 | edge | Query aktif; course/topic/year/type | Pakai filter | Zero result memberi reset filter; bukan error | P1 | SUP-FR-003 / SUP-AC-003 |
| SUP-T-004 | boundary | Akun aktif; resource_id sama dua kali | Bookmark/unbookmark | Tidak duplikat; hidden tidak menampilkan metadata lama | P2 | SUP-FR-004 / SUP-AC-004 |
| SUP-T-005 | integrasi | Form valid; category, description, steps optional; operation_id | Submit feedback | Retry operation_id sama mengembalikan report sama | P2 | SUP-FR-005 / SUP-AC-005 |
| SUP-T-006 | fungsional | Guest/user; Topik bobot/kurikulum/akses resource | Baca help | User menemukan penjelasan dan kembali ke layar asal | P1 | SUP-FR-006 / SUP-AC-006 |
| SUP-T-007 | integrasi | Akun aktif; timezone/theme/locale supported | Simpan preferences | Perubahan konsisten pada halaman terkait | P2 | SUP-FR-007 / SUP-AC-007 |
| SUP-T-008 | fungsional | Release content published; version, date, changes, known limits | Buka changelog | Fitur future tetap labeled planned | P1 | SUP-FR-008 / SUP-AC-008 |
| SUP-T-009 | privasi | Infrastruktur tersedia dan opt-in eksplisit; frequency,channel,quiet preferences | Aktifkan weekly digest | Tanpa opt-in tidak ada kiriman; opt-out menghentikan berikutnya | P2 | SUP-FR-009 / SUP-AC-009 |
| SUP-T-010 | fungsional | Owner dan re-auth; Term dan jenis hasil selected | Ekspor laporan akademik rapi | Laporan tidak disebut transkrip resmi; ekspor lokal AUTH-FR-015 P0 tetap tersedia, ekspor akun AUTH-FR-005 mengikuti mode multiuser P2 | P2 | SUP-FR-010 / SUP-AC-010 |
| SUP-T-011 | keamanan | Moderator membuka report; Description berisi tag script dan link berbahaya sebagai teks | Render feedback tersimpan | Tidak menjalankan script dan tidak memanggil URL dari isi report | P2 | SUP-FR-011 / SUP-AC-011 |
| SUP-T-101 | nonfungsional | Query exact,zero-result dan filtered | Jalankan masing-masing 30 kali | p95 ≤500 ms; tidak bypass permission demi performa | P0 | SUP-NFR-001 / SUP-AC-101 |
| SUP-T-102 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | SUP-NFR-002 / SUP-AC-102 |
| SUP-T-103 | nonfungsional | Form valid dan gangguan koneksi sebelum konfirmasi simpan | Simpan, pulihkan koneksi, lalu retry | Input tetap terlihat; tepat satu revisi tersimpan dan indikator sukses hanya setelah konfirmasi | P0 | SUP-NFR-003 / SUP-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| SUP-Q1 | Search cache usang | Kebocoran hidden metadata | Check visibility saat read/open |
| SUP-Q2 | Report spam | Beban moderator | Rate limit, plain text, no attachment pada feedback awal P2 |
| SUP-Q3 | Digest menambah infra | Scope melebar | P2; dukungan in-app mengikuti prioritas FR |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Full-text Drive, semantic/vector search, email delivery, push, weekly digest dan laporan akademik rapi ditunda. Help dasar, bookmark dan feedback tetap berfungsi manual.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: SUP-FR-004, SUP-FR-005, SUP-FR-007, SUP-FR-009, SUP-FR-010, SUP-FR-011. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-01 brief. Ranking, limits dan receipt behavior adalah PRODUCT_ASSUMPTION D-13; bukan kemampuan yang sudah diimplementasikan.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-15 pada audit untuk alasan revisi.

