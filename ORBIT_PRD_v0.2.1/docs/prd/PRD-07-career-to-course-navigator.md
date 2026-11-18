# PRD-07 — Career-to-Course / Competency Navigator

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-07 / v0.2 DDP1 Draft |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Competency Curator / Product Owner Navigator |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | P2; belum ada pemetaan kurasi aktual atau hasil validasi industri. Contoh jalur seluruhnya hipotetis. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). |

## 2. Executive Summary & Problem

Navigator menerjemahkan minat pengguna menjadi kompetensi yang dapat dipelajari dan mata kuliah yang relevan. Pemetaan harus menyebut alasan dan sumber; hubungan course-kompetensi tidak membuktikan pengguna telah menguasainya.

## 3. Goals, Non-Goals & Success Metrics

Pengguna dapat menelusuri alasan rekomendasi, melihat dependency akademik dan menyimpan alternatif tanpa terkunci ke satu karier.

**Non-goals:** Memprediksi pekerjaan/gaji, menilai bakat, memberi skor kecocokan personal seolah model tervalidasi, atau menjanjikan kompetensi otomatis.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Explainability | Setiap rekomendasi mempunyai mapping, alasan dan versi | 100% hasil |
| Keamanan eligibility | Rekomendasi terkunci menyertakan prasyarat | 100% fixture |
| Kendali minat | User bisa menghapus minat tanpa mengubah riwayat | 100% skenario |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Mahasiswa eksplorasi minat, mahasiswa dengan beberapa arah dan curator yang menyusun pemetaan dari sumber yang sah.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Guest | Lihat mapping published tanpa personalisasi | Minat pengguna lain |
| Student | Pilih minat dan rencana sendiri | Mengubah mapping global |
| Curator | Draft/review/publish mapping dengan sumber | Menyatakan kompetensi pengguna berdasarkan nilai |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Tidak ada; modul nonaktif | Tidak ada | Seluruh Career-to-Course / Competency Navigator |

**Slice rilis:** Mapping, ranking, rationale, alternatives dan acceptance tetap disimpan. Baru diaktifkan setelah sumber/mapping scope terverifikasi dan kapasitas tersedia.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Mapping, ranking, rationale, alternatives dan acceptance tetap disimpan. Baru diaktifkan setelah sumber/mapping scope terverifikasi dan kapasitas tersedia. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Menu Minat & Jalur → pilih sampai tiga minat → lihat kompetensi terkait → pilih course → baca alasan mapping dan provenance → buka Roadmap. Menghapus minat tidak menghapus course yang sudah disimpan dalam rencana.

**J2.** Course direkomendasikan tetapi prasyarat belum terpenuhi → lihat rantai pengantar → pilih alternatif fondasi atau simpan rencana bersyarat. Kembali ke Navigator mempertahankan filter.

**J3.** Curator menulis mapping → sertakan evidence, strength dan keterbatasan → reviewer approve → publish version. Scope kurikulum yang tidak cocok dikecualikan dari personalisasi.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| CAR-US-001 | As a student, I want mengeksplorasi beberapa minat, so that saya mendapat pilihan yang bisa dijelaskan. | P2 | CAR-FR-001, CAR-FR-002, CAR-FR-003 |
| CAR-US-002 | As a student, I want memeriksa prasyarat dan alternatif, so that rencana tetap realistis. | P2 | CAR-FR-004, CAR-FR-005, CAR-FR-006 |
| CAR-US-003 | As a curator, I want mengendalikan mutu mapping, so that hubungan course-kompetensi tidak mengada-ada. | P2 | CAR-FR-007, CAR-FR-008 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAR-FR-001 | P2 | Simpan minat | Akun aktif | 0–3 interest IDs | Simpan preferensi dan izinkan kosong | Tidak memilih minat tidak menghalangi modul personal | CAR-AC-001 |
| CAR-FR-002 | P2 | Minta rekomendasi | Mapping reviewed cocok kurikulum | Interest→competency→course | Kembalikan mapping published yang relevan beserta rationale | Tidak ada rekomendasi tanpa alasan/source_ref | CAR-AC-002 |
| CAR-FR-003 | P2 | Urutkan hasil | Dua course cocok | Coverage dan eligibility tags | Urutkan secara deterministik dengan aturan transparan | Tie diputus course code; tidak tampil probabilitas pekerjaan | CAR-AC-003 |
| CAR-FR-004 | P2 | Buka course rekomendasi | Course memiliki prerequisite | Eligibility unmet | Tampilkan prerequisite dan route ke roadmap tanpa auto-enroll | Course tetap unmet; CTA membuat scenario bersyarat | CAR-AC-004 |
| CAR-FR-005 | P2 | Lihat alternatif | Dua mapping mengarah kompetensi sama | Course A dan B; A offering unknown | Tampilkan keduanya dan batas ketersediaan | Bukan jaminan semester penawaran | CAR-AC-005 |
| CAR-FR-006 | P2 | Hapus minat | Scenario sudah berisi course | interest_id | Hapus preference dan refresh recommendations | Scenario dan actual grade tidak berubah | CAR-AC-006 |
| CAR-FR-007 | P2 | Publish mapping | Curator | Mapping tanpa bukti/rationale | Tolak publish sampai sumber dan batas klaim terisi | Mapping tetap draft | CAR-AC-007 |
| CAR-FR-008 | P2 | Buka navigator tanpa mapping | Kurikulum belum didukung | Interest valid | Tampilkan cakupan kosong dan katalog umum | Tidak menghasilkan course atau kompetensi palsu | CAR-AC-008 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| CAR-BR-001 | Interest, role karier, competency dan course adalah entitas berbeda. Satu role mempunyai banyak kompetensi; satu course bisa mendukung beberapa kompetensi dengan kekuatan kurasi. | CAR-FR-001, CAR-FR-002 |
| CAR-BR-002 | Mapping wajib source_ref, rationale, reviewer, curriculum_version dan level pengenalan/latihan/pendalaman yang merupakan label kurasi, bukan capaian mahasiswa. | CAR-FR-002, CAR-FR-007 |
| CAR-BR-003 | Ranking P2: jumlah kompetensi minat yang didukung, lalu eligibility met sebelum unknown/unmet, lalu kode course untuk tie. Tampilkan faktor tersebut, bukan skor kepribadian. | CAR-FR-003 |
| CAR-BR-004 | Eligibility dibaca dari MAP; rekomendasi tidak membuka prasyarat. Course yang sudah lulus dapat muncul sebagai latar belajar, bukan diusulkan untuk diambil ulang otomatis. | CAR-FR-004 |
| CAR-BR-005 | Source scope yang belum valid memblokir publish; mapping belum terbit tidak masuk pencarian atau guidance. | CAR-FR-007, CAR-FR-008 |
| CAR-BR-006 | Alternatif dan gaps menjelaskan kompetensi yang belum dicakup kurikulum; jangan menciptakan matkul baru untuk mengisi gap. | CAR-FR-005, CAR-FR-008 |

**Fixture hipotetis, bukan kurikulum UI:** minat “membangun produk digital” terkait kompetensi analisis kebutuhan dan pemodelan data. DEMO-A mendukung analisis kebutuhan; DEMO-B mendukung pemodelan data dan memerlukan DEMO-C. Jika C belum lulus, B tetap direkomendasikan sebagai relevan tetapi belum eligible; pengguna bisa menaruh C lebih dahulu di scenario.

**Tie:** course A dan B sama-sama mencakup dua kompetensi; A met dan B unmet → A tampil lebih dulu. Jika eligibility sama, urut kode course. Menyelesaikan A tidak otomatis menambah badge “kompeten”; Orbit hanya mencatat hubungan materi dan catatan studi.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| CareerInterest / interest_id | label, description; preference user↔interest | Curator/user | Published taxonomy / private selections | Public taxonomy, Private selection |
| Competency / competency_id | label, definition, source, version | Curator | draft/reviewed/published | Public |
| CompetencyCourseMapping / mapping_id | competency, course, curriculum, strength, rationale, reviewer | Curator | versioned; stale if source changes | Public published |
| NavigatorResult / result_id | owner, mapping version, eligibility revision, reasons | CAR turunan | recomputable/stale | Private |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Pilihan minat multi-select maksimal tiga untuk fokus UI, dapat diubah. Halaman hasil berisi kompetensi, course relevan, “Mengapa relevan”, prerequisite dan status sumber. Tidak ada progress bar kompetensi yang diisi otomatis dari nilai. Alternatif tampil sejajar dengan batas cakupan. Mobile menggunakan disclosure list; semua alasan tersedia tanpa hover.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| No interest | Pilih minat atau jelajah umum | Tidak memblokir dashboard |
| No mapping | Cakupan belum tersedia | Tidak fabricate |
| Locked prerequisite | Relevan tetapi belum eligible | Buka fondasi di MAP |
| Retired mapping | Perlu tinjau ulang | Tidak ubah scenario |
| Course unavailable | Penawaran belum pasti | Tampilkan alternatif |
| Unauthorized | Jangan memuat minat orang lain | Kembali ke akun sendiri |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** Seluruh jalur berikut P2; MAP/UX inti tidak menunggu mapping kompetensi. Data yang belum ada tetap unknown, bukan dibuat untuk demo. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| MAP-FR-001/002 → CAR-FR-004 | Catalog/eligibility version | Scope mismatch excluded |
| PRO-FR-007 → CAR-FR-001 | Private preference namespace | Tidak muncul sebagai credit publik |
| CAR-FR-002 → GDE-FR-002 | Optional interest rationale | GDE P0 berjalan tanpa CAR |
| CAR-FR-004 → MAP-FR-004 | AddToScenario intent | Preview; no actual enrollment |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Minat karier privat; tidak digunakan untuk iklan, pemeringkatan kemampuan atau memprediksi kondisi pribadi. Sumber publik mapping terpisah dari pilihan minat individual.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| CAR-NFR-001 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | CAR-AC-101 |
| CAR-NFR-002 | P0 | Tampilan utama p95 ≤2 detik setelah data tersedia pada beban uji dasar. | CAR-AC-102 |
| CAR-NFR-003 | P0 | Hasil deterministic pada snapshot input yang sama. | CAR-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| CAR-AC-001 | Given Akun aktif; 0–3 interest IDs | When Simpan minat | Then Tidak memilih minat tidak menghalangi modul personal | CAR-FR-001 |
| CAR-AC-002 | Given Mapping reviewed cocok kurikulum; Interest→competency→course | When Minta rekomendasi | Then Tidak ada rekomendasi tanpa alasan/source_ref | CAR-FR-002 |
| CAR-AC-003 | Given Dua course cocok; Coverage dan eligibility tags | When Urutkan hasil | Then Tie diputus course code; tidak tampil probabilitas pekerjaan | CAR-FR-003 |
| CAR-AC-004 | Given Course memiliki prerequisite; Eligibility unmet | When Buka course rekomendasi | Then Course tetap unmet; CTA membuat scenario bersyarat | CAR-FR-004 |
| CAR-AC-005 | Given Dua mapping mengarah kompetensi sama; Course A dan B; A offering unknown | When Lihat alternatif | Then Bukan jaminan semester penawaran | CAR-FR-005 |
| CAR-AC-006 | Given Scenario sudah berisi course; interest_id | When Hapus minat | Then Scenario dan actual grade tidak berubah | CAR-FR-006 |
| CAR-AC-007 | Given Curator; Mapping tanpa bukti/rationale | When Publish mapping | Then Mapping tetap draft | CAR-FR-007 |
| CAR-AC-008 | Given Kurikulum belum didukung; Interest valid | When Buka navigator tanpa mapping | Then Tidak menghasilkan course atau kompetensi palsu | CAR-FR-008 |
| CAR-AC-101 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | CAR-NFR-001 |
| CAR-AC-102 | Given Beban uji dasar dan data telah tersedia | When Buka tampilan utama 30 kali | Then p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | CAR-NFR-002 |
| CAR-AC-103 | Given Dua hasil tie dan mapping version sama | When Hitung ulang 30 kali | Then Urutan dan rationale identik; no random rank | CAR-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| CAR-T-001 | fungsional | Akun aktif; 0–3 interest IDs | Simpan minat | Tidak memilih minat tidak menghalangi modul personal | P2 | CAR-FR-001 / CAR-AC-001 |
| CAR-T-002 | fungsional | Mapping reviewed cocok kurikulum; Interest→competency→course | Minta rekomendasi | Tidak ada rekomendasi tanpa alasan/source_ref | P2 | CAR-FR-002 / CAR-AC-002 |
| CAR-T-003 | fungsional | Dua course cocok; Coverage dan eligibility tags | Urutkan hasil | Tie diputus course code; tidak tampil probabilitas pekerjaan | P2 | CAR-FR-003 / CAR-AC-003 |
| CAR-T-004 | integrasi | Course memiliki prerequisite; Eligibility unmet | Buka course rekomendasi | Course tetap unmet; CTA membuat scenario bersyarat | P2 | CAR-FR-004 / CAR-AC-004 |
| CAR-T-005 | fungsional | Dua mapping mengarah kompetensi sama; Course A dan B; A offering unknown | Lihat alternatif | Bukan jaminan semester penawaran | P2 | CAR-FR-005 / CAR-AC-005 |
| CAR-T-006 | negatif | Scenario sudah berisi course; interest_id | Hapus minat | Scenario dan actual grade tidak berubah | P2 | CAR-FR-006 / CAR-AC-006 |
| CAR-T-007 | negatif | Curator; Mapping tanpa bukti/rationale | Publish mapping | Mapping tetap draft | P2 | CAR-FR-007 / CAR-AC-007 |
| CAR-T-008 | edge | Kurikulum belum didukung; Interest valid | Buka navigator tanpa mapping | Tidak menghasilkan course atau kompetensi palsu | P2 | CAR-FR-008 / CAR-AC-008 |
| CAR-T-101 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | CAR-NFR-001 / CAR-AC-101 |
| CAR-T-102 | nonfungsional | Beban uji dasar dan data telah tersedia | Buka tampilan utama 30 kali | p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | P0 | CAR-NFR-002 / CAR-AC-102 |
| CAR-T-103 | nonfungsional | Dua hasil tie dan mapping version sama | Hitung ulang 30 kali | Urutan dan rationale identik; no random rank | P0 | CAR-NFR-003 / CAR-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| CAR-Q1 | Belum ada reviewer/sumber mapping | Rekomendasi lemah | P2 disabled sampai mapping reviewed |
| CAR-Q2 | Course dianggap menjamin skill | Ekspektasi keliru | Label mendukung pembelajaran; bukan sertifikasi |
| CAR-Q3 | Scope kurikulum luas | Biaya kurasi | Satu versi dulu |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Navigator P2 ditunda seluruhnya pada DDP1. Dataset lowongan, salary prediction, ML dan resource matchmaker Open Contents tidak masuk MVP.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: CAR-FR-001, CAR-FR-002, CAR-FR-003, CAR-FR-004, CAR-FR-005, CAR-FR-006, CAR-FR-007, CAR-FR-008. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-01 brief. Semua contoh dan ranking adalah PRODUCT_ASSUMPTION D-09; tidak ada pemetaan profesi aktual yang diklaim terverifikasi.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-10 pada audit untuk alasan revisi.

