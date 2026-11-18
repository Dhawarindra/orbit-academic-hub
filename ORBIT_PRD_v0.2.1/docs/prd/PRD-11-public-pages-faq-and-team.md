# PRD-11 — Public Pages, FAQ & Development Team

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-11 / v0.2.1 DDP1 Errata |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Content Owner / Product Lead |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | Nama anggota, kontak publik, biografi dan portofolio belum diberikan; jangan membuat identitas atau testimoni palsu. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). v0.2.1: errata prioritas/journey dari review independen; FR dan ID tetap. |

## 2. Executive Summary & Problem

Halaman publik menjelaskan manfaat, batas kemampuan, status independen dan cara mulai. Tim pembuat produk dipisahkan dari kating/alumni yang berkontribusi materi. Klaim fitur harus sesuai versi yang benar-benar dibangun.

## 3. Goals, Non-Goals & Success Metrics

Pengunjung memahami fungsi dan keterbatasan sebelum membuat akun, serta menemukan bantuan tanpa membuka data pribadi.

**Non-goals:** Promosi sebagai sistem resmi UI, testimoni rekaan, angka pengguna atau hasil akademik tanpa bukti.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Pemahaman status | Peserta menyebut Orbit independen dan prediksi bersyarat | Usulan ≥4/5 peserta |
| Kebenaran klaim | Konten cocok release capability manifest | 100% fitur diklaim tersedia memang aktif |
| CTA | Pengunjung menemukan mulai/bantuan | Usulan ≥4/5 dalam satu menit |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Guest yang baru mengenal produk, mahasiswa ingin tutorial, reviewer tugas yang ingin tahu tim dan kontributor.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Guest | Landing, FAQ, tutorial, tim dan metadata contributor opt-in | Data workspace |
| Content editor/admin | Draft/review/publish konten | Mempublikasikan identitas tanpa izin |
| Team member/contributor | Menyetujui/mencabut biodata/atribusi miliknya | Mengubah identitas orang lain |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Status independen dan label demo sintetis pada shell | Landing, FAQ dan tutorial sesuai capability | Biodata tim yang disetujui, apresiasi kontributor dan contact form |

**Slice rilis:** Shell menyatakan Orbit independen dan data demo; tidak mengklaim endorsement UI. Nama/foto tidak direka. Video dan README menjelaskan cara menjalankan; halaman marketing terpisah bukan syarat.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Shell menyatakan Orbit independen dan data demo; tidak mengklaim endorsement UI. Nama/foto tidak direka. Video dan README menjelaskan cara menjalankan; halaman marketing terpisah bukan syarat. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Guest membaca hero → melihat tiga langkah cara kerja → membaca status independen → CTA Mulai merencanakan → registrasi. Demo terpisah dan berlabel sintetis bila tersedia.

**J2.** Pengunjung bertanya nilai diambil dari mana → FAQ menjelaskan input manual dan integrasi belum tersedia → tutorial tambah matkul → CTA registrasi atau kembali dashboard jika sudah login.

**J3.** User ingin mengenal pembuat → Tim Pengembang menampilkan peran yang benar-benar disetujui; halaman Apresiasi Kontributor terpisah dan hanya menggunakan credit opt-in.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| PUB-US-001 | As a guest, I want memahami manfaat dan batas Orbit, so that saya tahu apakah produk membantu. | P0 / P1 (per FR) | PUB-FR-001, PUB-FR-002, PUB-FR-003 |
| PUB-US-002 | As a guest, I want membaca FAQ dan tutorial, so that saya bisa mulai tanpa bantuan. | P1 | PUB-FR-004, PUB-FR-005 |
| PUB-US-003 | As a team member, I want mengatur identitas publik saya, so that informasi yang tampil disetujui. | P2 | PUB-FR-006, PUB-FR-007, PUB-FR-008 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PUB-FR-001 | P1 | Buka landing | Guest | Capability manifest versi rilis | Tampilkan manfaat yang didukung dan CTA sesuai mode aktif: buka demo lokal atau registrasi ketika layanan akun tersedia | Fitur P2 tidak diklaim terhubung; pada DDP1 CTA membuka demo lokal, registrasi hanya bila AUTH P2 aktif | PUB-AC-001 |
| PUB-FR-002 | P0 | Baca About/footer | Shell demo atau halaman publik | Status produk | Tampilkan Orbit sebagai produk independen mahasiswa, bukan sistem resmi UI | Status independen terlihat pada shell sebelum pengguna memasukkan data; bila registrasi P2 ada, terlihat sebelum registrasi | PUB-AC-002 |
| PUB-FR-003 | P0 | Buka demo | Demo tersedia terpisah | Data sintetis | Pasang label demo pada setiap tampilan dan pisahkan dari workspace nyata | Tidak ada angka demo yang disimpan sebagai actual user | PUB-AC-003 |
| PUB-FR-004 | P1 | Buka FAQ | Published FAQ | Pertanyaan nilai/SSO/Drive/privasi | Jawab sesuai capability dan kebijakan berlaku beserta tanggal review | Tidak menjanjikan SSO/nilai otomatis | PUB-AC-004 |
| PUB-FR-005 | P1 | Ikuti tutorial | Pengguna baru | Langkah tambah offering/BRP/nilai | Gunakan fixture sintetis dan langkah yang cocok UI aktif | Tutorial berakhir pada data pribadi atau demo berlabel, bukan mengimpor contoh diam-diam | PUB-AC-005 |
| PUB-FR-006 | P2 | Publish profil tim | Content editor | Nama/foto/peran tanpa consent | Tahan publikasi sampai consent serta fakta diberikan | Nama dan foto rekaan tidak muncul | PUB-AC-006 |
| PUB-FR-007 | P2 | Buka apresiasi kontributor | Credit opt-in valid | ContributorProfile published | Pisahkan label kontributor komunitas dari pembuat website | Kontributor tidak dinyatakan sebagai developer tanpa data | PUB-AC-007 |
| PUB-FR-008 | P2 | Buka contact | Guest atau user | Form feedback internal | Arahkan ke SUP tanpa membuat alamat email/nomor kontak palsu | Laporan tercatat; tidak ada janji respons yang belum disepakati | PUB-AC-008 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| PUB-BR-001 | Public content version mengikuti kemampuan rilis. Planned features diberi label rencana dan tidak ditampilkan sebagai fungsi tersedia. | PUB-FR-001, PUB-FR-004 |
| PUB-BR-002 | Minimal landing: hero manfaat, cara kerja, fitur aktif, data/privacy summary, status independen dan CTA. Hindari klaim peningkatan IPK atau testimoni tanpa data. | PUB-FR-001, PUB-FR-002 |
| PUB-BR-003 | FAQ wajib mencakup status independen; sumber nilai; actual vs simulasi; SSO/SLCM; perbedaan BRP; bobot tidak 100%; privasi/consent; restricted Drive; report materi; export/delete. | PUB-FR-004 |
| PUB-BR-004 | Tim pengembang: nama/peran/biografi singkat disetujui; foto/link portofolio opsional. Data yang belum diberikan diganti empty state, bukan identitas placeholder yang menyerupai orang nyata. | PUB-FR-006 |
| PUB-BR-005 | Contributor credit berasal dari VLT dan consent; tidak disalin manual ke daftar tim. Pencabutan kredit memperbarui apresiasi pada pembacaan berikutnya. | PUB-FR-007 |
| PUB-BR-006 | Kontak aplikasi berupa feedback internal adalah P2 melalui PUB-FR-008 dan SUP-FR-005; bukan dependency atau kewajiban tersembunyi P0. Alamat organisasi atau kanal publik hanya ditampilkan setelah pengguna memberikan dan menyetujui publikasinya. | PUB-FR-008 |

**Draft copy yang dapat dipakai:** “Orbit membantu menyusun rencana semester, memantau nilai yang kamu masukkan, dan melihat beban tugas dalam satu tempat.” Subcopy: “Dikembangkan secara independen oleh mahasiswa. Bukan sistem resmi Universitas Indonesia.” CTA: “Mulai merencanakan”; secondary: “Lihat cara kerja”.

**FAQ contoh:** “Apakah nilainya otomatis dari UI?” → “Pada versi awal, kamu memasukkan nilai sendiri. Integrasi resmi belum tersedia.” “Apakah simulasi mengubah IRS?” → “Tidak. Simulasi hanya menyimpan rencana di Orbit.” “Apakah nilai saya terlihat oleh kating?” → “Nilai pribadi tidak tampil di komunitas. Kontribusi membutuhkan pilihan dan persetujuan terpisah.”

**Tim belum tersedia:** “Profil tim belum dipublikasikan.” Tampilkan konteks proyek yang telah diberikan tanpa menambahkan nama anggota. Jika anggota menarik foto, foto dihapus dari semua permukaan publik yang dikendalikan Orbit.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| PublicPage / page_id | slug,title,blocks,capability refs,reviewed_at | Content Owner | draft/reviewed/published/archived | Public published |
| FAQEntry / faq_id | question,answer,policy ref,version | Content Owner | Review saat rule berubah | Public |
| TeamProfile / team_profile_id | name,role,bio,optional photo/portfolio,consent ref | Member + editor | draft/approved/withdrawn | Private draft / Public approved |
| Tutorial / tutorial_id | steps,UI version,synthetic flag | UX/Content owner | Versioned; obsolete hidden | Public |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Landing ringan dengan headline manfaat, contoh alur tiga langkah dan CTA jelas. FAQ memakai pencarian judul sederhana atau accordion keyboard. About menjelaskan pembuat independen dan tujuan TA tanpa mengarang rubrik. Halaman tim hanya memuat data disetujui; apresiasi kontributor punya judul terpisah. Footer berisi bantuan, privasi, status independen dan tanggal pembaruan konten. Data personal tidak boleh tertempel pada metadata sosial.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| No team details | Empty team profile state | Jangan fabricate nama |
| FAQ stale | Review diperlukan | Jangan janji fitur lama |
| No contact channel | Form internal | Tidak membuat email palsu |
| Withdrawn profile | Hapus projection publik | Audit consent minimal |
| Guest CTA | Arah register | Tidak memuat private data |
| Unavailable demo | Jangan tampil tombol mati | Cara kerja tetap tersedia |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** P0 hanya status independen/demo pada shell; CTA register, contact dan biodata bergantung capability future. README/video DDP1 tidak bergantung halaman contact/SUP feedback. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| CORE-FR-005 → PUB-FR-001 | Capability manifest release | Content review saat fitur diaktifkan/dimatikan |
| AUTH-FR-006/VLT-FR-006 → PUB-FR-007 | Attribution consent | Invalidate projection segera |
| PUB-FR-008 → SUP-FR-005 | Feedback entry context=public | Tidak kirim email otomatis |
| UX-FR-001 → PUB-FR-005 | Navigation/UI version | Tutorial direview saat flow berubah |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Biografi tim dan credit kontributor punya tujuan berbeda; keduanya memerlukan persetujuan publikasi sesuai konteks. Tidak memajang email akademik, NPM atau status afiliasi individu yang belum dibuktikan.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| PUB-NFR-001 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | PUB-AC-101 |
| PUB-NFR-002 | P0 | Tampilan utama p95 ≤2 detik setelah data tersedia pada beban uji dasar. | PUB-AC-102 |
| PUB-NFR-003 | P0 | Konten publik tidak pernah menyertakan data workspace dalam response/metadata. | PUB-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| PUB-AC-001 | Given Guest; Capability manifest versi rilis | When Buka landing | Then Fitur P2 tidak diklaim terhubung; pada DDP1 CTA membuka demo lokal, registrasi hanya bila AUTH P2 aktif | PUB-FR-001 |
| PUB-AC-002 | Given Shell demo atau halaman publik; Status produk | When Baca About/footer | Then Status independen terlihat pada shell sebelum pengguna memasukkan data; bila registrasi P2 ada, terlihat sebelum registrasi | PUB-FR-002 |
| PUB-AC-003 | Given Demo tersedia terpisah; Data sintetis | When Buka demo | Then Tidak ada angka demo yang disimpan sebagai actual user | PUB-FR-003 |
| PUB-AC-004 | Given Published FAQ; Pertanyaan nilai/SSO/Drive/privasi | When Buka FAQ | Then Tidak menjanjikan SSO/nilai otomatis | PUB-FR-004 |
| PUB-AC-005 | Given Pengguna baru; Langkah tambah offering/BRP/nilai | When Ikuti tutorial | Then Tutorial berakhir pada data pribadi atau demo berlabel, bukan mengimpor contoh diam-diam | PUB-FR-005 |
| PUB-AC-006 | Given Content editor; Nama/foto/peran tanpa consent | When Publish profil tim | Then Nama dan foto rekaan tidak muncul | PUB-FR-006 |
| PUB-AC-007 | Given Credit opt-in valid; ContributorProfile published | When Buka apresiasi kontributor | Then Kontributor tidak dinyatakan sebagai developer tanpa data | PUB-FR-007 |
| PUB-AC-008 | Given Guest atau user; Form feedback internal | When Buka contact | Then Laporan tercatat; tidak ada janji respons yang belum disepakati | PUB-FR-008 |
| PUB-AC-101 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | PUB-NFR-001 |
| PUB-AC-102 | Given Beban uji dasar dan data telah tersedia | When Buka tampilan utama 30 kali | Then p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | PUB-NFR-002 |
| PUB-AC-103 | Given Guest dan user login mengunjungi URL publik sama | When Periksa page, metadata dan hasil pencarian publik | Then Tidak ada nilai, target, jadwal, username private atau session token | PUB-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| PUB-T-001 | fungsional | Guest; Capability manifest versi rilis | Buka landing | Fitur P2 tidak diklaim terhubung; pada DDP1 CTA membuka demo lokal, registrasi hanya bila AUTH P2 aktif | P1 | PUB-FR-001 / PUB-AC-001 |
| PUB-T-002 | fungsional | Shell demo atau halaman publik; Status produk | Baca About/footer | Status independen terlihat pada shell sebelum pengguna memasukkan data; bila registrasi P2 ada, terlihat sebelum registrasi | P0 | PUB-FR-002 / PUB-AC-002 |
| PUB-T-003 | negatif | Demo tersedia terpisah; Data sintetis | Buka demo | Tidak ada angka demo yang disimpan sebagai actual user | P0 | PUB-FR-003 / PUB-AC-003 |
| PUB-T-004 | fungsional | Published FAQ; Pertanyaan nilai/SSO/Drive/privasi | Buka FAQ | Tidak menjanjikan SSO/nilai otomatis | P1 | PUB-FR-004 / PUB-AC-004 |
| PUB-T-005 | fungsional | Pengguna baru; Langkah tambah offering/BRP/nilai | Ikuti tutorial | Tutorial berakhir pada data pribadi atau demo berlabel, bukan mengimpor contoh diam-diam | P1 | PUB-FR-005 / PUB-AC-005 |
| PUB-T-006 | privasi | Content editor; Nama/foto/peran tanpa consent | Publish profil tim | Nama dan foto rekaan tidak muncul | P2 | PUB-FR-006 / PUB-AC-006 |
| PUB-T-007 | fungsional | Credit opt-in valid; ContributorProfile published | Buka apresiasi kontributor | Kontributor tidak dinyatakan sebagai developer tanpa data | P2 | PUB-FR-007 / PUB-AC-007 |
| PUB-T-008 | fungsional | Guest atau user; Form feedback internal | Buka contact | Laporan tercatat; tidak ada janji respons yang belum disepakati | P2 | PUB-FR-008 / PUB-AC-008 |
| PUB-T-101 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | PUB-NFR-001 / PUB-AC-101 |
| PUB-T-102 | nonfungsional | Beban uji dasar dan data telah tersedia | Buka tampilan utama 30 kali | p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | P0 | PUB-NFR-002 / PUB-AC-102 |
| PUB-T-103 | nonfungsional | Guest dan user login mengunjungi URL publik sama | Periksa page, metadata dan hasil pencarian publik | Tidak ada nilai, target, jadwal, username private atau session token | P0 | PUB-NFR-003 / PUB-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| PUB-Q1 | Identitas tim belum diberikan | Halaman tim kosong | Empty state; Product Lead mengumpulkan consent |
| PUB-Q2 | Rencana dianggap fitur aktif | Ekspektasi salah | Capability-based copy |
| PUB-Q3 | Batas brand UI | Kesan resmi | Status independen; tidak mengklaim endorsement |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Konten blog, testimoni, data penggunaan dan portofolio tim hanya setelah bukti serta izin tersedia. Tidak ada publishing website dalam pekerjaan ini.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: PUB-FR-006, PUB-FR-007, PUB-FR-008. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-01 brief untuk identitas produk. Nama tim dan kontak: NEEDS_VALIDATION; copy manfaat adalah usulan, bukan klaim hasil riset.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-14 pada audit untuk alasan revisi.

