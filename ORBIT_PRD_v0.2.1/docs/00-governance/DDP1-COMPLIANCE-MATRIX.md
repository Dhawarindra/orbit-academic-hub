# ORBIT — DDP1 Compliance Matrix

Versi **v0.2 DDP1 Draft** · 18 November 2026 (Asia/Jakarta) · Owner: Product Lead bersama tim 3–4 mahasiswa.

Status: audit dan rekomendasi dokumentasi; belum ada aplikasi atau bukti kelulusan implementasi.

[Panduan resmi DDP1 yang diaudit](https://chatgpt.com/library?file_id=libfile_56bfcb27965c81918a1b5748323aff62&account_id=personal).

## Sumber kebenaran dan arti status

Sumber utama: **Panduan Proyek Kelompok DDP1 Semester Gasal 2026/2027**, versi 1 (4 November 2026 16.00),5 halaman, lampiran pengguna; SRC-11 pada Research Register. Seluruh halaman dibaca, bukan hanya ketentuan yang dikutip pengguna. Nomor halaman di bawah mengikuti nomor cetak PDF.

**WAJIB** berarti kewajiban eksplisit panduan. **ARAHAN** berarti tujuan/anjuran resmi. **BOLEH/FAKTA** bukan kewajiban menambah fitur. **REKOMENDASI** adalah keputusan teknis/proses Orbit. **ASUMSI** masih memerlukan validasi. “Terpetakan” berarti desain siap diverifikasi; tidak sama dengan implementasi patuh.

## Ketentuan resmi → rancangan → bukti

| ID | Ketentuan resmi / jenis | Sumber | Pemetaan Orbit | Bukti dan acceptance saat implementasi | Status 18 Nov |
| --- | --- | --- | --- | --- | --- |
| DDP-01 | Mengidentifikasi masalah kehidupan sehari-hari, topik bebas; masalah nyata dan dampak positif diharapkan — tujuan/ARAHAN | Hlm. 2–3 | PRD-00 masalah informasi terpisah; Roadmap dan Grade Rescue; RV-16 | Jelaskan pengguna/konteks, satu contoh kebutuhan dan bagaimana alur membantu; ringkasan wawancara/observasi direkomendasikan, jumlah responden tidak ditentukan panduan | Hipotesis produk; validasi pengguna belum ada |
| DDP-02 | Python sebagai bahasa utama dan komponen utama; teknologi lain boleh mendukung — WAJIB | Hlm. 2 | D-18, MAP/GRD Python, Flask route/services, persistensi dan Dashboard aggregation Python | Tunjukkan fungsi/domain Python, input→hasil tanpa perhitungan akademik inti di JS, test domain dan walkthrough. Tidak menilai hanya dari persentase baris Python | Rancangan terpetakan; belum ada kode |
| DDP-03 | Solusi berkualitas mengintegrasikan materi/konsep pemrograman baru di luar yang diajarkan — WAJIB dan rubrik | Hlm. 2/5 | Graph traversal, tree validation, transaksi dan automated testing sebagai kandidat; RV-15 | Bandingkan dengan silabus/lab aktual; catat konsep yang benar-benar baru, kegunaan, implementasi dan penjelasan seluruh anggota | Belum terbukti baru bagi kelas ini |
| DDP-04 | Setiap anggota memahami mendalam setiap bagian kode yang dihasilkan — WAJIB | Hlm. 2 | Teach-back lintas engine, storage, UI dan test; bukan pembagian silo | Masing-masing dapat menelusuri fungsi inti seluruh modul, menjelaskan edge case, memperbaiki perubahan kecil dan menjawab pertanyaan; reviewer catat gap | Belum ada kode atau bukti pemahaman |
| DDP-05 | Setiap anggota aktif berkontribusi pada repository kode, tampak melalui commit history GitHub — WAJIB | Hlm. 2/4 | Pembagian tugas 3–4 orang, review lintas modul, commit bermakna sejak awal | Riwayat GitHub menunjukkan kontribusi aktif seluruh anggota dengan author benar dan perubahan dapat dijelaskan; panduan tidak menentukan jumlah commit minimum | Nama/repo/history belum tersedia |
| DDP-06 | Kelompok 3–4 mahasiswa, pembagian oleh dosen/Asdos — WAJIB/pengaturan resmi | Hlm. 3 | Rencana kapasitas 3 dan 4 anggota; RV-14 | Daftar kelompok resmi dan pemetaan peran aktual; jangan mengarang nama atau membentuk tim berbeda dari penetapan pengajar | Ukuran diketahui, daftar belum tersedia |
| DDP-07 | Satu Asdos pembimbing; jadwal/mekanisme bimbingan disepakati; diskusi topik/stack pada kickoff — pengaturan resmi | Hlm. 3–4 | Review scope/stack/konsep bersama Asdos 18–19 Nov jika belum dilakukan | Nama Asdos dan kesepakatan bimbingan/catatan keputusan; tidak mengarang frekuensi wajib | Belum ada bukti pertemuan |
| DDP-08 | Proyek 5 minggu; rilis/kickoff 5 November 2026 — FAKTA jadwal | Hlm. 4–5 | Rencana memakai sisa 18 Nov–10 Des, bukan lima minggu baru | Kalender delivery mencakup pengujian, repository, video dan buffer sebelum deadline | Terpetakan di MVP Scope |
| DDP-09 | Repository GitHub publik berisi source dan commit aktif seluruh anggota — WAJIB deliverable | Hlm. 4 | README reproduksi, source Python, fixtures sintetis, tests dan history | Tautan GitHub dapat dibuka tanpa akses privat, source dapat diperoleh/dijalankan sesuai README, history kontribusi ada. Struktur/README/tests adalah rekomendasi bukti kualitas, bukan format wajib yang ditentukan panduan | Belum tersedia |
| DDP-10 | Video demonstrasi YouTube maksimal 15 menit, mencakup latar masalah, demo aplikasi, arsitektur kode dan solusi — WAJIB deliverable | Hlm. 4 | Run-of-show 14 menit di readiness | Video terunggah, durasi≤15:00, ketiga muatan ada, suara/teks jelas dan tautan dapat diakses penilai; visibility rinci tidak ditentukan panduan | Belum tersedia |
| DDP-11 | Mengumpulkan tautan GitHub dan tautan YouTube — WAJIB | Hlm. 4 | Checklist submission dua tautan; target internal 9 Des | Kedua URL benar, diuji, merujuk versi final dan dikumpulkan melalui kanal yang diarahkan pengajar; kanal tidak disebut dalam lampiran | Belum dikumpulkan |
| DDP-12 | Deadline Kamis 10 Desember 2026 pukul 23.59 WIB — WAJIB | Hlm. 1; tanggal pada hlm. 5 | Freeze fitur 3–5 Des, video 6–8 Des, target internal 9 Des, buffer 10 Des | Bukti submission sebelum/hingga 10 Des 2026 23.59 WIB; target 9 Des adalah rekomendasi tim, bukan deadline pengganti | Terpetakan; belum submission |
| DDP-13 | AI/LLM boleh membantu pembuatan kode — BOLEH; kewajiban memahami kode tetap | Hlm. 2 | Catatan bantuan AI/rujukan dan review manusia direkomendasikan | Anggota mampu menjelaskan/mengecek kode yang dipakai; log AI direkomendasikan untuk transparansi, tidak diklaim deliverable wajib | Tidak ada coding dalam audit ini |
| DDP-14 | Bentuk aplikasi bebas termasuk console; eksplorasi web/GUI modern dianjurkan — BOLEH/ARAHAN | Hlm. 2–3 | Flask/Jinja direkomendasikan untuk mempertahankan UX Orbit; fallback Streamlit/console memerlukan keputusan tercatat | Python tetap utama; tidak perlu React, Django, PyGame atau deployment publik sebagai syarat panduan | Framework bukan kewajiban dosen |
| DDP-15 | Kontribusi/komunikasi sampai akhir; masalah ketidakadilan dapat dilaporkan; seleksi penghargaan bertahap — ARAHAN/informasi | Hlm. 4 | Koordinasi rutin dan pembagian adil; tim tidak mengoptimalkan janji menang | Catatan kerja dan penyelesaian hambatan; kompetisi Asdos→kelas→9 kelas adalah konteks penghargaan, bukan deliverable tambahan | Tidak ada klaim nominasi/nilai |

## Matriks enam kriteria resmi

Bobot berjumlah 100%. Bukti berikut adalah cara yang direkomendasikan untuk mendemonstrasikan pekerjaan, **bukan subrubrik resmi atau jaminan nilai**.

| Kriteria resmi | Bobot | Rancangan yang relevan | Bukti implementasi yang dapat ditunjukkan | Keterbatasan / penerimaan bukti |
| --- | --- | --- | --- | --- |
| Masalah yang diangkat |20% | PRD-00; kebutuhan memahami prasyarat dan target nilai; RV-16 | Contoh situasi mahasiswa, ringkasan observasi/wawancara sukarela anonim, demo tugas “apa dampak menunda A?” dan “berapa nilai UAS untuk target 75?” | Belum ada riset pengguna; jangan mengklaim penurunan stres/kenaikan IPK atau kebutuhan seluruh mahasiswa tanpa bukti |
| Keunikan dan daya tarik solusi |10% | CORE-FR-003/004, UX-FR-002; hubungan Roadmap+Grade Rescue+Dashboard dengan alasan, sumber dan simulasi terpisah | Satu cerita demo menghubungkan proyeksi nilai, prasyarat aktual dan dampak rencana; perlihatkan state unknown/stale yang jujur dan UX Orbit konsisten | Integrasi alur adalah hipotesis diferensiasi; bukan klaim belum pernah ada produk serupa |
| Penerapan konsep baru di luar kelas |20% | MAP-FR-003/005/007, GRD-FR-002, persistensi transaksi/test; RV-15 | Catatan pembanding materi kelas; implementasi graph traversal/tree evaluation, transaksi atau automated tests yang benar-benar baru; penjelasan alasan memilih dan contoh kegagalan yang ditangani | Tidak otomatis baru hanya karena memakai library/framework. Pilih konsep setelah memeriksa silabus/lab dan diskusi Asdos |
| Kompleksitas program |20% | MAP: AND/OR tiga nilai, cycle/dangling validation, downstream traversal; GRD: tree weights, normalisasi, bounds/target, presisi; integrasi revision/scenario | Tampilkan fungsi Python, data structures, input validation, expected/actual golden tests, kompleksitas algoritma yang sesuai implementasi dan edge cases | Banyak halaman/CRUD/login atau library graph saja tidak membuktikan kompleksitas buatan tim; jangan menambah fitur hanya untuk memperbanyak kode |
| Kualitas repository |20% | DDP-05/09; struktur domain dan tests; README setup/demo/limitations; changelog | Public GitHub, commit bermakna semua anggota, struktur jelas, dependencies dipin setelah diuji, data fixture berlabel, fresh-clone run, test output dan issue/review yang terkait | Tidak ada kuota commit, wajib CI, branch strategy, lisensi tertentu atau jumlah test dari panduan. Semua itu rekomendasi proses, bukan ketentuan baru |
| Kualitas video presentasi |10% | DDP-10; demo 14 menit yang menghubungkan masalah, aplikasi dan arsitektur Python | Tautan YouTube, durasi≤15 menit, demo terbaca, audio jelas, kode/domain dijelaskan, batas dan fitur future dibedakan; versi demo sesuai repo | Setiap anggota wajib memahami kode; panduan tidak mewajibkan setiap orang tampil kamera/berbicara. Pembagian narasi adalah rekomendasi |

## Hal yang tidak diwajibkan atau belum dibuktikan

Panduan tidak menetapkan framework, frontend tertentu, database tertentu, hosting aplikasi, API kampus, SSO/SLCM, fitur akademik tertentu, jumlah commit, jumlah responden, cakupan test numerik, format laporan tambahan atau kewajiban semua anggota tampil kamera. Django/PyGame/SCELE pada hlm. 3 adalah contoh. Contoh tersebut **bukan bukti ketersediaan atau izin integrasi Orbit**.

Lima laporan revisi adalah deliverable yang diminta pengguna pada audit ini; deliverable resmi pengumpulan proyek dalam lampiran tetap dua tautan: GitHub dan YouTube. Source repository publik tidak mewajibkan layanan web Orbit publik. Pilihan demo lokal, Flask/SQLite, cadangan 25%, freeze dan target internal 9 Des adalah rekomendasi. Kapasitas dua jam per orang per hari adalah asumsi, bukan fakta jadwal mahasiswa.

## Verifikasi akhir kepatuhan

Owner setiap bukti adalah peran usulan sampai daftar kelompok tersedia. Simpan bukti pada release final: URL repository, commit/tag, daftar kontribusi, hasil walkthrough seluruh anggota, catatan konsep baru, hasil demonstrasi, URL/durasi video dan bukti pengumpulan. Rubrik tidak dapat dinyatakan terpenuhi hanya karena fitur dicantumkan dalam PRD.
