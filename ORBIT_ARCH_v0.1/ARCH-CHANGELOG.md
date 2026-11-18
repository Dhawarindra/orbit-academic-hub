# ORBIT · Architecture Changelog

Versi **0.1** · **18 November 2026, WIB** · **REVIEW**  
Baseline produk tetap **PRD v0.2.1**. Tujuan dokumen ini adalah melacak keputusan arsitektur, alasan, dan dampaknya pada tests. Scope: 14 dokumen baru. Non-goals: mengubah requirement ID/prioritas atau menulis kode aplikasi. Sumber: [ARCH-INDEX](ARCH-INDEX.md), baseline/errata, dan Prompt 02.

## Rilis awal

| ID | Keputusan / dokumen | Alasan dan sumber | Dampak / traceability |
| --- | --- | --- | --- |
| ARCH-CHG-001 | ARCH-00/01: monolit Python lokal; Flask/Jinja/sqlite3 sebagai default conditional, Streamlit sebagai fallback | Python utama adalah ketentuan dosen; scope lokal dari baseline; framework adalah rekomendasi | CORE-FR-005, AUTH-FR-014, ADR-01/06; RV-14/15 dan runtime OPEN |
| ARCH-CHG-002 | ARCH-02: 17 tabel, satu unit of work, epoch/state/source revisions, receipt, histori final | Menjabarkan actual/scenario, restart dan reset pada baseline | PRO-FR-001–005, GRD-FR-010, MAP-FR-006/011, AUTH-FR-015; INT-T-013/014 |
| ARCH-CHG-003 | ARCH-03: AST tiga nilai, validasi cycle/scope, chosen-OR conditional delay | MAP-BR-001–008 dan DDP-T-01/02/13 | Seluruh MAP P0; tanpa solver atau full rebase |
| ARCH-CHG-004 | ARCH-04: integer basis points, Decimal parsing, rational math, half-up/ceil; O adalah observed weight | GRD-BR-001–007 dan golden readiness; mekanisme presisi pada ADR-09 | Seluruh GRD P0 dan DDP-T-03–07; batas input/teach-back OD-03 OPEN |
| ARCH-CHG-005 | ARCH-05: satu actual writer, Dashboard read-only dari satu snapshot, errors terpisah dari outcomes | CORE-FR-002/003/005, UX-FR-002; tanpa dependency GDE | INT-T-001/003/010/013; formula tidak diduplikasi di frontend |
| ARCH-CHG-006 | ARCH-06: adaptasi light/list, sembunyikan IPK/tren, komunitas dan search | UX-BR-001/002 dan errata; bukti visual sebagian tersedia | UX-FR-001–008, PUB-FR-002/003; contrast belum diukur |
| ARCH-CHG-007 | ARCH-07: 48 FR dan 19 NFR aktif dipetakan; 5 integrasi dan 11 DDP tambahan aktif | RTM, readiness, CORE-NFR-003 | Semua application tests SPECIFIED / NOT EXECUTED; 20 NFR deferred bersama capability |
| ARCH-CHG-008 | ARCH-08/09: blueprint file, AGENTS draft, local run/backup/request guards | AUTH-FR-014/015 dan kewajiban kontribusi/pemahaman | Handoff setelah review manusia; tidak ada public deployment |
| ARCH-CHG-009 | ARCH-10: estimasi 86–116 jam-orang; capacity reserve 25% | Analisis granular memasukkan state/security/quality; baseline 84–100 belum tervalidasi | RV-14 OPEN; waktu test, repository, teach-back dan video termasuk |
| ARCH-CHG-010 | ARCH-11: siap ditinjau, implementasi conditional/not approved | Bukti kapasitas, novelty, runtime dan fixture belum ada | Approval record belum diisi; diam tidak dianggap approval |
| ARCH-CHG-011 | Review akhir memperjelas term manual, explicit demo-load, policy binding final, coverage actual vs assumed, dan stale read | Menutup celah antar kontrak tanpa mengubah FR | PRO-FR-001/004/005, GRD-FR-001/010/011, MAP-FR-006, AUTH-FR-015; tests asli tetap |

Pemeriksaan penjumlahan sebelum rilis mengoreksi total draft menjadi **86–116 jam-orang**, sesuai jumlah sepuluh work package. Seluruh capacity gate dan estimasi terkait telah diselaraskan; ini koreksi aritmetika dokumentasi, bukan hasil pengukuran implementasi.

Tidak ada PRD atau governance baseline yang diubah. Seluruh FR/BR/NFR/AC/test dan prioritas tetap. Tidak ada test aplikasi atau benchmark yang dieksekusi. Pemeriksaan paket mencakup source hashes, counts, errata diff, cakupan 48 P0, dan tautan internal; evidence ini bukan hasil kelulusan aplikasi.

## Change control berikutnya

Catat versi/tanggal/owner manusia, alasan (DOSEN/BASELINE/REKOMENDASI/ASUMSI), keputusan sebelum/sesudah, requirement/AC/test/konsumen terdampak, effort/capability, dan status approval. Perbarui keputusan canon lebih dahulu, lalu seluruh konsumen; jangan menambah fitur hanya pada UI. Silent edit/repriority ditolak karena menghilangkan traceability CORE-FR-008.

Risiko dan pertanyaan terbuka terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md). Semua ADR berstatus PROPOSED FOR REVIEW; belum ada approval manusia. Traceability lengkap tersedia di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).
