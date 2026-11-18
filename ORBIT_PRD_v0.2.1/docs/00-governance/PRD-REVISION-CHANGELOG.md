# ORBIT — PRD Revision Changelog

Versi **v0.1 Draft → v0.2 DDP1 Draft** · 18 November 2026 (Asia/Jakarta) · Owner: Product Lead bersama reviewer domain.

**Revisi terbaru: v0.2.1 errata.** Riwayat v0.1→v0.2 di bawah dipertahankan. Tambahan di akhir mencatat ERR-01–06 dari review independen; scope, semua FR/AC/test dan ID tetap.

## Dasar dan batas perubahan

Revisi menggunakan 13 PRD/governance aktual dan panduan resmi DDP1 versi 1 (SRC-11), bukan rekonstruksi. Requirement ID, judul dan 20 bagian per PRD dipertahankan. Tidak ada fitur dihapus; P2 berarti Future Development. Semua angka priority adalah keputusan kelayakan Orbit, bukan fitur wajib dosen. Sumber aturan tugas, rekomendasi dan asumsi dibedakan pada Compliance Matrix.

File [PRD-v0.1-to-v0.2.patch](PRD-v0.1-to-v0.2.patch) memberikan before/after literal semua perubahan pada berkas baseline, termasuk AC/test, stories, interface, sumber dan editorial. Tabel berikut memberi alasan per perubahan requirement. Manifest baru merangkum hash versi saat ini; checksum baseline tercatat pada audit/checkpoint. Dokumen baru disertakan langsung, bukan dimasukkan ke patch baseline.

## Ringkasan versi

| Jenis | v0.1 | v0.2 | Penjelasan |
| --- | --- | --- | --- |
| FR |141 |143 |141 ID lama utuh + AUTH-FR-014/015 baru |
| Prioritas FR |111 P0 /26 P1 /4 P2 |48 P0 /27 P1 /68 P2 |91 FR berubah prioritas; tidak ada penghapusan |
| FR dengan penyempurnaan kontrak |— |34 FR lama |Precondition/input/behavior/output; dapat tumpang tindih perubahan prioritas |
| BR / NFR |102 /39 |102 /39 |ID tetap, sejumlah wording diperjelas |
| AC / test primer |180 /180 |182 /182 |AC/test untuk dua FR baru; kontrak yang berubah disinkronkan |
| Integrasi |12 |14 |INT-T-013/014 ditambah; test future ditunda, tidak dihapus |

## Paket perubahan dan alasan

| Change ID | Perubahan | Dasar | Dampak / bukti |
| --- | --- | --- | --- |
| REV-01 | Catat panduan resmi, deadline/tim/teknologi/deliverables/rubrik; tutup RV-01 hanya untuk aturan | SRC-11 seluruh 5 halaman; AUD-01 | Semua sumber/risiko terkait diperbarui; kapasitas/konsep/masalah tetap RV-14/15/16 |
| REV-02 | Prioritas P0/P1/P2 berbasis estimasi 84–100 jam-orang, bukan scope seluruh produk | AUD-02 dan MVP Scope; deadline SRC-11 hlm. 1/5 | Tabel FR/stories/test/RTM/index diselaraskan; ID tidak dihapus |
| REV-03 | Core Dashboard langsung MAP/GRD; actual per course tanpa closeout | AUD-03/11; D-20 | CORE/GRD/UX/interfaces/glossary/INT-T-010/013 |
| REV-04 | Mode demo lokal sintetis, akun multiuser future; export/reset lokal | AUD-04/13; D-19; bentuk aplikasi bebas SRC-11 hlm. 2–3 | AUTH-FR-014/015 baru; PRO/UX context; INT-T-014; security mode akun tetap |
| REV-05 | Batasi satu skenario, stale/reset, lock struktur BRP; graf validasi dataset | AUD-05/06/16; D-21 | MAP/GRD AC/test; subkemampuan rebase/migration tetap P2 |
| REV-06 | Penjadwalan, Vault, GPA dan support opsional; community/career/closeout future | AUD-07–15; data/izin/effort | Semua perilaku/AC/test future dipertahankan; rights/security gate mengikuti kemampuan aktif |
| REV-07 | Pertahankan UI, batasi capability aktif; tren P1, dark P2 | AUD-12; D-17 | PRD-09 tidak mengganti identitas visual; empty/unknown dan aksesibilitas tetap |
| REV-08 | Tegaskan Python utama dan bukti repo/pemahaman/video; daftar keputusan terbuka | SRC-11 hlm. 2–5; D-18 | Lima laporan baru; jadwal/gate dan test tambahan |
| REV-09 | Selaraskan wording priority lama, source refs, gaya angka/spasi dan metadata versi | Audit konsistensi; bukan perubahan aturan akademik | Before/after literal di patch; judul/path/ID lama tetap |

## Perubahan setiap FR

Hanya FR yang prioritas atau kontraknya berubah ditampilkan. FR lainnya dipertahankan; seluruh disposisi 141 FR baseline ada pada PRD Audit Report. “Kontrak tetap” berarti hanya prioritas berubah. Seluruh AC/test primer dengan nomor yang sama mengikuti FR; tidak didaur ulang.

| Requirement | Sebelum→sesudah | Perubahan kontrak | Alasan / jejak |
| --- | --- | --- | --- |
| CORE-FR-001 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-01/02/03; SRC-11 hlm. 2–5; D-16/17/20 |
| CORE-FR-002 | P0→P0 | Output: **Proyeksi dan guidance memakai revision terbaru atau berlabel perlu diperbarui** → **Proyeksi GRD dan kelayakan MAP pada dashboard memakai revision terbaru atau berlabel perlu diperbarui; guidance hanya jika P2 aktif** | AUD-01/02/03; SRC-11 hlm. 2–5; D-16/17/20 |
| CORE-FR-005 | P0→P0 | Precondition: **SSO, SLCM, komunitas dan karier nonaktif** → **SSO, SLCM, SCH, SNR, VLT, CAR, GDE dan akun multiuser nonaktif**; Perilaku: **Izinkan lifecycle personal berjalan tanpa integrasi opsional** → **Izinkan alur inti dalam workspace demo lokal sintetis tanpa integrasi opsional**; Output: **Profil, grade, jadwal, simulasi dan closeout selesai** → **Profil, grade/target, satu simulasi roadmap, konfirmasi aktual per course dan dashboard selesai; tidak membutuhkan closeout** | AUD-01/02/03; SRC-11 hlm. 2–5; D-16/17/20 |
| CORE-FR-006 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-01/02/03; SRC-11 hlm. 2–5; D-16/17/20 |
| CORE-FR-007 | P0→P0 | Trigger: **Buka akun baru** → **Buka workspace baru** | AUD-01/02/03; SRC-11 hlm. 2–5; D-16/17/20 |
| PRO-FR-001 | P0→P0 | Precondition: **Akun aktif** → **Workspace lokal aktif; akun aktif hanya untuk mode multiuser P2** | AUD-04; D-19/21; kapasitas pada MVP Scope |
| PRO-FR-003 | P0→P0 | Trigger: **Masuk kembali** → **Buka kembali workspace lokal atau masuk akun P2**; Input: **user_id** → **owner_scope stabil** | AUD-04; D-19/21; kapasitas pada MVP Scope |
| PRO-FR-005 | P0→P0 | Precondition: **Pemilik akun** → **Pemilik workspace; fixture sintetis pada rilis DDP1** | AUD-04; D-19/21; kapasitas pada MVP Scope |
| PRO-FR-006 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04; D-19/21; kapasitas pada MVP Scope |
| PRO-FR-007 | P0→P1 | Precondition: **Pemilik akun** → **Pemilik workspace lokal atau akun P2**; Output: **Nama sapaan berubah; credit kontributor tetap sesuai consent** → **Nama sapaan/zona waktu lokal berubah; bila kredit kontributor P2 aktif, identitas publik tetap mengikuti consent terpisah** | AUD-04; D-19/21; kapasitas pada MVP Scope |
| PRO-FR-008 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04; D-19/21; kapasitas pada MVP Scope |
| PRO-FR-009 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04; D-19/21; kapasitas pada MVP Scope |
| MAP-FR-006 | P0→P0 | Perilaku: **Tandai stale dan tawarkan rebase dengan diff** → **Tandai stale dan tampilkan perubahan baseline; pada P0 tawarkan reset lalu pilih ulang, rebase yang mempertahankan pilihan merupakan P2**; Output: **Tidak memakai baseline lama sebagai hasil terkini** → **Revision r1 tidak tampil current setelah sumber r2; reset memuat r2, actual tidak berubah; mode P2 mempertahankan pilihan valid setelah review diff** | AUD-05/16; D-21; validasi prasyarat/ketidakpastian |
| MAP-FR-007 | P0→P0 | Trigger: **Publish graf** → **Validasi aktivasi dataset graf**; Precondition: **Curator** → **Kurator menyiapkan fixture/file konfigurasi; tidak perlu UI admin**; Output: **Versi tetap draft; cycle A/B terlihat** → **Dataset cycle tidak diaktifkan; cycle A/B terlihat; versi lama tetap aktif** | AUD-05/16; D-21; validasi prasyarat/ketidakpastian |
| MAP-FR-008 | P0→P0 | Trigger: **Beralih ke daftar** → **Buka roadmap dalam mode daftar**; Precondition: **Graf tampil** → **Katalog dan rule tersedia; tampilan graf opsional**; Output: **Seluruh prasyarat dapat dibaca melalui keyboard** → **Seluruh prasyarat dapat dibaca melalui keyboard tanpa memerlukan renderer graf interaktif** | AUD-05/16; D-21; validasi prasyarat/ketidakpastian |
| MAP-FR-010 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-05/16; D-21; validasi prasyarat/ketidakpastian |
| MAP-FR-012 | P0→P0 | Trigger: **Publish katalog referensi rusak** → **Validasi aktivasi katalog referensi rusak**; Precondition: **Curator** → **Kurator menyiapkan fixture/file konfigurasi; tidak perlu UI admin**; Output: **Draft tetap; daftar missing/mismatch course terlihat** → **Dataset ditolak dan tidak mengganti versi aktif; daftar missing/mismatch course terlihat** | AUD-05/16; D-21; validasi prasyarat/ketidakpastian |
| GRD-FR-001 | P0→P0 | Perilaku: **Buat BRPVersion scoped; perubahan struktur sesudah skor ada memerlukan preview migrasi** → **Buat BRPVersion scoped; P0 mengunci struktur setelah skor tersimpan dan menolak perubahan struktur tanpa menulis apa pun; preview migrasi tersimpan sebagai GRD-FR-020 P2**; Output: **Versi lama tetap bisa direproduksi; nilai tidak dipindah antar leaf tanpa mapping** → **BRP valid tersimpan; upaya mengganti struktur bernilai pada P0 ditolak, versi/skor lama tetap; P2 memakai mapping eksplisit** | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| GRD-FR-008 | P0→P1 | Input: **A: 4 SKS, g=3,7; B: 3 SKS, g=3; C: 2 SKS, g=2** → **A: 4 SKS, g=3,7; B: 3 SKS, g=3; C: 2 SKS, g=2** | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| GRD-FR-009 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| GRD-FR-010 | P0→P0 | Precondition: **Preview closeout dan policy terlihat** → **Preview hasil aktual per course dan policy/provenance terlihat; GDE dinonaktifkan pada P0**; Input: **Huruf/hasil aktual yang dilaporkan serta source** → **Hasil aktual yang dimasukkan eksplisit, source, revision dan alasan bila koreksi**; Perilaku: **Simpan ActualFinalGrade terpisah dari Prediction dan emit revisi aktual** → **Konfirmasi atau koreksi ActualFinalGrade per course, simpan revisi dan invalidasi MAP/dashboard; tolak preview stale; jangan menyalin Prediction otomatis**; Output: **Roadmap menerima actual_user_reported; consent komunitas tetap off** → **A yang dikonfirmasi lulus memperbarui MAP sebagai actual_user_reported; B unresolved tetap unknown; koreksi menyimpan revisi lama; nol contribution dan tidak memerlukan closeout** | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| GRD-FR-013 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| GRD-FR-015 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| GRD-FR-017 | P0→P2 | Precondition: **Fixture A lama 4×2; A baru 4×3,7; B3×3** → **Fixture A lama 4×2; A baru 4×3,7; B3×3** | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| GRD-FR-019 | P0→P1 | Input: **History 30 SKS/96 points; term 10 SKS/35 points** → **History 30 SKS/96 points; term 10 SKS/35 points**; Output: **131/40=3,275; display 3,28; label proyeksi bila term masih prediksi** → **131/40=3,275; display 3,28; label proyeksi bila term masih prediksi** | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| GRD-FR-020 | P0→P2 | Input: **Template v2 menghapus Q1 dan menambah Lab 1** → **Template v2 menghapus Q1 dan menambah Lab 1**; Output: **Lab 1 tetap unknown; Q1 lama tidak hilang dan tidak pindah otomatis** → **Lab 1 tetap unknown; Q1 lama tidak hilang dan tidak pindah otomatis** | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| SCH-FR-001 | P0→P1 | Input: **assessment_id, due_at** → **assessment_id, due_at** | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-002 | P0→P1 | Input: **start/end dan rentang recurrence** → **start/end dan timezone; recurrence hanya P2**; Perilaku: **Validasi end>start dan tampilkan zona waktu** → **Validasi end>start dan tampilkan zona waktu; P1 memasukkan pertemuan satu per satu; editor recurrence dipertahankan sebagai P2** | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-003 | P0→P1 | Perilaku: **Gunakan interval half-open [start, end)** → **Gunakan interval half-open [start, end)** | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-004 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-005 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-006 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-007 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-008 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-009 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-010 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-011 | P0→P2 | Precondition: **Tugas remaining 6 jam** → **Tugas remaining 6 jam**; Input: **Blok 4+3 jam, estimasi−1, kapasitas−2** → **Blok 4+3 jam, estimasi−1, kapasitas−2** | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SCH-FR-012 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| SNR-FR-001 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| SNR-FR-002 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| SNR-FR-003 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| SNR-FR-004 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| SNR-FR-005 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| SNR-FR-006 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| SNR-FR-007 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| SNR-FR-008 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| SNR-FR-009 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| VLT-FR-001 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-002 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-003 | P0→P1 | Precondition: **Moderator melakukan pemeriksaan manual** → **Kurator memeriksa manual dan memperbarui metadata; UI moderator P2** | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-004 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-005 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-006 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-007 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-008 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-009 | P0→P1 | Precondition: **Moderator meninjau** → **Kurator memeriksa dataset sebelum aktivasi; moderator melalui UI pada P2**; Perilaku: **Tahan/hide resource dan catat alasan** → **Tolak aktivasi item dengan hak tidak jelas atau ujian tertutup; hide item jika bukti hak dicabut; workflow moderasi akun disimpan untuk P2** | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-010 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-FR-011 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| CAR-FR-001 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-10; D-17; RV-09 belum tersedia |
| CAR-FR-002 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-10; D-17; RV-09 belum tersedia |
| CAR-FR-003 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-10; D-17; RV-09 belum tersedia |
| CAR-FR-004 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-10; D-17; RV-09 belum tersedia |
| CAR-FR-005 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-10; D-17; RV-09 belum tersedia |
| CAR-FR-006 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-10; D-17; RV-09 belum tersedia |
| CAR-FR-007 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-10; D-17; RV-09 belum tersedia |
| CAR-FR-008 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-10; D-17; RV-09 belum tersedia |
| GDE-FR-001 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| GDE-FR-002 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| GDE-FR-003 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| GDE-FR-004 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| GDE-FR-005 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| GDE-FR-006 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| GDE-FR-007 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| GDE-FR-008 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| GDE-FR-009 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| GDE-FR-010 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-03/11; D-17/20; dependency dan transaksi future |
| UX-FR-001 | P0→P0 | Precondition: **Akun dan term aktif** → **Workspace dan term aktif; akun hanya untuk mode multiuser P2** | AUD-12; D-17/20; capability rilis, identitas visual tetap |
| UX-FR-002 | P0→P0 | Input: **Actual/prediction/target/simulation summaries** → **Summary GRD (K, bounds, target) dan MAP (eligibility, rencana, peringatan SKS)**; Perilaku: **Tampilkan tipe/provenance setiap angka dan jangan isi demo di workspace real** → **Baca hasil Python GRD/MAP langsung dengan revision dan provenance; tampilkan tautan ke input/peringatan asal; jangan mensyaratkan GDE, SCH atau GPA P1**; Output: **Unknown menjadi belum tersedia, bukan angka ilustrasi** → **Dashboard konsisten dengan hasil GRD/MAP; unknown berlabel; seluruh P1/P2 off tetap dapat dibuka; tidak ada angka atau tren fiktif** | AUD-12; D-17/20; capability rilis, identitas visual tetap |
| UX-FR-009 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-12; D-17/20; capability rilis, identitas visual tetap |
| UX-FR-010 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-12; D-17/20; capability rilis, identitas visual tetap |
| AUTH-FR-001 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-002 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-003 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-004 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-005 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-006 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-007 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-010 | P0→P0 | Perilaku: **Tampilkan status belum tersedia dan alternatif akun/input lokal** → **Tampilkan status belum tersedia dan alternatif input manual di workspace lokal; akun Orbit hanya jika mode P2 diaktifkan** | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-011 | P0→P2 | Input: **user_id, role, alasan** → **user_id, role, alasan** | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-012 | P0→P2 | Precondition: **Akun/source mencapai 5 kegagalan dalam 15 menit** → **Akun/source mencapai 5 kegagalan dalam 15 menit** | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-013 | P0→P2 | Precondition: **Sesi usia 13 jam, atau idle 31 menit pada fixture default** → **Sesi usia 13 jam, atau idle 31 menit pada fixture default** | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-014 | baru→P0 | Gunakan satu owner_scope lokal stabil, bind loopback, nonaktifkan debug pada demo, akun publik dan semua adapter kampus; nyatakan batas data sintetis pada UI/README; Aplikasi dapat berjalan di localhost tanpa login; konfigurasi akses jaringan publik ditolak pada mode ini; tidak ada data nyata/kredensial pada fixture atau repository; ditambah AUTH-AC-014 dan AUTH-T-014 | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| AUTH-FR-015 | baru→P0 | Ekspor JSON lokal tanpa secrets; reset hanya setelah preview/konfirmasi; simpan data di luar berkas seed dan tandai database/export runtime tidak dilacak Git; Restart mempertahankan input dan owner_scope; cancel reset tidak mengubah data; confirm mengosongkan data lokal, seed tetap; ekspor memuat versi dan provenance tanpa secrets; ditambah AUTH-AC-015 dan AUTH-T-015 | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| PUB-FR-001 | P0→P1 | Perilaku: **Tampilkan manfaat yang didukung dan CTA register** → **Tampilkan manfaat yang didukung dan CTA sesuai mode aktif: buka demo lokal atau registrasi ketika layanan akun tersedia**; Output: **Fitur P2 tidak diklaim sudah terhubung** → **Fitur P2 tidak diklaim terhubung; pada DDP1 CTA membuka demo lokal, registrasi hanya bila AUTH P2 aktif** | AUD-14; D-17/19; label demo/independen dan capability |
| PUB-FR-002 | P0→P0 | Precondition: **Halaman publik** → **Shell demo atau halaman publik**; Output: **Status terlihat sebelum registrasi** → **Status independen terlihat pada shell sebelum pengguna memasukkan data; bila registrasi P2 ada, terlihat sebelum registrasi** | AUD-14; D-17/19; label demo/independen dan capability |
| PUB-FR-004 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-14; D-17/19; label demo/independen dan capability |
| PUB-FR-005 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-14; D-17/19; label demo/independen dan capability |
| PUB-FR-006 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-14; D-17/19; label demo/independen dan capability |
| PUB-FR-007 | P1→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-14; D-17/19; label demo/independen dan capability |
| PUB-FR-008 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-14; D-17/19; label demo/independen dan capability |
| SUP-FR-001 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-FR-002 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-FR-003 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-FR-004 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-FR-005 | P0→P2 | Input: **category, description, steps optional; operation_id** → **category, description, steps optional; operation_id** | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-FR-006 | P0→P1 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-FR-007 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-FR-008 | P0→P1 | Input: **version, date, changes, known limits** → **version, date, changes, known limits** | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-FR-010 | P2→P2 | Output: **Laporan tidak disebut transkrip resmi; privacy export P0 tetap tersedia** → **Laporan tidak disebut transkrip resmi; ekspor lokal AUTH-FR-015 P0 tetap tersedia, ekspor akun AUTH-FR-005 mengikuti mode multiuser P2** | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-FR-011 | P0→P2 | Kontrak tetap; AC/test tetap disimpan dengan prioritas baru. | AUD-15; D-17/19; search opsional, layanan lanjutan future |

## Business rules dan NFR yang berubah

| Requirement | Sebelum | Sesudah | Alasan |
| --- | --- | --- | --- |
| CORE-BR-004 | P0 adalah baseline rekomendasi. Jika rubrik memangkas fitur, keputusan dicatat sebagai perubahan scope dan test yang terdampak, bukan klaim fitur selesai. | P0 adalah rekomendasi rilis DDP1 hasil analisis kapasitas pada MVP-SCOPE-AND-PRIORITIES; bukan fitur wajib dosen. Perubahan kapasitas dicatat bersama dampak scope/test, bukan klaim fitur selesai. | AUD-01/02/03; SRC-11 hlm. 2–5; D-16/17/20 |
| CORE-BR-005 | Skenario tidak menulis event ActualFinalGradeChanged; hanya aksi finalisasi eksplisit yang dapat memengaruhi riwayat aktual. | Skenario tidak menulis ActualFinalGradeChanged. Hanya konfirmasi aktual eksplisit per course (GRD-FR-010, P0) atau closeout semester (GDE-FR-006, P2) dapat memengaruhi riwayat aktual. | AUD-01/02/03; SRC-11 hlm. 2–5; D-16/17/20 |
| MAP-BR-005 | Earliest term dihitung topological untuk graf didukung: lebih besar dari term prasyarat; availability unknown menghasilkan earliest bersyarat, bukan tanggal pasti. Corequisite/izin khusus unsupported → unknown. | Earliest term dihitung topological pada graf yang didukung: AND menunggu semua prasyarat, sementara OR memakai jalur alternatif yang dipilih eksplisit pada skenario dan dilabeli asumsi. P0 tidak mengoptimalkan semua kombinasi OR. Bila jalur OR belum dipilih, availability belum diketahui atau ada corequisite/izin khusus unsupported, hasil waktu tetap unknown/bersyarat. Fixture setiap-term memberi term anak lebih besar dari term prasyarat terpilih. | AUD-05/16; D-21; validasi prasyarat/ketidakpastian |
| MAP-BR-007 | Reset menghapus overlay skenario saja. Rebase mempertahankan pilihan yang masih valid dan meminta tinjau konflik. | Reset menghapus overlay skenario saja dan membaca baseline terbaru. P0 memakai stale → review perubahan → reset/pilih ulang. Rebase yang mempertahankan pilihan valid dan meminta tinjau konflik disimpan sebagai kemampuan P2 pada MAP-FR-006; tidak dihapus. | AUD-05/16; D-21; validasi prasyarat/ketidakpastian |
| GRD-BR-010 | Actual final berbeda dari skor input komponen dan proyeksi. Semua input manual ber-provenance user_reported. Koreksi final memerlukan reopen closeout dan alasan; tidak perlu data identitas tambahan. | Actual final berbeda dari skor komponen dan proyeksi. Input manual ber-provenance user_reported; fixture demo tetap berlabel sintetis. P0 memakai preview/konfirmasi atau koreksi per course, source revision dan alasan koreksi; histori lama tersimpan. P2 yang sudah dalam snapshot closeout memakai reopen sebelum koreksi. | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| SNR-BR-005 | P1 hanya fixed non-overlapping cells tanpa filter cohort kecil, selisih total/subtotal, nilai min/max, ranking, atau time-series delta. Jika pembaca dapat menyimpulkan cell kecil lewat selisih, suppress pasangan/complement. | P2 hanya fixed non-overlapping cells tanpa filter cohort kecil, selisih total/subtotal, nilai min/max, ranking, atau time-series delta. Jika pembaca dapat menyimpulkan cell kecil lewat selisih, suppress pasangan/complement. | AUD-08; D-17; RV-07/data/consent belum tersedia |
| VLT-BR-002 | P0 kurasi oleh moderator; kontribusi mandiri P1 memakai pending → approved/published atau rejected. Hak terduga bermasalah segera hidden sampai review. | P1 kurasi metadata oleh tim melalui dataset tervalidasi; tidak memerlukan akun moderator atau antrean submit. Kontribusi mandiri dan UI moderasi P2 memakai pending → approved/published atau rejected. Hak meragukan memblokir item; pencabutan hak segera hidden. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| VLT-BR-003 | Allowlist HTTPS drive.google.com/docs.google.com pada input; tolak kredensial dalam URL, javascript/data/internal IP dan hostname tiruan. Tidak mengikuti redirect atau mengambil isi secara otomatis pada P0. | Allowlist HTTPS drive.google.com/docs.google.com pada input; tolak kredensial dalam URL, javascript/data/internal IP dan hostname tiruan. Tidak mengikuti redirect atau mengambil isi secara otomatis pada P1. | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| CAR-BR-003 | Ranking P1: jumlah kompetensi minat yang didukung, lalu eligibility met sebelum unknown/unmet, lalu kode course untuk tie. Tampilkan faktor tersebut, bukan skor kepribadian. | Ranking P2: jumlah kompetensi minat yang didukung, lalu eligibility met sebelum unknown/unmet, lalu kode course untuk tie. Tampilkan faktor tersebut, bukan skor kepribadian. | AUD-10; D-17; RV-09 belum tersedia |
| AUTH-BR-002 | Usulan P0 tanpa MFA: password minimal 15 karakter, maksimum yang didukung sekurangnya 64; izinkan paste/password manager. Jangan mewajibkan pergantian berkala tanpa alasan risiko. Hash/token tidak dicatat di log. | Usulan mode akun P2 tanpa MFA: password minimal 15 karakter, maksimum yang didukung sekurangnya 64; izinkan paste/password manager. Jangan mewajibkan pergantian berkala tanpa alasan risiko. Hash/token tidak dicatat di log. | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| SUP-BR-006 | Feedback P0 plain text, kategori bug/content/accessibility/idea, description 10–2.000 karakter; steps optional. Attachment tidak tersedia P0. Guest diberi receipt secret berentropi untuk mengecek laporan sendiri bila status view diaktifkan. | Feedback P2 plain text, kategori bug/content/accessibility/idea, description 10–2.000 karakter; steps optional. Attachment tidak termasuk scope feedback awal. Guest diberi receipt secret berentropi untuk mengecek laporan sendiri bila status view diaktifkan. | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| SUP-BR-008 | Preferensi punya owner tunggal PRO/UX; help/changelog PUB/SUP editorial. Privacy export AUTH P0 tidak ditunda oleh laporan akademik rapi P2. | Preferensi punya owner tunggal PRO/UX; help/changelog PUB/SUP editorial. Ekspor workspace lokal AUTH-FR-015 P0 tidak ditunda oleh laporan akademik rapi P2; ekspor akun AUTH-FR-005 berlaku dalam mode multiuser P2. | AUD-15; D-17/19; search opsional, layanan lanjutan future |
| AUTH-NFR-003 | Mutasi sesi/akun memerlukan proteksi terhadap pemalsuan request dan secret tidak bocor di logs. | Mutasi workspace lokal, sesi atau akun memerlukan validasi request terhadap pemalsuan; secret dan nilai mentah tidak bocor di log. | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |

Perubahan editorial yang tidak mengubah makna, misalnya label prioritas pada kalimat atau spasi angka, tetap terlihat di patch. BR mengikuti FR aktif. NFR tetap menjadi gate kemampuan aktif; AUTH-NFR-001/002 dan SCH-NFR-003 menunggu fitur akun/alokasi P2. AUTH-NFR-003 diperluas eksplisit ke mutasi lokal.

## Acceptance, test dan kontrak integrasi

AC/test lama yang kontrak FR-nya berubah diperbarui dengan ID yang sama; kolom prioritas test disamakan dengan FR. US dengan campuran prioritas kini menampilkan “per FR”, bukan menganggap seluruh story wajib P0. Kontrak lengkap future tetap didokumentasikan tetapi tidak memblokir core. INT-T-002 menjadi P1 deadline tanpa GDE;005 P1 GPA tanpa GDE;004/006–009/011/012 P2;010 P0 demo seluruh opsional off. INT-T-001/003 dipertahankan P0. INT-T-013 menguji aktual per course/stale revision;014 menguji persistensi/export/reset lokal. Semua masih SPECIFIED—NOT EXECUTED.

Test tambahan DDP-T-01–13 pada readiness adalah rencana menutup cabang semantik, tidak dihitung sebagai test primer atau hasil aplikasi. DDP-01–15 pada compliance adalah kriteria bukti tugas, bukan requirement fitur baru.

## Dampak per berkas baseline

Semua 13 PRD terdampak scope/dependency; perubahan terbatas pada bagian yang disebut. Bagian visi/data/algoritma yang tidak perlu diubah dipertahankan. Angka bagian merujuk heading asli; perbedaan literal tersedia pada patch.

| Berkas | Bagian berubah | Alasan utama |
| --- | --- | --- |
| [PRD-00-master-product-overview.md](../prd/PRD-00-master-product-overview.md) | 1, 3, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20 | AUD-01/02/03; SRC-11 hlm. 2–5; D-16/17/20 |
| [PRD-01-academic-profile-and-onboarding.md](../prd/PRD-01-academic-profile-and-onboarding.md) | 1, 3, 5, 6, 7, 8, 13, 15, 16, 17, 18, 19, 20 | AUD-04; D-19/21; kapasitas pada MVP Scope |
| [PRD-02-roadmap-and-semester-simulator.md](../prd/PRD-02-roadmap-and-semester-simulator.md) | 1, 5, 6, 8, 9, 13, 15, 16, 17, 19, 20 | AUD-05/16; D-21; validasi prasyarat/ketidakpastian |
| [PRD-03-grade-rescue-and-gpa-engine.md](../prd/PRD-03-grade-rescue-and-gpa-engine.md) | 1, 5, 6, 7, 8, 9, 13, 15, 16, 17, 19, 20 | AUD-03/06/16; D-17/20/21; model linear dan dependensi core |
| [PRD-04-schedule-and-stress-radar.md](../prd/PRD-04-schedule-and-stress-radar.md) | 1, 5, 6, 7, 8, 11, 13, 15, 16, 17, 18, 19, 20 | AUD-07; D-17; analisis effort dan deadline SRC-11 hlm. 1/5 |
| [PRD-05-senior-playbook-and-insights.md](../prd/PRD-05-senior-playbook-and-insights.md) | 1, 5, 6, 7, 8, 9, 13, 14, 15, 17, 18, 19, 20 | AUD-08; D-17; RV-07/data/consent belum tersedia |
| [PRD-06-knowledge-vault-and-contributors.md](../prd/PRD-06-knowledge-vault-and-contributors.md) | 1, 4, 5, 6, 7, 8, 9, 13, 15, 16, 17, 18, 19, 20 | AUD-09; D-17; RV-08 dan scope kurasi minimum |
| [PRD-07-career-to-course-navigator.md](../prd/PRD-07-career-to-course-navigator.md) | 1, 5, 6, 7, 8, 9, 13, 15, 17, 18, 19, 20 | AUD-10; D-17; RV-09 belum tersedia |
| [PRD-08-guidance-engine-and-semester-closeout.md](../prd/PRD-08-guidance-engine-and-semester-closeout.md) | 1, 5, 6, 7, 8, 13, 14, 15, 17, 19, 20 | AUD-03/11; D-17/20; dependency dan transaksi future |
| [PRD-09-design-system-navigation-and-ux.md](../prd/PRD-09-design-system-navigation-and-ux.md) | 1, 3, 5, 6, 7, 8, 11, 13, 15, 16, 17, 18, 19, 20 | AUD-12; D-17/20; capability rilis, identitas visual tetap |
| [PRD-10-authentication-privacy-and-integrations.md](../prd/PRD-10-authentication-privacy-and-integrations.md) | 1, 2, 5, 6, 7, 8, 9, 13, 15, 16, 17, 18, 19, 20 | AUD-04/13/16; D-19; demo sintetis dan izin integrasi |
| [PRD-11-public-pages-faq-and-team.md](../prd/PRD-11-public-pages-faq-and-team.md) | 1, 5, 6, 7, 8, 13, 15, 16, 17, 19, 20 | AUD-14; D-17/19; label demo/independen dan capability |
| [PRD-12-search-feedback-and-supporting-features.md](../prd/PRD-12-search-feedback-and-supporting-features.md) | 1, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20 | AUD-15; D-17/19; search opsional, layanan lanjutan future |

| Governance / dukungan | Perubahan | Alasan |
| --- | --- | --- |
| PRODUCT-DOC-INDEX.md | Hitungan, dependency diagram, minimum slice, review gate dan tautan laporan | Scope rilis berbeda, sumber resmi tersedia |
| GLOSSARY-AND-DECISION-LOG.md | Local owner_scope, pemicu actual dan D-16–21; D-01–15 tetap sebagai riwayat | Menjaga canon/jejak keputusan |
| REQUIREMENTS-TRACEABILITY-MATRIX.md | Semua prioritas/perilaku terkait; dua FR baru dan 14 integrasi; status deferred | Konsistensi sumber PRD→AC/test |
| RESEARCH-AND-VALIDATION-REGISTER.md | SRC-11–15, RV-01 closed, RV-14–16 baru; prioritas gap disesuaikan | Pisahkan aturan diketahui dari bukti yang belum ada |
| QA-DOCUMENTATION-REPORT.md | Lampiran audit v0.2; hasil historis v0.1 tetap | Jangan mengubah pemeriksaan dokumen menjadi klaim test aplikasi |
| README.md / MANIFEST.json | Navigasi/versi/hitungan/checksum terbaru | Paket dapat dibaca dan diverifikasi |

## Dokumen baru dan ketidakpastian tersisa

Lima laporan yang diminta dibuat terpisah: audit, compliance matrix, MVP scope, changelog ini, dan implementation readiness. Diff tambahan memberikan jejak literal revisi. Tidak ada kode aplikasi yang ditambahkan, tidak ada Figma diubah, integrasi/izin tidak diklaim tersedia, dan tidak ada nilai penilaian dijanjikan. Keputusan scope/stack adalah rekomendasi berdasarkan kelayakan; kapasitas aktual tim dan kebaruan terhadap materi kelas perlu diverifikasi sebelum komitmen delivery.

## v0.2 → v0.2.1 — 18 November 2026

Sumber: SRC-16 review independen; diperiksa terhadap baseline v0.2 aktual. Tidak ada prioritas FR yang berubah. Empat BR, penjelasan archive root dan pelabelan journey dikoreksi. Hasil validasi baru terpisah dari hasil historis v0.2.

| Change ID | Perubahan | Alasan / dampak |
| --- | --- | --- |
| ERR-01 | UX-BR-001: P1 dark → P2 dark, capability explicit | Selaras UX-FR-010 dan scope future; RTM diperbarui |
| ERR-02 | UX-BR-002: Minat & Jalur bila P1 → menu mengikuti capability, CAR P2 | Menghilangkan dependency tersirat dan navigasi fitur nonaktif; RTM diperbarui |
| ERR-03 | PUB-BR-006: contact P0 → feedback/contact P2 | Selaras PUB-FR-008/SUP-FR-005; bukan dependency core; RTM diperbarui |
| ERR-04 | SUP-BR-001: corpus P0 → saat search P1 aktif | Selaras SUP-FR-001; batas data tidak berubah; RTM diperbarui |
| ERR-05 | README membedakan folder historis, root ZIP v0.2 dan root v0.2.1; manifest archive_root | Menghindari asumsi path keliru; arsip lama tetap |
| ERR-06 | Journey PRD-00/09 diberi label; J1 lokal tanpa login; login/closeout/komunitas future; batas handoff eksplisit | P0 tidak meluas dari cerita produk lengkap; scope/readiness/index diperjelas |

PRD terdampak hanya 00/09/11/12, dengan metadata versi v0.2.1; sembilan PRD lain byte-identik dengan v0.2. Changelog ini, RTM, glossary D-22, research SRC-16, scope/readiness/index/audit/QA, README dan manifest diselaraskan. Compliance Matrix dan diff historis v0.1→v0.2 dipertahankan. Lampiran review pengguna tidak diubah.

Before/after empat BR dan penutupan enam temuan ada di [PRD-v0.2.1-ERRATA.md](PRD-v0.2.1-ERRATA.md). [Patch v0.2→v0.2.1](PRD-v0.2-to-v0.2.1.patch) merekam setiap perubahan literal pada berkas baseline selain manifest. Masalah kapasitas RV-14, kebaruan RV-15 dan kesiapan runtime tetap belum ditutup; tidak ada coding atau test aplikasi dalam errata ini.
