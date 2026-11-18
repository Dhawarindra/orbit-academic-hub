# PRD-06 — Semester Knowledge Vault & Contributors

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-06 / v0.2 DDP1 Draft |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Knowledge Curator / Community Moderator |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | P1 menyimpan metadata link Drive saja dan beberapa resource yang izin baginya jelas. Status akses link diperiksa manual; tidak mengklaim live availability tanpa pemeriksaan. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). |

## 2. Executive Summary & Problem

Vault membuat resource sah lebih mudah ditemukan melalui course, topik dan periode. Link bukan izin menyalin atau mempublikasikan isi. Kredit kontributor opt-in; status identitas internal tidak mengungkap nama atau email publik.

## 3. Goals, Non-Goals & Success Metrics

Mahasiswa menemukan resource relevan, tahu siapa yang memberi kredit secara sukarela, dan dapat melaporkan masalah.

**Non-goals:** Hosting/mirroring file Drive, bypass restricted access, distribusi soal ujian tertutup atau materi tanpa hak.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Metadata layak publikasi | Resource terbit punya scope, izin dan access_checked_at | 100% curated set |
| Penemuan resource | Peserta menemukan 1 resource sesuai course/topik | Usulan ≥4/5 dalam 2 menit |
| Pemulihan link | Laporan menghasilkan status dapat ditelusuri | 100% laporan tersimpan dan bisa direview |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Mahasiswa mencari catatan; kating/alumni membagi materi milik sendiri; moderator meninjau legalitas berbagi secara praktis tanpa klaim pemeriksaan hukum lengkap.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Guest/student | Baca metadata published dan buka link eksternal | Draft/rejected resource |
| Contributor/alumni | P2 submit/edit/withdraw milik sendiri lewat akun lokal | Mengubah kontribusi orang lain |
| Moderator | P1 kurasi dataset; UI review/publish/hide P2 | Membuka akses Drive yang tidak diizinkan |
| Admin | Kelola moderator | Menyamakan contributor dengan development team |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Tidak ada fitur Vault yang menghalangi P0 | Metadata link yang diizinkan, filter/search, status pemeriksaan manual, rights/URL gate | Bookmark, self-submit, kredit kontributor, withdrawal/report queue, dedup dan UI moderator |

**Slice rilis:** Kurasi maksimal 3–5 link dengan bukti izin dan timestamp; daftar boleh kosong. Edit fixture metadata oleh tim; tanpa auto-fetch/proxy isi atau permintaan kredensial Drive.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Kurasi maksimal 3–5 link dengan bukti izin dan timestamp; daftar boleh kosong. Edit fixture metadata oleh tim; tanpa auto-fetch/proxy isi atau permintaan kredensial Drive. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Course → Vault terfilter → pilih resource → lihat scope, akses dan kredit → Buka di Google Drive. Jika restricted, pengguna kembali dan melaporkan atau mengikuti mekanisme permintaan akses milik Drive; Orbit tidak mengubah share permission.

**J2.** P2 kontributor → tambah tautan → isi metadata/hak berbagi/credit preference → preview publik → kirim review. Edit URL atau pernyataan hak setelah publish menghasilkan revisi pending; versi lama hanya tetap terlihat bila aman.

**J3.** Moderator → queue/report → review link secara manual → publish/hide/reject dengan alasan → pengguna melihat status. Withdrawal pemilik menyembunyikan resource tanpa menunggu moderator.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| VLT-US-001 | As a student, I want menemukan resource yang jelas aksesnya, so that saya tidak membuang waktu. | P1 / P2 (per FR) | VLT-FR-001, VLT-FR-002, VLT-FR-003, VLT-FR-004 |
| VLT-US-002 | As a contributor, I want mengendalikan kredit dan kontribusi, so that berbagi tetap sukarela. | P2 | VLT-FR-005, VLT-FR-006, VLT-FR-007 |
| VLT-US-003 | As a moderator, I want meninjau dan menurunkan resource bermasalah, so that katalog dapat dipercaya. | P1 / P2 (per FR) | VLT-FR-008, VLT-FR-009 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VLT-FR-001 | P1 | Buka katalog | Ada resource published | course/topic/year/type filters | Tampilkan metadata yang cocok dan status akses terakhir | Draft/rejected tidak muncul pada hasil | VLT-AC-001 |
| VLT-FR-002 | P1 | Buka link | Resource published | HTTPS Drive URL yang tervalidasi | Buka tujuan eksternal dengan label domain; jangan proxy isi | Tidak menyalin atau meng-host file Drive | VLT-AC-002 |
| VLT-FR-003 | P1 | Tandai akses | Kurator memeriksa manual dan memperbarui metadata; UI moderator P2 | restricted/broken/accessible/unknown + waktu | Simpan hasil sebagai observasi waktu tertentu | Restricted diberi label, bukan disebut broken | VLT-AC-003 |
| VLT-FR-004 | P2 | Bookmark resource | Akun aktif | resource_id | Simpan referensi bookmark privat yang unik | Klik ulang tidak membuat duplikat | VLT-AC-004 |
| VLT-FR-005 | P2 | Submit resource | Akun lokal; izin berbagi dinyatakan | URL, judul, course, tipe, hak, kredit optional | Validasi required metadata dan masukkan pending | Tidak langsung published | VLT-AC-005 |
| VLT-FR-006 | P2 | Ubah atribusi | Contributor pemilik | public name opt-in → anonymous | Perbarui projection kredit tanpa menghapus bukti consent internal yang diperlukan | Nama/email tidak tampil; label Kontributor anonim | VLT-AC-006 |
| VLT-FR-007 | P2 | Tarik resource | Pemilik resource | resource_id | Unpublish metadata dan tombstone bookmark | Tidak menghapus file dari Drive; tidak lagi ditemukan lewat search | VLT-AC-007 |
| VLT-FR-008 | P2 | Laporkan konten | Resource published | broken/restricted/rights/closed exam + catatan minimal | Simpan report dan beri nomor pelacakan; kasus hak/ujian ditandai urgent | Reviewer melihat queue; pelapor tidak perlu melampirkan isi sensitif | VLT-AC-008 |
| VLT-FR-009 | P1 | Moderasi materi terlarang | Kurator memeriksa dataset sebelum aktivasi; moderator melalui UI pada P2 | Soal ujian tertutup atau hak distribusi tidak jelas | Tolak aktivasi item dengan hak tidak jelas atau ujian tertutup; hide item jika bukti hak dicabut; workflow moderasi akun disimpan untuk P2 | Resource tidak muncul pada katalog dan direct public view | VLT-AC-009 |
| VLT-FR-010 | P2 | Submit link duplikat | Drive file id sudah published | URL sama dengan parameter tracking berbeda | Canonicalize identifier tanpa mengambil isi dan arahkan ke resource ada | Tidak membuat kontribusi terbit kedua | VLT-AC-010 |
| VLT-FR-011 | P1 | Validasi URL resource kurasi | Moderator/editor resource | javascript: payload; drive.google.com.evil.example; URL user:pass@host | Tolak skema/host/kredensial yang tidak sesuai allowlist sebelum preview atau fetch | URL tidak disimpan sebagai published; tidak ada request keluar | VLT-AC-011 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| VLT-BR-001 | Required metadata: judul, URL, course_id atau general-scope, tipe, deskripsi singkat, pernyataan hak/source permission, access status. Topic dan tahun boleh unknown; tidak mengarang. | VLT-FR-001, VLT-FR-005 |
| VLT-BR-002 | P1 kurasi metadata oleh tim melalui dataset tervalidasi; tidak memerlukan akun moderator atau antrean submit. Kontribusi mandiri dan UI moderasi P2 memakai pending → approved/published atau rejected. Hak meragukan memblokir item; pencabutan hak segera hidden. | VLT-FR-005, VLT-FR-008, VLT-FR-009 |
| VLT-BR-003 | Allowlist HTTPS drive.google.com/docs.google.com pada input; tolak kredensial dalam URL, javascript/data/internal IP dan hostname tiruan. Tidak mengikuti redirect atau mengambil isi secara otomatis pada P1. | VLT-FR-002, VLT-FR-010, VLT-FR-011 |
| VLT-BR-004 | Akses accessible adalah observasi manual pada timestamp, bukan jaminan semua akun. Restricted tidak otomatis illegal dan tidak di-bypass; pengguna memilih apakah meminta izin di Drive. | VLT-FR-003 |
| VLT-BR-005 | Default kredit anonymous. Verified identity adalah badge internal terpisah; local login saja tidak memberi verified campus badge. | VLT-FR-006 |
| VLT-BR-006 | Edit URL/hak/scope utama kembali ke review. Jika edit mengungkap risiko hak pada versi lama, hide versi lama segera; perubahan teks aman boleh menunggu review tanpa memutus link. | VLT-FR-005, VLT-FR-009 |
| VLT-BR-007 | Withdrawal hanya menghilangkan metadata Orbit; file Drive dan salinan yang sudah diambil pihak lain di luar kendali Orbit. | VLT-FR-007 |
| VLT-BR-008 | Dedup berdasarkan canonical Drive resource identifier; query tracking dibuang, tetapi resourcekey yang diperlukan untuk akses dipertahankan dan tidak dicatat dalam log publik. | VLT-FR-010, VLT-FR-002 |

**Skenario sintetis:** alumni memakai akun lokal untuk mengirim catatan miliknya sendiri, memilih kredit anonim dan izin berbagi yang dinyatakan. Moderator memeriksa metadata, isi hanya jika memiliki akses, serta status link; resource terbit dengan credit anonim dan timestamp cek. Identitas akun tidak tampil.

**Restricted vs broken:** link mengarah halaman minta akses → restricted; target dihapus → broken berdasarkan hasil cek; timeout → unknown, bukan broken. Jika laporan menyebut soal ujian tertutup, hide sementara dan review tanpa meminta pelapor mengunggah soal itu.

**Status:** draft → pending → published; published → pending_revision/hidden/withdrawn; rejected dapat diperbaiki menjadi pending. Withdrawn tidak dapat dibuka melalui URL internal lama, sedangkan bookmark menampilkan tombstone.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| Resource / resource_id | canonical Drive id/url, title, course/topic, year, type, rights statement, revision | Contributor/curator | draft/pending/published/hidden/withdrawn | Public only approved metadata |
| ContributorProfile / contributor_id | user_id link restricted; public_name optional, attribution consent | Contributor | anonymous default; revision | Restricted link / Public opted-in credit |
| AccessObservation / observation_id | resource, status, checked_at, reviewer | Moderator | History of checks, not permanent truth | Public status; Private reviewer id |
| ResourceReport / report_id | resource, category, note, reporter optional, state | Reporter/moderator | open/triaged/resolved | Private |
| Bookmark / bookmark_id | owner+resource unique | SUP owner; VLT action | active/tombstone/deleted | Private |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Vault menampilkan list ringkas, filter course/topik/tahun/tipe dan badge akses. Detail menunjukkan judul, alasan relevan, izin yang dinyatakan, kredit, tanggal cek dan CTA eksternal. Form submit mempunyai preview persis metadata yang akan publik; checkbox kredit default off. Halaman Tim Pengembang berbeda dari Apresiasi Kontributor. Label “akun terverifikasi” tidak muncul tanpa bukti mekanisme verifikasi. Tombol Report tersedia sebelum link dibuka.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| No matching resources | Reset filter dan saran course | Tidak memaksa login untuk katalog |
| Restricted | Butuh izin pemilik Drive | Jangan bypass |
| Broken/expired | Tandai dan beri report | Jangan klaim file dipulihkan |
| Unknown check | Belum diperiksa / cek gagal | Tampilkan timestamp terakhir |
| Withdrawn | Tidak tersedia lagi | Bookmark tombstone, no private details |
| Duplicate/malicious URL | Validasi field spesifik | Tidak fetch otomatis |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** P1 hanya dataset published yang dikurasi tim dan diperiksa Python sebelum tampil; bukan layanan moderator multiuser. SUP search P1 membaca metadata ini. AUTH account, self-submit, credit dan report queue pada tabel berikut P2. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| MAP-FR-001 → VLT-FR-001 | Course/topic catalog IDs | Unknown scope diberi general, bukan fake course |
| VLT-FR-001 → SUP-FR-001 | Published metadata untuk search | Hide/withdraw segera membatalkan hasil |
| VLT-FR-004 → SUP-FR-004 | BookmarkRequested | Unique owner+resource; retry idempotent |
| AUTH-FR-006 → VLT-FR-006 | AttributionConsentChanged | Identitas private tetap terpisah |
| VLT-FR-009 → GDE-FR-004 | ResourceVisibilityChanged | Guidance tidak menyarankan hidden resource |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Tidak menyimpan file Drive, token akun Google, atau data sensitif di URL log. Review manual hanya menggunakan akses yang sah; izin membagikan resource harus dinyatakan pemilik/kontributor. Tidak mendorong pembagian ujian tertutup. Report dapat tanpa data identitas publik; moderator tidak menjanjikan waktu penyelesaian tanpa kapasitas.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| VLT-NFR-001 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | VLT-AC-101 |
| VLT-NFR-002 | P0 | Tampilan utama p95 ≤2 detik setelah data tersedia pada beban uji dasar. | VLT-AC-102 |
| VLT-NFR-003 | P0 | Unpublish menghapus akses metadata pada semua permukaan berikutnya. | VLT-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| VLT-AC-001 | Given Ada resource published; course/topic/year/type filters | When Buka katalog | Then Draft/rejected tidak muncul pada hasil | VLT-FR-001 |
| VLT-AC-002 | Given Resource published; HTTPS Drive URL yang tervalidasi | When Buka link | Then Tidak menyalin atau meng-host file Drive | VLT-FR-002 |
| VLT-AC-003 | Given Kurator memeriksa manual dan memperbarui metadata; UI moderator P2; restricted/broken/accessible/unknown + waktu | When Tandai akses | Then Restricted diberi label, bukan disebut broken | VLT-FR-003 |
| VLT-AC-004 | Given Akun aktif; resource_id | When Bookmark resource | Then Klik ulang tidak membuat duplikat | VLT-FR-004 |
| VLT-AC-005 | Given Akun lokal; izin berbagi dinyatakan; URL, judul, course, tipe, hak, kredit optional | When Submit resource | Then Tidak langsung published | VLT-FR-005 |
| VLT-AC-006 | Given Contributor pemilik; public name opt-in → anonymous | When Ubah atribusi | Then Nama/email tidak tampil; label Kontributor anonim | VLT-FR-006 |
| VLT-AC-007 | Given Pemilik resource; resource_id | When Tarik resource | Then Tidak menghapus file dari Drive; tidak lagi ditemukan lewat search | VLT-FR-007 |
| VLT-AC-008 | Given Resource published; broken/restricted/rights/closed exam + catatan minimal | When Laporkan konten | Then Reviewer melihat queue; pelapor tidak perlu melampirkan isi sensitif | VLT-FR-008 |
| VLT-AC-009 | Given Kurator memeriksa dataset sebelum aktivasi; moderator melalui UI pada P2; Soal ujian tertutup atau hak distribusi tidak jelas | When Moderasi materi terlarang | Then Resource tidak muncul pada katalog dan direct public view | VLT-FR-009 |
| VLT-AC-010 | Given Drive file id sudah published; URL sama dengan parameter tracking berbeda | When Submit link duplikat | Then Tidak membuat kontribusi terbit kedua | VLT-FR-010 |
| VLT-AC-011 | Given Moderator/editor resource; javascript: payload; drive.google.com.evil.example; URL user:pass@host | When Validasi URL resource kurasi | Then URL tidak disimpan sebagai published; tidak ada request keluar | VLT-FR-011 |
| VLT-AC-101 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | VLT-NFR-001 |
| VLT-AC-102 | Given Beban uji dasar dan data telah tersedia | When Buka tampilan utama 30 kali | Then p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | VLT-NFR-002 |
| VLT-AC-103 | Given Resource pada search, bookmark dan guidance | When Hide resource lalu buka masing-masing | Then Search/guidance menghilangkan resource; bookmark hanya tombstone | VLT-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| VLT-T-001 | fungsional | Ada resource published; course/topic/year/type filters | Buka katalog | Draft/rejected tidak muncul pada hasil | P1 | VLT-FR-001 / VLT-AC-001 |
| VLT-T-002 | fungsional | Resource published; HTTPS Drive URL yang tervalidasi | Buka link | Tidak menyalin atau meng-host file Drive | P1 | VLT-FR-002 / VLT-AC-002 |
| VLT-T-003 | edge | Kurator memeriksa manual dan memperbarui metadata; UI moderator P2; restricted/broken/accessible/unknown + waktu | Tandai akses | Restricted diberi label, bukan disebut broken | P1 | VLT-FR-003 / VLT-AC-003 |
| VLT-T-004 | boundary | Akun aktif; resource_id | Bookmark resource | Klik ulang tidak membuat duplikat | P2 | VLT-FR-004 / VLT-AC-004 |
| VLT-T-005 | fungsional | Akun lokal; izin berbagi dinyatakan; URL, judul, course, tipe, hak, kredit optional | Submit resource | Tidak langsung published | P2 | VLT-FR-005 / VLT-AC-005 |
| VLT-T-006 | privasi | Contributor pemilik; public name opt-in → anonymous | Ubah atribusi | Nama/email tidak tampil; label Kontributor anonim | P2 | VLT-FR-006 / VLT-AC-006 |
| VLT-T-007 | integrasi | Pemilik resource; resource_id | Tarik resource | Tidak menghapus file dari Drive; tidak lagi ditemukan lewat search | P2 | VLT-FR-007 / VLT-AC-007 |
| VLT-T-008 | fungsional | Resource published; broken/restricted/rights/closed exam + catatan minimal | Laporkan konten | Reviewer melihat queue; pelapor tidak perlu melampirkan isi sensitif | P2 | VLT-FR-008 / VLT-AC-008 |
| VLT-T-009 | negatif | Kurator memeriksa dataset sebelum aktivasi; moderator melalui UI pada P2; Soal ujian tertutup atau hak distribusi tidak jelas | Moderasi materi terlarang | Resource tidak muncul pada katalog dan direct public view | P1 | VLT-FR-009 / VLT-AC-009 |
| VLT-T-010 | boundary | Drive file id sudah published; URL sama dengan parameter tracking berbeda | Submit link duplikat | Tidak membuat kontribusi terbit kedua | P2 | VLT-FR-010 / VLT-AC-010 |
| VLT-T-011 | keamanan | Moderator/editor resource; javascript: payload; drive.google.com.evil.example; URL user:pass@host | Validasi URL resource kurasi | URL tidak disimpan sebagai published; tidak ada request keluar | P1 | VLT-FR-011 / VLT-AC-011 |
| VLT-T-101 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | VLT-NFR-001 / VLT-AC-101 |
| VLT-T-102 | nonfungsional | Beban uji dasar dan data telah tersedia | Buka tampilan utama 30 kali | p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | P0 | VLT-NFR-002 / VLT-AC-102 |
| VLT-T-103 | nonfungsional | Resource pada search, bookmark dan guidance | Hide resource lalu buka masing-masing | Search/guidance menghilangkan resource; bookmark hanya tombstone | P0 | VLT-NFR-003 / VLT-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| VLT-Q1 | Hak distribusi belum jelas | Konten bermasalah | Default pending/hidden; moderator periksa |
| VLT-Q2 | Link berubah di luar Orbit | Metadata usang | Timestamp dan report; tidak jamin akses |
| VLT-Q3 | Kapasitas moderasi kecil | Queue menumpuk | P1 curated-only; self-service P2 |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Tidak ada unggah file, mirror Drive, indexing isi Drive, share permission otomatis, auto-open konten restricted atau fasilitas berbagi soal ujian tertutup.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: VLT-FR-004, VLT-FR-005, VLT-FR-006, VLT-FR-007, VLT-FR-008, VLT-FR-010. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-01 brief; aturan status akses dan moderasi merupakan PRODUCT_ASSUMPTION D-08. API Drive tidak diperiksa atau diasumsikan tersedia; tidak dibutuhkan untuk MVP link-only.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-09 pada audit untuk alasan revisi.

