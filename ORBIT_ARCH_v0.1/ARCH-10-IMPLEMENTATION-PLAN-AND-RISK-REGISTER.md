# ORBIT · ARCH-10 · IMPLEMENTATION PLAN AND RISK REGISTER

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Menguji kelayakan rencana terhadap kapasitas nyata, waktu untuk quality/repository/video, dan tenggat resmi.

**Scope:** work packages P0, estimasi bersyarat, alokasi 3–4 orang, release gates, rubrik dan risiko kritis.  
**Non-goals:** komitmen tanggal selesai tanpa data tim, scope P1 otomatis, janji nilai, atau menganggap 23 tanggal kalender sebagai 23 hari kerja.

**Sumber:** MVP-SCOPE-AND-PRIORITIES baseline 84–100 jam-orang; Readiness; RV-11/12/14/15/16; panduan DDP1 hlm 1–5; seluruh 48 FR P0. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. Estimasi granular dan kapasitas

Baseline sumber **84–100 jam-orang belum tervalidasi**. Rekomendasi estimasi arsitektur **86–116 jam-orang sebelum cadangan**, bukan hasil pengukuran. Kenaikan terutama karena transaksi/idempotency/reset, precision boundary, request protection dan bukti UI/integrasi yang kini dirinci. Interval adalah low–high judgement, bukan confidence interval statistik. Paket domain/service termasuk focused unit tests; WP-08 hanya pengujian lintas modul/UI/performance agar tidak menghitung semua unit test dua kali.

| WP | Cluster requirement / pekerjaan | Jam-orang | Keyakinan / bottleneck / dependensi |
| --- | --- | --- | --- |
| WP-01 | CORE004/008,PRO001–004,MAP001: scope, DTO, fixture/source schema dan runtime spike |7–9|Rendah; RV-14/15/OD-01; awal critical path |
| WP-02 | MAP002/003/007/009/012: AST, validator, actual eligibility, golden negatives |8–10|Sedang; WP-01, skill graph/source binding |
| WP-03 | MAP004/005/006/011: SKS, chosen OR, delay, overlay reset/stale |7–10|Rendah; WP-02+revision contract |
| WP-04 | GRD001–007/012/014/016/018: tree/math/target/parser/rounding |10–13|Sedang; WP-01, precision dan boundary |
| WP-05 | GRD010/011,PRO005,CORE002/003: explicit actual, history, scenario integration |8–11|Rendah; WP-04+WP-06 UoW, conflict handling |
| WP-06 | AUTH010/014/015,PRO001–005: schema/store, ownership, transactions, receipts, restart/export/reset/guards |11–15|Rendah; WP-01, SQLite/web consistency |
| WP-07 | UX001–008,MAP008,PUB002/003,CORE005/007: forms/list/dashboard/navigation/labels |12–17|Rendah; services stable; Figma fidelity dibatasi |
| WP-08 | NFR aktif,INT001/003/010/013/014,DDP active: integrated failures, browser accessibility, perf/fresh clone |11–15|Rendah; WP-02–07, perangkat tim dan defect repair kecil |
| WP-09 | CORE008/103, repo docs/review/teach-back/contribution audit |6–8|Rendah; dilakukan bertahap, semua anggota |
| WP-10 | Video≤15 min, upload/access checks, GitHub public check, dua tautan submission |6–8|Sedang; build freeze dan koneksi unggah |
| Total |Seluruh P0+quality+deliverables|**86–116**|Belum komitmen; spike/actual velocity harus mengoreksi |

Cadangan 25% dari jam tersedia tidak dialokasikan ke fitur. Jika 86–116 adalah usable effort, raw hours yang diperlukan kira-kira 114,7–154,7. Jangan menambahkan cadangan dua kali saat memakai tabel capacity berikut.

Tanggal 18 Nov–10 Des mencakup 23 tanggal kalender (selisih 22 hari), **bukan** asumsi semua tanggal bebas kuliah/ujian. Formula keputusan nyata: `usable_capacity = 0.75 × sum(jam efektif setiap anggota pada tanggal yang benar-benar tersedia)`.

| Skenario ilustratif, bukan data anggota | Usable capacity | Kesimpulan terhadap 86–116 |
| --- | --- | --- |
|3 orang×23 tanggal×1.5 jam×75%|77.625 jam|Di bawah low estimate; tidak layak berkomitmen tanpa revisi |
|3 orang×23×2 jam×75%|103.5 jam|Menutupi low case, belum high case; perlu bukti spike dan scope discipline |
|4 orang×23×1.5 jam×75%|103.5 jam|Sama total; koordinasi bukan gratis |
|4 orang×23×2 jam×75%|138 jam|Menutupi upper estimate secara aritmetika; ketersediaan/skills tetap harus dibuktikan |

Jika usable capacity<86, jangan menyatakan “cukup asal cepat”. Tinjau renderer sederhana/fallback Streamlit dan estimasi ulang berbasis spike; bila masih tidak cukup, buat usulan pengurangan scope yang menyebut FR/AC/dampak untuk keputusan manusia. Paket ini tetap mempertahankan 48 P0. Gate lolos tidak mengaktifkan P1; seluruh P1 off dalam rencana pertama.

## 3. Milestone dan dependensi kalender

Tanggal adalah **target internal bersyarat**, bukan perubahan deadline dosen. Bila gate terlambat, jadwal downstream harus direvisi, bukan menurunkan kualitas secara diam-diam.

| Jendela WIB | Deliverable/evidence | Peran dan gate keluar |
| --- | --- | --- |
|18–19 Nov|Review arsitektur, RV-14/15, daftar perangkat/skills, fixture plan; bounded spike hanya setelah izin manusia|Semua; capacity/novelty/runtime evidence tercatat |
|20–24 Nov|Pure MAP dan GRD golden/negative; schema/UoW dasar|A MAP, B GRD, C data; bila 4 orang D integration tests; engine checkpoint 24 Nov |
|25–28 Nov|Profile/offering→BRP→target→scenario→actual→Dashboard + persistence|A/B/C/D cross-review; INT003/013/014 menjadi fokus |
|29 Nov–2 Des|Seluruh 48 P0 end-to-end, NFR/negative/perf/UX, README fresh clone|Quality gate; defect core menahan freeze; P1 tetap off pada paket ini |
|3–5 Des|Fix defects, freeze build/fixture, semua anggota teach-back seluruh kode, repo public audit|Release candidate dengan evidence, tanpa scope baru |
|6–8 Des|Rekam/edit video target 14 min, unggah, cek durasi/audio/akses|Semua memahami demo; narasi arsitektur berbasis code aktual |
|9 Des|Cek final commit, public GitHub, YouTube accessible, dua URL via kanal pengajar|Internal submission target, simpan bukti penerimaan |
|10 Des|Buffer upload/defect/submission; cutoff resmi 23.59 WIB|Tidak memulai fitur baru; pastikan kedua tautan terkumpul |

Critical path: WP-01→engine+store→actual/scenario integration→UI/end-to-end→quality freeze→video/link checks. Parallel kerja engine membantu, tetapi DTO/revision/schema harus disepakati awal. Semua orang mendapat perubahan code/test bermakna dan review area lain. Pembagian roles bukan nama orang yang diada-adakan.

## 4. Rubrik: bukti yang dapat dipersiapkan

| Kriteria resmi | Bobot | Bukti implementasi/repository/video yang relevan | Batas klaim |
| --- | --- | --- | --- |
|Masalah yang diangkat|20%|Catatan kebutuhan mahasiswa secara sukarela, contoh kebingungan prasyarat/target, alur sebelum/sesudah|Fixture sintetis bukan validasi dampak nyata; RV-16 open |
|Keunikan/daya tarik solusi|10%|Hubungan target grade→actual confirmation→eligibility→scenario/Dashboard dengan source labels|Tidak mengklaim belum pernah ada solusi serupa |
|Konsep baru di luar kelas|20%|Graph/tree/transaction/exact arithmetic/testing yang **telah dibandingkan** materi kelas, dijelaskan semua anggota|RV-15 menentukan novelty; sekadar memakai Flask tidak otomatis cukup |
|Kompleksitas program|20%|AND/OR tiga nilai, graph validation/delay, weighted tree/target, revision/history/atomic persistence; complexity explanation|Kompleksitas harus terkait masalah; banyak dependency bukan bukti sendiri |
|Kualitas repository|20%|Source terstruktur, README fresh clone, meaningful history seluruh anggota, tests/fixture/provenance dan review|Tidak ada quota commit buatan atau klaim repo sudah tersedia |
|Kualitas video|10%|Masalah+demo+arsitektur/solusi terbaca, audio jelas,≤15 menit, link accessible|Tidak menjanjikan nilai tertentu |

## 5. Video dan submission contract

Target 14 menit:00:00–01:30 masalah;01:30–02:30 nilai solusi/scope;02:30–06:30 demo;06:30–10:30 arsitektur+kode;10:30–12:00 konsep baru/test aktual;12:00–13:00 repo/kontribusi;13:00–14:00 batas/future. Konten resmi tetap tiga bagian utama, durasi≤15:00. Tidak wajib semua anggota muncul kamera; semua tetap harus memahami kode. Video dan public-repo checks termasuk WP-10, bukan setelah deadline. Kanal pengumpulan final mengikuti arahan pengajar yang belum diberikan; jangan mengarang portal/submission URL.

## 6. Risiko kritis dan mitigasi termurah

| Risiko | Pemicu / dampak | Mitigasi dan fallback paling kecil | Owner / bukti |
| --- | --- | --- | --- |
|R1 Kapasitas/skill kurang|Usable<86 atau engine checkpoint 24 Nov gagal|P1 off, list UI, pair-review, uji fallback; perubahan scope lewat review, bukan hidden omission|Tim/RV-14; actual time log dan reestimate |
|R2 Kebaruan/pemahaman belum terbukti|Konsep sudah diajarkan; satu anggota tidak dapat jelaskan code|Bandingkan silabus, konsultasi Asdos, pilih satu konsep berguna, teach-back semua file|Tim+Asdos/RV-15 |
|R3 Salah angka/rule resmi|Float rounding, weight salah, sumber Figma dipakai sebagai aturan|Exact math+golden fixtures, provenance/unknown, synthetic only; no actual conversion otomatis|A/B/OD-02/03, DDP01–06 |
|R4 State/history hilang atau campur|Stale overwrite, reset salah scope, response-loss double write|Satu UoW/token/receipt, append-only final, temp-file rollback/restart/concurrency tests|C dengan A/B, INT003/013/014 |
|R5 Demo no-auth terbuka|Bind wildcard/tunnel atau runtime secrets masuk GitHub|Guard loopback/Host/CSRF/debugoff, no public deployment, staged diff+video review|C/D, DDP09 |
|R6 Integrasi/UX/video mepet|UI polish terus, browser errors, upload 9–10 Des gagal|Kontrol future disembunyikan, freeze 3–5 Des, rekam 6–8 Des, submit internal 9 Des|Semua, DDP10 + evidence upload |

Risiko lain RV-02–10 (data resmi, integrasi/komunitas/operasi) tidak berada di critical path demo karena capability off; tetap terbuka untuk future. Kegagalan primary P0 gate tidak ditutup dengan menandai test deferred tanpa keputusan scope.

## 7. Release gates

G0 input architecture/source consistency; G1 manusia+RV-14/15/runtime/fixture; G2 pure engine golden/negative; G3 service transaction/history/restart; G4 all P0 +NFR/UX/perf/fresh clone; G5 human review/teach-back/no secrets; G6 public repo+video≤15 min+dua URL terkumpul. **Saat ini hanya pemeriksaan dokumentasi G0 dilakukan**; G1 open, G2–G6 not executed. Tidak ada status implementation complete.

## Risiko, dependensi, dan bukti terbuka

86–116 jam tetap estimasi kasar dengan confidence rendah; tidak menjamin tim 3 orang cukup. Jadwal menuntut review gates segera tetapi tidak menganggap ketidakhadiran jawaban sebagai persetujuan.

**Traceability:** CORE-AC/T-008/103; seluruh aktif ARCH-07; resmi DDP deadline/contribution/understanding/deliverables/rubric. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** RV-14 jam efektif aktual, RV-15 novelty, RV-16 evidence masalah, OD-01 runtime; tanggal internal harus diperbarui jika bukti gate terlambat. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
