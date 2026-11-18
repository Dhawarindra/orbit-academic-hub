# ORBIT — Errata PRD v0.2.1

Tanggal **18 November 2026 (WIB)** · Baseline: **v0.2 DDP1 Draft** · Status: dokumentasi dikoreksi; **CONDITIONAL GO untuk desain arsitektur**.

## Putusan dan sumber

[Review independen yang dilampirkan](https://chatgpt.com/library?file_id=libfile_2ba58f1dfc7481919f5d0044b9065870&account_id=personal) telah dibaca penuh dan dicocokkan dengan PRD/RTM/README serta isi ZIP v0.2 yang aktual. Seluruh enam temuan dapat dikonfirmasi. Empat temuan pertama adalah label bisnis yang tertinggal dari prioritas FR; kelima membingungkan dua jenis path; keenam adalah risiko scope creep karena journey belum diberi label langsung.

Koreksi ini tidak mengubah scope atau jumlah requirement: **143 FR (48 P0, 27 P1, 68 P2), 102 BR, 39 NFR, 182 AC dan 182 test primer**, serta 14 test integrasi tetap. Seluruh baris FR, NFR, AC dan test primer identik dengan v0.2; hanya empat BR diperjelas. Empat PRD terdampak adalah PRD-00/09/11/12. Sembilan PRD lain tidak disentuh. Identitas dan nama berkas/requirement tetap; tidak ada kode aplikasi atau perubahan Figma.

Review adalah masukan audit, bukan aturan baru dari dosen. Panduan resmi SRC-11 tetap sumber utama ketentuan tugas. Review diberi SRC-16; hash lampiran `b0045859cdc895a707487fadbaca13649c89ff61674444863a87bf00db00fade`. Dokumen review asli tidak diubah.

## Respons per temuan

| ID | Temuan dan bukti v0.2 | Koreksi v0.2.1 | Lokasi / verifikasi | Status |
| --- | --- | --- | --- | --- |
| ERR-01 | UX-BR-001 menyebut P1 dark, UX-FR-010 P2 | Dark mode tetap P2, global dan hanya aktif melalui capability manifest | PRD-09 BR001 dan row RTM; FR010/AC010/test010 tidak berubah | CLOSED — dokumentasi |
| ERR-02 | UX-BR-002 menampilkan Minat & Jalur bila P1 aktif, sementara CAR seluruhnya P2 | Navigasi berbasis capability; Career Navigator/Playbook P2, Jadwal/Vault/search P1, core P0 | PRD-09 BR002 + RTM; fitur nonaktif tidak memiliki aksi aktif | CLOSED — dokumentasi |
| ERR-03 | PUB-BR-006 menyebut contact P0; PUB-FR-008 dan SUP-FR-005 P2 | Contact/feedback internal tetap P2 dan tidak menjadi dependency P0 | PRD-11 BR006 + RTM | CLOSED — dokumentasi |
| ERR-04 | SUP-BR-001 menyebut P0 corpus; SUP-FR-001 P1 | “Saat search aktif (P1)” dengan corpus/privacy yang sama | PRD-12 BR001 + RTM | CLOSED — dokumentasi |
| ERR-05 | README menyebut folder historis v0.1 tanpa membedakan root ZIP aktual v0.2 | Bedakan folder historis dari root archive; ZIP baru root ORBIT_PRD_v0.2.1/ dan manifest archive_root | README, manifest dan inspeksi root ZIP aktual | CLOSED — dokumentasi/kemasan |
| ERR-06 | Journey master/UX masih menyebut login, pekan padat, closeout atau resource tanpa label langsung | J1 core memakai workspace lokal P0; login disimpan sebagai varian P2; journey lain diberi label P0/P1/P2; handoff hanya P0+gate terkait | PRD-00/09 bagian 6, MVP Scope, Readiness dan indeks | CLOSED — mitigasi dokumentasi; penerapan tetap perlu dicek saat coding |

## Before/after aturan yang dikoreksi

| ID | Sebelum | Sesudah |
| --- | --- | --- |
| UX-BR-001 | Source visual hanya arah: Dashboard v2 terang, Roadmap v2 gelap. P0 memilih tema terang lintas halaman; P1 dark harus berlaku global dan diuji sendiri. | Source visual hanya arah: Dashboard v2 terang, Roadmap v2 gelap. P0 memilih tema terang lintas halaman; dark mode P2 harus berlaku global dan diuji sendiri, serta hanya tampil aktif bila capability tema gelap diaktifkan. |
| UX-BR-002 | Navigasi primary: Ringkasan, Roadmap, Nilai & Target, Jadwal, Komunitas. Vault/Playbook berada di Komunitas; Minat & Jalur tampil bila P1 aktif. Pengaturan/Bantuan tetap tersedia. | Navigasi mengikuti capability manifest, bukan label prioritas saja. P0 menampilkan Ringkasan, Roadmap dan Nilai & Target serta akses ekspor/reset lokal. Jadwal, Vault dan search P1 hanya aktif setelah keputusan scope tercatat; Playbook dan Minat & Jalur adalah P2 dan hanya tampil aktif bila capability terkait diaktifkan. Pengelompokan Komunitas tetap bagian desain. Menu fitur nonaktif disembunyikan atau berlabel direncanakan, tanpa aksi aktif; bantuan lanjutan mengikuti capability, sedangkan petunjuk menjalankan demo tersedia pada README. |
| PUB-BR-006 | Kontak P0 adalah feedback internal; alamat organisasi atau kanal publik baru ditampilkan setelah pengguna memberikan dan menyetujui publikasinya. | Kontak aplikasi berupa feedback internal adalah P2 melalui PUB-FR-008 dan SUP-FR-005; bukan dependency atau kewajiban tersembunyi P0. Alamat organisasi atau kanal publik hanya ditampilkan setelah pengguna memberikan dan menyetujui publikasinya. |
| SUP-BR-001 | P0 search corpus: published Course/CurriculumCourse, Topic dan Resource metadata. Tidak ada grade, nama pemilik akun, contribution raw, feedback atau isi Drive dalam global search. | Saat search aktif (P1), corpus terdiri dari published Course/CurriculumCourse, Topic dan Resource metadata. Tidak ada grade, nama pemilik akun, contribution raw, feedback atau isi Drive dalam global search. |

## Kontrak handoff berikutnya

Desain arsitektur boleh dilanjutkan berdasarkan dokumen ini sambil menyelesaikan bukti yang belum ada. Jangan menyebut MVP final/siap implementasi penuh sebelum RV-14 kapasitas anggota, RV-15 kebaruan konsep dan kesiapan runtime pada perangkat tim terbukti. Estimasi 84–100 jam-orang adalah perkiraan paket, bukan estimasi implementasi tiap FR; uraikan kembali setelah spike teknis yang kelak dikerjakan pada tahap terpisah.

Handoff harus mencantumkan:

1. Daftar anggota resmi 3–4 orang, jam efektif nyata, kemampuan Python/Git/web, catatan bimbingan dan konsep baru yang dipilih berdasarkan materi kelas.
2. Scope awal **hanya 48 FR P0**, bersama BR/NFR/AC/test kemampuan aktif. Semua P1/P2 dan subkemampuan future dalam FR campuran nonaktif. Gate kapasitas tidak mengaktifkan fitur otomatis; diperlukan keputusan scope tercatat beserta dependensi/test dan capability manifest.
3. Arsitektur monolit Python modular; rencana file per file, writer/reader data, transaksi, revision/stale, actual/scenario, dan daftar test yang harus lulus. Ini rencana untuk tahap berikutnya, bukan kode dalam errata ini.
4. Dashboard hanya menunjukkan hasil nyata dari engine demo atau unknown/unavailable. IPK/tren tetap P1, insight kating dan dark mode P2. Frame Figma tidak memberi izin memasukkan delapan semester/data resmi rekaan atau membuat fitur future aktif.
5. Bukti yang belum ada tetap open: validasi masalah pengguna, data akademik resmi sesuai scope, kesiapan perangkat, kontribusi GitHub, pemahaman seluruh kode dan video. Tetap sediakan waktu pengujian/repository/video sebelum **10 Desember 2026 pukul 23.59 WIB**.

## Penilaian ulang risiko strategis

| Risiko dari review | Tindak lanjut | Status |
| --- | --- | --- |
|48 FR P0 masih banyak bagi tim pemula | Validasi kapasitas nyata; prioritaskan vertical slice; pecah estimasi setelah spike; P1 off jika core belum stabil | OPEN — RV-14 |
| Graf/tree/transaksi belum tentu baru | Cocokkan silabus/lab dan diskusi Asdos; pilih konsep yang berguna dan dapat dijelaskan semua anggota | OPEN — RV-15 |
| Fixture sintetis tidak membuktikan manfaat nyata | Catatan kebutuhan sukarela; subset aturan resmi hanya jika sumber dan applicability sah | OPEN — RV-16 dan RV-02–04 |
| UI menyerap waktu engine/test | Pertahankan identitas Orbit, gunakan list accessible/tema terang; pixel-perfect bukan kriteria tugas yang disebut panduan | Dikendalikan dalam scope; belum diuji |

Errata tidak mengklaim bahwa “CONDITIONAL GO” adalah persetujuan dosen. Itu penilaian kesiapan dokumentasi dengan batas bukti yang disebutkan. Tidak ada hasil test aplikasi baru.

## Jejak perubahan

[Changelog](PRD-REVISION-CHANGELOG.md) mencatat ERR-01–06. [Diff v0.2→v0.2.1](PRD-v0.2-to-v0.2.1.patch) menunjukkan perubahan literal pada berkas baseline; manifest checksum dikecualikan dari diff untuk menghindari referensi berputar. Arsip v0.2 tetap sebagai snapshot sebelum errata. Paket ini berakar di `ORBIT_PRD_v0.2.1/`; nama folder historis dokumen tidak dipakai sebagai asumsi root ZIP.
