# ORBIT — Implementation Readiness Report

Versi **v0.2.1 DDP1 Errata** · 18 November 2026 (Asia/Jakarta) · Owner: Product Lead bersama tim 3–4 mahasiswa.

Status: audit dan rekomendasi dokumentasi; belum ada aplikasi atau bukti kelulusan implementasi.

## Status kesiapan

**CONDITIONAL GO untuk desain arsitektur demo lokal; belum dapat disebut MVP final atau siap implementasi penuh sebelum kapasitas, kebaruan konsep dan kesiapan perangkat tervalidasi.** Panduan sudah diverifikasi, scope/dependency dan kontrak Python utama sudah dijelaskan. Kesiapan memulai implementasi masih bersyarat pada jam/kemampuan tim dan pilihan konsep di luar kelas. Tugas ini hanya menghasilkan audit/revisi dokumentasi, tanpa kode aplikasi.

Repository/video implementasi belum diberikan. Nama anggota/Asdos, ketersediaan kerja, versi runtime, kurikulum/BRP/policy aktual dan akses kampus belum dikonfirmasi. Hal ini tidak memblokir perencanaan atau demo berbasis fixture sintetis, tetapi membatasi klaim dan rilis data nyata.

## Keputusan teknis: diketahui, direkomendasikan, belum final

| Area | Status / keputusan | Yang harus diputuskan berikutnya | Owner / target |
| --- | --- | --- | --- |
| Bahasa utama | WAJIB Python (SRC-11 hlm. 2); engine/validation/state/aggregation Python | Tidak perlu memilih ulang bahasa utama | Semua anggota |
| Framework/presentation | REKOMENDASI Flask/Jinja + HTML/CSS; JS presentasi saja | Konfirmasi berdasarkan kemampuan tim; Streamlit fallback memerlukan catatan tradeoff UI | Tim + Asdos, 18–19 Nov |
| Runtime/dependencies | Belum final; jangan pin versi rekaan atau “latest” | Pilih Python/Flask kompatibel yang tersedia bersama; record environment dan dependency lock setelah smoke check | Peran C, 19 Nov |
| Persistensi | REKOMENDASI SQLite via sqlite3, owner_scope lokal stabil, transaksi/parameterized queries | Skema fisik, transaction boundaries, lokasi runtime DB dan fixture seeding | C dengan A/B, 20–25 Nov |
| UI/identitas | Baseline PRD-09 dipertahankan; tema terang P0, list accessible; dark P2 | Detail implementasi responsif dan pengukuran contrast/focus | C/UX reviewer, 25–28 Nov |
| Data akademik | Fixture sintetis P0; RV-02/03/04 open untuk aturan nyata | Pilih 6–12 course, 2 offerings dan policy demo jelas; jangan mengganti status jadi resmi | A/B, 19 Nov |
| Actual/scenario/revision | Kontrak tetap terpisah; konfirmasi per course P0, closeout P2 | Bentuk revision key, penyimpanan histori koreksi dan stale rejection | A/B/C, 20–28 Nov |
| Demo/auth | REKOMENDASI local-demo sintetis, loopback, debug off pada demo, export/reset lokal | Pastikan mode public-host tidak dapat dinyalakan tanpa paket akun/operasional | C + reviewer, 25–28 Nov |
| Privasi/hosting produksi | Belum siap; akun multiuser dan RV-10 P2 | Auth/authorization, recovery, lifecycle, operator dan security review sebelum data nyata | Future Development |
| Konsep di luar kelas | Kandidat graph/tree/transaction/testing; kebaruan belum terverifikasi | Bandingkan silabus/lab aktual dan sepakati konsep yang dapat dijelaskan seluruh anggota | Tim + Asdos, 18–19 Nov |
| P1 | Tidak dijanjikan; satu paket maksimum | Gate 2 Des, bukti core stabil dan sisa kapasitas setelah video/cadangan | Product Lead/tim |
| Pengumpulan | GitHub publik + YouTube≤15 menit; 10 Des 23.59 WIB | Kanal pengumpulan sesuai arahan pengajar dan URL final | Semua anggota, 9–10 Des |

## Batas komponen Python dan kontrak implementasi

Lapisan yang direkomendasikan: domain Python MAP/GRD yang dapat dipanggil tanpa UI; services Python untuk transaksi/revision dan aggregation; repository SQLite; route/template untuk presentasi. Ini pembagian tanggung jawab dalam satu aplikasi, bukan microservices. Bentuk endpoint, schema fisik dan nama file final belum dipaksakan pada tahap PRD.

| Kontrak | Input | Output / invariant | Verifikasi terkait |
| --- | --- | --- | --- |
| MAP eligibility | Graph/rule version, actual finals, source scope | met/unmet/unknown dan alasan per leaf; prediction tidak membuka course | MAP-AC-002/003/009; DDP-T-01/02 |
| MAP simulation | base_revision, chosen courses, personal SKS cap, assumed_pass | Plan overlay, totals dan dampak bersyarat; tidak menulis actual | MAP-AC-004/005/006/011; INT-T-003 |
| GRD calculation | BRP tree, earned/max, target, policy optional | K/O/U, bounds, observed average, required/feasibility, provenance | GRD-AC-002–007/012/014/016/018; DDP-T-03/04 |
| GRD actual confirmation | Explicit final, source, expected revision, correction reason | Revisi actual terpisah, sejarah lama tersimpan, downstream stale/recompute | GRD-AC-010; INT-T-013 |
| Dashboard | Python view models MAP/GRD dan input revisions | Angka sama, source/freshness terlihat, unknown jujur; GDE off | UX-AC-002; CORE-AC-002/005; INT-T-010 |
| Local persistence | owner_scope, records/revisions, operation identity | Restart konsisten, no duplicate retry, DB runtime terpisah dari seed | AUTH-AC-014/015; PRO-NFR-003; INT-T-014 |

## Kompleksitas algoritma yang layak didemonstrasikan

V=jumlah course, E=jumlah edge, L=jumlah leaf ekspresi prasyarat, A=jumlah node/assessment, R=jumlah resource, Q=panjang query. Kompleksitas di bawah adalah analisis rancangan; harus disesuaikan dengan kode yang benar-benar dipilih.

| Algoritma | Struktur / pendekatan | Kompleksitas yang dapat dijelaskan | Bukti bermakna |
| --- | --- | --- | --- |
| Cycle/dangling/scope validation | Adjacency map + DFS warna atau topological sort; dictionary IDs | O(V+E) traversal dan validasi edge dengan lookup rata-rata O(1) | Graf valid, cycle A↔B, node hilang, graph disconnected; tampilkan daftar error |
| AND/OR tiga nilai | Expression tree; met/unmet/unknown, short circuit yang menjaga alasan | O(L) per ekspresi jika setiap leaf dikunjungi sekali; cache hasil leaf hanya pada snapshot sama | Truth table dan nested AND(A, OR(B, C)); unknown tidak diluluskan |
| Dampak penundaan | Topological traversal downstream; constraint term | O(V+E) untuk fixture DAG dengan semua course tersedia setiap term. Jika mencari penawaran hingga horizon H, worst case menambah O(V×H); jangan mengklaim selalu linear | A1→B2→C3 menjadi A2→B3→C4; availability unknown menghasilkan conditional output |
| BRP tree / target | Validasi sibling groups, flatten effective weights, agregasi leaf | O(A) kunjungan pada tree valid, ruang O(A) atau stack kedalaman tree; tidak menghitung parent dua kali | Leaf 10/10/30/50; K=36, observed 72, bounds 36–86, target 75→78, target 90→108/impossible |
| Scenario/revision | Overlay keyed IDs + expected_revision | Biaya sebanding input yang dihitung ulang; bukan menyalin semua histori atau enumerasi semua kombinasi | What-if81 tidak mengubah actual; stale r1 ditolak sesudah r2 |
| P1 overlap/search | Pairwise interval untuk dataset kecil; metadata token/ranking | Pairwise overlap O(N²) dapat diterima untuk fixture kecil; alternatif sorting/sweep memerlukan analisis output. Search naive sekitar O(R×Q) bergantung tokenisasi, bukan klaim mesin pencari besar | Boundary end=start tidak overlap; exact code di depan partial match; hidden metadata hilang |

Graf dan formula terukur memberi kompleksitas yang berkaitan langsung dengan masalah. Menggunakan library hanya untuk menggambar graf tidak menggantikan implementasi/penjelasan validasi dan traversal. Tidak perlu ML, scraping atau optimasi kombinatorial untuk menunjukkan usaha pemrograman.

## Test tambahan untuk menutup gap semantik

Semua kasus berikut adalah **rencana**, belum dieksekusi. Gunakan data sintetis dan oracle terpisah dari implementasi; jangan menandai PASS karena expected result tercetak dalam dokumen. Test primer di PRD tetap berlaku.

| ID | Target / setup | Expected result dan kriteria lulus | Prioritas |
| --- | --- | --- | --- |
| DDP-T-01 | MAP-FR-003: pasangan met/unmet/unknown untuk AND dan OR, termasuk nested | Seluruh 9 kombinasi masing-masing operator cocok MAP-BR-003; AND(A met, OR(B unmet, C unknown))=unknown; alasan leaf sesuai | P0 |
| DDP-T-02 | MAP-FR-007/012: cycle A↔B, missing node Z, scope mismatch dan komponen graf terpisah | Tiga dataset rusak ditolak tanpa mengganti catalog aktif; disconnected DAG sah tetap dapat dihitung | P0 |
| DDP-T-03 | GRD-FR-002: sibling total 99,99/100/100,01; cycle tree; leaf dua parent | Hanya group tepat 100%/10.000bp dan tree valid diterima; tidak menghitung node ganda; pesan node/group jelas | P0 |
| DDP-T-04 | GRD-FR-007/014/018: semua unknown, U=0 dengan target tercapai/tidak, zero, negative, NaN/Inf, max≤0 | Unknown≠zero; denominator 0 tidak dibagi; nilai nonfinite/range invalid ditolak sebelum kalkulasi; input sah lain tetap | P0 |
| DDP-T-05 | GRD-FR-005/016: target 75,01 dengan granularity integer vs0,01; policy demo threshold 85 | Required 78,02 ditampilkan 79 untuk integer dan 78,02 untuk 0,01;84,995 tetap B walau display 85,00,85=A | P0 |
| DDP-T-06 | GRD-FR-001/020: skor Q1=80, upaya mengganti leaf/struktur pada modeP 0 | Perubahan ditolak; Q1/BRP lama utuh, tidak memindah skor diam-diam; jalur migrasi tidak diiklankan aktif | P0 |
| DDP-T-07 | GRD-FR-010: confirm actual A, cancel koreksi, confirm koreksi dengan revision usang, lalu revision benar | Cancel tidak mengubah; stale ditolak; konfirmasi terbaru menambah histori dan refresh MAP/UX; prediksi tidak pernah diprefill sebagai actual tanpa aksi eksplisit | P0 |
| DDP-T-08 | CORE-FR-005/UX-FR-002: semua opsional dan semua campus adapter off | Profil→BRP/target→simulasi→konfirmasi aktual→dashboard selesai; tidak ada import GDE wajib, panggilan API kampus atau angka fake | P0 |
| DDP-T-09 | AUTH-FR-014/015: loopback, forbidden public bind, restart, export/reset/cancel | Public bind ditolak dalam demo mode; owner/data konsisten; export tanpa secret; reset terkonfirmasi saja; seed terpisah; DB/export runtime tidak dilacak Git | P0 |
| DDP-T-10 | UX-NFR dan forms: keyboard, 320 CSS px/zoom 200%, kontras, invalid bobot dan save failure | Aksi inti tetap tersedia, label/fokus/error jelas; tidak ada sukses palsu; hasil contrast dicatat, bukan diasumsikan dari screenshot | P0 |
| DDP-T-11 | P1 Schedule: 09–10 vs10–11 lalu 09.30–11;6+4+unknown jam;capacity 8/0/unknown;date-only | Tidak overlap/overlap 30 menit;10 jam, coverage 2/3,ratio 1,25 jikacapacity 8; denominator 0/unknown tidak dibagi;date-only tidak dipaksa 23.59 | P1 jika aktif |
| DDP-T-12 | P1 Vault: link allowed berizin, rights unknown, hostname palsu, user:pass URL, hidden resource pada search | Hanya metadata sah/published tampil; invalid/right-unknown ditahan; tidak fetch/proxy konten; hidden tidak bocor lewat count/snippet | P1 jika aktif |
| DDP-T-13 | MAP-BR-005: D memerlukan OR(A, E); scenario memilih jalur A, lalu tanpa pilihan jalur; availability unknown | Jalur A dipakai dengan banner asumsi; tanpa pilihan/availability cukup, earliest tetap unknown/bersyarat; engine tidak menganggap kedua alternatif OR wajib atau mengklaim jadwal optimal | P0 |

Untuk latency NFR, catat perangkat, OS, versi Python/dependency, build/commit, ukuran fixture, kondisi awal, definisi interval pengukuran dan 30 pengulangan; urutkan durasi dan gunakan nearest-rank p95 (observasi ke 29 dari 30). Target 100 course/300 assessment/1.000 metadata adalah benchmark sintetis terpisah dari demo, bukan cakupan data nyata. Catat hasil aktual/error; target belum terbukti saat ini.

## Risiko dan mitigasi

| ID | Risiko / peluang-dampak kualitatif | Mitigasi konkret | Trigger / fallback | Owner |
| --- | --- | --- | --- | --- |
| R-01 | Kapasitas aktual lebih kecil dari asumsi — tinggi/tinggi | Isi RV-14 dan cek progres engine 24 Nov; cadangan 25% | Jika kapasitas<84 jam-orang, revisi scope tercatat; P1 off | Semua anggota |
| R-02 | Tim belum memahami graph/tree/web — sedang/tinggi | Belajar pada fixture kecil, pair-review, teach-back; pilih konsep baru yang terbatas | Jika engine belum bekerja 24 Nov, hentikan enhancement dan utamakan core | A/B |
| R-03 | Konsep “baru” ternyata sudah diajarkan — sedang/tinggi | Bandingkan silabus/lab dan bimbingan Asdos; RV-15 | Pilih konsep lain yang berguna tanpa memperbesar scope; jangan klaim kebaruan tanpa bukti | Tim |
| R-04 | Salah prasyarat/nilai resmi — tinggi/tinggi bila memakai data nyata | Demo sintetis, source/provenance dan unknown policy | RV-02/03/04 open memblokir klaim resmi, bukan demo | Academic Curator |
| R-05 | Proyeksi menulis actual atau stale hasil — sedang/tinggi | Pisahkan overlays, revision checks dan golden integration tests | INT-T-003/010/013 wajib lulus sebelum demo | A/B/C |
| R-06 | Struktur BRP berubah sesudah skor dan merusak histori — sedang/tinggi | P0 lock struktur; migration P2 | Ubah skor boleh; edit struktur ditolak tanpa write | B |
| R-07 | Demo lokal keliru dipasang publik tanpa auth — sedang/tinggi | Guard mode/bind, fixtures sintetis, debug off, README batas | Kebutuhan multiuser memerlukan paket AUTH/operasi terverifikasi; jangan sekadar membuka port | C |
| R-08 | Link materi tanpa hak atau data personal masuk repo/video — sedang/tinggi | Rights gate, synthetic fixtures, review staged files/video, DB/export tidak tracked | Item tanpa bukti ditunda/hidden; gunakan screenshot/demo sintetis | Tim/Vault curator |
| R-09 | Kontribusi tertumpuk pada satu anggota atau tidak memahami modul lain — sedang/tinggi | Commit bermakna tiap anggota sejak awal, cross-review dan explain-back | Redistribusi tugas segera; bicarakan hambatan dengan Asdos sesuai panduan | Semua anggota |
| R-10 | P1 menghabiskan waktu video/testing — tinggi/tinggi | Gate 2 Des, satu paket maksimum, freeze 3–5 Des | Defect core atau buffer berkurang → P1 off | Product Lead |
| R-11 | Video>15 menit, upload/link gagal — sedang/tinggi | Target 14 menit, rekam 6–8 Des, cek durasi/akses, internal submit 9 Des | Edit/unggah ulang sebelum deadline; jangan mulai rekam 10 Des | Tim |
| R-12 | Klaim hasil riset/usability/score berlebihan — sedang/sedang | Pisahkan hipotesis, spesifikasi dan hasil; tulis batas | Tanpa bukti, tetap unknown/belum diuji | Product Lead |

Risiko integrasi SSO/SLCM, donor SNR, mapping career dan operasi komunitas tetap tercatat RV-05/06/07/09/10 tetapi tidak berada pada critical path P0. Tidak ada janji mendapatkan izin sebelum deadline.

## Repository dan pemahaman semua anggota

Rekomendasi struktur repository memisahkan domain, presentation, storage, tests, synthetic fixtures dan docs. README menjelaskan masalah, fitur aktif/future, arsitektur Python, versi/setup/run/test, contoh input/output, provenance data, batas model, anggota/kontribusi serta video. Simpan secrets, environment lokal, database runtime dan export di luar tracking. Fixture yang aman dapat dilacak dengan label sintetis. License/attribution dapat ditambahkan sesuai kepemilikan; panduan tidak mewajibkan lisensi tertentu.

Setiap anggota menulis kode atau test bermakna pada fungsi yang ditugaskan, melakukan commit dengan author benar, mereview modul lain, dan mampu menjelaskan seluruh codebase. Pair work diberi atribusi jujur; hindari satu unggahan akhir yang mengaburkan riwayat. Jangan memecah commit kosong untuk mengejar jumlah yang tidak diminta panduan. CI, issues dan pull requests berguna bila tim mampu, tetapi bukan kewajiban eksplisit dosen.

| Area teach-back | Bukti yang direkomendasikan untuk setiap anggota |
| --- | --- |
| MAP | Menelusuri AND/OR unknown, cycle rejection dan penundaan A→B→C |
| GRD | Menghitung manual K=36/required 78/what-if81, membedakan actual/prediction dan menjelaskan precision |
| Data/state | Menjelaskan owner_scope, transaction/revision, scenario reset dan koreksi aktual |
| Presentation | Menelusuri form→Python service→view model→template; menunjukkan error/unknown/stale |
| Quality | Menjelaskan satu test gagal, memperbaiki bug kecil dan menjalankan fresh-clone |

Catatan teach-back adalah rekomendasi bukti DDP-04, bukan format pengumpulan baru. Bila memakai AI, setiap anggota tetap memeriksa dan memahami kode; simpan catatan bantuan/rujukan bila berguna. Penjelasan hafalan tanpa memahami aliran data tidak memenuhi tujuan pemahaman mendalam.

## Rencana video maksimum 15 menit

Target rekaman akhir **14 menit**, menyisakan 1 menit toleransi. Ini rekomendasi durasi segmen; batas resmi tetap 15 menit. Semua materi menggunakan versi repo final dan fixture sintetis. Narator dapat dibagi, tetapi panduan tidak mewajibkan setiap anggota tampil kamera.

| Timecode | Durasi | Isi / bukti |
| --- | --- | --- |
|00:00–01:30 |1:30 | Masalah pengguna, konteks dan batas bukti validasi |
|01:30–02:30 |1:00 | Nilai solusi dan scope core; Orbit independen, data demo |
|02:30–06:30 |4:00 | Demo Grade Rescue (target 75→78, impossible), Roadmap prasyarat/penundaan, Dashboard dan what-if yang tidak menulis actual |
|06:30–10:30 |4:00 | Arsitektur dan kode Python, graph/tree/math, persistensi/revision, keputusan desain |
|10:30–12:00 |1:30 | Konsep di luar kelas yang terverifikasi, test/edge cases dan hasil yang benar-benar dijalankan |
|12:00–13:00 |1:00 | Repository, cara run, struktur dan kontribusi anggota |
|13:00–14:00 |1:00 | Keterbatasan/policy unknown, fitur future, penutup |

Checklist video: seluruh tiga muatan resmi ada (latar belakang, demo, arsitektur/solusi), total≤15:00, teks/audio terbaca, tidak mengekspos nilai/credential nyata, fitur ditunda tidak diperagakan seolah selesai, link YouTube dapat diakses penilai. Tidak membuat video dalam tahap dokumentasi ini.

## Checklist kesiapan dan penutupan

Status `[x]` hanya untuk pekerjaan dokumen yang benar-benar selesai. `[ ]` adalah bukti/keputusan yang masih diperlukan, bukan request izin untuk menyelesaikan audit ini.

- [x] Panduan resmi seluruh 5 halaman dibaca, deadline/teknologi/tim/deliverables/rubrik dicatat dengan halaman sumber.
- [x]13 PRD dan governance baseline tersedia; seluruh ID lama dipertahankan; prioritas/AC/test/interface yang terdampak diselaraskan.
- [x] Lima laporan terpisah disusun; fitur future, changelog dan source register dipertahankan.
- [x] Python diberi tanggung jawab inti konkret; scope dan jadwal dianalisis dengan estimasi serta sensitivitas kapasitas.
- [ ] Daftar kelompok resmi, Asdos, jam efektif dan kemampuan tim dicatat (RV-14).
- [ ] Konsep yang di luar kelas dipilih dengan bukti silabus/lab/bimbingan (RV-15); masalah pengguna divalidasi secukupnya (RV-16).
- [ ] Runtime/dependencies dipilih dan fresh-clone environment berhasil pada perangkat anggota.
- [ ] Fixture demo kecil, label sumber, policy dan boundary input direview A/B; tidak ada data pribadi nyata.
- [ ] Core Python/SQLite/Flask dan UI diterapkan; semua FR P0 serta NFR aktif dibuktikan, bukan hanya dispesifikasikan.
- [ ] Test primer, tambahan dan integrasi aktif dijalankan; build/environment/actual/evidence/defect dicatat.
- [ ] Review keyboard/responsif/contrast dan target latency dilakukan; hasil belum dianggap PASS sebelumnya.
- [ ] P1 hanya diaktifkan bila gate 2 Des lolos; dependency/rights tests terkait ikut dijalankan.
- [ ] Seluruh anggota mempunyai kontribusi GitHub aktif dan lulus teach-back seluruh bagian kode.
- [ ] Repository GitHub publik memuat source final dan README reproduksi; akses dari sesi tanpa hak privat diperiksa.
- [ ] Video YouTube final≤15 menit mencakup masalah/demo/arsitektur, audio dan akses tautan diperiksa.
- [ ] Kedua tautan dikumpulkan melalui kanal pengajar; bukti waktu≤10 Des 2026 23.59 WIB disimpan.

**Tidak ada klaim siap produksi:** data akademik nyata/SSO/SLCM/komunitas membutuhkan keputusan serta bukti tambahan sesuai RV masing-masing. Hambatan itu tidak dijadikan alasan menunda dokumentasi atau demo sintetis yang telah direncanakan.

## Handoff v0.2.1 — scope awal yang diizinkan

Status **CONDITIONAL GO untuk desain arsitektur**, bukan MVP final atau bukti siap implementasi penuh. Sebelum komitmen delivery, lengkapi kapasitas nyata anggota (RV-14), konsep yang benar-benar di luar kelas (RV-15), dan bukti runtime/stack dapat dijalankan pada perangkat tim. Estimasi 84–100 jam-orang adalah estimasi paket; perlu dipecah menurut pekerjaan implementasi/FR dan diestimasi ulang setelah spike yang kelak diotorisasi. Audit/errata ini tidak mengerjakan spike atau kode aplikasi.

Default handoff: hanya 48 FR P0 beserta BR/NFR/AC/test untuk kemampuan yang aktif. Semua P1/P2 nonaktif; subkemampuan future dalam FR P0 campuran (misalnya rebase penuh MAP-FR-006) juga nonaktif. Lolos gate kapasitas tidak otomatis mengaktifkan fitur: catat keputusan scope, ID yang diaktifkan, dependensi dan test, lalu perbarui capability manifest. Jangan menambahkan fitur dari journey produk lengkap atau mockup Figma sebagai P0 tersirat.

Desain arsitektur berikutnya dapat merinci monolit Python modular, rencana file per file, kontrak data/revision dan test plan. IPS/IPK/tren tetap P1; Senior Playbook, Career Navigator, full closeout dan dark mode tetap P2. Dashboard P0 memakai hasil MAP/GRD yang benar-benar dihitung atau unknown/unavailable; tidak mengisi kartu IPK/tren/insight dengan data ilustrasi seolah hasil nyata. Roadmap dapat memakai tema terang dan list accessible sesuai baseline; identitas visual Orbit tetap.

Rincian koreksi dan bukti penutupan ada di [PRD-v0.2.1-ERRATA.md](PRD-v0.2.1-ERRATA.md).
