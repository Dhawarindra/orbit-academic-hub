# ORBIT — Research & Validation Register

Versi: **v0.2.1 DDP1 Errata** · Tanggal: **18 November 2026 (Asia/Jakarta)** · Owner: **Product Lead** · Status: untuk review manusia.


## Audit konteks: known / assumed / unknown / external approval

| Kelompok | Temuan | Akibat produk |
| --- | --- | --- |
| Known dari brief | Produk independen, target awal Fasilkom UI, input once, 13 PRD, link-only Vault, no ML wajib | Dipertahankan sebagai keputusan pengguna |
| Known hasil pemeriksaan | Dua frame Figma dapat dibaca; halaman program resmi, dokumen Peraturan No.1/2024, roadmap sekunder dan referensi aksesibilitas/keamanan dapat dibuka | Sumber dicatat dengan batas; tidak mengklaim implementasi |
| Assumed | P0/P1/P2, threshold beban, k=10, retention, target latency, pilihan tema terang | Keputusan produk draft, perlu review |
| Unknown | Jam/kemampuan aktual anggota, kurikulum target, BRP, policy binding, dataset komunitas, resource berizin, nama tim | Tidak diisi dengan tebakan; fallback di RV terkait |
| Needs External Approval | SSO client dan schedule access SLCM | Integrasi P2 off; fitur manual tetap jalan |

## Arti label confidence

VERIFIED_OFFICIAL berarti isi spesifik ditemukan pada penerbit otoritatif, tidak mengesahkan seluruh aplikasi. VERIFIED_SECONDARY berarti referensi sekunder/visual benar-benar diamati. PRODUCT_ASSUMPTION adalah keputusan desain yang bukan fakta kampus. NEEDS_VALIDATION berarti bukti belum cukup. Kategori “NEEDS EXTERNAL APPROVAL” pada register mengidentifikasi izin di luar tim, bukan status sumber kelima.

## Sumber yang benar-benar diperiksa

| ID | Jenis | URL / ref | Confidence | Temuan dan batas | Akses |
| --- | --- | --- | --- | --- | --- |
| SRC-01 | Brief pengguna | ORBIT_Master_Prompt_01_Modular_PRD.md; salinan lampiran dibaca penuh | PRODUCT_ASSUMPTION / keputusan pengguna | Konteks, batas modul dan deliverable; bukan rubrik resmi atau bukti API | 18 Nov 2026 |
| SRC-02 | Primer: Fasilkom UI | https://cs.ui.ac.id/sarjana-ilmu-komputer/ | VERIFIED_OFFICIAL (konten halaman) | Halaman memuat konteks program, kurikulum delapan semester dan minimum 144 SKS. Tidak memverifikasi seluruh kode/prasyarat atau applicability angkatan pengguna. | 18 Nov 2026 |
| SRC-03 | Primer: Fasilkom UI | https://cs.ui.ac.id/sarjana-sistem-informasi/ | VERIFIED_OFFICIAL (konten halaman) | Memuat program SI dan referensi profil lulusan kurikulum 2024. Bukan bukti binding versi setiap mahasiswa. | 18 Nov 2026 |
| SRC-04 | Primer: Peraturan Rektor UI | https://sa.ui.ac.id/wp-content/uploads/2024/10/2024-PR-1-TENTANG-PENYELENGGARAAN-PROGRAM-SARJANA.pdf | VERIFIED_OFFICIAL (dokumen ditemukan/dibaca terbatas) | Peraturan No.1/2024; definisi IPS/IPK, Pasal 38–41 dan tabel konversi diperiksa. Applicability/ketentuan operasional terkini masih RV-04. | 18 Nov 2026 |
| SRC-04A | Primer: Direkt. Pendidikan UI | https://pendidikan.ui.ac.id/peraturan-rektor-universitas-indonesia/ | VERIFIED_OFFICIAL (daftar indeks) | Hasil penelusuran indeks mencantumkan Peraturan Sarjana No.1/2024; bukan audit lengkap seluruh amandemen. | 18 Nov 2026 |
| SRC-05 | Sekunder: roadmap komunitas | https://course.csui.dev/ | VERIFIED_SECONDARY (observasi halaman) | Pilihan semester, detail course/prasyarat dan relasi membuka course diamati dari teks halaman. Data tidak diangkat menjadi sumber resmi. | 18 Nov 2026 |
| SRC-06 | Desain pengguna: Figma | https://www.figma.com/design/uGYiD2ePUEiC7fu52Hp7uL?node-id=11-22 | VERIFIED_SECONDARY (observasi visual) | Dashboard v2 screenshot 1440×980 berhasil dibaca. Bukan inspeksi interaksi/layer/tokens atau bukti fungsi. | 18 Nov 2026 |
| SRC-07 | Desain pengguna: Figma | https://www.figma.com/design/uGYiD2ePUEiC7fu52Hp7uL?node-id=11-183 | VERIFIED_SECONDARY (observasi visual) | Roadmap v2 screenshot 1680×980 berhasil dibaca; menyatakan course/edge ilustratif. | 18 Nov 2026 |
| SRC-08 | Primer: W3C | https://www.w3.org/TR/WCAG22/ | VERIFIED_OFFICIAL (standar sumber primer) | WCAG 2.2 diperiksa untuk target aksesibilitas; belum audit implementasi Orbit. | 18 Nov 2026 |
| SRC-09 | Primer: OWASP project | https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html | VERIFIED_OFFICIAL (panduan penerbit asli, bukan kebijakan UI) | Authentication, password/recovery, generic error dan kontrol brute force diperiksa. | 18 Nov 2026 |
| SRC-10 | Primer: OWASP project | https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html | VERIFIED_OFFICIAL (panduan penerbit asli, bukan kebijakan UI) | Least privilege, deny-by-default dan permission per request diperiksa. | 18 Nov 2026 |
| SRC-11 | Primer: panduan dosen terlampir | Panduan Proyek Kelompok DDP1 Gasal 26_27.docx.pdf, versi 1,4 Nov 2026 16.00;5 halaman; SHA-256 `16d64e6c23b6c601e028232f97c298228a07175911f3b0570132c1c1810a49f5` | VERIFIED_OFFICIAL untuk tugas | Seluruh halaman teks dan visual diperiksa; deadline, teknologi, tim, bimbingan, kontribusi, deliverables dan rubrik. Bukan izin API atau validasi data kurikulum. | 18 Nov 2026 |
| SRC-12 | Primer: Flask | https://flask.palletsprojects.com/en/stable/ | VERIFIED_OFFICIAL untuk dokumentasi teknologi | Framework WSGI, Jinja dan test client; dasar rekomendasi teknis, bukan aturan DDP1 | 18 Nov 2026 |
| SRC-13 | Primer: Python sqlite3 | https://docs.python.org/3/library/sqlite3.html | VERIFIED_OFFICIAL untuk dokumentasi teknologi | SQLite berbasis berkas tanpa server terpisah; ketersediaan modul runtime tim perlu diperiksa | 18 Nov 2026 |
| SRC-14 | Primer: Python unittest | https://docs.python.org/3/library/unittest.html | VERIFIED_OFFICIAL untuk dokumentasi teknologi | Test cases/fixtures/suites dan otomasi; belum ada test aplikasi Orbit | 18 Nov 2026 |
| SRC-15 | Primer: Streamlit | https://docs.streamlit.io/develop/concepts/architecture | VERIFIED_OFFICIAL untuk dokumentasi teknologi | Session state/forms/rerun; alternatif yang memerlukan penyesuaian UI/state | 18 Nov 2026 |
| SRC-16 | Review dokumentasi independen yang dilampirkan pengguna | [ORBIT_Review_Independen_PRD_v0.2.md](https://chatgpt.com/library?file_id=libfile_2ba58f1dfc7481919f5d0044b9065870&account_id=personal); SHA-256 `b0045859cdc895a707487fadbaca13649c89ff61674444863a87bf00db00fade` | VERIFIED_SECONDARY untuk isi review; koreksi diperiksa langsung | Enam temuan prioritas/path/journey diverifikasi dan ditutup pada errata v0.2.1; bukan ketentuan dosen atau bukti test aplikasi. RV-14/15 dan kesiapan perangkat tetap open. | 18 Nov 2026 |

### Catatan terbatas dari SRC-04

Dokumen No.1/2024 memuat tabel konversi angka/huruf/bobot pada Pasal 38, aturan grade khusus dan pengulangan pada Pasal 40, serta perhitungan IPS/IPK pada Pasal 41. Teks menyebut kelulusan course yang diulang berdasarkan nilai terakhir; rumusan IPK menyebut mata kuliah dengan minimal C dan pengecualian BS/I. Karena itu, “semua attempt”, “nilai tertinggi” atau “nilai terakhir” tidak boleh diterapkan seragam ke semua perhitungan tanpa memeriksa ketentuan operasional dan applicability. Isi dokumen resmi telah ditemukan, tetapi Orbit belum memiliki binding policy lengkap untuk pengguna target. Dokumen ini tidak menetapkan eligibility IRS atau merangkum seluruh aturan kelulusan.

Contoh target 75/90 dan GPA 3,09 pada PRD-03 adalah fixture matematis dengan input eksplisit, bukan nilai mahasiswa atau hasil perhitungan kampus. Threshold per-course masih menunggu BRP dan aturan yang benar-benar berlaku.

### Observasi desain

Frame 11:22 memperlihatkan dashboard terang dengan sidebar, metric tiles, chart dan daftar tindakan; frame 11:183 menampilkan roadmap gelap, tab graf/list, kontrol semester dan legenda. Keduanya menyatakan isi ilustratif. Tidak dilakukan edit Figma, pengujian klik, inspect font/token exact atau pengukuran contrast. PRD-09 mengubah observasi visual menjadi usulan perilaku, bukan mengklaim semua interaksi sudah ada.

### Yang tidak diperiksa / tidak diasumsikan

Tidak mengakses akun akademik mahasiswa, portal SLCM personal, dokumentasi private SSO, data nilai nyata, dataset kating, isi Drive resource ; panduan DDP1 kini dibaca penuh melalui SRC-11. Tidak melakukan scraping portal, menguji login, atau memverifikasi afiliasi mahasiswa. Source roadmap komunitas tidak digunakan sebagai otoritas akademik. Tidak memerlukan riset exhaustive katalog untuk mendefinisikan kontrak PRD; kelengkapan data katalog adalah RV-02.

## Validation backlog

| ID | Status | Pertanyaan / gap | Dampak | Owner role | Bukti penutup / default aman |
| --- | --- | --- | --- | --- | --- |
| RV-01 | CLOSED — VERIFIED_OFFICIAL | Panduan DDP1 versi 1, seluruh 5 halaman diperiksa; Python utama, tim 3–4, deadline dan rubrik diketahui | Menutup gap aturan tugas; tidak membuktikan implementasi atau kapasitas aktual | Product Lead | SRC-11; kapasitas aktual dipisahkan ke RV-14 dan kebaruan konsep ke RV-15 |
| RV-02 | NEEDS_VALIDATION | Program/angkatan/versi kurikulum dan transisi target | Blocker klaim roadmap akurat produksi | Academic Curator | Buku/keputusan kurikulum resmi cocok scope; cek kode/SKS/prereq; default unknown atau demo |
| RV-03 | NEEDS_VALIDATION | BRP aktual per offering/kelas/periode, minimum komponen/bonus/drop | Blocker kalkulasi yang mengklaim aturan kelas | Grade Owner / pengampu sumber | BRP sah dan rule mapping reviewed; default personal linear draft |
| RV-04 | NEEDS_VALIDATION | Binding konversi, SKS, grade khusus, inclusion IPS/IPK, retake dan aturan terbaru | Blocker hasil GPA lengkap dan eligibility resmi | Academic Curator / Calculation Reviewer | Peraturan + pedoman operasional terbaru; examples compared to permitted reference; default partial/policy unknown |
| RV-05 | NEEDS EXTERNAL APPROVAL | SSO UI protocol, register client, scopes/claims dan izin | Blocker integrasi P2 saja | Integration Owner / otoritas kampus | Izin tertulis dan kontrak teknis; default demo lokal sintetis; layanan akun Orbit P2 |
| RV-06 | NEEDS EXTERNAL APPROVAL | API jadwal personal SLCM dan grant resmi | Blocker sync P2 saja | Integration Owner / pengelola SLCM | Dokumentasi authorized + scope+rate/failure rules; default manual |
| RV-07 | NEEDS_VALIDATION | Gate privasi k, fixed cells, rounds, withdrawals dan abuse donor | Blocker analytics SNR P2 | Privacy Reviewer | Threat review pada fixture differencing, review donor dedup dan policy release; default aggregate off |
| RV-08 | NEEDS_VALIDATION | Tiga resource awal dan hak distribusinya | Blocker publikasi resource terkait | Knowledge Curator | Permission/ownership evidence dan link check per item; default empty Vault |
| RV-09 | NEEDS_VALIDATION | Mapping career→competency→course dengan sumber | Blocker Navigator P2 | Competency Curator | Mapping reviewed dan scope kurikulum; default feature disabled |
| RV-10 | NEEDS_VALIDATION | Operator, hosting, akses admin, backups, deletion, retention | Blocker memakai data nyata/deployment | Security/Privacy Owner | Arsitektur dan operasi diverifikasi; review aturan yang berlaku bila dibutuhkan; default data sintetis |
| RV-11 | NEEDS_VALIDATION | Nama, peran, foto/portfolio dan kontak tim | Blocker publikasi biodata saja | Content Owner / anggota | Data dan consent pemilik; default empty profile dan contact internal |
| RV-12 | NEEDS_VALIDATION | Usability, contrast, keyboard, mobile dan feasibility target NFR | Blocker klaim accessible/performant | UX Lead / QA Lead | Prototype test dengan evidence; default target belum teruji |
| RV-13 | NEEDS_VALIDATION | Perubahan sumber akademik setelah tanggal akses | Risiko stale policy | Academic Curator | Review sebelum release dan tiap pergantian term/policy; default source badge & stop conflicted binding |
| RV-14 | NEEDS_VALIDATION | Nama anggota, kemampuan Python/web/Git dan jam efektif hingga 10 Des | Estimasi 84–100 jam-orang masih bersyarat | Product Lead + seluruh anggota | Catatan ketersediaan 18–19 Nov; fallback scope P0 tanpa P1; bukan mengarang jadwal personal |
| RV-15 | NEEDS_VALIDATION | Konsep mana benar-benar di luar materi kelas ini | Belum dapat mengklaim kriteria kebaruan terpenuhi | Seluruh anggota + Asdos | Bandingkan silabus/lab dan bahas graph traversal, tree validation, transaksi/tests; catat konsep terpilih dan teach-back |
| RV-16 | NEEDS_VALIDATION | Besarnya masalah dan kegunaan alur Roadmap/Grade Rescue | Klaim dampak masih hipotesis | Product Lead / UX | Rekomendasi 3–5 wawancara sukarela tanpa data nilai; ringkasan anonim dan observasi tugas; jumlah ini bukan ketentuan dosen |


RV-01 ditutup untuk aturan tugas pada 18 Nov 2026. RV-02–13 tetap open sesuai cakupan; izin kampus hanya memblokir fitur integrasi P2. RV-14 kapasitas aktual dan RV-15 konsep di luar kelas harus ditinjau 18–19 Nov. RV-16 masalah pengguna ditinjau sebelum feature freeze. RV-02/03/04 tidak memblokir demo sintetis berlabel; wajib sebelum klaim akademik resmi. RV-08 wajib sebelum link Vault P1 terbit; RV-10 wajib sebelum data nyata atau layanan publik.

## Prosedur verifikasi lanjutan

Simpan source URL/ref, penerbit, judul/versi, tanggal akses, bagian yang mendukung, program/cohort/period applicability, reviewer dan status berlaku. Dua sumber resmi berbeda tidak dipilih dengan voting; tahan binding dan minta klarifikasi otoritas terkait. Rule superseded tetap tersimpan untuk mereproduksi semester lama. Review ulang sebelum release, saat term berganti, atau sumber berubah. Jangan menjanjikan crawler/monitor otomatis pada MVP.

## Temuan → requirement

| Temuan | Respons kebutuhan |
| --- | --- |
| Figma memakai data ilustratif | UX-FR-002/009, PUB-FR-003, MAP-FR-001 |
| Policy akademik bergantung scope | PRO-FR-006/008, MAP-FR-003/009, GRD-FR-009/012 |
| Integrasi belum terbukti tersedia | CORE-FR-005, AUTH-FR-010, SCH-FR-001 |
| Tidak ada data kating sah | SNR-FR-004/008, GDE-FR-004 |
| Raw grades sensitif | AUTH-FR-004/006/007, SNR-FR-001/007 |
| Belum ada resource/tim terverifikasi | VLT-FR-005/009, PUB-FR-006 |
