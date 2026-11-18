# ORBIT — PRD Audit Report

Versi **v0.2 DDP1 Draft** · 18 November 2026 (Asia/Jakarta) · Owner: Product Lead bersama tim 3–4 mahasiswa.

Status: audit dan rekomendasi dokumentasi; belum ada aplikasi atau bukti kelulusan implementasi.

[Panduan resmi DDP1 yang diaudit](https://chatgpt.com/library?file_id=libfile_56bfcb27965c81918a1b5748323aff62&account_id=personal).

**Catatan v0.2.1:** laporan ini menyimpan hasil audit v0.2. Review independen kemudian menemukan empat label bisnis yang belum konsisten, satu penjelasan akar arsip dan risiko interpretasi journey. Koreksi serta batas penutupan dicatat di [errata](PRD-v0.2.1-ERRATA.md); angka FR/AC/test tidak berubah. Klaim konsistensi struktur pada v0.2 tidak berarti seluruh label semantik telah benar.

## Kesimpulan audit

Baseline dapat diakses: seluruh **13 PRD**, empat dokumen governance, QA baseline, README dan manifest. Tidak ada PRD yang direkonstruksi dari ingatan. Sebelum revisi, 19 berkas pada manifest cocok SHA-256; checkpoint v0.1 dipertahankan untuk perbandingan. Panduan resmi terlampir dibaca lengkap, melalui ekstraksi teks dan pemeriksaan visual seluruh 5 halaman.

Baseline memiliki **141 FR: 111 P0, 26 P1, 4 P2**, 102 BR, 39 NFR, 180 AC dan 180 test primer serta 12 skenario integrasi. Struktur dan prinsip integritas data sudah kuat, tetapi scope P0 mencakup terlalu banyak layanan untuk periode tersisa. Belum ada pilihan konkret yang menjamin Python menjadi komponen utama, dan dokumen belum memetakan kontribusi, video serta enam kriteria resmi.

Revisi mempertahankan semua ID lama, judul, 20 bagian setiap PRD, aturan numerik dan visi produk. Hasilnya **143 FR: 48 P0, 27 P1, 68 P2**, dengan dua FR baru khusus batas operasi demo lokal. Seluruh fitur yang ditunda tetap berada di PRD masing-masing dan berstatus Future Development. Sebagian FR memuat batas subkemampuan, misalnya MAP-FR-006: stale/reset P0, rebase penuh P2; hitungan FR mengikuti prioritas bagian yang aktif lebih dahulu.

**Status kepatuhan:** selaras pada tingkat rancangan setelah revisi; **belum terverifikasi pada implementasi**. Tidak ada kode aplikasi, repository implementasi, riwayat kontribusi, video, hasil usability atau hasil test aplikasi yang diperiksa/dihasilkan dalam tugas ini. Jumlah requirement bukan ukuran skor atau bukti kompleksitas implementasi.

## Sumber dan metode

| Sumber | Peran dan batas |
| --- | --- |
| Panduan DDP1 versi 1, timestamp 4 Nov 2026 16.00;5 halaman; SRC-11 | Sumber utama aturan tugas dan rubrik. SHA-256 `16d64e6c23b6c601e028232f97c298228a07175911f3b0570132c1c1810a49f5`. Hlm. 1/5 deadline; hlm. 2 Python/konsep/pemahaman/kontribusi; hlm. 3–4 tim/bimbingan/deliverables; hlm. 5 rubrik. |
| Baseline PRD v0.1,18 Nov 2026 | Kontrak produk yang direvisi; bukan bukti fitur sudah bekerja. Nama, ID, hubungan data, UX dan keputusan yang tidak terdampak dipertahankan. |
| Instruksi pengguna pada revisi ini | Hipotesis prioritas P0/P1/P2 dan larangan coding/rekonstruksi; bukan ketentuan dosen. |
| SRC-12–15, dokumentasi primer teknologi | Dasar rekomendasi teknis; tidak mengubah aturan tugas. Sumber akademik SRC-02–04 tetap perlu applicability RV-02–04. |

Audit memeriksa bagian scope, FR/BR/NFR, model/ownership, interfaces, UI/states, privacy, AC/test, risiko dan future pada setiap PRD; membandingkan dependency core; menelusuri FR→AC→test serta BR→FR; kemudian memberi disposisi dan merevisi bagian yang terdampak. Audit ini tidak menguji akses SSO/SLCM, melakukan scraping, mengakses nilai mahasiswa atau menerbitkan materi pihak lain.

## Temuan yang memerlukan perubahan

| ID | Tingkat | Bukti baseline / masalah | Revisi dan dasar | Status dokumentasi |
| --- | --- | --- | --- | --- |
| AUD-01 | Tinggi | PRD-00 Q-001, RV-01 dan indeks menyatakan rubrik/deadline belum tersedia; belum ada matriks enam kriteria | SRC-11 menutup gap aturan; pisahkan kapasitas/konsep baru ke RV-14/15; buat compliance matrix | Ditutup untuk ketersediaan panduan, implementasi tetap open |
| AUD-02 | Tinggi |111 FR P0 termasuk schedule, komunitas, auth, closeout, public pages dan feedback | Analisis 84–100 jam-orang untuk core; sisa waktu 18 Nov–10 Des; pindahkan requirement tanpa menghapusnya | Prioritas direvisi; kapasitas aktual belum dikonfirmasi |
| AUD-03 | Tinggi | Diagram master mengalir GDE→UX dan GDE→actual; CORE-FR-005 memerlukan closeout | Dashboard membaca MAP/GRD; GRD-FR-010 dapat konfirmasi/koreksi per course tanpa GDE; INT-T-010/013 menguji jalur ini | Dependency P0 diputus tanpa mengubah actual≠prediction |
| AUD-04 | Tinggi | PRO dan UX mensyaratkan akun; AUTH P0 mencakup sessions/recovery/roles/export/delete | AUTH-FR-014/015 baru untuk local-demo sintetis; layanan akun P2 tetap utuh sebelum penggunaan multiuser/data nyata | Batas mode dan AC/test ditambahkan |
| AUD-05 | Sedang | MAP-FR-006 rebase mempertahankan pilihan;010 multi-scenario;007/012 diasumsikan publish kurator | Satu skenario; stale/reset P0, rebase/compare P2; validasi dataset Python tanpa UI admin | Kompleksitas graf inti dipertahankan |
| AUD-06 | Tinggi | GRD-FR-001/020 mengharuskan migrasi struktur bernilai;010 melalui closeout;017 retake compare P0 | Kunci struktur setelah skor pada P0; migrasi/compare P2; GPA 008/009/015/019 P1; konfirmasi per course P0 | Rumus/golden fixtures tetap; batas rilis diperjelas |
| AUD-07 | Sedang | SCH hampir semua P0 termasuk blok/alokasi/salience; recurrence tersirat | Schedule/Stress sederhana P1; recurrence dan preparation engine P2; core Dashboard tidak menunggu SCH | Beban bukan indikator klinis; tidak mengklaim API jadwal tersedia |
| AUD-08 | Tinggi | SNR tips/empty state P0, agregat P1; donor/consent/privacy belum tersedia | Seluruh SNR P2; suppression/withdrawal dan fixture tetap; tidak membuat sampel kating palsu | Dependensi data dan operasional diakui |
| AUD-09 | Sedang | VLT P0 bergantung bookmark/report/moderator; hak resource belum ada | P1 hanya kurasi link, pencarian, URL/rights gate; akun/queue/credits P2; publikasi diblokir jika izin tidak jelas | Hak tidak dipangkas demi scope |
| AUD-10 | Sedang | CAR P1 membutuhkan mapping reviewed yang belum ada | Seluruh CAR P2 dengan alasan/source/ranking tetap | RV-09 masih open |
| AUD-11 | Tinggi | GDE P0 menggabungkan banyak sumber, dismissal, transaksi closeout dan concurrency | Seluruh GDE P2; konfirmasi hasil satu course tetap di GRD | Fitur lengkap dan AC/test tidak dihapus |
| AUD-12 | Sedang | UX dashboard lintas delapan domain, tren P0 dan dark theme P1 | Dashboard inti hanya MAP/GRD; tren P1, dark P2; mempertahankan token/identitas visual | Perubahan capability, bukan redesign |
| AUD-13 | Tinggi | AUTH local-account P0 terlalu besar; SSO/SLCM sudah guarded tetapi belum ada bukti izin | Local-demo tidak dipublikasikan sebagai layanan; integrasi 010 tetap P0 unavailable;008/009 P2 dengan RV-05/06 | Tidak ada asumsi API/SSO tersedia |
| AUD-14 | Sedang | PUB P0 marketing, team consent, tutorial/contact memerlukan alur akun/feedback | Status independen/demo P0; landing/FAQ/tutorial P1; tim/contact/community P2 | Tidak mengarang identitas tim |
| AUD-15 | Sedang | SUP search/bookmark/feedback/preferences P0 memperluas surface | Search/help/changelog aplikasi P1; layanan lainnya P2; changelog dokumentasi tetap diperbarui | Tidak menunda keamanan fitur yang kelak aktif |
| AUD-16 | Tinggi | Semua FR punya AC/test, tetapi target beberapa AC terlalu umum; belum ada bukti administratif DDP1 | Perjelas AC kontrak yang berubah, tambahkan guard lokal dan test integrasi; daftar cabang tambahan pada readiness | Coverage struktural bukan kecukupan semua cabang |
| AUD-17 | Sedang | NFR P0 lintas modul berpotensi dianggap wajib membangun semua modul; perangkat ukur belum ditetapkan | Tegaskan gate mengikuti fitur aktif, beban sintetis dan target belum diuji; AUTH/SCH gate future dipisahkan | Target angka adalah keputusan produk, bukan rubrik |

## Audit per dokumen

Kolom selaras berarti mendukung tujuan/aturan DDP1 atau prinsip produk; **tidak berarti dosen mewajibkan fitur tersebut**. Seluruh 13 PRD terdampak oleh perubahan scope/dependency; kedalaman revisinya berbeda. Bagian desain visual tidak diganti.

| Dokumen | Selaras / kontribusi nyata | Risiko kompleksitas, data atau teknologi | Disposisi / temuan |
| --- | --- | --- | --- |
| [PRD-00](../prd/PRD-00-master-product-overview.md) | Masalah terpadu, provenance, skenario terpisah; CORE-FR-003/004/008 tetap | Tidak ada mandat Python/kontribusi/video konkret; scope terlalu luas | AUD-01/02/03; lihat prioritas setiap FR di bawah |
| [PRD-01](../prd/PRD-01-academic-profile-and-onboarding.md) | Profil/offering/attempt memberi input valid untuk engine | Account dependency, migrasi versi/import, binding kurikulum belum ada | AUD-04; lihat prioritas setiap FR di bawah |
| [PRD-02](../prd/PRD-02-roadmap-and-semester-simulator.md) | AND/OR tiga nilai, DFS/topological traversal, constraint SKS; input/error dapat dijelaskan dalam Python | Kurikulum/prasyarat/penawaran resmi belum scope-bound; rebase/compare menambah state | AUD-05; lihat prioritas setiap FR di bawah |
| [PRD-03](../prd/PRD-03-grade-rescue-and-gpa-engine.md) | Traversal bobot bertingkat, validasi, bounds/target, presisi dan unknown; kompleksitas bukan sekadar CRUD | BRP/konversi/retake resmi belum bound; migrasi skor dan closeout memperbesar dependency | AUD-06; lihat prioritas setiap FR di bawah |
| [PRD-04](../prd/PRD-04-schedule-and-stress-radar.md) | Interval overlap dan agregasi beban/coverage bermakna bila P1 aktif | Recurring/allocating/salience; data jadwal manual; tidak ada bukti API SLCM | AUD-07; lihat prioritas setiap FR di bawah |
| [PRD-05](../prd/PRD-05-senior-playbook-and-insights.md) | Agregasi/dedup/suppression bermakna untuk visi penuh | Donor sah, consent, risiko reidentifikasi dan moderasi belum tersedia | AUD-08; lihat prioritas setiap FR di bawah |
| [PRD-06](../prd/PRD-06-knowledge-vault-and-contributors.md) | Filter/ranking metadata dan validasi URL; link-only menghindari hosting materi | Hak distribusi setiap link belum ada; contribution/report/bookmark bergantung layanan tambahan | AUD-09; lihat prioritas setiap FR di bawah |
| [PRD-07](../prd/PRD-07-career-to-course-navigator.md) | Ranking deterministik dan prasyarat tidak dilangkahi | Mapping kompetensi/sumber/reviewer belum tersedia; manfaat tidak perlu untuk demo inti | AUD-10; lihat prioritas setiap FR di bawah |
| [PRD-08](../prd/PRD-08-guidance-engine-and-semester-closeout.md) | Rule precedence, konflik, idempotensi dan snapshot terdefinisi | Membutuhkan banyak modul dan transaksi lifecycle; bukan prasyarat Dashboard | AUD-03/11; lihat prioritas setiap FR di bawah |
| [PRD-09](../prd/PRD-09-design-system-navigation-and-ux.md) | Dashboard, label actual/prediction, keyboard, list dan input errors mendukung demonstrasi | Belum ada uji contrast/usability; visual Figma bukan bukti fungsi | AUD-12; lihat prioritas setiap FR di bawah |
| [PRD-10](../prd/PRD-10-authentication-privacy-and-integrations.md) | No password kampus, no hidden integration, ownership dan privacy gates baik | Auth/recovery/role/retention kompleks; kontrak SSO/SLCM belum ada | AUD-04/13; lihat prioritas setiap FR di bawah |
| [PRD-11](../prd/PRD-11-public-pages-faq-and-team.md) | Independensi dan data demo jelas; klaim fitur sesuai capability | Landing/contact/biodata bukan deliverable resmi dan identitas belum diberikan | AUD-14; lihat prioritas setiap FR di bawah |
| [PRD-12](../prd/PRD-12-search-feedback-and-supporting-features.md) | Search metadata, safe text dan ownership bukan retrieval isi Drive | Feedback queue/bookmark/preferences memperluas dependency; digest perlu infra | AUD-15; lihat prioritas setiap FR di bawah |

## Audit governance

| Dokumen | Temuan baseline | Revisi |
| --- | --- | --- |
| PRODUCT-DOC-INDEX.md | Dependency dan vertical slice lama memasukkan closeout serta komunitas; gate menunggu rubrik | Indeks prioritas/urutan dan dependency core diselaraskan; lima laporan ditautkan |
| GLOSSARY-AND-DECISION-LOG.md | D-03/07–13 mencatat prioritas lama; actual selalu dipicu closeout | Riwayat keputusan tidak dihapus; D-16–21 memberi supersesi terbatas, local owner_scope dan konfirmasi per course |
| REQUIREMENTS-TRACEABILITY-MATRIX.md | P0 lama pada 141 FR dan sebagian integrasi; baseline 180 AC | Priority, perilaku, test eligibility dan dua FR baru disinkronkan; menjadi 182 AC, 182 test primer dan 14 integrasi |
| RESEARCH-AND-VALIDATION-REGISTER.md | RV-01 mencampur aturan tugas dengan kapasitas; sumber DDP1 belum ada | SRC-11 resmi dan SRC-12–15 teknis; RV-01 closed hanya aturan; RV-14/15/16 menampung kapasitas, kebaruan dan bukti masalah |
| QA-DOCUMENTATION-REPORT.md / README / MANIFEST | Menggambarkan snapshot v0.1 dan pemeriksaan referensi, bukan implementasi | Riwayat QA dipertahankan, lampiran QA v0.2 dan manifest terbaru; tidak mengubah hasil lama menjadi hasil aplikasi |

## Kecukupan acceptance criteria dan test cases

Tidak ditemukan FR/NFR baseline tanpa tautan AC dan test primer: 141 FR+39 NFR→180 AC/test;102 BR menunjuk FR terkait. Ini **coverage struktural**, bukan bukti setiap perilaku dan cabang telah diuji. Contoh gap semantik yang diperbaiki/ditindaklanjuti:

| Requirement / test | Gap | Penanganan |
| --- | --- | --- |
| CORE-FR-005, CORE-AC/T-005, INT-T-010 | Definisi demo selesai masih memerlukan fitur yang dipindahkan | Setup seluruh modul opsional off; keluaran inti terukur dan export lokal |
| UX-FR-002 dan CORE-FR-002 | Dashboard belum menjelaskan perilaku bila GDE tidak dibangun | Read langsung MAP/GRD dengan revision, unknown dan stale; AC diselaraskan |
| MAP-FR-006 | “Tidak memakai baseline lama” tidak memastikan pilihan reset/rebase yang tersedia | R1→r2, stale, reset tidak mengubah actual; full rebase tetap P2 |
| GRD-FR-001/020 | AC lama tidak menjelaskan penolakan perubahan struktur jika migrasi tidak dibangun | Lock setelah skor, perubahan ditolak tanpa write; migration AC020 tetap P2 |
| GRD-FR-010 | Hasil aktual hanya diuji dari closeout, koreksi per course belum punya jalur | Preview, explicit source, revisi/koreksi dan stale rejection; INT-T-013 tambahan |
| AUTH-FR-014/015 baru | Mode lokal, export/reset/restart belum dispesifikasikan | AC/T014/015 serta INT-T-014 ditambahkan; bukan mengganti kontrol akun future |
| MAP-FR-003/005/007/012, GRD-FR-002/007/018 | Fixture utama belum mencakup seluruh kombinasi truth table, disconnected graph, tree invalid dan numeric input | Test tambahan DDP-T-01–05 di readiness; implementasi tetap harus mengembangkan kasus berbasis cabang, bukan menyalin expected output saja |
| NFR latency/accessibility | Perangkat, build dan hasil ukur belum ada; target generic tidak membuktikan p95/WCAG | Definisikan rekaman lingkungan dan cara ukur sebelum eksekusi; klaim lulus ditahan |
| Kontribusi/pemahaman/video | Belum dipetakan sebagai bukti tugas | DDP-04/05/09/10 dan rubric matrix; bukti aktual masih belum tersedia |

## Data dan izin institusi

| Data/akses | Diperlukan untuk | Status dan fallback DDP1 |
| --- | --- | --- |
| Kode/SKS/prasyarat/versi kurikulum dan penawaran | Klaim Roadmap akademik nyata | RV-02/13 open; fixture sintetis jelas. Jangan menyebut semua kurikulum UI terverifikasi. Dokumen publik resmi yang cocok scope dapat ditelaah; akses nonpublik memerlukan izin. |
| BRP per kelas/periode dan kebijakan nilai/inclusion | Hasil yang mengklaim aturan kelas/IPS/IPK | RV-03/04 open; model linear personal/demo dan policy unknown; tidak menebak konversi A atau aturan retake. |
| SSO UI, SLCM dan API universitas | Login/sinkronisasi resmi | RV-05/06 memerlukan izin/kontrak resmi; adapter off P2. Contoh scraping SCELE pada panduan bukan bukti akses untuk Orbit. |
| Nilai/identitas mahasiswa, kontribusi kating | Akun nyata/SNR | Tidak tersedia; tidak dikumpulkan pada demo. Consent/keamanan dan data layak harus terpenuhi sebelum fitur future. |
| Materi Drive/tautan resource | Vault P1 | Bukti hak berbagi dan pemeriksaan link per item; tanpa bukti tetap kosong/hidden. Link publik tidak otomatis memberikan hak mendistribusikan konten. |
| Mapping karier/kompetensi | CAR | RV-09 open; seluruh mapping hipotetis tetap fixture P2. |

## Disposisi setiap requirement fungsional

Seluruh 141 FR baseline ditinjau. Dua baris baru ditandai “baru”. ID/AC/test lama tetap; rincian aturan yang tidak berubah dapat dibaca pada PRD. Penilaian “dipertahankan” tidak berarti wajib dosen atau sudah diimplementasikan. Temuan memberi alasan dan dependency/data risk melalui tabel di atas.

| Requirement | Prioritas v0.1→v0.2 | Disposisi | Dasar | AC / test |
| --- | --- | --- | --- | --- |
| CORE-FR-001 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-02/AUD-03 | CORE-AC-001 / CORE-T-001 |
| CORE-FR-002 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-02/AUD-03 | CORE-AC-002 / CORE-T-002 |
| CORE-FR-003 | P0→P0 | Dipertahankan | AUD-02/AUD-03 | CORE-AC-003 / CORE-T-003 |
| CORE-FR-004 | P0→P0 | Dipertahankan | AUD-02/AUD-03 | CORE-AC-004 / CORE-T-004 |
| CORE-FR-005 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-02/AUD-03 | CORE-AC-005 / CORE-T-005 |
| CORE-FR-006 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-02/AUD-03 | CORE-AC-006 / CORE-T-006 |
| CORE-FR-007 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-02/AUD-03 | CORE-AC-007 / CORE-T-007 |
| CORE-FR-008 | P0→P0 | Dipertahankan | AUD-02/AUD-03 | CORE-AC-008 / CORE-T-008 |
| PRO-FR-001 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-04 | PRO-AC-001 / PRO-T-001 |
| PRO-FR-002 | P0→P0 | Dipertahankan | AUD-04 | PRO-AC-002 / PRO-T-002 |
| PRO-FR-003 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-04 | PRO-AC-003 / PRO-T-003 |
| PRO-FR-004 | P0→P0 | Dipertahankan | AUD-04 | PRO-AC-004 / PRO-T-004 |
| PRO-FR-005 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-04 | PRO-AC-005 / PRO-T-005 |
| PRO-FR-006 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04 | PRO-AC-006 / PRO-T-006 |
| PRO-FR-007 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-04 | PRO-AC-007 / PRO-T-007 |
| PRO-FR-008 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04 | PRO-AC-008 / PRO-T-008 |
| PRO-FR-009 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04 | PRO-AC-009 / PRO-T-009 |
| MAP-FR-001 | P0→P0 | Dipertahankan | AUD-05 | MAP-AC-001 / MAP-T-001 |
| MAP-FR-002 | P0→P0 | Dipertahankan | AUD-05 | MAP-AC-002 / MAP-T-002 |
| MAP-FR-003 | P0→P0 | Dipertahankan | AUD-05 | MAP-AC-003 / MAP-T-003 |
| MAP-FR-004 | P0→P0 | Dipertahankan | AUD-05 | MAP-AC-004 / MAP-T-004 |
| MAP-FR-005 | P0→P0 | Dipertahankan | AUD-05 | MAP-AC-005 / MAP-T-005 |
| MAP-FR-006 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-05 | MAP-AC-006 / MAP-T-006 |
| MAP-FR-007 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-05 | MAP-AC-007 / MAP-T-007 |
| MAP-FR-008 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-05 | MAP-AC-008 / MAP-T-008 |
| MAP-FR-009 | P0→P0 | Dipertahankan | AUD-05 | MAP-AC-009 / MAP-T-009 |
| MAP-FR-010 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-05 | MAP-AC-010 / MAP-T-010 |
| MAP-FR-011 | P0→P0 | Dipertahankan | AUD-05 | MAP-AC-011 / MAP-T-011 |
| MAP-FR-012 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-05 | MAP-AC-012 / MAP-T-012 |
| GRD-FR-001 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-06 | GRD-AC-001 / GRD-T-001 |
| GRD-FR-002 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-002 / GRD-T-002 |
| GRD-FR-003 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-003 / GRD-T-003 |
| GRD-FR-004 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-004 / GRD-T-004 |
| GRD-FR-005 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-005 / GRD-T-005 |
| GRD-FR-006 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-006 / GRD-T-006 |
| GRD-FR-007 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-007 / GRD-T-007 |
| GRD-FR-008 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-06 | GRD-AC-008 / GRD-T-008 |
| GRD-FR-009 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-06 | GRD-AC-009 / GRD-T-009 |
| GRD-FR-010 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-06 | GRD-AC-010 / GRD-T-010 |
| GRD-FR-011 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-011 / GRD-T-011 |
| GRD-FR-012 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-012 / GRD-T-012 |
| GRD-FR-013 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-06 | GRD-AC-013 / GRD-T-013 |
| GRD-FR-014 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-014 / GRD-T-014 |
| GRD-FR-015 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-06 | GRD-AC-015 / GRD-T-015 |
| GRD-FR-016 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-016 / GRD-T-016 |
| GRD-FR-017 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-06 | GRD-AC-017 / GRD-T-017 |
| GRD-FR-018 | P0→P0 | Dipertahankan | AUD-06 | GRD-AC-018 / GRD-T-018 |
| GRD-FR-019 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-06 | GRD-AC-019 / GRD-T-019 |
| GRD-FR-020 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-06 | GRD-AC-020 / GRD-T-020 |
| SCH-FR-001 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-07 | SCH-AC-001 / SCH-T-001 |
| SCH-FR-002 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-07 | SCH-AC-002 / SCH-T-002 |
| SCH-FR-003 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-07 | SCH-AC-003 / SCH-T-003 |
| SCH-FR-004 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-07 | SCH-AC-004 / SCH-T-004 |
| SCH-FR-005 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-07 | SCH-AC-005 / SCH-T-005 |
| SCH-FR-006 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-07 | SCH-AC-006 / SCH-T-006 |
| SCH-FR-007 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-07 | SCH-AC-007 / SCH-T-007 |
| SCH-FR-008 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-07 | SCH-AC-008 / SCH-T-008 |
| SCH-FR-009 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-07 | SCH-AC-009 / SCH-T-009 |
| SCH-FR-010 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-07 | SCH-AC-010 / SCH-T-010 |
| SCH-FR-011 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-07 | SCH-AC-011 / SCH-T-011 |
| SCH-FR-012 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-07 | SCH-AC-012 / SCH-T-012 |
| SNR-FR-001 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-08 | SNR-AC-001 / SNR-T-001 |
| SNR-FR-002 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-08 | SNR-AC-002 / SNR-T-002 |
| SNR-FR-003 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-08 | SNR-AC-003 / SNR-T-003 |
| SNR-FR-004 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-08 | SNR-AC-004 / SNR-T-004 |
| SNR-FR-005 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-08 | SNR-AC-005 / SNR-T-005 |
| SNR-FR-006 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-08 | SNR-AC-006 / SNR-T-006 |
| SNR-FR-007 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-08 | SNR-AC-007 / SNR-T-007 |
| SNR-FR-008 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-08 | SNR-AC-008 / SNR-T-008 |
| SNR-FR-009 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-08 | SNR-AC-009 / SNR-T-009 |
| VLT-FR-001 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-09 | VLT-AC-001 / VLT-T-001 |
| VLT-FR-002 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-09 | VLT-AC-002 / VLT-T-002 |
| VLT-FR-003 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-09 | VLT-AC-003 / VLT-T-003 |
| VLT-FR-004 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-09 | VLT-AC-004 / VLT-T-004 |
| VLT-FR-005 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-09 | VLT-AC-005 / VLT-T-005 |
| VLT-FR-006 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-09 | VLT-AC-006 / VLT-T-006 |
| VLT-FR-007 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-09 | VLT-AC-007 / VLT-T-007 |
| VLT-FR-008 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-09 | VLT-AC-008 / VLT-T-008 |
| VLT-FR-009 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-09 | VLT-AC-009 / VLT-T-009 |
| VLT-FR-010 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-09 | VLT-AC-010 / VLT-T-010 |
| VLT-FR-011 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-09 | VLT-AC-011 / VLT-T-011 |
| CAR-FR-001 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-10 | CAR-AC-001 / CAR-T-001 |
| CAR-FR-002 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-10 | CAR-AC-002 / CAR-T-002 |
| CAR-FR-003 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-10 | CAR-AC-003 / CAR-T-003 |
| CAR-FR-004 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-10 | CAR-AC-004 / CAR-T-004 |
| CAR-FR-005 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-10 | CAR-AC-005 / CAR-T-005 |
| CAR-FR-006 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-10 | CAR-AC-006 / CAR-T-006 |
| CAR-FR-007 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-10 | CAR-AC-007 / CAR-T-007 |
| CAR-FR-008 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-10 | CAR-AC-008 / CAR-T-008 |
| GDE-FR-001 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-001 / GDE-T-001 |
| GDE-FR-002 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-002 / GDE-T-002 |
| GDE-FR-003 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-003 / GDE-T-003 |
| GDE-FR-004 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-004 / GDE-T-004 |
| GDE-FR-005 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-005 / GDE-T-005 |
| GDE-FR-006 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-006 / GDE-T-006 |
| GDE-FR-007 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-007 / GDE-T-007 |
| GDE-FR-008 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-008 / GDE-T-008 |
| GDE-FR-009 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-009 / GDE-T-009 |
| GDE-FR-010 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-03/AUD-11 | GDE-AC-010 / GDE-T-010 |
| UX-FR-001 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-12 | UX-AC-001 / UX-T-001 |
| UX-FR-002 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-12 | UX-AC-002 / UX-T-002 |
| UX-FR-003 | P0→P0 | Dipertahankan | AUD-12 | UX-AC-003 / UX-T-003 |
| UX-FR-004 | P0→P0 | Dipertahankan | AUD-12 | UX-AC-004 / UX-T-004 |
| UX-FR-005 | P0→P0 | Dipertahankan | AUD-12 | UX-AC-005 / UX-T-005 |
| UX-FR-006 | P0→P0 | Dipertahankan | AUD-12 | UX-AC-006 / UX-T-006 |
| UX-FR-007 | P0→P0 | Dipertahankan | AUD-12 | UX-AC-007 / UX-T-007 |
| UX-FR-008 | P0→P0 | Dipertahankan | AUD-12 | UX-AC-008 / UX-T-008 |
| UX-FR-009 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-12 | UX-AC-009 / UX-T-009 |
| UX-FR-010 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-12 | UX-AC-010 / UX-T-010 |
| AUTH-FR-001 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-001 / AUTH-T-001 |
| AUTH-FR-002 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-002 / AUTH-T-002 |
| AUTH-FR-003 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-003 / AUTH-T-003 |
| AUTH-FR-004 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-004 / AUTH-T-004 |
| AUTH-FR-005 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-005 / AUTH-T-005 |
| AUTH-FR-006 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-006 / AUTH-T-006 |
| AUTH-FR-007 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-007 / AUTH-T-007 |
| AUTH-FR-008 | P2→P2 | Dipertahankan; Future Development | AUD-04/AUD-13 | AUTH-AC-008 / AUTH-T-008 |
| AUTH-FR-009 | P2→P2 | Dipertahankan; Future Development | AUD-04/AUD-13 | AUTH-AC-009 / AUTH-T-009 |
| AUTH-FR-010 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-04/AUD-13 | AUTH-AC-010 / AUTH-T-010 |
| AUTH-FR-011 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-011 / AUTH-T-011 |
| AUTH-FR-012 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-012 / AUTH-T-012 |
| AUTH-FR-013 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-04/AUD-13 | AUTH-AC-013 / AUTH-T-013 |
| AUTH-FR-014 | baru→P0 | Baru: batas demo lokal | AUD-04/AUD-13 | AUTH-AC-014 / AUTH-T-014 |
| AUTH-FR-015 | baru→P0 | Baru: batas demo lokal | AUD-04/AUD-13 | AUTH-AC-015 / AUTH-T-015 |
| PUB-FR-001 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-14 | PUB-AC-001 / PUB-T-001 |
| PUB-FR-002 | P0→P0 | Prioritas/perilaku disesuaikan | AUD-14 | PUB-AC-002 / PUB-T-002 |
| PUB-FR-003 | P0→P0 | Dipertahankan | AUD-14 | PUB-AC-003 / PUB-T-003 |
| PUB-FR-004 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-14 | PUB-AC-004 / PUB-T-004 |
| PUB-FR-005 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-14 | PUB-AC-005 / PUB-T-005 |
| PUB-FR-006 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-14 | PUB-AC-006 / PUB-T-006 |
| PUB-FR-007 | P1→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-14 | PUB-AC-007 / PUB-T-007 |
| PUB-FR-008 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-14 | PUB-AC-008 / PUB-T-008 |
| SUP-FR-001 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-15 | SUP-AC-001 / SUP-T-001 |
| SUP-FR-002 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-15 | SUP-AC-002 / SUP-T-002 |
| SUP-FR-003 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-15 | SUP-AC-003 / SUP-T-003 |
| SUP-FR-004 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-15 | SUP-AC-004 / SUP-T-004 |
| SUP-FR-005 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-15 | SUP-AC-005 / SUP-T-005 |
| SUP-FR-006 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-15 | SUP-AC-006 / SUP-T-006 |
| SUP-FR-007 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-15 | SUP-AC-007 / SUP-T-007 |
| SUP-FR-008 | P0→P1 | Prioritas/perilaku disesuaikan; opsional | AUD-15 | SUP-AC-008 / SUP-T-008 |
| SUP-FR-009 | P2→P2 | Dipertahankan; Future Development | AUD-15 | SUP-AC-009 / SUP-T-009 |
| SUP-FR-010 | P2→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-15 | SUP-AC-010 / SUP-T-010 |
| SUP-FR-011 | P0→P2 | Prioritas/perilaku disesuaikan; Future Development | AUD-15 | SUP-AC-011 / SUP-T-011 |

## Batas hasil audit

Lima laporan dan revisi ini menutup gap dokumentasi yang dapat diselesaikan dari sumber tersedia. Ketersediaan waktu anggota, kebaruan relatif terhadap kelas, data akademik nyata, akses institusi dan bukti implementasi tetap terbuka. Rekomendasi scope bersyarat pada estimasi; tidak menjanjikan nilai atau persetujuan dosen. Tidak ada aplikasi dibangun dalam tahap ini.
