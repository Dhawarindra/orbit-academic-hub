# ORBIT — MVP Scope and Priorities

Versi **v0.2.1 DDP1 Errata** · 18 November 2026 (Asia/Jakarta) · Owner: Product Lead bersama tim 3–4 mahasiswa.

Status: audit dan rekomendasi dokumentasi; belum ada aplikasi atau bukti kelulusan implementasi.

## Keputusan rilis dan dasar kelayakan

Rekomendasi v0.2 adalah **Roadmap + Grade Rescue + Dashboard**, dengan profil/persistensi minimum dan guard demo lokal sintetis. Ini keputusan analisis untuk proyek DDP1, bukan fitur yang diwajibkan dosen. Visi penuh Orbit tetap berada di 13 PRD; tidak ada requirement lama dihapus. Scope ini layak **bersyarat** pada kapasitas 84–100 jam-orang dan kemampuan dasar Python/Git tim; ketersediaan aktual belum diketahui.

Hipotesis pengguna sebagian besar diterima setelah analisis: Schedule/Stress sederhana dan Vault layak sebagai P1, sedangkan Senior Playbook, Career Navigator, advanced Guidance, Semester Closeout lengkap dan integrasi resmi tetap P2. Dua penyesuaian tambahan mengurangi risiko: layanan akun multiuser menjadi P2 dengan mode demo lokal yang eksplisit, serta IPS/IPK lintas attempt/term menjadi P1 sementara perhitungan bobot, proyeksi dan target nilai course tetap P0. Dampaknya: demo tidak menjanjikan portal produksi atau kalkulasi IPK resmi lengkap.

## Analisis opsi sebelum memilih scope

| Kandidat | Manfaat pengguna | Kesulitan / dependensi | Kontribusi Python | Penilaian kelayakan |
| --- | --- | --- | --- | --- |
| Roadmap: prasyarat, SKS dan satu simulasi | Memahami course yang dapat direncanakan dan dampak penundaan | Sedang; graph/rule validation; dataset resmi belum tersedia tetapi fixture sintetis memungkinkan demo | Boolean tiga nilai, graf, DFS/topological order, constraint checking | P0; scope satu kurikulum demo kecil dan satu skenario |
| Grade Rescue: bobot/known/unknown/target/what-if | Menjawab kebutuhan nilai sisa dan batas yang mungkin | Sedang; presisi, tree, invalid input; BRP aktual tidak diperlukan untuk fixture berlabel | Traversal tree, normalisasi, aljabar target, bounds, validation | P0; linear saja; struktur terkunci setelah skor |
| Dashboard inti | Menyatukan hasil dan tindakan berikutnya | Rendah–sedang jika membaca GRD/MAP; tinggi bila memerlukan seluruh GDE | Aggregation/provenance/revision; bukan rumus kedua di frontend | P0; tidak memerlukan guidance engine atau chart historis |
| Schedule/Stress sederhana | Melihat bentrok dan kepadatan pekerjaan | Sedang; timezone/date-only/unknown; data manual | Interval overlap, total jam dan coverage | P1 paket terpisah, bukan sekadar tambah kalender visual |
| Vault kurasi/search | Menemukan resource yang boleh dibagikan | Rendah–sedang teknis, bergantung bukti hak link | Validasi URL, filtering/ranking metadata | P1 jika 3–5 link berizin tersedia; kosong/ditunda jika tidak |
| IPS/IPK sederhana | Ringkasan target semester | Sedang; inclusion/retake/policy/unknown menambah cabang | Weighted quality points dan denominator handling | P1; tidak aktif sebagai angka resmi tanpa policy binding |
| SNR advanced dan contributor workflows | Belajar dari pengalaman komunitas | Tinggi; donor, consent, moderation, suppression/reidentifikasi | Dedup/agregasi/rule gates bermakna, tetapi data belum ada | P2; tidak layak dijanjikan untuk deadline ini |
| Career-to-Course | Mengaitkan minat dan course | Sedang–tinggi; mapping/reviewer/sumber belum ada | Ranking deterministik; biaya kurasi dominan | P2 |
| Advanced Guidance dan Closeout | Menutup siklus akademik lengkap | Tinggi; sumber lintas modul, conflict resolution, idempotensi, snapshot | Rule precedence dan transaksi | P2; konfirmasi aktual per course dipertahankan P0 |
| Akun multiuser / SSO / SLCM | Pengalaman layanan produksi dan sinkronisasi | Tinggi; keamanan, lifecycle, operator; SSO/SLCM memerlukan izin/kontrak | Infrastruktur bukan pusat demonstrasi algoritma akademik | Akun P2; SSO/SLCM P2 dan diblokir izin; demo lokal tetap memenuhi pilihan bentuk aplikasi di panduan |

Alternatif yang tidak dipilih: seluruh P0 v0.1 memiliki 111 FR lintas layanan dan tidak mempunyai estimasi yang mendukung penyelesaian; console saja mengurangi pekerjaan UI tetapi memerlukan perubahan pengalaman Orbit yang lebih besar. Flask/Jinja lokal mempertahankan bentuk produk dengan beban dua runtime/framework yang lebih kecil daripada frontend SPA + backend terpisah. Penilaian effort ini adalah analisis, bukan benchmark kinerja tim.

## Kapasitas dan sensitivitas waktu

Panduan menetapkan proyek 5 minggu dengan kickoff 5 November. Pada tanggal audit **18 November 2026**, jarak ke 10 Desember adalah 22 hari kalender; jika menghitung kedua tanggal ada 23 tanggal kerja potensial. Itu tidak berarti mahasiswa tersedia setiap hari. Perhitungan berikut memakai asumsi jam efektif per hari untuk membandingkan skenario dan harus diganti dengan RV-14.

| Anggota | Jam efektif/orang/hari (asumsi) | Kapasitas bruto 23 hari | Cadangan 25% | Kapasitas rencana 75% | Implikasi terhadap 84–100 jam-orang |
| --- | --- | --- | --- | --- | --- |
|3 |1,5 |103,5 |25,875 |77,625 | Tidak cukup untuk scope rekomendasi penuh; perlu pengurangan tercatat atau jam tambahan |
|3 |2 |138 |34,5 |103,5 | P0 masuk rentang; ruang tersisa 3,5–19,5, bukan janji P1 |
|4 |1,5 |138 |34,5 |103,5 | P0 masuk rentang, P1 tetap bersyarat |
|4 |2 |184 |46 |138 | P0 plus paling banyak satu paket P1 setelah gate; buffer tetap dijaga |

Cadangan menampung ketidakpastian belajar, integrasi, sakit/jadwal kuliah dan perbaikan; pekerjaan pengujian, README dan video **sudah masuk** estimasi inti, sehingga tidak boleh dibiayai hanya dari cadangan. Tim tiga orang pada dua jam/hari cukup secara aritmetika, tetapi bottleneck kemampuan atau keterlambatan fixture dapat membuatnya tidak layak. Tanpa data kapasitas nyata, scope ini adalah baseline kerja yang direkomendasikan, bukan komitmen final tim.

| Paket kerja P0 | Jam-orang estimasi | Termasuk | Ketidakpastian utama |
| --- | --- | --- | --- |
| Scope, bimbingan, fixture dan penetapan konsep |6–8 | Scope satu kurikulum demo, source labels, pemilihan materi baru, validasi masalah ringan | Jadwal Asdos dan ketersediaan anggota |
| Roadmap engine |16–18 | Rule tiga nilai, cycle/dangling validation, SKS, penundaan, stale/reset satu skenario | Pengalaman graf dan edge cases |
| Grade engine |16–18 | Tree weights, numeric guards, bounds/target, what-if, aktual per course | Presisi dan pemisahan provenance |
| Persistensi/profil/demo guards |8–10 | owner_scope lokal, SQLite, checkpoint, export/reset dan restart | Transaksi serta environment tim |
| Shell Flask/Jinja dan Dashboard |14–16 | Bentuk Orbit, form/list, errors/unknown/stale, responsive/keyboard | Pengalaman HTML/CSS dan integrasi view models |
| Pengujian/review integrasi |12–14 | Golden/negative tests, fresh-clone, benchmark kecil, teach-back lintas modul | Temuan integrasi dan perbaikan |
| Repository, demonstrasi dan video |12–16 | README/kontribusi, script 14 menit, rekaman/edit, upload/cek dua tautan | Kualitas rekaman, koneksi dan revisi narasi |
| **Total** | **84–100** | Seluruh alur inti sampai bukti pengumpulan | Belum berdasarkan velocity tim aktual |

Estimasi tambahan jika core sudah stabil: Schedule/Stress 12–18 jam-orang; Vault+search+rights checks 8–12; GPA/tren 8–12. Ini paket alternatif; **jangan menjumlahkan semuanya sebagai janji P1**. Waktu belajar tambahan yang melampaui asumsi memakai cadangan atau memicu scope review.

## Isi konkret P0

1. **Workspace demo lokal**: satu owner_scope stabil, input sintetis, state tersimpan lintas restart, export JSON lokal, reset dengan konfirmasi. Aplikasi bind loopback; tidak membuka layanan tanpa auth kepada publik. Repository kode tetap publik sesuai panduan.
2. **Profil minimum**: konteks program/angkatan atau unknown, satu term aktif, offering/enrollment dan riwayat manual; tidak ada import/migrasi kurikulum.
3. **Roadmap**:6–12 course sintetis, katalog/list dengan sumber, AND/OR met/unmet/unknown, actual-only eligibility, total SKS personal, dampak downstream, validasi cycle/dangling, satu scenario overlay. Mode stale meminta reset/pilih ulang; tidak ada solver kombinasi jadwal/kelulusan optimal.
4. **Grade Rescue**: dua offering untuk demo, satu BRP bertingkat dengan leaf 10/10/30/50, input unknown/zero, validation, K/bounds/observed average, numeric target dan what-if. Target huruf hanya jika policy eksplisit cocok; unknown policy tidak ditebak. Perubahan struktur sesudah skor tersimpan ditolak; koreksi nilai tetap dapat dilakukan.
5. **Konfirmasi aktual per course**: input hasil aktual eksplisit dengan source, preview/revision dan alasan koreksi; tidak menyalin proyeksi menjadi actual dan tidak memerlukan semester closeout. Pada demo, seluruh record ini tetap sintetis meskipun mensimulasikan provenance user_reported.
6. **Dashboard Orbit**: ringkasan GRD/MAP langsung, source/type/freshness labels, unmet/unknown dan link ke layar asal. Tanpa GPA P1, deadline P1, community, guidance atau chart fiktif. Shell, warna/typografi/motif dan list accessibility mengikuti PRD-09.

Informasi yang belum ada tampil unknown/unavailable. UI boleh menyembunyikan menu future atau menampilkan status “direncanakan”, dengan capability manifest yang konsisten. Menonaktifkan menu bukan menghapus dokumentasi fitur. Tidak dibutuhkan server admin, event bus, Docker, layanan cloud, email atau API akademik untuk demo inti.

## P1 dan syarat aktivasi

Gate dilakukan **2 Desember 2026**. P1 hanya boleh dipilih jika semua alur P0 end-to-end berjalan, test numerik/integrasi utama lulus, tidak ada defect blocker, seluruh anggota dapat menjelaskan kedua engine, dokumentasi/kontribusi sudah berjalan, dan proyeksi sisa jam setelah pekerjaan video serta cadangan cukup. Jika salah satu gagal, seluruh P1 ditunda otomatis dalam rencana rilis; requirement tetap disimpan.

| Paket | Syarat khusus | Batas |
| --- | --- | --- |
| Schedule/Stress sederhana | Input manual, source assessment sama, timezone/date-only dan unknown capacity ditangani | Pertemuan individual, overlap, total remaining hours/coverage; tanpa recurring editor, alokasi otomatis atau diagnosis |
| Vault+search | Hak berbagi jelas per link, allowlist/URL gate, timestamp pemeriksaan |3–5 metadata link; tanpa hosting/crawler, akun kontributor, bookmark atau report queue |
| GPA/tren sederhana | Policy sintetis eksplisit atau sumber sah cocok scope; denominator/retake unknown guards | IPS/IPK basic dengan label; tanpa policy comparison atau klaim transkrip resmi |

Help, landing, FAQ dan UI changelog adalah enhancement kecil yang ikut paket terpilih, bukan alasan menggeser video/testing. Pilih maksimal satu paket; jangan memulai P1 setelah freeze 3 Des jika akan menambah risiko.

## Future Development dan dependency yang dipertahankan

| Kemampuan future | Requirement utama yang tetap ada | Prasyarat aktivasi |
| --- | --- | --- |
| Senior Playbook tingkat lanjut/komunitas | Seluruh SNR-FR-001–009 | Donor/consent, compatible scope, privacy review, layanan akun dan moderasi |
| Career-to-Course Navigator | Seluruh CAR-FR-001–008 | Mapping bersumber/reviewed, scope kurikulum dan reviewer |
| Advanced Guidance | GDE-FR-001–005 | Data source/version dan rules dari modul yang aktif |
| Semester Closeout penuh/handover | GDE-FR-006–010; CORE-FR-006 | Atomic snapshot, reopen/concurrency/idempotensi; consent terpisah |
| Integrasi resmi SSO UI/SLCM | AUTH-FR-008/009 | Izin resmi, kontrak provider, scopes, account-link/security review; tidak diasumsikan tersedia |
| Akun Orbit multiuser | AUTH-FR-001–007/011–013 dan NFR terkait | Operator/hosting dan kontrol data nyata RV-10; tidak diganti password plaintext atau identitas lokal palsu |
| Migrasi/import dan perbandingan | PRO-FR-006/008/009, MAP-FR-010 dan subkemampuan 006, GRD-FR-013/017/020 | Dataset/policy/UX dan kapasitas tambahan; historical records tetap |
| Schedule lanjutan | SCH-FR-007–011 dan recurrence pada 002 | PreparationBlock/capacity model, konflik/alokasi dan tests |
| Kontributor/bookmark/report | VLT-FR-004–008/010, SUP-FR-004/005/007/011, PUB-FR-006–008 | Account/consent, rights review, operasi moderasi |
| Tema gelap/laporan/digest | UX-FR-010, SUP-FR-009/010 | QA token, izin channel dan infrastruktur yang sesuai |

Daftar exact per-ID ada pada audit dan RTM; rentang di sini adalah navigasi ringkas. P1 yang tidak dibangun juga masuk pengembangan setelah DDP1, tetap dengan ID semula. Tidak ada komitmen tanggal untuk P2.

## Arsitektur dan rekomendasi tech stack

**Rekomendasi: monolit Python + Flask/Jinja + HTML/CSS + JavaScript minimum, SQLite melalui sqlite3, serta unittest dan Flask test client.** Satu runtime Python memudahkan tim menelusuri seluruh logika dan menjelaskan arsitektur dalam video. Rekomendasi ini tidak membuktikan semua anggota sudah menguasainya; lakukan environment/skills check 18–19 Nov.

| Komponen | Peran konkret | Alasan dan batas |
| --- | --- | --- |
| Python domain MAP/GRD | Parse/validate input; evaluasi prasyarat; graph traversal; BRP tree; Decimal/basis-point math; target/bounds; actual/scenario separation | Ini komponen utama aplikasi yang memenuhi arah DDP-02; dapat diuji tanpa browser |
| Python application/services | Validasi revision, transaksi persistensi, export/reset, aggregation dashboard dan provenance | UI tidak menjadi pemilik rumus atau data akademik kedua |
| Flask dan Jinja | Route/form handling, server-rendered HTML, presentation data dari Python | Flask menyediakan framework WSGI dan Jinja; menjaga shell Orbit dengan effort frontend terbatas (SRC-12) |
| HTML/CSS + JS kecil | Layout, focus/dialog, progressive enhancement | Tidak menghitung eligibility, grade atau target inti; tidak memerlukan SPA/build chain terpisah |
| SQLite/sqlite3 | Persistensi lokal profiles/enrollments/grades/scenario/revisions; parameterized queries dan transaksi | SQLite tidak memerlukan proses server terpisah; modul sqlite3 harus ada pada runtime tim (SRC-13) |
| unittest + Flask test client | Unit/domain fixtures, negative cases dan request/integration checks | unittest menyediakan cases/fixtures/suites; test client didokumentasikan Flask; tak perlu framework test kedua (SRC-12/14) |
| Git/GitHub + YouTube | Kolaborasi source publik dan pengumpulan dua tautan | Kewajiban panduan, berbeda dari hosting aplikasi |

Versi Python/Flask/dependencies belum dikunci: pilih satu versi Python yang tersedia pada semua perangkat tim dan kompatibel dengan Flask terpilih, catat versi, buat virtual environment dan pin dependencies setelah fresh-clone smoke check. Jangan menulis “latest” sebagai kontrak reproduksi. Tidak ada persyaratan Django khusus; Django pada panduan adalah contoh.

Alternatif **Streamlit** dapat dipilih jika kemampuan web tim rendah dan waktu aktual kurang, karena alur UI/data dapat ditulis di Python; session state, forms dan rerun perlu dipahami (SRC-15). Tradeoff analisis: penyesuaian shell Orbit mungkin lebih besar, sehingga bukan default. Console diperbolehkan panduan dan menjadi jalan terakhir setelah revisi scope/UX tercatat. React/Next.js + API Python terpisah tidak direkomendasikan untuk jadwal ini karena menambah integrasi/runtimes tanpa memperkuat kebutuhan inti. Ini penilaian kelayakan, bukan larangan teknologi dosen.

## Pembagian kerja 3–4 anggota

| Peran sementara | Kontribusi kode yang direncanakan | Review silang / pemahaman |
| --- | --- | --- |
| A | MAP graph/rules/scenario dan test cabang | Menjelaskan GRD serta mereview math/unknown handling |
| B | GRD tree/target/actual dan test numerik | Menjelaskan MAP dan mereview graf/prasyarat |
| C | Flask/Jinja, PRO, dashboard dan persistensi/export/reset | Menjelaskan kedua engine; A/B mereview transaksi dan UI boundary |
| D bila 4 anggota | Integration tests, revision/state validation dan bagian repository/service yang konkret; membantu UI/persistence | Tidak hanya mengedit video; tetap menghasilkan kontribusi kode bermakna, memahami semua modul |

Pada 3 anggota, tests/integrasi/dokumentasi/video dibagi bersama, tidak seluruhnya dibebankan ke C. Peran bukan silo kepemilikan pengetahuan: **semua wajib memahami seluruh kode**. Nama dan author GitHub diisi dari daftar kelompok resmi; tidak dibuat dalam audit. Commit kecil yang menyelesaikan perubahan bermakna, review dan diskusi dianjurkan; tidak ada kuota commit atau strategi branch wajib dari panduan.

## Jadwal delivery yang direkomendasikan

Semua tanggal 2026 dalam WIB. Target internal tidak mengubah deadline resmi.

| Periode | Hasil yang harus tersedia | Gate / keputusan |
| --- | --- | --- |
|18–19 Nov | Scope kapasitas aktual, daftar anggota/Asdos, konsep baru, fixture dan environment terpilih | RV-14/15; revisi estimasi bila kemampuan/jam berbeda |
|20–24 Nov | Python MAP/GRD berjalan pada fixture dengan validasi dan test utama | Jangan memulai fitur komunitas; review lintas engine |
|25–28 Nov | Persistensi/profil, shell dan Dashboard terhubung; aktual per course, scenario/reset | Uji restart, unknown, stale dan isolation |
|29 Nov–2 Des | Core end-to-end stabil, test/integrasi, README/run; kontribusi semua anggota terlihat |2 Des: pilih maksimal satu P1 hanya jika ada kapasitas setelah cadangan/video |
|3–5 Des | Feature freeze, perbaikan defect, fresh-clone, tampilan/keyboard dan proof checklist | Tidak menambah fitur baru; batas yang belum selesai disebut jujur |
|6–8 Des | Rehearsal, teach-back seluruh anggota, rekam/edit/upload video≤15 menit | Repo dan video menggambarkan versi sama; cek suara/teks/tautan |
|9 Des | Dua tautan siap dan target pengumpulan internal | Uji akses penilai, public repo, durasi dan bukti submission |
|10 Des | Buffer unggah/perbaikan submission | Deadline resmi **23.59 WIB**, jangan menjadikan hari ini hari mulai rekaman |

Jika pada 24 Nov engine utama belum bekerja, hentikan P1 dan review kapasitas hari itu. Jika pada 28 Nov core belum terintegrasi, utamakan daftar/table yang sudah didesain, kurangi polish dan gunakan fixture lebih kecil; jangan memangkas validasi, label sumber atau pemisahan actual/scenario. Jika 84 jam-orang pun tidak tersedia, buat keputusan scope baru dengan ID/perubahan tercatat; jangan diam-diam mengklaim baseline ini terpenuhi.

## Definition of done rilis DDP1

Seluruh FR P0 yang aktif serta NFR terkait mempunyai bukti test; demo inti selesai dengan modul opsional off; data/sumber/scenario jujur; repository publik dapat dijalankan dari README dan menunjukkan kontribusi seluruh anggota; setiap anggota memahami semua bagian kode; video YouTube≤15 menit mencakup masalah, demo dan arsitektur; dua tautan dikumpulkan tepat waktu. P1/P2 yang tidak dibangun berlabel ditunda, bukan gagal atau fitur tersembunyi.

Rujukan teknis primer (diakses 18 Nov 2026): [Flask](https://flask.palletsprojects.com/en/stable/), [sqlite3](https://docs.python.org/3/library/sqlite3.html), [unittest](https://docs.python.org/3/library/unittest.html), [Streamlit architecture](https://docs.streamlit.io/develop/concepts/architecture). Rujukan aturan resmi dan nomor halaman ada di Compliance Matrix.

## Handoff v0.2.1 — scope awal yang diizinkan

Status **CONDITIONAL GO untuk desain arsitektur**, bukan MVP final atau bukti siap implementasi penuh. Sebelum komitmen delivery, lengkapi kapasitas nyata anggota (RV-14), konsep yang benar-benar di luar kelas (RV-15), dan bukti runtime/stack dapat dijalankan pada perangkat tim. Estimasi 84–100 jam-orang adalah estimasi paket; perlu dipecah menurut pekerjaan implementasi/FR dan diestimasi ulang setelah spike yang kelak diotorisasi. Audit/errata ini tidak mengerjakan spike atau kode aplikasi.

Default handoff: hanya 48 FR P0 beserta BR/NFR/AC/test untuk kemampuan yang aktif. Semua P1/P2 nonaktif; subkemampuan future dalam FR P0 campuran (misalnya rebase penuh MAP-FR-006) juga nonaktif. Lolos gate kapasitas tidak otomatis mengaktifkan fitur: catat keputusan scope, ID yang diaktifkan, dependensi dan test, lalu perbarui capability manifest. Jangan menambahkan fitur dari journey produk lengkap atau mockup Figma sebagai P0 tersirat.

Desain arsitektur berikutnya dapat merinci monolit Python modular, rencana file per file, kontrak data/revision dan test plan. IPS/IPK/tren tetap P1; Senior Playbook, Career Navigator, full closeout dan dark mode tetap P2. Dashboard P0 memakai hasil MAP/GRD yang benar-benar dihitung atau unknown/unavailable; tidak mengisi kartu IPK/tren/insight dengan data ilustrasi seolah hasil nyata. Roadmap dapat memakai tema terang dan list accessible sesuai baseline; identitas visual Orbit tetap.

Rincian koreksi dan bukti penutupan ada di [PRD-v0.2.1-ERRATA.md](PRD-v0.2.1-ERRATA.md).
