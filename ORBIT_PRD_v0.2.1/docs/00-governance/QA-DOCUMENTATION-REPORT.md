# ORBIT — Documentation QA Report

> Dokumen ini mempertahankan audit historis v0.1. Status versi sekarang ada di lampiran v0.2 di akhir; ketidaktersediaan panduan pada bagian historis telah ditutup oleh SRC-11.

Versi **v0.1 Draft** · Tanggal **18 November 2026 (Asia/Jakarta)** · Owner **QA Lead**.

**QA terbaru: errata v0.2.1.** Bagian audit v0.1/v0.2 tetap historis. Koreksi semantik dan pemeriksaan paket terbaru dicatat pada lampiran v0.2.1 di akhir; tidak ada test aplikasi dijalankan.

## Kesimpulan dan batas

Paket dokumentasi lengkap terhadap struktur wajib: **13 PRD dan 4 dokumen governance**. Setiap PRD memuat 20 bagian, functional requirements, business rules, model konseptual, UI/states, dependensi, privasi, NFR, acceptance dan test matrix. Audit ini menilai dokumentasi dan fixture perhitungan. **Tidak ada aplikasi, database, integrasi atau deployment yang dibuat atau diuji.** Review manusia tetap diperlukan sebelum menetapkan baseline implementasi.

## Hasil audit

| Pemeriksaan | Hasil | Bukti / batas |
| --- | --- | --- |
| File utama | 13 PRD +4 governance | Nama dan struktur direktori sesuai kontrak |
| Struktur | 20 bagian ×13 PRD | Heading bernomor diperiksa secara programatis |
| Functional requirements | 141 FR: P0=111, P1=26, P2=4 | Semua mempunyai AC/test primer; prioritas usulan |
| Business / nonfunctional rules | 102 BR +39 NFR | RTM memetakan rules ke acceptance/test |
| Acceptance dan test primer | 180 AC +180 test | SPECIFIED — NOT EXECUTED pada aplikasi |
| Cross-module scenarios | 12 skenario INT-T | Spesifikasi tambahan, belum diuji implementasi |
| Referensi ID | 642 definisi unik | Tidak ada definisi ganda atau referensi tidak ditemukan pada ID yang diperiksa |
| Tautan internal dan tabel | Lulus pemeriksaan | Path internal ada; jumlah kolom tabel konsisten |
| Fixture numerik / batas | 34 pemeriksaan independen lulus | Menguji hasil referensi di dokumen, bukan kode aplikasi |
| Source confidence | Register tersedia | Official/secondary/assumption/unknown dipisahkan; applicability tetap open |
| Desain Figma | 2 frame diamati | Screenshot dibaca; tidak menguji klik, kontras, mobile atau prototype |
| Keamanan / privasi | Kontrak dan test dirancang | Owner isolation, consent, suppression, retention dan deletion belum diuji dalam software |

## Hasil perhitungan referensi yang dijalankan

Pemeriksaan memakai aritmetika desimal dan kondisi referensi independen untuk fixture sintetis. Angka berikut tidak berasal dari data mahasiswa. Penerapan aturan akademik aktual tetap memerlukan RV-02/03/04.

| Check | Hasil | Expected | Status |
| --- | --- | --- | --- |
| K | 36.0 | 36 | PASS |
| observed average | 72 | 72 | PASS |
| upper bound | 86.0 | 86 | PASS |
| required T75 | 78 | 78 | PASS |
| required T90 | 108 | 108 | PASS |
| scenario UAS 90 | 81.0 | 81 | PASS |
| weights | 1.0 | 1 | PASS |
| IPS | 3.09 | 3.09 | PASS |
| cumulative | 3.28 | 3.28 | PASS |
| repeat latest | 3.40 | 3.40 | PASS |
| repeat all | 2.89 | 2.89 | PASS |
| ceil integer target | 79 | 79 | PASS |
| load | 1.25 | 1.25 | PASS |
| allocation conservation | 10 | 10 | PASS |
| post allocation ratio | 1 | 1 | PASS |
| senior mean | 70 | 70 | PASS |
| sensitivity 70 | 71.0 | 71 | PASS |
| sensitivity 80 | 76.0 | 76 | PASS |
| sensitivity 90 | 81.0 | 81 | PASS |
| all unknown lower bound | 0 | 0 | PASS |
| all unknown upper bound | 100 | 100 | PASS |
| observed unavailable when O0 | None | None | PASS |
| GPA unavailable when denominator 0 | None | None | PASS |
| conversion 84.995 | B | B | PASS |
| display 84.995 | 85.00 | 85.00 | PASS |
| conversion 85 | A | A | PASS |
| invalid weights 150 -50 | False | False | PASS |
| valid group exact 10000bp | True | True | PASS |
| invalid group 9999bp | False | False | PASS |
| back-to-back overlap | False | False | PASS |
| overlap duration | 0.5 | 0.5 | PASS |
| over allocation | False | False | PASS |
| k9 suppressed | False | False | PASS |
| k10 candidate | True | True | PASS |

## Review substantif dan perbaikan draft

1. Scope personal tidak membutuhkan SSO, SLCM, dataset kating atau ML. Community analytics dan career navigator adalah P1, integrasi P2; gate kualitas untuk P1 hanya berlaku saat diaktifkan.
2. Offering personal memungkinkan input BRP ketika kurikulum belum pasti. Profile migration tidak mengubah historical credits/final grades. Scope source yang unknown menahan klaim eligibility resmi.
3. Bobot diperiksa per sibling group dan per nilai: sum 100 saja tidak cukup karena 150/−50 juga sum 100. Input nonfinite, max_score0, target di luar rentang dan over-allocation ditolak.
4. Observed average, contribution points, bounds, prediction dan actual final dipisahkan. Full precision dipakai untuk threshold sebelum format; 84, 995 dapat tampil 85,00 tetapi tidak melampaui threshold 85 pada fixture.
5. Deadline dimiliki Assessment (GRD), dengan SCH sebagai editor terdelegasi. Allocation memindahkan jam antarminggu tanpa menggandakan total. Kapasitas unknown/zero dan date-only tidak dipaksakan menjadi angka/waktu tertentu.
6. Closeout tidak menyalin prediction menjadi actual otomatis. Revision check, idempotency dan unresolved status dirancang agar retry/concurrent edit tidak membuat riwayat salah.
7. Nilai pribadi tidak disumbangkan otomatis. Fixed-cell threshold k=10 hanya usulan minimum; suppression, anti-differencing, review dan withdrawal masih dibutuhkan. Jika belum feasible, analytics tetap off.
8. Metadata Vault, search, bookmark dan guidance mengikuti unpublish/consent revocation. P0 tidak fetch atau host file Drive; malicious URL ditolak sebelum akses.
9. Privacy export P0 dipisahkan dari laporan akademik berformat P2. Tim pengembang dan kontributor komunitas tetap berbeda; tidak ada nama anggota, kontak, testimoni atau statistik yang dikarang.
10. Perbedaan tema Figma diselesaikan dengan satu tema terang P0; dark P1. Label data ilustratif dipertahankan pada demo, tidak disalin ke workspace nyata.

## Keterbatasan audit

- Belum ada uji pengguna, pengukuran latency, screen reader, contrast, keamanan aplikasi, restore backup atau integrasi eksternal; semua tetap test plan.
- Pencocokan ID dan path memastikan referensi tersedia, bukan membuktikan semua kebutuhan semantik telah tercakup sempurna. QA implementasi perlu menambah fixture untuk kombinasi rule non-linear atau policy baru.
- Tidak seluruh kurikulum/prasyarat UI diverifikasi. Dokumen resmi yang dibaca tidak otomatis membuktikan applicability untuk angkatan dan kelas pengguna.
- Gate retensi, keamanan dan agregasi adalah proposal operasional, bukan sertifikasi compliance, anonimitas atau keamanan produksi.
- Rubrik TA, tim, deadline dan batas teknologi belum diberikan. Paket siap untuk review produk; kesiapan arsitektur/development masih bergantung pada keputusan tersebut.

## Handoff

Review PRD-00 dan D-03 untuk scope; glossary untuk data; PRD-02/03 untuk akademik/perhitungan; PRD-10 untuk privasi/integrasi; PRD-09 untuk UX; RTM untuk acceptance. Tutup RV-01 sebelum memilih stack. Selesaikan RV-02/03/04/10 sebelum memakai data nyata dengan klaim aturan akademik. Gate P1/P2 mengikuti modul yang dipilih, bukan menunda MVP manual.

## Lampiran QA revisi v0.2 — 18 November 2026

Audit baru memeriksa dokumen hasil revisi, bukan aplikasi. Panduan resmi seluruh 5 halaman dibaca melalui teks dan visual; baseline 19 checksum cocok sebelum edit. Hasil historis 34 reference checks di atas tetap milik v0.1, tidak digabung sebagai test aplikasi atau dianggap pengujian baru.

| Pemeriksaan v0.2 | Hasil |
| --- | --- |
| 13 judul/nama PRD dan 20 bagian asli | Dipertahankan |
| ID baseline FR/BR/NFR/AC/T/US | Semua dipertahankan, tidak ada duplikat definisi dalam PRD |
| FR/BR/NFR sekarang |143 /102 /39 |
| AC/test primer sekarang |182 /182, referensi FR dan prioritas test cocok |
| RTM |284 row requirement cocok sumber;14 integrasi terdaftar |
| Prioritas FR |48 P0 / 27 P1 / 68 P2;91 FR lama berubah prioritas |
| Tautan relatif dokumen aktif |440 diperiksa, tidak ada target hilang |
| Struktur tabel Markdown | Jumlah kolom konsisten per tabel pada dokumen aktif yang diperiksa |
| Reference arithmetic |12 pemeriksaan independen dokumen lulus: golden math inti, effort/capacity, rubric total dan runtime video |
| Implementasi / test aplikasi | Tidak dibuat atau dijalankan; seluruh test aplikasi tetap belum dieksekusi |

Pemeriksaan struktur tidak membuktikan semua cabang acceptance cukup atau implementasi sesuai. Gap semantik yang memerlukan test tambahan ada di Implementation Readiness (DDP-T-01–13). NFR aksesibilitas/latency, data nyata, konsep di luar kelas, kontribusi GitHub dan video tetap memerlukan bukti aktual. Manifest/checksum paket diperbarui setelah QA ini; patch menyimpan perubahan literal baseline.

## Lampiran QA v0.2.1 — 18 November 2026

Pemeriksaan ditargetkan pada enam temuan review independen dan dampaknya. Tidak mengulang atau mengklaim ulang hasil benchmark/aplikasi; hasil aritmetika v0.2 tetap historis karena rumus tidak berubah.

| Pemeriksaan | Hasil |
| --- | --- |
| Baseline sebelum edit | 25 hash manifest v0.2 cocok; identitas/versi/ukuran berkas aktif sesuai metadata terkini |
| Empat label BR yang dilaporkan | UX-BR-001/002, PUB-BR-006, SUP-BR-001 konsisten dengan FR dan row RTM |
| Root ZIP | v0.2=ORBIT_PRD_v0.2/; paket baru v0.2.1=ORBIT_PRD_v0.2.1/; README/manifest menjelaskan perbedaannya |
| Journey master/UX | Label P0/P1/P2 eksplisit; login hanya varian future; batas handoff P0+gate ditambahkan |
| FR/NFR/AC/test primer/user stories | Seluruh baris identik dengan v0.2; tidak ada ID ditambah/dihapus/diganti |
| BR | 102 ID tetap; tepat 4 BR yang berubah |
| PRD | 13 judul dan 20 bagian per PRD tetap; 4 PRD terdampak, 9 PRD byte-identik |
| Prioritas FR | Tetap 48 P0 / 27 P1 / 68 P2, total 143 |
| Tautan/tabel | Semua target tautan relatif yang diperiksa ada; kolom tiap tabel konsisten |
| Bukti kesiapan | RV-14/15 dan runtime tetap belum tervalidasi; tidak ada aplikasi/tes aplikasi dibuat |

Sebaran ID dan tautan yang valid tidak membuktikan konsistensi semantik seluruh dokumentasi; temuan review ini menunjukkan batas pemeriksaan struktural sebelumnya. Pemeriksaan baru menutup enam temuan tersebut, bukan sertifikasi bebas seluruh kemungkinan masalah. Detail ada di errata dan changelog.
