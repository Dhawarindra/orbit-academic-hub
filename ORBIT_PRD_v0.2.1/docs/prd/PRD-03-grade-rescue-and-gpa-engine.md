# PRD-03 — Grade Rescue, BRP Tracker & IPS/IPK Engine

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-03 / v0.2 DDP1 Draft |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Product Owner Grade / Calculation Reviewer |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | Model P0 mendukung penilaian berbobot linear bertingkat; aturan kurva, drop-lowest, bonus dan nilai minimum komponen perlu rule khusus atau dinyatakan unsupported. Semua fixture berikut sintetis. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). |

## 2. Executive Summary & Problem

Grade Rescue membantu pengguna memahami kontribusi nilai yang sudah diketahui dan usaha yang masih dibutuhkan. Skor kosong bukan nol. Proyeksi tidak menjadi nilai final dan target huruf tidak dapat dikonversi tanpa policy yang cocok. IPS/IPK dihitung dari himpunan attempt yang dipilih oleh aturan inklusi terverifikasi atau asumsi simulasi yang dinyatakan.

## 3. Goals, Non-Goals & Success Metrics

Perhitungan dapat direproduksi, unknown terlihat, dan hasil mustahil dijelaskan dengan angka serta asumsi.

**Non-goals:** Memprediksi keputusan dosen, membenarkan grade resmi, atau menerapkan satu threshold universal pada semua offering.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Kebenaran matematis | Golden fixtures bobot, target, GPA dan boundary | 100% golden tests lulus |
| Pemisahan status | Perubahan skenario vs actual final | Nol mutasi silang |
| Keterjelasan hasil | Peserta menjelaskan achieved points vs average observed | Usulan ≥4/5 peserta setelah prototipe |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Mahasiswa dengan BRP parsial, nilai kuis/lab berulang, target akhir, atau course mengulang. Reviewer perhitungan meninjau aturan tanpa akses nilai nyata.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Student | Konfigurasi BRP personal, skor dan target sendiri | Mengedit nilai orang lain |
| Curator | Publish BRP template dengan scope dan sumber | Menetapkan hasil aktual mahasiswa |
| Moderator/guest | Tidak mengakses nilai personal | Membaca ekspor/riwayat privat |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| BRP linear bertingkat, known/unknown, bounds/target, what-if dan konfirmasi aktual per course | IPS/IPK dengan inclusion eksplisit dan guard missing/zero credit | Sensitivitas grid, perbandingan retake, migrasi struktur bernilai, model non-linear |

**Slice rilis:** BRP 20/30/50, leaf 10/10/30/50 → K=36, bounds 36–86, target 75 memerlukan 78, what-if UAS 90 menghasilkan 81. GPA boleh unavailable saat P1 off.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: BRP 20/30/50, leaf 10/10/30/50 → K=36, bounds 36–86, target 75 memerlukan 78, what-if UAS 90 menghasilkan 81. GPA boleh unavailable saat P1 off. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Matkul aktif → konfigurasi BRP → pilih template yang cocok atau input manual → susun parent/subassessment → validasi total → isi skor. Jika total tidak valid, BRP disimpan sebagai draft dan kalkulasi final ditahan; pengguna bisa kembali memperbaiki.

**J2.** Target → pilih skor angka atau huruf dengan policy → lihat kebutuhan sisa dan batas maksimum → buka what-if → isi skor per assessment → simpan scenario. Reset mengembalikan input actual dan tidak menghapus skor nyata.

**J3.** Closeout → tinjau course, SKS, policy dan final grade yang dilaporkan → konfirmasi → pembaruan IPS/IPK serta roadmap. Jika ada attempt mengulang tanpa policy, tampilkan partial GPA dan alasan pengecualian.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| GRD-US-001 | As a student, I want menyusun BRP bertingkat, so that bobot kuis dan ujian tepat. | P0 | GRD-FR-001, GRD-FR-002, GRD-FR-003 |
| GRD-US-002 | As a student, I want menghitung target dengan data parsial, so that saya mengetahui ruang perbaikan. | P0 | GRD-FR-004, GRD-FR-005, GRD-FR-006, GRD-FR-007 |
| GRD-US-003 | As a student, I want menghitung IPS/IPK dan menyimpan hasil akhir, so that riwayat saya tetap konsisten. | P0 / P1 (per FR) | GRD-FR-008, GRD-FR-009, GRD-FR-010, GRD-FR-011 |
| GRD-US-004 | As a calculation reviewer, I want menguji domain numerik dan migrasi BRP, so that engine tidak menghasilkan kepastian palsu. | P0 / P1 / P2 (per FR) | GRD-FR-014, GRD-FR-015, GRD-FR-016, GRD-FR-017, GRD-FR-018, GRD-FR-019, GRD-FR-020 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GRD-FR-001 | P0 | Simpan BRP | Enrollment aktif milik user | offering, kelas, periode, sumber, parent/leaf | Buat BRPVersion scoped; P0 mengunci struktur setelah skor tersimpan dan menolak perubahan struktur tanpa menulis apa pun; preview migrasi tersimpan sebagai GRD-FR-020 P2 | BRP valid tersimpan; upaya mengganti struktur bernilai pada P0 ditolak, versi/skor lama tetap; P2 memakai mapping eksplisit | GRD-AC-001 |
| GRD-FR-002 | P0 | Validasi bobot | BRP draft | root 20/30/50 dan subkuis 50/50 | Validasi setiap sibling group berjumlah 100% setelah parsing basis point | Leaf efektif 10%,10%,30%,50%; root 99,99% ditolak | GRD-AC-002 |
| GRD-FR-003 | P0 | Input skor | Leaf dengan max_score >0 | skor kosong, 0, -1, 101 dari max 100 | Bedakan unknown dari nol; tolak di luar rentang | Kosong=unknown; 0=nilai sah; -1/101 ditolak | GRD-AC-003 |
| GRD-FR-004 | P0 | Hitung ringkasan | Bobot valid; Q1=80,Q2=100,UTS=60,UAS unknown | Leaf 0,1/0,1/0,3/0,5 | Hitung K, O, rentang dan rerata observed terpisah | K=36; O=0,5; rerata observed=72; rentang akhir 36–86 | GRD-AC-004 |
| GRD-FR-005 | P0 | Hitung target | Fixture GRD-FR-004 | T=75 | Hitung rerata sisa yang diperlukan memakai bobot unknown | UAS minimum=78; hasil dapat dicapai bersyarat | GRD-AC-005 |
| GRD-FR-006 | P0 | Hitung target mustahil | Fixture GRD-FR-004 | T=90 | Bandingkan target dengan maksimum feasible | Kebutuhan 108; maksimum akhir 86; label tidak tercapai dengan asumsi ini | GRD-AC-006 |
| GRD-FR-007 | P0 | Hitung target semua diketahui | Semua leaf actual dan K=75 | T=75 lalu T=80; sisa bobot 0 | Tangani penyebut nol lewat perbandingan hasil | T75 tercapai; T80 tidak tercapai; tidak ada division-by-zero | GRD-AC-007 |
| GRD-FR-008 | P1 | Hitung IPS berbobot | Policy inclusion eksplisit; data lengkap | A: 4 SKS, g=3,7; B: 3 SKS, g=3; C: 2 SKS, g=2 | Jumlahkan quality points dan bagi SKS included | 27,8/9=3,088888…; tampil 3,09 dengan label sesuai provenance | GRD-AC-008 |
| GRD-FR-009 | P1 | Hitung IPK dengan repeat | Dua attempt course sama; repeat rule unknown | A lama g=2, A baru g=3,7; masing-masing 4 SKS | Tahan satu angka IPK definitif sampai kebijakan inclusion dipilih | Tampilkan policy unknown dan daftar attempt; jangan pilih tertinggi otomatis | GRD-AC-009 |
| GRD-FR-010 | P0 | Konfirmasi final grade | Preview hasil aktual per course dan policy/provenance terlihat; GDE dinonaktifkan pada P0 | Hasil aktual yang dimasukkan eksplisit, source, revision dan alasan bila koreksi | Konfirmasi atau koreksi ActualFinalGrade per course, simpan revisi dan invalidasi MAP/dashboard; tolak preview stale; jangan menyalin Prediction otomatis | A yang dikonfirmasi lulus memperbarui MAP sebagai actual_user_reported; B unresolved tetap unknown; koreksi menyimpan revisi lama; nol contribution dan tidak memerlukan closeout | GRD-AC-010 |
| GRD-FR-011 | P0 | Simpan what-if | Scenario aktif | UAS asumsi=90 pada fixture | Hitung overlay tanpa menulis GradeEntry aktual | Proyeksi=81; UAS aktual tetap unknown; eligibility tidak berubah | GRD-AC-011 |
| GRD-FR-012 | P0 | Konversi target huruf | Belum ada policy cocok | Target A | Tahan konversi dan minta policy atau target angka eksplisit | Tidak mengasumsikan A=85; target angka tetap bisa digunakan | GRD-AC-012 |
| GRD-FR-013 | P2 | Buka sensitivitas | Fixture K=36 dan bobot UAS=0,5 | UAS 70,80,90 | Hitung proyeksi pada grid asumsi | Nilai akhir 71,76,81; setiap kenaikan 10 UAS memberi 5 poin | GRD-AC-013 |
| GRD-FR-014 | P0 | Hitung semua skor unknown | BRP linear valid | Seluruh earned=null | Kembalikan coverage nol dan bounds, tanpa rerata observed | K=0; O=0; bounds=0–100; observed average unavailable | GRD-AC-014 |
| GRD-FR-015 | P1 | Hitung GPA tanpa included credit | Policy valid, no included attempts | ΣSKS=0 | Kembalikan unavailable dengan alasan penyebut kosong | Tidak ada NaN, Infinity atau IPK 0 yang tampak aktual | GRD-AC-015 |
| GRD-FR-016 | P0 | Konversi pada batas policy | Policy sintetis: A≥85; B=70–<85; C<70 | 84,995 lalu 85 | Gunakan nilai presisi penuh sebelum format dua desimal | 84,995 tetap B walau display 85,00; 85 menjadi A; tampil precision note | GRD-AC-016 |
| GRD-FR-017 | P2 | Bandingkan kebijakan repeat di scenario | Fixture A lama 4×2; A baru 4×3,7; B3×3 | Policy latest-only lalu all-attempts secara eksplisit | Hitung keduanya sebagai scenario policy, bukan aturan UI | Latest-only 3,40; all-attempts 2,89; actual history sama | GRD-AC-017 |
| GRD-FR-018 | P0 | Validasi input numerik | BRP atau target sedang diedit | Bobot150/−50; skor NaN; target101; max_score0 | Tolak angka nonfinite, bobot di luar0–100, target di luar0–100 dan max≤0 | Tidak melakukan kalkulasi; pesan field spesifik dan draft valid lain dipertahankan | GRD-AC-018 |
| GRD-FR-019 | P1 | Gabungkan GPA antar term | Tidak ada course overlap dan inclusion eksplisit | History 30 SKS/96 points; term 10 SKS/35 points | Gunakan total quality points dan kredit, bukan rata-rata dua GPA | 131/40=3,275; display 3,28; label proyeksi bila term masih prediksi | GRD-AC-019 |
| GRD-FR-020 | P2 | Ubah struktur BRP bernilai | Q1=80 pada BRP v1 | Template v2 menghapus Q1 dan menambah Lab 1 | Minta mapping eksplisit atau simpan score lama sebagai history tanpa assignment baru | Lab 1 tetap unknown; Q1 lama tidak hilang dan tidak pindah otomatis | GRD-AC-020 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| GRD-BR-001 | Bobot input finite pada rentang 0–100%, maksimal 2 desimal persen, disimpan konseptual sebagai basis point. Setiap sibling group aktif harus tepat 10.000 bp. Parent tanpa distribusi anak tidak dibagi rata diam-diam. | GRD-FR-001, GRD-FR-002, GRD-FR-018 |
| GRD-BR-002 | Effective leaf weight = produk proporsi sepanjang ancestry. Hanya leaf dihitung; parent tidak ditambah lagi. Tree tidak boleh cycle atau leaf memiliki dua parent. | GRD-FR-002 |
| GRD-BR-003 | Normalisasi score = 100 × earned/max; max finite >0. Unknown tidak disubstitusi nol; skor finite pada 0–max dan target numerik finite pada 0–100. Missing/absent hanya menjadi nol jika user mencatat hasil nol sesuai rule dan provenance. | GRD-FR-003, GRD-FR-004, GRD-FR-014, GRD-FR-018 |
| GRD-BR-004 | K=Σ_known wᵢsᵢ; O=Σ_known wᵢ; U=1−O. Untuk sisa 0–100 tanpa syarat lain, bounds=[K,K+100U]. Observed average=K/O bila O>0, bukan prediksi final. | GRD-FR-004, GRD-FR-014 |
| GRD-BR-005 | Untuk T dan U>0, required=(T−K)/U. Required≤0 berarti sudah memenuhi target numerik pada model; 0<required≤100 berarti feasible bersyarat; >100 mustahil pada model. U=0 gunakan perbandingan K vs T. | GRD-FR-005, GRD-FR-006, GRD-FR-007 |
| GRD-BR-006 | Jika ada minimum komponen atau aturan non-linear belum didukung, jangan memberi kesimpulan kelulusan dari model linear. Beri numeric-only dan unresolved rule. Unknown conversion menahan target huruf. | GRD-FR-012, GRD-FR-006 |
| GRD-BR-007 | Nilai tampilan 2 desimal round-half-up; kalkulasi dan threshold memakai presisi penuh. Kebutuhan target dibulatkan ke atas sesuai granularitas skor, bukan half-up agar tidak menurunkan syarat. | GRD-FR-005, GRD-FR-008, GRD-FR-016 |
| GRD-BR-008 | GPA=Σ(SKS×grade_point)/ΣSKS pada included attempts. Penyebut 0 → unavailable, bukan 0. Missing grade/credit/policy → partial result berlabel dan daftar excluded; bukan IPS/IPK lengkap. | GRD-FR-008, GRD-FR-009, GRD-FR-015, GRD-FR-019 |
| GRD-BR-009 | Setiap attempt tetap tersimpan. Repeat/inclusion/status special harus policy-bound; tidak memilih highest/latest untuk GPA tanpa binding yang eksplisit. Policy sintetis boleh dipakai di scenario. | GRD-FR-009, GRD-FR-017 |
| GRD-BR-010 | Actual final berbeda dari skor komponen dan proyeksi. Input manual ber-provenance user_reported; fixture demo tetap berlabel sintetis. P0 memakai preview/konfirmasi atau koreksi per course, source revision dan alasan koreksi; histori lama tersimpan. P2 yang sudah dalam snapshot closeout memakai reopen sebelum koreksi. | GRD-FR-010, GRD-FR-011 |
| GRD-BR-011 | BRP template tidak otomatis cocok antar kelas/periode. Mismatch menawarkan copy sebagai personal draft, bukan klaim verified. | GRD-FR-001, GRD-FR-012, GRD-FR-020 |

### Contoh perhitungan sintetis

BRP: Kuis 20% berisi Q1 dan Q2 masing-masing 50%; UTS 30%; UAS 50%. Leaf weights=(0,10;0,10;0,30;0,50). Q1=80, Q2=100, UTS=60 memberi K=8+10+18=36. Bobot diketahui=0,50; rata-rata komponen yang sudah diketahui=72. Itu bukan nilai akhir 72. Batas nilai akhir adalah 36 sampai 86. Untuk T=75: (75−36)/0,50=78. Untuk T=90: 108, sehingga tidak feasible. Asumsi UAS=90 menghasilkan 81.

Jika target=75,01 maka kebutuhan UAS=78,02 pada skor bergranularitas 0,01; bila skor ujian hanya bilangan bulat, kebutuhan tampil 79. Dengan semua skor unknown, K=0, O=0, bounds=0–100 dan observed average unavailable. Bila aturan mewajibkan UAS minimal 50, rentang numerik tidak cukup untuk menyatakan lulus.

**IPK sintetis dengan rule yang dipilih eksplisit:** riwayat included memiliki 30 SKS dan 96 quality points; semester baru 10 SKS dan 35 quality points, tanpa course overlap. Proyeksi kumulatif=131/40=3,275 → 3,28. Jika hanya rata-rata 3,20 tersedia tanpa kredit included, tidak dapat digabung. Jika IPK historis sudah dibulatkan, quality points rekonstruksi juga berlabel estimasi.

**Pengulangan sintetis:** A lama 4 SKS×2, A baru 4×3,7, B 3×3. Policy latest-only memberi 23,8/7=3,40; policy all-attempts memberi 31,8/11≈2,89. Keduanya ilustrasi pilihan kebijakan, bukan klaim aturan UI.

**Urutan engine:** periksa izin dan scenario → validasi scope/revision BRP → flatten leaf weights → normalize scores → hitung known/unknown → evaluasi bounds dan target → terapkan conversion policy bila tersedia → hitung GPA menggunakan included attempts → simpan provenance hasil turunan.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| BRPVersion / brp_version_id | offering_id, source, rule type, revision, verification | Student/curator | draft → valid → superseded; version immutable | Private/template public |
| Assessment / assessment_id | parent_id, local weight bp, max_score, topic_id optional, due_at nullable | GRD owns; SCH references due_at | Revisi deadline event; mapping saat BRP change | Private |
| GradeEntry / entry_id | enrollment_id, assessment_id, earned, status unknown/actual_input, provenance | Student | Revisi audit; unknown ≠ 0 | Private |
| ActualFinalGrade / final_id | attempt, letter/point/pass, source_status, policy_version | Student / future authorized source | draft → confirmed → corrected | Private |
| GradePrediction / prediction_id | input revisions, K/O/U, bounds, target, scenario_id | Engine turunan | stale dan recomputable | Private |
| GradePolicy / policy_id | scope, conversion, inclusion, repeats, special grades, sources | Academic Curator | draft/verified_active/superseded | Public config |
| Target / target_id | owner, offering/term scope, numeric/letter, policy_ref | Student | Independent from graduation rule | Private |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

BRP editor berupa tree sederhana dengan total bobot per parent, tambah assessment dan preview leaf efektif. Tracker menampilkan kolom skor diperoleh/max, bobot, status, deadline dan sumber. Kosong menampilkan “Belum ada nilai”, nol menampilkan 0. Ringkasan memisahkan “Kontribusi diketahui: 36 poin”, “Bobot dinilai: 50%”, “Rentang akhir: 36–86”. Target card memuat asumsi dan tombol buka skenario. Dialog finalisasi meminta hasil aktual, bukan menyalin prediksi. Policy link membuka aturan yang benar-benar dipakai. Grafik menyediakan tabel; mobile memakai baris assessment yang dapat dibuka tanpa kehilangan label.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| Invalid weights | Simpan draft, hitung ditahan | Tunjukkan sibling group penyebab |
| Unknown score | Coverage berkurang | Tidak isi nol |
| Impossible target | Tampilkan batas maksimum dan opsi ubah target | Tidak menyalahkan pengguna |
| Unknown letter policy | Target angka masih tersedia | Jangan infer A/kelulusan |
| Zero included SKS | GPA unavailable | Tidak NaN atau nol semu |
| Version mismatch | Preview migration diperlukan | Nilai lama tetap di versi lama |
| Special grade/repeat unresolved | Partial GPA dan exclusions | Tidak mengubah eligibility otomatis |
| Unauthorized / failed save | Tolak / pertahankan draft lokal sementara | Tidak emit event sukses |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** P0 GRD-FR-010 menerima konfirmasi per course secara langsung dan mengirim revisi ke MAP/UX. Trigger GDE closeout tetap P2; GPA summary hanya bila P1 aktif. Perubahan struktur setelah skor tersimpan ditolak P0; migrasi GRD-FR-020 P2. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| PRO-FR-004 → GRD-FR-001 | Enrollment dan offering → BRP scope | Personal draft jika template tidak cocok |
| GRD-FR-001 → SCH-FR-001 | AssessmentDueChanged memakai assessment_id canon | SCH tidak membuat clone assessment |
| GRD-FR-010 → MAP-FR-002/GDE-FR-006 | ActualFinalGradeChanged dengan final_id/revision | Consumer menghitung ulang; duplicate event diabaikan |
| GRD-FR-004 → GDE-FR-001/UX-FR-002 | ProjectionChanged berisi uncertainty dan rule_version | Unknown tidak diperlakukan gagal |
| GRD-FR-010 → SNR-FR-001 | Hanya preview contribution atas aksi user | Tidak ada silent sync grade privat |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Seluruh raw grade privat. Ekspor tidak dibagi secara otomatis. Template BRP publik tidak berisi hasil peserta. Debug numeric memakai fixture sintetis; logs tidak merekam angka nilai mahasiswa.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| GRD-NFR-001 | P0 | Golden numeric output harus konsisten lintas tampilan hingga presisi 0,000001 sebelum format. | GRD-AC-101 |
| GRD-NFR-002 | P0 | Hitung ulang 300 leaf p95 ≤200 ms setelah input tervalidasi. | GRD-AC-102 |
| GRD-NFR-003 | P0 | Kegagalan simpan tidak menghapus input; retry dengan identitas operasi sama tidak menghasilkan duplikasi. | GRD-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| GRD-AC-001 | Given Enrollment aktif milik user; offering, kelas, periode, sumber, parent/leaf | When Simpan BRP | Then BRP valid tersimpan; upaya mengganti struktur bernilai pada P0 ditolak, versi/skor lama tetap; P2 memakai mapping eksplisit | GRD-FR-001 |
| GRD-AC-002 | Given BRP draft; root 20/30/50 dan subkuis 50/50 | When Validasi bobot | Then Leaf efektif 10%,10%,30%,50%; root 99,99% ditolak | GRD-FR-002 |
| GRD-AC-003 | Given Leaf dengan max_score >0; skor kosong, 0, -1, 101 dari max 100 | When Input skor | Then Kosong=unknown; 0=nilai sah; -1/101 ditolak | GRD-FR-003 |
| GRD-AC-004 | Given Bobot valid; Q1=80,Q2=100,UTS=60,UAS unknown; Leaf 0,1/0,1/0,3/0,5 | When Hitung ringkasan | Then K=36; O=0,5; rerata observed=72; rentang akhir 36–86 | GRD-FR-004 |
| GRD-AC-005 | Given Fixture GRD-FR-004; T=75 | When Hitung target | Then UAS minimum=78; hasil dapat dicapai bersyarat | GRD-FR-005 |
| GRD-AC-006 | Given Fixture GRD-FR-004; T=90 | When Hitung target mustahil | Then Kebutuhan 108; maksimum akhir 86; label tidak tercapai dengan asumsi ini | GRD-FR-006 |
| GRD-AC-007 | Given Semua leaf actual dan K=75; T=75 lalu T=80; sisa bobot 0 | When Hitung target semua diketahui | Then T75 tercapai; T80 tidak tercapai; tidak ada division-by-zero | GRD-FR-007 |
| GRD-AC-008 | Given Policy inclusion eksplisit; data lengkap; A:4 SKS,g=3,7; B:3 SKS,g=3; C:2 SKS,g=2 | When Hitung IPS berbobot | Then 27,8/9=3,088888…; tampil 3,09 dengan label sesuai provenance | GRD-FR-008 |
| GRD-AC-009 | Given Dua attempt course sama; repeat rule unknown; A lama g=2, A baru g=3,7; masing-masing 4 SKS | When Hitung IPK dengan repeat | Then Tampilkan policy unknown dan daftar attempt; jangan pilih tertinggi otomatis | GRD-FR-009 |
| GRD-AC-010 | Given Preview hasil aktual per course dan policy/provenance terlihat; GDE dinonaktifkan pada P0; Hasil aktual yang dimasukkan eksplisit, source, revision dan alasan bila koreksi | When Konfirmasi final grade | Then A yang dikonfirmasi lulus memperbarui MAP sebagai actual_user_reported; B unresolved tetap unknown; koreksi menyimpan revisi lama; nol contribution dan tidak memerlukan closeout | GRD-FR-010 |
| GRD-AC-011 | Given Scenario aktif; UAS asumsi=90 pada fixture | When Simpan what-if | Then Proyeksi=81; UAS aktual tetap unknown; eligibility tidak berubah | GRD-FR-011 |
| GRD-AC-012 | Given Belum ada policy cocok; Target A | When Konversi target huruf | Then Tidak mengasumsikan A=85; target angka tetap bisa digunakan | GRD-FR-012 |
| GRD-AC-013 | Given Fixture K=36 dan bobot UAS=0,5; UAS 70,80,90 | When Buka sensitivitas | Then Nilai akhir 71,76,81; setiap kenaikan 10 UAS memberi 5 poin | GRD-FR-013 |
| GRD-AC-014 | Given BRP linear valid; Seluruh earned=null | When Hitung semua skor unknown | Then K=0; O=0; bounds=0–100; observed average unavailable | GRD-FR-014 |
| GRD-AC-015 | Given Policy valid, no included attempts; ΣSKS=0 | When Hitung GPA tanpa included credit | Then Tidak ada NaN, Infinity atau IPK 0 yang tampak aktual | GRD-FR-015 |
| GRD-AC-016 | Given Policy sintetis: A≥85; B=70–<85; C<70; 84,995 lalu 85 | When Konversi pada batas policy | Then 84,995 tetap B walau display 85,00; 85 menjadi A; tampil precision note | GRD-FR-016 |
| GRD-AC-017 | Given Fixture A lama4×2; A baru4×3,7; B3×3; Policy latest-only lalu all-attempts secara eksplisit | When Bandingkan kebijakan repeat di scenario | Then Latest-only 3,40; all-attempts 2,89; actual history sama | GRD-FR-017 |
| GRD-AC-018 | Given BRP atau target sedang diedit; Bobot150/−50; skor NaN; target101; max_score0 | When Validasi input numerik | Then Tidak melakukan kalkulasi; pesan field spesifik dan draft valid lain dipertahankan | GRD-FR-018 |
| GRD-AC-019 | Given Tidak ada course overlap dan inclusion eksplisit; History30 SKS/96points; term10 SKS/35points | When Gabungkan GPA antar term | Then 131/40=3,275; display3,28; label proyeksi bila term masih prediksi | GRD-FR-019 |
| GRD-AC-020 | Given Q1=80 pada BRP v1; Template v2 menghapus Q1 dan menambah Lab1 | When Ubah struktur BRP bernilai | Then Lab1 tetap unknown; Q1 lama tidak hilang dan tidak pindah otomatis | GRD-FR-020 |
| GRD-AC-101 | Given Fixture pada bagian 9 | When Bandingkan tracker, simulator dan dashboard | Then K=36, bounds=36–86, required=78 dan preview 81 pada semua tampilan | GRD-NFR-001 |
| GRD-AC-102 | Given 300 assessment leaf dengan scope valid | When Hitung 30 kali | Then p95 ≤200 ms dan output deterministik | GRD-NFR-002 |
| GRD-AC-103 | Given Form valid dan gangguan koneksi sebelum konfirmasi simpan | When Simpan, pulihkan koneksi, lalu retry | Then Input tetap terlihat; tepat satu revisi tersimpan dan indikator sukses hanya setelah konfirmasi | GRD-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| GRD-T-001 | fungsional | Enrollment aktif milik user; offering, kelas, periode, sumber, parent/leaf | Simpan BRP | BRP valid tersimpan; upaya mengganti struktur bernilai pada P0 ditolak, versi/skor lama tetap; P2 memakai mapping eksplisit | P0 | GRD-FR-001 / GRD-AC-001 |
| GRD-T-002 | boundary | BRP draft; root 20/30/50 dan subkuis 50/50 | Validasi bobot | Leaf efektif 10%,10%,30%,50%; root 99,99% ditolak | P0 | GRD-FR-002 / GRD-AC-002 |
| GRD-T-003 | boundary | Leaf dengan max_score >0; skor kosong, 0, -1, 101 dari max 100 | Input skor | Kosong=unknown; 0=nilai sah; -1/101 ditolak | P0 | GRD-FR-003 / GRD-AC-003 |
| GRD-T-004 | numerik | Bobot valid; Q1=80,Q2=100,UTS=60,UAS unknown; Leaf 0,1/0,1/0,3/0,5 | Hitung ringkasan | K=36; O=0,5; rerata observed=72; rentang akhir 36–86 | P0 | GRD-FR-004 / GRD-AC-004 |
| GRD-T-005 | numerik | Fixture GRD-FR-004; T=75 | Hitung target | UAS minimum=78; hasil dapat dicapai bersyarat | P0 | GRD-FR-005 / GRD-AC-005 |
| GRD-T-006 | boundary | Fixture GRD-FR-004; T=90 | Hitung target mustahil | Kebutuhan 108; maksimum akhir 86; label tidak tercapai dengan asumsi ini | P0 | GRD-FR-006 / GRD-AC-006 |
| GRD-T-007 | boundary | Semua leaf actual dan K=75; T=75 lalu T=80; sisa bobot 0 | Hitung target semua diketahui | T75 tercapai; T80 tidak tercapai; tidak ada division-by-zero | P0 | GRD-FR-007 / GRD-AC-007 |
| GRD-T-008 | numerik | Policy inclusion eksplisit; data lengkap; A: 4 SKS, g=3,7; B: 3 SKS, g=3; C: 2 SKS, g=2 | Hitung IPS berbobot | 27,8/9=3,088888…; tampil 3,09 dengan label sesuai provenance | P1 | GRD-FR-008 / GRD-AC-008 |
| GRD-T-009 | negatif | Dua attempt course sama; repeat rule unknown; A lama g=2, A baru g=3,7; masing-masing 4 SKS | Hitung IPK dengan repeat | Tampilkan policy unknown dan daftar attempt; jangan pilih tertinggi otomatis | P1 | GRD-FR-009 / GRD-AC-009 |
| GRD-T-010 | integrasi | Preview hasil aktual per course dan policy/provenance terlihat; GDE dinonaktifkan pada P0; Hasil aktual yang dimasukkan eksplisit, source, revision dan alasan bila koreksi | Konfirmasi final grade | A yang dikonfirmasi lulus memperbarui MAP sebagai actual_user_reported; B unresolved tetap unknown; koreksi menyimpan revisi lama; nol contribution dan tidak memerlukan closeout | P0 | GRD-FR-010 / GRD-AC-010 |
| GRD-T-011 | integrasi | Scenario aktif; UAS asumsi=90 pada fixture | Simpan what-if | Proyeksi=81; UAS aktual tetap unknown; eligibility tidak berubah | P0 | GRD-FR-011 / GRD-AC-011 |
| GRD-T-012 | negatif | Belum ada policy cocok; Target A | Konversi target huruf | Tidak mengasumsikan A=85; target angka tetap bisa digunakan | P0 | GRD-FR-012 / GRD-AC-012 |
| GRD-T-013 | numerik | Fixture K=36 dan bobot UAS=0,5; UAS 70,80,90 | Buka sensitivitas | Nilai akhir 71,76,81; setiap kenaikan 10 UAS memberi 5 poin | P2 | GRD-FR-013 / GRD-AC-013 |
| GRD-T-014 | boundary | BRP linear valid; Seluruh earned=null | Hitung semua skor unknown | K=0; O=0; bounds=0–100; observed average unavailable | P0 | GRD-FR-014 / GRD-AC-014 |
| GRD-T-015 | boundary | Policy valid, no included attempts; ΣSKS=0 | Hitung GPA tanpa included credit | Tidak ada NaN, Infinity atau IPK 0 yang tampak aktual | P1 | GRD-FR-015 / GRD-AC-015 |
| GRD-T-016 | boundary | Policy sintetis: A≥85; B=70–<85; C<70; 84,995 lalu 85 | Konversi pada batas policy | 84,995 tetap B walau display 85,00; 85 menjadi A; tampil precision note | P0 | GRD-FR-016 / GRD-AC-016 |
| GRD-T-017 | numerik | Fixture A lama 4×2; A baru 4×3,7; B3×3; Policy latest-only lalu all-attempts secara eksplisit | Bandingkan kebijakan repeat di scenario | Latest-only 3,40; all-attempts 2,89; actual history sama | P2 | GRD-FR-017 / GRD-AC-017 |
| GRD-T-018 | negatif | BRP atau target sedang diedit; Bobot150/−50; skor NaN; target101; max_score0 | Validasi input numerik | Tidak melakukan kalkulasi; pesan field spesifik dan draft valid lain dipertahankan | P0 | GRD-FR-018 / GRD-AC-018 |
| GRD-T-019 | numerik | Tidak ada course overlap dan inclusion eksplisit; History 30 SKS/96 points; term 10 SKS/35 points | Gabungkan GPA antar term | 131/40=3,275; display 3,28; label proyeksi bila term masih prediksi | P1 | GRD-FR-019 / GRD-AC-019 |
| GRD-T-020 | integrasi | Q1=80 pada BRP v1; Template v2 menghapus Q1 dan menambah Lab 1 | Ubah struktur BRP bernilai | Lab 1 tetap unknown; Q1 lama tidak hilang dan tidak pindah otomatis | P2 | GRD-FR-020 / GRD-AC-020 |
| GRD-T-101 | nonfungsional | Fixture pada bagian 9 | Bandingkan tracker, simulator dan dashboard | K=36, bounds=36–86, required=78 dan preview 81 pada semua tampilan | P0 | GRD-NFR-001 / GRD-AC-101 |
| GRD-T-102 | nonfungsional | 300 assessment leaf dengan scope valid | Hitung 30 kali | p95 ≤200 ms dan output deterministik | P0 | GRD-NFR-002 / GRD-AC-102 |
| GRD-T-103 | nonfungsional | Form valid dan gangguan koneksi sebelum konfirmasi simpan | Simpan, pulihkan koneksi, lalu retry | Input tetap terlihat; tepat satu revisi tersimpan dan indikator sukses hanya setelah konfirmasi | P0 | GRD-NFR-003 / GRD-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| GRD-Q1 | BRP aktual belum diberikan | Model mungkin tidak linear | Draft manual; kurator validasi sebelum klaim |
| GRD-Q2 | Binding aturan GPA/special/repeat belum disahkan | IPK salah jika dipukul rata | Tampilkan partial; verifikasi SRC-04 dan pedoman operasional |
| GRD-Q3 | Input nilai salah | Guidance menyesatkan | Preview, audit dan provenance; tidak mengklaim resmi |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Tidak melakukan OCR transkrip, kurva grading, auto-drop lowest, bonus di atas maksimum, atau prediksi probabilistik pada P0. Fitur tersebut memerlukan policy dan test baru.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: GRD-FR-013, GRD-FR-017, GRD-FR-020. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-04: Pasal 38–41 diperiksa; fakta ringkas dibatasi di Research Register. Rumus dan semua angka bagian 9 adalah model/fixture produk, bukan data mahasiswa atau jaminan penerapan kebijakan UI. SRC-01 menentukan pemisahan actual vs what-if.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-06 pada audit untuk alasan revisi.

