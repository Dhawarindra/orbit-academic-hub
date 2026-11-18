# ORBIT · ARCH-07 · TEST STRATEGY AND TRACEABILITY

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Menetapkan oracle, test layers dan bukti penerimaan sebelum coding; memastikan setiap P0 requirement punya alamat desain dan test asli.

**Scope:** 48 FR P0,19 NFR aktif,5 integrasi P0 dan 11 kasus DDP tambahan P0; seluruh hasil aplikasi belum dieksekusi.  
**Non-goals:** menjalankan test aplikasi yang belum ada, fake pass/fail, coverage percentage target tanpa alasan, atau membangun fitur deferred demi NFR-nya.

**Sumber:** 13 PRD bagian 15–18; RTM v0.2.1; Readiness DDP-T-01–13; CORE-NFR-003 dan seluruh AC/test P0. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. Arsitektur test dan oracle

| Layer | Setup dan runner rekomendasi | Bukti yang harus dihasilkan setelah implementasi |
| --- | --- | --- |
| Unit domain | unittest stdlib, DTO kecil, tanpa Flask/DB; subTest untuk truth table/boundaries | Expected dihitung manual/oracle terpisah; exact rational equality, bukan toleransi float |
| Service/repository | SQLite temporary file + factory; in-memory hanya untuk kasus isolated connection | Transaction/revision, FK, uniqueness, idempotency, rollback dan ownership scope |
| Restart/concurrency | File DB sama pada proses baru; dua connection/tab dengan expected token sama | Owner/data bertahan; satu write sukses dan satu conflict; response-loss retry tidak duplikasi |
| Web route | Flask test client, CSRF tokens dari form, temp DB | Status codes, field errors, no writes on GET/cancel, future routes tidak tersedia |
| Manual UI | Browser pada build tercatat, keyboard/resize/zoom/contrast | Catatan langkah/actual, screenshot hanya bukti visual yang relevan; daftar defect |
| Perf | perf_counter di domain; ukur page timing terpisah pada laptop referensi | 30 samples, p 95 nearest-rank, raw data + environment/commit |
| Dokumentasi/release | Manifest/links/capabilities, fresh clone README, staged-file review | Semua source/test ref valid, no secrets/runtime DB, repo/video accessible |

Tidak perlu Hypothesis untuk P0: property checks praktis dapat berupa enumerasi 18 truth-table rows, score boundary fixtures dan urutan mutasi yang deterministik. Jika library property testing dipilih nanti, buat ADR dan masukkan biaya belajar. CI GitHub Actions dapat menjalankan unittest bila tersedia; local test tetap jalur wajib dan CI bukan ketentuan dosen.

## 3. Matriks lengkap 48 FR P0

Nama test di bawah adalah **alamat yang direncanakan**, bukan file/fungsi yang sudah ada. Setiap row mempertahankan AC dan test primer asli; kasus tambahan tidak menggantikan test primer. UI tests berpasangan dengan checklist manual memakai ID asli yang sama. CORE-T-008 adalah pemeriksaan governance, bukan algoritma aplikasi.

| FR ID | ARCH / bagian | Service/fungsi konseptual | AC dan test asli | Test implementasi yang direncanakan / oracle | Status |
| --- | --- | --- | --- | --- | --- |
| CORE-FR-002 | [ARCH-05](ARCH-05-SERVICE-CONTRACTS-AND-DASHBOARD.md) §5 | `DashboardService.read` | CORE-AC-002; CORE-T-002 | `tests/test_integration.py::test_core_t_002` — Revisi skor/final → summary terbaru atau stale; sama dengan engine | SPECIFIED |
| CORE-FR-003 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §6 | `ScenarioService.save` | CORE-AC-003; CORE-T-003 | `tests/test_integration.py::test_core_t_003` — What-if tidak mengubah actual | SPECIFIED |
| CORE-FR-004 | [ARCH-05](ARCH-05-SERVICE-CONTRACTS-AND-DASHBOARD.md) §2 | `SourceMeta / DashboardService.read` | CORE-AC-004; CORE-T-004 | `tests/test_integration.py::test_core_t_004` — Source kosong → NEEDS_VALIDATION | SPECIFIED |
| CORE-FR-005 | [ARCH-00](ARCH-00-SYSTEM-OVERVIEW.md) §5 | `P0 vertical slice` | CORE-AC-005; CORE-T-005 | `tests/test_integration.py::test_core_t_005` — Semua optional off; alur inti selesai | SPECIFIED |
| CORE-FR-007 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §5 | `WorkspaceService.open / empty view` | CORE-AC-007; CORE-T-007 | `tests/test_web.py::test_core_t_007` — DB kosong tanpa angka/tren palsu | SPECIFIED |
| CORE-FR-008 | [ARCH-08](ARCH-08-REPOSITORY-AND-CODEX-HANDOFF.md) §6 | `change_control / documentation audit` | CORE-AC-008; CORE-T-008 | `tests/test_documentation.py::test_core_t_008` — Perubahan scope mempertahankan ID, RTM dan changelog | SPECIFIED |
| PRO-FR-001 | [ARCH-05](ARCH-05-SERVICE-CONTRACTS-AND-DASHBOARD.md) §3 | `ProfileService.save_profile` | PRO-AC-001; PRO-T-001 | `tests/test_integration.py::test_pro_t_001` — Field nullable dan checkpoint | SPECIFIED |
| PRO-FR-002 | [ARCH-05](ARCH-05-SERVICE-CONTRACTS-AND-DASHBOARD.md) §3 | `ProfileService.save_profile` | PRO-AC-002; PRO-T-002 | `tests/test_integration.py::test_pro_t_002` — Unknown scope → personal offering boleh | SPECIFIED |
| PRO-FR-003 | [ARCH-02](ARCH-02-DATABASE-AND-STATE.md) §5 | `WorkspaceService.open` | PRO-AC-003; PRO-T-003 | `tests/test_integration.py::test_pro_t_003` — Restart/resume checkpoint owner sama | SPECIFIED |
| PRO-FR-004 | [ARCH-05](ARCH-05-SERVICE-CONTRACTS-AND-DASHBOARD.md) §3 | `ProfileService.add_enrollment` | PRO-AC-004; PRO-T-004 | `tests/test_integration.py::test_pro_t_004` — Satu enrollment valid; shortcut BRP | SPECIFIED |
| PRO-FR-005 | [ARCH-05](ARCH-05-SERVICE-CONTRACTS-AND-DASHBOARD.md) §3 | `ProfileService.record_history` | PRO-AC-005; PRO-T-005 | `tests/test_integration.py::test_pro_t_005` — Attempt duplikat ditolak, term berbeda diterima | SPECIFIED |
| MAP-FR-001 | [ARCH-03](ARCH-03-ACADEMIC-ROADMAP-ENGINE.md) §2 | `RoadmapService.read` | MAP-AC-001; MAP-T-001 | `tests/test_map_domain.py::test_map_t_001` — Course/SKS tidak campur versi | SPECIFIED |
| MAP-FR-002 | [ARCH-03](ARCH-03-ACADEMIC-ROADMAP-ENGINE.md) §4 | `evaluate_eligibility` | MAP-AC-002; MAP-T-002 | `tests/test_map_domain.py::test_map_t_002` — Predicted 95 tidak unlock C | SPECIFIED |
| MAP-FR-003 | [ARCH-03](ARCH-03-ACADEMIC-ROADMAP-ENGINE.md) §4 | `evaluate_expression` | MAP-AC-003; MAP-T-003 | `tests/test_map_domain.py::test_map_t_003` — Nested AND/OR unknown+alasan | SPECIFIED |
| MAP-FR-004 | [ARCH-03](ARCH-03-ACADEMIC-ROADMAP-ENGINE.md) §5 | `validate_plan / summarize_credits` | MAP-AC-004; MAP-T-004 | `tests/test_map_domain.py::test_map_t_004` — 3+4=7 vs cap personal 6 | SPECIFIED |
| MAP-FR-005 | [ARCH-03](ARCH-03-ACADEMIC-ROADMAP-ENGINE.md) §5 | `simulate_delay` | MAP-AC-005; MAP-T-005 | `tests/test_map_domain.py::test_map_t_005` — A2→B3→C4 bersyarat | SPECIFIED |
| MAP-FR-006 | [ARCH-02](ARCH-02-DATABASE-AND-STATE.md) §5 | `ScenarioService.read/reset` | MAP-AC-006; MAP-T-006 | `tests/test_integration.py::test_map_t_006` — Source r 2 menandai base r 1 stale; reset/reselect | SPECIFIED |
| MAP-FR-007 | [ARCH-03](ARCH-03-ACADEMIC-ROADMAP-ENGINE.md) §3 | `validate_catalog / activate` | MAP-AC-007; MAP-T-007 | `tests/test_integration.py::test_map_t_007` — Cycle ditolak; aktif lama utuh | SPECIFIED |
| MAP-FR-008 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §4 | `roadmap list renderer` | MAP-AC-008; MAP-T-008 | `tests/test_web.py::test_map_t_008` — Semua relasi dan alasan tanpa hover | SPECIFIED |
| MAP-FR-009 | [ARCH-03](ARCH-03-ACADEMIC-ROADMAP-ENGINE.md) §4 | `evaluate_expression` | MAP-AC-009; MAP-T-009 | `tests/test_map_domain.py::test_map_t_009` — Unsupported tetap unknown | SPECIFIED |
| MAP-FR-011 | [ARCH-02](ARCH-02-DATABASE-AND-STATE.md) §6 | `ScenarioService.reset` | MAP-AC-011; MAP-T-011 | `tests/test_integration.py::test_map_t_011` — Semua overlay clear; actual utuh | SPECIFIED |
| MAP-FR-012 | [ARCH-03](ARCH-03-ACADEMIC-ROADMAP-ENGINE.md) §3 | `validate_catalog / activate` | MAP-AC-012; MAP-T-012 | `tests/test_integration.py::test_map_t_012` — Dangling/scope mismatch tidak diaktifkan | SPECIFIED |
| GRD-FR-001 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §3 | `GradeService.save_brp` | GRD-AC-001; GRD-T-001 | `tests/test_integration.py::test_grd_t_001` — Lock setelah skor, versi lama utuh | SPECIFIED |
| GRD-FR-002 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §3 | `validate_brp / effective_weights` | GRD-AC-002; GRD-T-002 | `tests/test_grade_domain.py::test_grd_t_002` — 10000 bp tepat, leaf 10/10/30/50 | SPECIFIED |
| GRD-FR-003 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §2 | `normalize_score / save_scores` | GRD-AC-003; GRD-T-003 | `tests/test_grade_domain.py::test_grd_t_003` — Unknown≠0; range errors | SPECIFIED |
| GRD-FR-004 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §4 | `summarize_grade` | GRD-AC-004; GRD-T-004 | `tests/test_grade_domain.py::test_grd_t_004` — K36,O.5,observed 72,bounds 36–86 | SPECIFIED |
| GRD-FR-005 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §5 | `solve_target` | GRD-AC-005; GRD-T-005 | `tests/test_grade_domain.py::test_grd_t_005` — T75→78; ceiling granularity | SPECIFIED |
| GRD-FR-006 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §5 | `solve_target` | GRD-AC-006; GRD-T-006 | `tests/test_grade_domain.py::test_grd_t_006` — T90→108 impossible | SPECIFIED |
| GRD-FR-007 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §5 | `solve_target` | GRD-AC-007; GRD-T-007 | `tests/test_grade_domain.py::test_grd_t_007` — U0 compare 75/80, tanpa div 0 | SPECIFIED |
| GRD-FR-010 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §6 | `preview_actual / confirm_actual` | GRD-AC-010; GRD-T-010 | `tests/test_integration.py::test_grd_t_010` — Explicit confirm, stale reject, histori koreksi | SPECIFIED |
| GRD-FR-011 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §6 | `calculate_what_if / save_overlay` | GRD-AC-011; GRD-T-011 | `tests/test_integration.py::test_grd_t_011` — UAS90→81; actual unknown | SPECIFIED |
| GRD-FR-012 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §5 | `resolve_target_policy` | GRD-AC-012; GRD-T-012 | `tests/test_grade_domain.py::test_grd_t_012` — A unresolved tanpa policy; numeric tetap | SPECIFIED |
| GRD-FR-014 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §4 | `summarize_grade` | GRD-AC-014; GRD-T-014 | `tests/test_grade_domain.py::test_grd_t_014` — All unknown O0 observed unavailable | SPECIFIED |
| GRD-FR-016 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §5 | `classify / format_number` | GRD-AC-016; GRD-T-016 | `tests/test_grade_domain.py::test_grd_t_016` — 84.995 B,85 A sebelum format | SPECIFIED |
| GRD-FR-018 | [ARCH-04](ARCH-04-GRADE-RESCUE-ENGINE.md) §2 | `parse_numeric_input` | GRD-AC-018; GRD-T-018 | `tests/test_grade_domain.py::test_grd_t_018` — NaNInf/max 0/negative/bobot/target invalid | SPECIFIED |
| UX-FR-001 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §4 | `navigation / term context` | UX-AC-001; UX-T-001 | `tests/test_web.py::test_ux_t_001` — Term dan breadcrumb bertahan | SPECIFIED |
| UX-FR-002 | [ARCH-05](ARCH-05-SERVICE-CONTRACTS-AND-DASHBOARD.md) §5 | `DashboardService.read` | UX-AC-002; UX-T-002 | `tests/test_integration.py::test_ux_t_002` — GRD/MAP langsung, GDE/GPA off | SPECIFIED |
| UX-FR-003 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §6 | `responsive layout` | UX-AC-003; UX-T-003 | `tests/test_web.py::test_ux_t_003` — 360/768/1280 +320/zoom 200 | SPECIFIED |
| UX-FR-004 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §6 | `form/focus handling` | UX-AC-004; UX-T-004 | `tests/test_web.py::test_ux_t_004` — Tab,ShiftTab,Enter,Escape,return focus | SPECIFIED |
| UX-FR-005 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §3 | `readable list/table renderer` | UX-AC-005; UX-T-005 | `tests/test_web.py::test_ux_t_005` — Seluruh nilai/edge setara tanpa warna/hover | SPECIFIED |
| UX-FR-006 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §5 | `field error renderer` | UX-AC-006; UX-T-006 | `tests/test_web.py::test_ux_t_006` — Summary fokus dan input valid utuh | SPECIFIED |
| UX-FR-007 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §5 | `submit state / MutationResult` | UX-AC-007; UX-T-007 | `tests/test_web.py::test_ux_t_007` — Pending/failed/saved/stale; tidak sukses dini | SPECIFIED |
| UX-FR-008 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §6 | `status labels/icons` | UX-AC-008; UX-T-008 | `tests/test_web.py::test_ux_t_008` — Passed/planned/unknown dalam grayscale | SPECIFIED |
| AUTH-FR-010 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §4 | `integration unavailable view` | AUTH-AC-010; AUTH-T-010 | `tests/test_web.py::test_auth_t_010` — Manual fallback; no password/scrape | SPECIFIED |
| AUTH-FR-014 | [ARCH-09](ARCH-09-LOCAL-DEMO-AND-FUTURE-DEPLOYMENT.md) §2 | `local startup guard` | AUTH-AC-014; AUTH-T-014 | `tests/test_local_safety.py::test_auth_t_014` — Owner stabil, public bind ditolak, debugoff | SPECIFIED |
| AUTH-FR-015 | [ARCH-02](ARCH-02-DATABASE-AND-STATE.md) §6 | `WorkspaceService.export/reset` | AUTH-AC-015; AUTH-T-015 | `tests/test_integration.py::test_auth_t_015` — Restart/export/cancel/confirm; seed utuh | SPECIFIED |
| PUB-FR-002 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §4 | `independent product shell` | PUB-AC-002; PUB-T-002 | `tests/test_web.py::test_pub_t_002` — Label independen sebelum input | SPECIFIED |
| PUB-FR-003 | [ARCH-06](ARCH-06-UI-UX-MVP-MAPPING.md) §5 | `synthetic namespace/labels` | PUB-AC-003; PUB-T-003 | `tests/test_web.py::test_pub_t_003` — Demo terpisah dari data nyata; semua halaman berlabel | SPECIFIED |

Subkemampuan full rebase pada MAP-FR-006 tetap P2; row hanya menguji stale→reset/reselect P0. GRD-FR-001 hanya edit sebelum lock dan reject sesudah lock; migration GRD-FR-020 tetap P2. UX-FR-005 menguji list Roadmap/grade yang aktif, bukan menuntut chart tren P1. Seluruh 95 FR non-P0 tetap di baseline (27 P1+68 P2), tidak dihapus atau diaktifkan lewat test plan.

## 4. NFR dan AC primer aktif

Total primer aktif **67 pasangan AC/test**:48 FR+19 NFR. Ini jumlah kewajiban yang dipetakan, bukan jumlah test function atau hasil lulus. Shared keyboard/retry checks boleh memenuhi beberapa ID jika evidence mencatat semua target.

| NFR | Gate sesuai baseline | AC/test asli | Status |
| --- | --- | --- | --- |
| CORE-NFR-001 | Semua alur P0 harus bisa dijalankan dengan integrasi eksternal dimatikan. | CORE-AC-101; CORE-T-101 | SPECIFIED / NOT EXECUTED |
| CORE-NFR-002 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | CORE-AC-102; CORE-T-102 | SPECIFIED / NOT EXECUTED |
| CORE-NFR-003 | Seluruh requirement rilis punya AC dan test terdaftar; konflik data canon nol. | CORE-AC-103; CORE-T-103 | SPECIFIED / NOT EXECUTED |
| PRO-NFR-001 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | PRO-AC-101; PRO-T-101 | SPECIFIED / NOT EXECUTED |
| PRO-NFR-002 | Tampilan utama p 95 ≤2 detik setelah data tersedia pada beban uji dasar. | PRO-AC-102; PRO-T-102 | SPECIFIED / NOT EXECUTED |
| PRO-NFR-003 | Kegagalan simpan tidak menghapus input; retry dengan identitas operasi sama tidak menghasilkan duplikasi. | PRO-AC-103; PRO-T-103 | SPECIFIED / NOT EXECUTED |
| MAP-NFR-001 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | MAP-AC-101; MAP-T-101 | SPECIFIED / NOT EXECUTED |
| MAP-NFR-002 | Validasi graf 100 node/300 edge p 95 ≤300 ms setelah input tersedia. | MAP-AC-102; MAP-T-102 | SPECIFIED / NOT EXECUTED |
| MAP-NFR-003 | Kegagalan simpan tidak menghapus input; retry dengan identitas operasi sama tidak menghasilkan duplikasi. | MAP-AC-103; MAP-T-103 | SPECIFIED / NOT EXECUTED |
| GRD-NFR-001 | Golden numeric output harus konsisten lintas tampilan hingga presisi 0,000001 sebelum format. | GRD-AC-101; GRD-T-101 | SPECIFIED / NOT EXECUTED |
| GRD-NFR-002 | Hitung ulang 300 leaf p 95 ≤200 ms setelah input tervalidasi. | GRD-AC-102; GRD-T-102 | SPECIFIED / NOT EXECUTED |
| GRD-NFR-003 | Kegagalan simpan tidak menghapus input; retry dengan identitas operasi sama tidak menghasilkan duplikasi. | GRD-AC-103; GRD-T-103 | SPECIFIED / NOT EXECUTED |
| UX-NFR-001 | Target WCAG 2.2 AA pada alur P0; teks normal contrast ≥4,5:1, teks besar ≥3:1; komponen nonteks esensial ≥3:1. | UX-AC-101; UX-T-101 | SPECIFIED / NOT EXECUTED |
| UX-NFR-002 | Reflow 320 CSS px dan zoom 200% tetap mempertahankan fungsi; graf/tabel punya alternatif list. | UX-AC-102; UX-T-102 | SPECIFIED / NOT EXECUTED |
| UX-NFR-003 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | UX-AC-103; UX-T-103 | SPECIFIED / NOT EXECUTED |
| AUTH-NFR-003 | Mutasi workspace lokal, sesi atau akun memerlukan validasi request terhadap pemalsuan; secret dan nilai mentah tidak bocor di log. | AUTH-AC-103; AUTH-T-103 | SPECIFIED / NOT EXECUTED |
| PUB-NFR-001 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | PUB-AC-101; PUB-T-101 | SPECIFIED / NOT EXECUTED |
| PUB-NFR-002 | Tampilan utama p 95 ≤2 detik setelah data tersedia pada beban uji dasar. | PUB-AC-102; PUB-T-102 | SPECIFIED / NOT EXECUTED |
| PUB-NFR-003 | Konten publik tidak pernah menyertakan data workspace dalam response/metadata. | PUB-AC-103; PUB-T-103 | SPECIFIED / NOT EXECUTED |

**20 NFR deferred bersama capability:** SCH/SNR/VLT/CAR/GDE/SUP masing-masing 001–003 (18), AUTH-NFR-001 owner A/B dan AUTH-NFR-002 restore lifecycle akun (2). Bukan penurunan prioritas NFR; feature multiuser/restore akun belum aktif. AUTH-NFR-003 request forgery/log safety tetap aktif untuk demo. PUB-NFR-003 diterapkan pada shell/footer/public assets/metadata statis: tidak memuat private workspace payload. Halaman grade lokal bukan halaman publik; semua public hosting tetap off.

## 5. Integrasi baseline dan DDP tambahan

| ID asli | Scope awal | Skenario/penerimaan |
| --- | --- | --- |
| INT-T-001 | Aktif | Scope profil unknown→offering manual→BRP/grade; tidak membutuhkan verified curriculum |
| INT-T-003 | Aktif | UAS what-if 90→81; reset seluruh overlay; actual tetapunknown |
| INT-T-010 | Aktif | Seluruh P1/P2/adapter off; core+Dashboard+export selesai |
| INT-T-013 | Aktif | Actual per-course confirm/correction dengan stale rejection dan history; GDE off |
| INT-T-014 | Aktif | Owner/input persist restart; export; cancel reset; confirm reset; seed utuh |
| INT-T-002/005 | Deferred P1 | Shared deadline/GPA hanya saat capability aktif |
| INT-T-004/006/007/008/009/011/012 | Deferred P2 | Closeout, community/withdraw, multiuser, migration, account delete dan closeout stale tetap future |

| DDP ID | Setup tambahan | Oracle / layer | Status |
| --- | --- | --- | --- |
| DDP-T-01 | 9 pasangan AND+9 OR+nested | ARCH-03 truth table; semua reason leaf tersedia | SPECIFIED |
| DDP-T-02 | Cycle/self-loop/dangling/scope/disconnected | Invalid tidak mengganti catalog aktif; disconnected sah | SPECIFIED |
| DDP-T-03 | Sibling 99.99/100/100.01; cycle/shared leaf | Hanya tepat 10000 bp dan tree sah diterima | SPECIFIED |
| DDP-T-04 | Unknown/0,U0,negative,NaNInf,max 0 | Tidak default 0 atau division-by-zero; field errors | SPECIFIED |
| DDP-T-05 | Target 75.01 quantum 1/.01;84.995/85 |78.02→79/78.02; B/A sebelum format | SPECIFIED |
| DDP-T-06 | Q1=80 lalu edit struktur/bobot/max | Tolak, BRP+score lama utuh, lock tidak hilang saat clear | SPECIFIED |
| DDP-T-07 | Confirm, cancel, stale correction, valid correction | Append history hanya pada valid confirm; refresh MAP/UX | SPECIFIED |
| DDP-T-08 | Seluruh optional off | End-to-end core tanpa GDE/SCH/GPA/API | SPECIFIED |
| DDP-T-09 | Restart, no-public-bind, export/reset/gitignore | Data/owner konsisten, CSRF, debug off, no seed overwrite | SPECIFIED |
| DDP-T-10 | Keyboard 320/zoom 200/contrast/error/save failure | Field/action tetap tersedia; tidak ada fake saved | SPECIFIED |
| DDP-T-11 | Schedule overlap/stress | Ditunda; capability P1 off | DEFERRED WITH CAPABILITY |
| DDP-T-12 | Vault rights/URLs/hidden metadata | Ditunda; capability P1 off | DEFERRED WITH CAPABILITY |
| DDP-T-13 | OR chosen A, tanpa chosen, availability unknown | Hanya jalur dipilih dipakai; unknown bersyarat; no optimizer | SPECIFIED |

## 6. Fixture golden dan negatif

Fixture canonical kecil yang akan dibuat pada tahap implementasi: catalog 8 course A–H dengan chain A→B→C, D=OR(A,E), F=AND(A,OR(B,C)), G tanpa prasyarat eksplisit, H unsupported rule. A/E/G dapat menjadi komponen disconnected yang valid. Dua offering dan tree grade 10/10/30/50. Semua nama/code diberi prefix demo, source_ref/version/hash dan is_synthetic. Definisi ini rencana fixture; belum menyatakan file fixture telah diuji. Fixture invalid terpisah dari dataset aktif: cycle, dangling, scope 2, duplicate attempt,99.99/100.01 bp, parent sharing, invalid earned/target.

Golden grade: K36,O.5,U.5,observed 72,bounds 36–86; T75→78; T90→108; UAS what-if 90→81. Golden MAP: actualApassed unlockB; predictedB95 tidak unlockC; delayA1→2 memberiB3/C4 hanya dengan every-term+assumed pass. Unit tests tidak menghitung expected dengan fungsi yang sama yang sedang diuji.

Test transaction harus menginjeksi kegagalan **sesudah insert pertama sebelum commit**: row/history/revision/receipt seluruhnya tidak berubah. Uji response hilang setelah commit→retry same op/hash returns receipt; same op/different payload rejected. Dua command expected r 1→satu r 2, satu 409. Uji stale preview yang payloadnya diubah, epoch lama setelah reset, retry reset identik, reset saat ada overlay stale, export snapshot saat write concurrent, dan no implicit load fixture on restart. Semua ini dijalankan dalam temp DB, tidak menyentuh data kerja pengguna.

## 7. Performance dan UI measurement

Target desain baseline: MAP100 node/300 edge p 95≤300 ms; GRD300 leaf p 95≤200 ms setelah validasi input; tampilan utama PRO/PUB p 95≤2 detik setelah data tersedia. Laporkan interval berbeda: validasi graph, hitung grade, dan page load, tidak mencampurnya. Synthetic DAG100/300 dan 300 leaf tidak berarti scope demo harus sebesar itu. Resource 1000 benchmark baseline ditunda karena Vault/search off.

Catat CPU/RAM/OS, browser/Python/dependencies, commit, fixture hash, ukuran/depth graph/tree, cold/warm policy, dan 30 durasi. Urut ascending; nearest-rank 95%=ceil(.95×30)=29 (indeks 28). Error/nontermination dilaporkan, tidak dikeluarkan agar p 95 terlihat bagus. Tidak mengklaim latency jaringan internet dari demo offline.

Manual accessibility memakai checklist per action, viewport 320/360/768/1280, zoom 200%, keyboard/grayscale, computed contrast foreground/background dan focus. Catat actual ratio/capture/failure; “terlihat bagus” atau screenshot Figma tidak cukup. Target WCAG2.2 AA tetap target, bukan sertifikat hasil otomatis.

## 8. Definition of Done dan evidence template

Setiap slice: test primer/negative relevan lulus pada build aktual; demo manual; README instruksi slice benar; review manusia dan teach-back lintas anggota; tidak ada route/capability future; input/source/freshness labels benar; perubahan requirement tercatat. Defect core belum tertutup memblokir freeze/video final. Perf/UX gate tidak boleh dilabeli pass sebelum pengukuran.

Evidence row yang kelak diisi: `test_id | FR/AC | commit | environment | fixture/hash | steps | expected | actual | status NOT_RUN/PASS/FAIL/BLOCKED | artifact/defect | reviewer/date`. Saat ini seluruh application evidence=NOT_RUN. Pemeriksaan hash/ID/link paket dokumentasi di ARCH-INDEX adalah jenis evidence berbeda.

Alternatif test hanya happy path atau menganggap coverage baris kode sebagai correctness ditolak. Prioritas test adalah batas numerik, actual/scenario, source scope dan atomic persistence yang membawa risiko nyata.

## Risiko, dependensi, dan bukti terbuka

Rencana 83 kewajiban aktif (67 primer+5 integrasi+11 DDP) dapat berbagi fixture/test harness; bukan 83 skrip terpisah. UI/latency memerlukan perangkat tim, dan schema/concurrency memerlukan file DB bukan hanya in-memory.

**Traceability:** Seluruh ID dalam matriks; pemetaan generated dari ID baseline diverifikasi pada audit paket. Tidak ada application test result. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** OD-01 perangkat/runtime, OD-02 fixture oracle, RV-12 pengukuran; review manusia menyepakati evidence per gate, bukan mengurangi AC diam-diam. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
