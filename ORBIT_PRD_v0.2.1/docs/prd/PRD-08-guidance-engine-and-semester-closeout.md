# PRD-08 — Academic Guidance Engine & Semester Closeout

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-08 / v0.2 DDP1 Draft |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Guidance Product Owner |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | Engine berbasis rule deterministik, bukan model AI. Rekomendasi tidak mengubah pilihan akademik tanpa tindakan pengguna. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). |

## 2. Executive Summary & Problem

Guidance memilih sedikit tindakan yang relevan dari data personal dan sumber komunitas yang layak. Setiap saran menyebut trigger, input, asumsi dan tujuan tindakan. Closeout menutup siklus semester dengan finalisasi eksplisit serta kontribusi yang tetap sukarela.

## 3. Goals, Non-Goals & Success Metrics

Pengguna dapat memahami mengapa saran muncul, menindaklanjutinya di sumber data, dan menutup semester tanpa mewariskan simulasi sebagai aktual.

**Non-goals:** Membuat keputusan akademik, memaksa target, auto-publish nilai atau menjanjikan perbaikan hasil studi.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Explainability | Saran punya input refs, rule version, reason dan CTA | 100% guidance items |
| Konflik rekomendasi | Fixture saran nilai vs kapasitas | Nol rencana otomatis melebihi kapasitas tanpa label |
| Integritas closeout | Finalisasi/retry/reopen pada fixture | Nol partial write yang terlihat sukses |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Mahasiswa bingung prioritas; mahasiswa di akhir semester; kontributor yang ingin melewati donation.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Student | Lihat/dismiss/apply saran dan closeout sendiri | Closeout orang lain |
| Moderator | Konten komunitas yang dipakai engine | Mengubah target/nilai pengguna |
| Admin | Rule version terkurasi | Mengirim saran personal sebagai pesan eksternal tanpa opt-in |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Tidak ada; Dashboard inti membaca GRD/MAP langsung | Tidak ada | Seluruh advanced guidance dan Semester Closeout lengkap, reopen/handover/idempotensi |

**Slice rilis:** Konfirmasi aktual per course P0 dimiliki GRD-FR-010; tidak membuat snapshot semester final. Closeout P2 tetap memakai kontrak GRD dan consent terpisah.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Konfirmasi aktual per course P0 dimiliki GRD-FR-010; tidak membuat snapshot semester final. Closeout P2 tetap memakai kontrak GRD dan consent terpisah. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Dashboard → kartu Fokus pekan ini → Mengapa ini muncul → buka assessment sumber → ubah data → kembali. Item lama ditandai stale bila input berubah; hasil baru memakai revision terbaru.

**J2.** Target memerlukan skor tinggi sementara pekan padat → engine menampilkan konflik dan pilihan mulai lebih awal/ubah alokasi/tinjau target. Pengguna dapat abaikan; tidak ada kalender yang berubah otomatis.

**J3.** Akhir semester → Review → isi hasil aktual atau tandai unresolved → preview IPS/IPK dan course status → konfirmasi → snapshot final. Setelah finalisasi, prompt berbagi terpisah dapat dilewati; koreksi kemudian melalui Reopen dengan alasan.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| GDE-US-001 | As a student, I want mendapat saran yang beralasan, so that saya bisa menentukan prioritas. | P2 | GDE-FR-001, GDE-FR-002, GDE-FR-003, GDE-FR-004, GDE-FR-005 |
| GDE-US-002 | As a student, I want memfinalisasi dan mengoreksi semester, so that riwayat aktual dapat dipercaya. | P2 | GDE-FR-006, GDE-FR-007, GDE-FR-009 |
| GDE-US-003 | As a student, I want memilih apakah berbagi pengalaman, so that data pribadi tetap terkendali. | P2 | GDE-FR-008 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GDE-FR-001 | P2 | Bangun guidance | Input sources valid atau partial | GradeProjection, WorkloadSummary, ConstraintResult | Evaluasi rule dan sertakan input revisions + reason + CTA | Setiap item bisa ditelusuri; unknown grade menghasilkan ajakan isi data, bukan gagal | GDE-AC-001 |
| GDE-FR-002 | P2 | Urutkan guidance | Ada >3 kandidat | Kategori, due_at, source quality | Pilih maksimal 3 actionable items menurut precedence | Urgent actionable deadline mendahului eksplorasi minat | GDE-AC-002 |
| GDE-FR-003 | P2 | Gabungkan konflik | Saran belajar butuh 6 jam; sisa kapasitas 2 | Target feasible dan workload overloaded | Tawarkan tradeoff tanpa menjadwalkan 6 jam otomatis | Teks menyebut gap 4 jam dan opsi; kalender tidak berubah | GDE-AC-003 |
| GDE-FR-004 | P2 | Ambil sumber opsional | Playbook/Vault/Career unavailable | Candidate komunitas tidak valid | Gunakan sumber personal dan hilangkan resource hidden | Guidance tetap berfungsi tanpa data kating | GDE-AC-004 |
| GDE-FR-005 | P2 | Dismiss rekomendasi | Item aktif milik user | item_id, snooze sampai tanggal atau dismiss | Simpan dismissal keyed rule+entity+input_revision | Item sama tidak muncul kembali sebelum batas/trigger revisi | GDE-AC-005 |
| GDE-FR-006 | P2 | Konfirmasi closeout | Preview hasil actual dan unresolved terlihat | Final grades explicit; id operasi | Finalisasi snapshot dan hasil aktual secara all-or-nothing dalam scope semester | Semua final sah tersimpan sekali; unresolved tidak menjadi lulus | GDE-AC-006 |
| GDE-FR-007 | P2 | Reopen closeout | Snapshot final milik user | Alasan koreksi | Buat revisi reopen dan tandai hasil turunan stale | Snapshot lama tersimpan; koreksi tidak silent overwrite | GDE-AC-007 |
| GDE-FR-008 | P2 | Tawarkan handover | Closeout berhasil | Consent purpose default off | Preview field per tujuan sebelum submit kontribusi | Skip menghasilkan nol contribution; tidak mengubah closeout | GDE-AC-008 |
| GDE-FR-009 | P2 | Retry closeout | Konfirmasi sebelumnya timeout | operation_id yang sama | Temukan hasil commit yang sama atau ulang secara idempotent | Tepat satu snapshot final, tidak double-count GPA | GDE-AC-009 |
| GDE-FR-010 | P2 | Input berubah saat preview | Preview revision r1; source kini r2 | Confirm dengan r1 | Tolak commit dan minta review diff terbaru | Tidak finalisasi nilai stale | GDE-AC-010 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| GDE-BR-001 | Precedence: pemblokir data yang diperlukan untuk aksi terdekat → deadline overdue/≤7 hari yang actionable → target dan kapasitas minggu berjalan → dependensi semester → resource/eksplorasi opsional. Tiap rule menyebut time window. | GDE-FR-001, GDE-FR-002 |
| GDE-BR-002 | Dalam kategori, urut due_at terdekat (unknown terakhir), lalu tingkat kekuatan sumber, lalu stable rule_id. Dedup per entity+action; maksimum 3 item, dengan link lihat semua kandidat. | GDE-FR-002 |
| GDE-BR-003 | Rekomendasi tidak memiliki efek samping sebelum apply. Conflict resolution menggabungkan saran pada entity sama dan mengungkap constraint yang tidak dapat dipenuhi bersamaan. | GDE-FR-003, GDE-FR-005 |
| GDE-BR-004 | Low-quality input → ajakan mengisi/review; bukan estimasi lebih pasti. Komunitas hanya contextual dan tidak mengalahkan fakta personal atau aturan akademik aktif. | GDE-FR-001, GDE-FR-004 |
| GDE-BR-005 | Closeout lifecycle: draft → review → final → reopened → review → final revision. Final artinya catatan semester dikunci pengguna, bukan verifikasi kampus. Unresolved tetap ditampilkan dan tidak membuka prasyarat. | GDE-FR-006, GDE-FR-007 |
| GDE-BR-006 | Setiap confirmed final memiliki source/provenance dan policy scope. Prediksi tidak diprefill sebagai actual tanpa aksi memasukkan/menegaskan hasil secara eksplisit. | GDE-FR-006, GDE-FR-010 |
| GDE-BR-007 | Commit closeout memeriksa source revisions, menyimpan snapshot dan actual changes, lalu memicu invalidasi konsumen. Retry memakai operation_id; gagal commit tidak tampil final parsial. | GDE-FR-006, GDE-FR-009, GDE-FR-010 |
| GDE-BR-008 | Handover adalah langkah setelah closeout dengan consent per purpose. Menolak donation tidak mengurangi akses atau menghalangi closeout. | GDE-FR-008 |

**Skenario sintetis 1:** UAS membutuhkan minimal 78 berdasarkan data yang tersedia, due dalam 5 hari; tugas lain menyebabkan demand 10 jam pada kapasitas 8. Engine tidak mengatakan “pasti dapat A”. Ia menampilkan kebutuhan nilai beserta asumsi dan menyarankan meninjau alokasi 2 jam di minggu sebelumnya atau target.

**Skenario 2:** user belum mengisi durasi 2 dari 3 tugas; engine memprioritaskan isi estimasi agar beban dapat dipahami, tanpa menyebut overload hanya dari jumlah deadline. Tidak ada insight kating → tetap memberi saran personal.

**Skenario 3:** dua course difinalisasi; course A actual_user_reported lulus, B unresolved. Setelah commit, MAP memperbarui A berdasarkan catatan pengguna; B belum membuka prerequisite. Skip berbagi tidak membuat contribution. Reopen A setelah koreksi membuat projections stale dan membutuhkan re-review.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| GuidanceRule / rule_id | version, inputs, predicate, priority, copy template, action | Product owner | reviewed rules; versioned | Public explanation / internal config |
| GuidanceItem / item_id | owner, rule version, source revisions, reason, CTA, uncertainty | Engine | active/dismissed/stale/resolved | Private |
| Dismissal / dismissal_id | owner+rule+entity+input_revision, until | Student | expires or new trigger | Private |
| SemesterCloseout / closeout_id | owner, term, status, snapshot revision, unresolved, operation_id | Student/GDE | draft/review/final/reopened | Private |
| CloseoutResultRefs | actual_final_ids and policy refs, no duplicated independent grades | GRD canonical | Immutable snapshot; next revision corrects | Private |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Dashboard menampilkan maksimal tiga tindakan dengan judul konkret, satu kalimat alasan dan CTA. “Mengapa?” membuka detail input, tanggal data, batas kesimpulan dan rule. Dismiss tersedia tanpa mempermalukan pengguna. Closeout wizard: review data → hasil aktual → preview → konfirmasi; donation terpisah setelah sukses. Tombol konfirmasi menampilkan jumlah course final dan unresolved. Banner stale meminta review ulang, bukan diam-diam memakai input lama.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| No data | Satu langkah awal yang bisa dikerjakan | Tidak memproduksi insight fiktif |
| Conflicting advice | Tradeoff dan pilihan | Tidak auto-apply |
| Stale inputs | Refresh diperlukan | Reason lama tidak aktif |
| Partial final | Unresolved terlihat | Tidak dianggap gagal/lulus otomatis |
| Duplicate confirm | Kembalikan hasil existing | Tidak duplikasi snapshot |
| Unauthorized/offline | Tolak/pertahankan review draft | Tidak tampil berhasil |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** Seluruh jalur berikut P2. UX Dashboard P0 membaca MAP/GRD langsung. GRD-FR-010 memiliki konfirmasi/koreksi per course P0; GDE menambahkan transaksi closeout semester ketika kelak diaktifkan. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| GRD-FR-004/SCH-FR-004/MAP-FR-004 → GDE-FR-001 | Typed summaries + source revisions | Missing source yields limited action |
| SNR-FR-009/VLT-FR-001/CAR-FR-002 → GDE-FR-004 | Published compatible context only | Disabled modules omitted |
| GDE-FR-006 → GRD-FR-010/MAP-FR-002 | CloseoutConfirmed references final_id | Atomic commit boundary; retry idempotent |
| GDE-FR-008 → SNR-FR-001/VLT-FR-005 | Explicit contribution intent and chosen fields | Default no data transfer |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Engine memproses data pribadi hanya untuk akun itu. Alasan tidak membandingkan user dengan kelompok kecil. Guidance tidak mengirim email, push atau digest otomatis; notifikasi memiliki scope/consent terpisah. Kontribusi hanya setelah preview dan consent, tidak karena menekan finalisasi.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| GDE-NFR-001 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | GDE-AC-101 |
| GDE-NFR-002 | P0 | Identitas output stabil dan reason konsisten untuk snapshot sama. | GDE-AC-102 |
| GDE-NFR-003 | P0 | Closeout tahan retry dan concurrent revision. | GDE-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| GDE-AC-001 | Given Input sources valid atau partial; GradeProjection, WorkloadSummary, ConstraintResult | When Bangun guidance | Then Setiap item bisa ditelusuri; unknown grade menghasilkan ajakan isi data, bukan gagal | GDE-FR-001 |
| GDE-AC-002 | Given Ada >3 kandidat; Kategori, due_at, source quality | When Urutkan guidance | Then Urgent actionable deadline mendahului eksplorasi minat | GDE-FR-002 |
| GDE-AC-003 | Given Saran belajar butuh 6 jam; sisa kapasitas 2; Target feasible dan workload overloaded | When Gabungkan konflik | Then Teks menyebut gap 4 jam dan opsi; kalender tidak berubah | GDE-FR-003 |
| GDE-AC-004 | Given Playbook/Vault/Career unavailable; Candidate komunitas tidak valid | When Ambil sumber opsional | Then Guidance tetap berfungsi tanpa data kating | GDE-FR-004 |
| GDE-AC-005 | Given Item aktif milik user; item_id, snooze sampai tanggal atau dismiss | When Dismiss rekomendasi | Then Item sama tidak muncul kembali sebelum batas/trigger revisi | GDE-FR-005 |
| GDE-AC-006 | Given Preview hasil actual dan unresolved terlihat; Final grades explicit; id operasi | When Konfirmasi closeout | Then Semua final sah tersimpan sekali; unresolved tidak menjadi lulus | GDE-FR-006 |
| GDE-AC-007 | Given Snapshot final milik user; Alasan koreksi | When Reopen closeout | Then Snapshot lama tersimpan; koreksi tidak silent overwrite | GDE-FR-007 |
| GDE-AC-008 | Given Closeout berhasil; Consent purpose default off | When Tawarkan handover | Then Skip menghasilkan nol contribution; tidak mengubah closeout | GDE-FR-008 |
| GDE-AC-009 | Given Konfirmasi sebelumnya timeout; operation_id yang sama | When Retry closeout | Then Tepat satu snapshot final, tidak double-count GPA | GDE-FR-009 |
| GDE-AC-010 | Given Preview revision r1; source kini r2; Confirm dengan r1 | When Input berubah saat preview | Then Tidak finalisasi nilai stale | GDE-FR-010 |
| GDE-AC-101 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | GDE-NFR-001 |
| GDE-AC-102 | Given Rules, waktu evaluasi dan sumber tetap | When Evaluasi 30 kali | Then Urutan maksimal 3 dan output reasons sama | GDE-NFR-002 |
| GDE-AC-103 | Given Dua tab dan satu timeout | When Confirm bersamaan lalu retry operation_id | Then Satu commit valid; tab stale meminta review; tidak ada final parsial | GDE-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| GDE-T-001 | fungsional | Input sources valid atau partial; GradeProjection, WorkloadSummary, ConstraintResult | Bangun guidance | Setiap item bisa ditelusuri; unknown grade menghasilkan ajakan isi data, bukan gagal | P2 | GDE-FR-001 / GDE-AC-001 |
| GDE-T-002 | fungsional | Ada >3 kandidat; Kategori, due_at, source quality | Urutkan guidance | Urgent actionable deadline mendahului eksplorasi minat | P2 | GDE-FR-002 / GDE-AC-002 |
| GDE-T-003 | numerik | Saran belajar butuh 6 jam; sisa kapasitas 2; Target feasible dan workload overloaded | Gabungkan konflik | Teks menyebut gap 4 jam dan opsi; kalender tidak berubah | P2 | GDE-FR-003 / GDE-AC-003 |
| GDE-T-004 | integrasi | Playbook/Vault/Career unavailable; Candidate komunitas tidak valid | Ambil sumber opsional | Guidance tetap berfungsi tanpa data kating | P2 | GDE-FR-004 / GDE-AC-004 |
| GDE-T-005 | fungsional | Item aktif milik user; item_id, snooze sampai tanggal atau dismiss | Dismiss rekomendasi | Item sama tidak muncul kembali sebelum batas/trigger revisi | P2 | GDE-FR-005 / GDE-AC-005 |
| GDE-T-006 | integrasi | Preview hasil actual dan unresolved terlihat; Final grades explicit; id operasi | Konfirmasi closeout | Semua final sah tersimpan sekali; unresolved tidak menjadi lulus | P2 | GDE-FR-006 / GDE-AC-006 |
| GDE-T-007 | edge | Snapshot final milik user; Alasan koreksi | Reopen closeout | Snapshot lama tersimpan; koreksi tidak silent overwrite | P2 | GDE-FR-007 / GDE-AC-007 |
| GDE-T-008 | privasi | Closeout berhasil; Consent purpose default off | Tawarkan handover | Skip menghasilkan nol contribution; tidak mengubah closeout | P2 | GDE-FR-008 / GDE-AC-008 |
| GDE-T-009 | boundary | Konfirmasi sebelumnya timeout; operation_id yang sama | Retry closeout | Tepat satu snapshot final, tidak double-count GPA | P2 | GDE-FR-009 / GDE-AC-009 |
| GDE-T-010 | negatif | Preview revision r1; source kini r2; Confirm dengan r1 | Input berubah saat preview | Tidak finalisasi nilai stale | P2 | GDE-FR-010 / GDE-AC-010 |
| GDE-T-101 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | GDE-NFR-001 / GDE-AC-101 |
| GDE-T-102 | nonfungsional | Rules, waktu evaluasi dan sumber tetap | Evaluasi 30 kali | Urutan maksimal 3 dan output reasons sama | P0 | GDE-NFR-002 / GDE-AC-102 |
| GDE-T-103 | nonfungsional | Dua tab dan satu timeout | Confirm bersamaan lalu retry operation_id | Satu commit valid; tab stale meminta review; tidak ada final parsial | P0 | GDE-NFR-003 / GDE-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| GDE-Q1 | Saran terkesan otoritatif | User mengikuti tanpa pertimbangan | Bahasa pilihan, alasan, provenance dan batas |
| GDE-Q2 | Banyak event cascade | Inconsistency | Invalidate/recompute versioned; tidak perlu broker MVP |
| GDE-Q3 | Semester final tanpa semua hasil | Membuka course secara salah | Unresolved eksplisit; hanya confirmed actual untuk MAP |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Tidak ada decision automation, predictive ML, push/email tanpa opt-in atau reward karena menyumbangkan nilai. Digest P2.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: GDE-FR-001, GDE-FR-002, GDE-FR-003, GDE-FR-004, GDE-FR-005, GDE-FR-006, GDE-FR-007, GDE-FR-008, GDE-FR-009, GDE-FR-010. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-01 brief. Prioritas, jumlah item dan lifecycle closeout merupakan PRODUCT_ASSUMPTION D-10; bukan saran akademik resmi.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-03/AUD-11 pada audit untuk alasan revisi.

