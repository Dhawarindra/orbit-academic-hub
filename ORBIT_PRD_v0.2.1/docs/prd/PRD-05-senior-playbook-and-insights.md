# PRD-05 — Senior Playbook & Collective Academic Insights

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-05 / v0.2 DDP1 Draft |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Community Insights Owner / Privacy Reviewer |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | Tidak ada dataset kating nyata diberikan. Tips/empty state Playbook dan pipeline agregat P2 hanya boleh aktif setelah gate privasi dan kualitas siap. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). |

## 2. Executive Summary & Problem

Playbook membantu mahasiswa belajar dari pengalaman sukarela, tanpa menampilkan nilai individu. Angka agregat harus memiliki scope kompatibel dan ukuran sampel memadai. Kaitan topik membutuhkan kontribusi kesulitan topik atau mapping assessment yang diperiksa; nilai rendah sendiri tidak membuktikan topik sulit.

## 3. Goals, Non-Goals & Success Metrics

Menyediakan konteks yang relevan dengan limitations jelas serta penarikan consent yang benar-benar memengaruhi publikasi.

**Non-goals:** Ranking dosen/kelas, menghakimi mahasiswa, inferensi kemampuan individual, atau klaim populasi dari sampel self-selected.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Kepatuhan publication gate | Cell berukuran kecil dan consent ditarik | 100% disembunyikan sesuai policy |
| Kualitas cakupan | n, periode, BRP compatibility dan bias tampil pada insight | 100% insight angka |
| Voluntariness | Menolak kontribusi tidak membatasi fitur personal | 100% journey P0 |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Kating menyumbang data terbatas; mahasiswa membaca tips; moderator meninjau teks; Privacy Reviewer mengaktifkan analytics setelah review.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Guest/student | Tips published; agregat yang lolos gate | Raw grade, donor identity, filter drill-down |
| Contributor | Preview, submit, edit/withdraw kontribusi sendiri | Membaca raw kontribusi pengguna lain |
| Moderator | Review teks dan metadata kualitas | Melihat raw nilai personal workspace |
| Aggregation service role | Proses data minimum yang disetujui | Mengekspor baris mentah ke UI komunitas |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Tidak ada; modul nonaktif | Tidak ada | Seluruh Senior Playbook, tips, kontribusi, agregat, suppression, withdrawal dan insight |

**Slice rilis:** Dokumentasi lengkap dipertahankan; tidak mencari donor atau membuat data komunitas nyata untuk demo DDP1. Empty state global cukup bila menu future ditampilkan.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Dokumentasi lengkap dipertahankan; tidak mencari donor atau membuat data komunitas nyata untuk demo DDP1. Empty state global cukup bila menu future ditampilkan. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Mahasiswa membuka course → Playbook → memilih scope kompatibel → membaca tips dan batas data. Jika belum cukup, lihat pesan data belum memadai dan tetap bisa ke Vault.

**J2.** P2: closeout → preview kontribusi → pilih skor dan/atau kesulitan topik dengan toggle terpisah → submit. Default semua off; melewati layar tidak membuat record raw.

**J3.** Kontributor → kontribusiku → tarik izin → ringkasan dampak → konfirmasi. Insight terkait segera disembunyikan sampai agregat aman dihitung ulang; akun dan nilai pribadi tetap dapat digunakan.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| SNR-US-001 | As a student, I want membaca insight yang terukur, so that saya tidak mengikuti klaim palsu. | P2 | SNR-FR-004, SNR-FR-005, SNR-FR-006 |
| SNR-US-002 | As a contributor, I want memilih dan menarik kontribusi, so that kendali data tetap pada saya. | P2 | SNR-FR-001, SNR-FR-002, SNR-FR-007 |
| SNR-US-003 | As a moderator, I want mengkurasi tips tanpa identitas, so that pengalaman aman dibagikan. | P2 | SNR-FR-003, SNR-FR-008 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SNR-FR-001 | P2 | Submit kontribusi | Contributor memilih scope | Toggle skor off, topik on | Salin hanya payload topik yang dipilih dan consent version | Tidak ada GradeEntry mentah tersalin | SNR-AC-001 |
| SNR-FR-002 | P2 | Submit ulang | Kontribusi aktif sudah ada | user+offering+assessment+consent purpose sama | Upsert revisi kontribusi sendiri, bukan menambah sampel | Satu donor hanya dihitung satu pada cell yang sama | SNR-AC-002 |
| SNR-FR-003 | P2 | Terbitkan tips | Moderator telah review | Teks dengan nama mahasiswa dan nomor kontak | Minta redaksi data identitas sebelum publish | Teks sensitif tetap pending; versi teredaksi dapat terbit | SNR-AC-003 |
| SNR-FR-004 | P2 | Bangun agregat | Scope kompatibel dan consent aktif | 9 donor unik lalu 10 donor unik | Terapkan gate k=10 donor unik per published cell sebagai ambang awal produk | n9 disembunyikan; n10 hanya kandidat publikasi setelah guard lainnya lolos | SNR-AC-004 |
| SNR-FR-005 | P2 | Gabungkan cohort | Dua BRP berbeda tanpa compatibility mapping | Skor assessment bernama sama | Tolak pooling otomatis dan jelaskan mismatch | Tidak ada rata-rata gabungan | SNR-AC-005 |
| SNR-FR-006 | P2 | Buat topik insight | Skor rendah tanpa topic mapping | Course X memiliki skor assessment | Tahan klaim topik sulit sampai ada mapping/respon kesulitan topik | Tidak menyimpulkan rekursi sulit dari skor total course | SNR-AC-006 |
| SNR-FR-007 | P2 | Cabut consent | Agregat published dari 10 donor | Satu donor withdraw | Hide semua affected release sebelum recalc | Cell menjadi 9 donor dan tetap disembunyikan; raw terhapus menurut retention | SNR-AC-007 |
| SNR-FR-008 | P2 | Buka course tanpa data | Belum ada tips/agregat | course_id | Tampilkan empty state dan jalur cari resource | Tidak ada grafik atau angka contoh yang tampak sebagai data nyata | SNR-AC-008 |
| SNR-FR-009 | P2 | Lihat insight terbit | Semua gate lolos | Release aggregate | Tampilkan periode, n-band, denominator, BRP scope, selection-bias note dan tanggal | Interpretasi terbatas pada kontributor kompatibel, bukan seluruh mahasiswa | SNR-AC-009 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| SNR-BR-001 | Consent untuk skor, kesulitan topik dan atribusi adalah purpose terpisah. Copy kontribusi dilakukan atas tindakan eksplisit; tidak menyinkronkan perubahan nilai privat diam-diam. | SNR-FR-001, SNR-FR-007 |
| SNR-BR-002 | Dedup per contributor internal pseudonymous key dan cell; akun ganda belum dapat dieliminasi sempurna. Account local tidak membuktikan satu orang; review abuse dibutuhkan. | SNR-FR-002, SNR-FR-004 |
| SNR-BR-003 | Compatible cell wajib course+offering/compatibility group+BRP version+assessment/topic+periode. Nama assessment identik tidak membuktikan ekuivalensi. | SNR-FR-005 |
| SNR-BR-004 | k=10 donor unik adalah PRODUCT_ASSUMPTION awal, bukan jaminan anonimitas atau representativitas. Jika risiko identifikasi tetap tinggi, suppress walaupun k lolos. | SNR-FR-004, SNR-FR-009 |
| SNR-BR-005 | P2 hanya fixed non-overlapping cells tanpa filter cohort kecil, selisih total/subtotal, nilai min/max, ranking, atau time-series delta. Jika pembaca dapat menyimpulkan cell kecil lewat selisih, suppress pasangan/complement. | SNR-FR-004, SNR-FR-007 |
| SNR-BR-006 | Publikasi berupa batch release yang ditinjau privacy; n ditampilkan band 10–19/20–49/50+, skor rata-rata dibulatkan ke kelipatan 5. Persentase kesulitan memakai denominator responden topik, bukan seluruh peserta kelas. | SNR-FR-009, SNR-FR-004 |
| SNR-BR-007 | Teks kualitatif disunting untuk informasi pengenal; anekdot tunggal diberi label pengalaman satu kontributor dan tidak dinamai pola. Klaim topik memerlukan mapping/reported difficulty. | SNR-FR-003, SNR-FR-006 |
| SNR-BR-008 | Withdrawal segera menyembunyikan release terkait; raw dihapus ≤7 hari, backup sesuai AUTH. Sisa cell boleh terbit kembali hanya setelah review anti-differencing; salinan eksternal tidak dapat ditarik otomatis. | SNR-FR-007 |

**Fixture gate:** 10 donor yang kompatibel memberi skor [50,60,60,70,70,70,80,80,80,80], rerata 70. Tampilan kandidat: “rata-rata dibulatkan 70; 10–19 kontributor; offering/BRP/periode ini; partisipasi sukarela”. Itu tidak membuktikan rata-rata kelas. Jika donor ke-10 ditarik, release disembunyikan, bukan menampilkan n=9.

**Kesulitan topik:** 6 dari 10 responden topik melaporkan kesulitan pada rekursi. Proporsi internal 60%, publikasi hanya bila gate dan identifikasi lolos, dengan denominator responden topik. Jika 6 skor kuis rendah tanpa mapping topik, tidak membuat insight rekursi.

**Data bias:** sampel kecil, self-selection, recall dan beda BRP dicantumkan. Tidak ada nilai p, confidence interval atau klaim kausal tanpa desain analisis dan dasar data yang sesuai.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| Contribution / contribution_id | owner pseudonymous key, purpose, scoped payload, source revision, consent ref | Contributor / SNR | draft/pending/accepted/withdrawn | Restricted |
| TopicDifficulty / response_id | topic_id, offering, difficulty ordinal 1–5, optional redacted note | Contributor | Self-report; not inferred from total grade | Restricted |
| CompatibilityGroup / group_id | course/BRP mappings, rationale, reviewer | Curator | Draft → reviewed; versioned | Public rationale |
| AggregateRelease / release_id | fixed cell, n_band, rounded metrics, source set fingerprint, reviewed_at | Aggregation / Privacy Reviewer | draft/published/hidden/retracted | Public only when published |
| PlaybookTip / tip_id | redacted text, scope, attribution consent, source date | Moderator | pending/published/withdrawn | Public edited text |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Halaman Playbook memisahkan “Catatan pengalaman” dan “Ringkasan kontribusi”. Semua angka mempunyai badge scope dan penjelasan ukuran sampel. Tidak ada tooltip yang membocorkan angka mentah ter-suppress. Tombol kontribusi membuka preview field per purpose; tombol Lewati jelas. Halaman kontribusiku menampilkan izin aktif dan aksi Tarik kontribusi dengan akibat yang spesifik. Empty copy: “Belum cukup kontribusi yang sesuai untuk menampilkan ringkasan.”

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| No contributions | Empty state | Jangan generate angka |
| n<k | Insufficient data | Jangan bocorkan n tepat pada cell kecil |
| Version mismatch | Tidak digabung | Minta kurasi mapping |
| Duplicate | Update revisi | Sampel tidak bertambah |
| Withdrawn | Release tersembunyi | Recompute + privacy review |
| Identifying note | Pending redaction | Tidak publish mentah |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** Seluruh kontrak kontribusi, moderasi, consent dan agregat pada tabel berikut P2. Modul tidak menjadi provider wajib untuk Dashboard atau demo inti. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| GRD-FR-010/GDE-FR-008 → SNR-FR-001 | Preview selected data after opt-in | No automatic donation |
| AUTH-FR-006 → SNR-FR-007 | ConsentRevoked with purpose/revision | Hide cache before recalc; retry idempotent |
| SNR-FR-009 → GDE-FR-004 | Only published compatible aggregate/tip | No data → guidance personal-only |
| MAP-FR-001 → SNR-FR-005 | Versioned course/topic scope | Unsupported mapping excluded |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Pseudonymization raw bukan anonimisasi penuh. Pemisahan linkage identitas, fixed cells, suppression dan review tetap diperlukan. Jangan pernah menampilkan nilai individu atau memungkinkan moderator menelusuri grade personal dari tips. Jika pipeline tidak feasible untuk TA, matikan analytics dan kontribusi raw bersama-sama; curated tips tetap tersimpan sebagai P2.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| SNR-NFR-001 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | SNR-AC-101 |
| SNR-NFR-002 | P0 | Penarikan consent menghilangkan akses insight terkait pada pembacaan berikutnya. | SNR-AC-102 |
| SNR-NFR-003 | P0 | Seluruh suppression rules berlaku pada UI dan export. | SNR-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| SNR-AC-001 | Given Contributor memilih scope; Toggle skor off, topik on | When Submit kontribusi | Then Tidak ada GradeEntry mentah tersalin | SNR-FR-001 |
| SNR-AC-002 | Given Kontribusi aktif sudah ada; user+offering+assessment+consent purpose sama | When Submit ulang | Then Satu donor hanya dihitung satu pada cell yang sama | SNR-FR-002 |
| SNR-AC-003 | Given Moderator telah review; Teks dengan nama mahasiswa dan nomor kontak | When Terbitkan tips | Then Teks sensitif tetap pending; versi teredaksi dapat terbit | SNR-FR-003 |
| SNR-AC-004 | Given Scope kompatibel dan consent aktif; 9 donor unik lalu 10 donor unik | When Bangun agregat | Then n9 disembunyikan; n10 hanya kandidat publikasi setelah guard lainnya lolos | SNR-FR-004 |
| SNR-AC-005 | Given Dua BRP berbeda tanpa compatibility mapping; Skor assessment bernama sama | When Gabungkan cohort | Then Tidak ada rata-rata gabungan | SNR-FR-005 |
| SNR-AC-006 | Given Skor rendah tanpa topic mapping; Course X memiliki skor assessment | When Buat topik insight | Then Tidak menyimpulkan rekursi sulit dari skor total course | SNR-FR-006 |
| SNR-AC-007 | Given Agregat published dari 10 donor; Satu donor withdraw | When Cabut consent | Then Cell menjadi 9 donor dan tetap disembunyikan; raw terhapus menurut retention | SNR-FR-007 |
| SNR-AC-008 | Given Belum ada tips/agregat; course_id | When Buka course tanpa data | Then Tidak ada grafik atau angka contoh yang tampak sebagai data nyata | SNR-FR-008 |
| SNR-AC-009 | Given Semua gate lolos; Release aggregate | When Lihat insight terbit | Then Interpretasi terbatas pada kontributor kompatibel, bukan seluruh mahasiswa | SNR-FR-009 |
| SNR-AC-101 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | SNR-NFR-001 |
| SNR-AC-102 | Given Release published dan cache ada | When Withdraw lalu buka ulang insight | Then Release tidak dapat dibaca dari cache maupun search sebelum recalc | SNR-NFR-002 |
| SNR-AC-103 | Given Cell n9 dan complementary cell | When Buka halaman dan ekspor yang diizinkan | Then Tidak ada angka tersembunyi dalam payload, tooltip atau file | SNR-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| SNR-T-001 | privasi | Contributor memilih scope; Toggle skor off, topik on | Submit kontribusi | Tidak ada GradeEntry mentah tersalin | P2 | SNR-FR-001 / SNR-AC-001 |
| SNR-T-002 | boundary | Kontribusi aktif sudah ada; user+offering+assessment+consent purpose sama | Submit ulang | Satu donor hanya dihitung satu pada cell yang sama | P2 | SNR-FR-002 / SNR-AC-002 |
| SNR-T-003 | privasi | Moderator telah review; Teks dengan nama mahasiswa dan nomor kontak | Terbitkan tips | Teks sensitif tetap pending; versi teredaksi dapat terbit | P2 | SNR-FR-003 / SNR-AC-003 |
| SNR-T-004 | boundary | Scope kompatibel dan consent aktif; 9 donor unik lalu 10 donor unik | Bangun agregat | n9 disembunyikan; n10 hanya kandidat publikasi setelah guard lainnya lolos | P2 | SNR-FR-004 / SNR-AC-004 |
| SNR-T-005 | negatif | Dua BRP berbeda tanpa compatibility mapping; Skor assessment bernama sama | Gabungkan cohort | Tidak ada rata-rata gabungan | P2 | SNR-FR-005 / SNR-AC-005 |
| SNR-T-006 | negatif | Skor rendah tanpa topic mapping; Course X memiliki skor assessment | Buat topik insight | Tidak menyimpulkan rekursi sulit dari skor total course | P2 | SNR-FR-006 / SNR-AC-006 |
| SNR-T-007 | privasi | Agregat published dari 10 donor; Satu donor withdraw | Cabut consent | Cell menjadi 9 donor dan tetap disembunyikan; raw terhapus menurut retention | P2 | SNR-FR-007 / SNR-AC-007 |
| SNR-T-008 | edge | Belum ada tips/agregat; course_id | Buka course tanpa data | Tidak ada grafik atau angka contoh yang tampak sebagai data nyata | P2 | SNR-FR-008 / SNR-AC-008 |
| SNR-T-009 | fungsional | Semua gate lolos; Release aggregate | Lihat insight terbit | Interpretasi terbatas pada kontributor kompatibel, bukan seluruh mahasiswa | P2 | SNR-FR-009 / SNR-AC-009 |
| SNR-T-101 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | SNR-NFR-001 / SNR-AC-101 |
| SNR-T-102 | nonfungsional | Release published dan cache ada | Withdraw lalu buka ulang insight | Release tidak dapat dibaca dari cache maupun search sebelum recalc | P0 | SNR-NFR-002 / SNR-AC-102 |
| SNR-T-103 | nonfungsional | Cell n9 dan complementary cell | Buka halaman dan ekspor yang diizinkan | Tidak ada angka tersembunyi dalam payload, tooltip atau file | P0 | SNR-NFR-003 / SNR-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| SNR-Q1 | Threshold k bukan jaminan privasi | Reidentifikasi | Privacy Reviewer menyetujui release policy sebelum aktivasi P2 |
| SNR-Q2 | Akun ganda dan selection bias | Agregat tidak representatif | Deteksi duplikasi terbatas dan limitations |
| SNR-Q3 | Tidak ada kontributor nyata | Fitur kosong | Tips sah kurasi; jangan pakai synthetic sebagai live |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

ML, ranking dosen, open raw dataset, realtime aggregates dan drill-down bebas tidak masuk scope. Ekspansi analitik memerlukan review privasi baru.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: SNR-FR-001, SNR-FR-002, SNR-FR-003, SNR-FR-004, SNR-FR-005, SNR-FR-006, SNR-FR-007, SNR-FR-008, SNR-FR-009. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-01 brief; threshold k, batching, n-band dan rounding adalah PRODUCT_ASSUMPTION D-07, belum divalidasi empiris atau sebagai jaminan anonimisasi.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-08 pada audit untuk alasan revisi.

