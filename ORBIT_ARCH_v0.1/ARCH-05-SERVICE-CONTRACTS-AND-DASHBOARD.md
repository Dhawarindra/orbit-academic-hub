# ORBIT · ARCH-05 · SERVICE CONTRACTS AND DASHBOARD

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Menyatukan interface antar modul, satu writer per data, dan Dashboard yang konsisten dengan engine Python.

**Scope:** DTO, command/read operations, transaction/error contract, serta read model dan route adapter P0.  
**Non-goals:** API publik, event bus, formula di browser, guidance P2 dan writer ganda untuk actual/history.

**Sumber:** CORE-FR-002/003/004/005/007; PRO-FR-001–005; MAP P0; GRD P0; UX-FR-001/002/006/007; AUTH-FR-014/015. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. DTO bersama

| Nama | Fields / tipe | Pemakaian |
| --- | --- | --- |
| RevisionToken | epoch:str, state_revision:int≥0 | Semua command dan actual/reset preview |
| CommandMeta | expected:RevisionToken, operation_id:str, actor='local_owner' | owner_scope diperoleh server; hash request meliputi jenis operasi dan payload kanonik |
| SourceMeta | source_kind:synthetic_fixture/manual_demo, source_ref:str nullable, source_version:str nullable, applicability:object, verification:synthetic/needs_validation, is_synthetic:true | source_ref kosong menampilkan NEEDS_VALIDATION; actual manual demo tetap user_reported, bukan official |
| InputRevisions | epoch, state_revision, source_revision, catalog_version?, brp_versions:map, policy_versions:map, scenario_id?, scenario_revision?, base_source_revision? | Domain response, Dashboard, export; `calculated_at` bukan revision |
| ResultMeta | input_revisions, rule_version, calculated_at UTC, quality_flags:[], uncertainty_reasons:[], freshness:current_at_read/stale | current hanya terhadap snapshot; label “dihitung pada revisi…” |
| MutationResult | status:saved/already_applied, entity_ids:[], token:RevisionToken, event_id? | Returned hanya sesudah COMMIT; replay boleh tanpa event baru |
| FieldError | code, field_path?, entity_ids:[], message_key, recovery_action, correlation_id? | Tidak memuat stack trace/SQL/secret; input lama tetap di adapter form |

Source kind dan academic outcome adalah sumbu berbeda. Dataset demo tidak pernah dipromosikan ke data resmi oleh confirm pengguna. Hasil computed mempunyai references input dan label derived/what-if, bukan provenance resmi baru. Envelope perubahan menyimpan event_id, entity_id, revision (state_revision), occurred_at, owner_scope, source_ref dan scenario_id nullable; ini log lokal/synchronous invalidation, bukan event transport.

## 3. Kontrak service yang dapat dibangun

Semua command mengikuti transaksi ARCH-02§5 dan semua read memakai snapshot tunggal. Range/shape domain dinyatakan di ARCH-03/04. Nama method konseptual dapat dipakai langsung untuk blueprint; perubahan nama perlu update RTM.

| Service.operation | Input → output schema | Precondition dan postcondition | Errors dan tests |
| --- | --- | --- | --- |
| WorkspaceService.open | none→WorkspaceSnapshot{owner,profile?,token,capabilities} | Create owner hanya saat DB benar-benar baru; restart tidak seed ulang; resume checkpoint | SCHEMA_UNSUPPORTED/WRITE_FAILED; PRO-T-003,AUTH-T-014/015 |
| ProfileService.save_profile | CommandMeta+{program?,cohort?,curriculum_id?,active_term_id?,checkpoint}→MutationResult | Nullable unknown valid; curriculum mismatch tidak menjadi verified; source rev increment | INPUT_INVALID/SCOPE_MISMATCH/STALE_REVISION; PRO-T-001/002/003 |
| ProfileService.save_term | CommandMeta+{academic_year,part,label,sequence_no,dates?}→MutationResult{term_id} | Buat term manual dengan urutan eksplisit; pilih term yang sudah ada bila identik; term yang telah dirujuk tidak diurut ulang diam-diam | INPUT_INVALID/TERM_CONFLICT; PRO-T-001/004 |
| WorkspaceService.load_demo | Meta+{fixture_version,confirmed_demo_choice}→MutationResult | Dataset akademik runtime harus kosong; validate semua fixture lalu tulis atomik; profile checkpoint boleh ada tetapi tidak ditimpa. Pemilihan scope demo tetap eksplisit; seed tidak diubah dan restart tidak reload | WORKSPACE_NOT_EMPTY/FIXTURE_INVALID/SCOPE_MISMATCH; CORE-T-005,PUB-T-003,AUTH-T-015 |
| ProfileService.add_enrollment | Meta+{term_id,offering_ref or personal label,course_binding?,attempt_no}→MutationResult{offering,enrollment} | Term ada, owner server; duplicate attempt/enrollment ditolak; personal grade boleh tanpa curriculum | DUPLICATE_ATTEMPT/SCOPE_MISMATCH; PRO-T-004/005,INT-T-001 |
| ProfileService.record_history | Meta+{attempt identity,explicit_final,confirmed_preview}→MutationResult | Jalur GRD confirmation dipanggil dalam UoW sama; enrollment+actual keduanya commit/rollback | DUPLICATE_ATTEMPT/STALE_PREVIEW; PRO-T-005,GRD-T-010 |
| CatalogService.activate | Meta+ValidatedCatalog→MutationResult | Draft validation dahulu; cek kembali hash/source saat write; invalid tidak mengganti aktif | GRAPH_INVALID/SCOPE_MISMATCH; MAP-T-007/012 |
| GradeService.save_brp | Meta+{enrollment_id,tree,source,rule_version}→MutationResult | Binding sesuai; structure lock diperiksa di DB dalam transaksi | STRUCTURE_LOCKED/INVALID_TREE; GRD-T-001/002 |
| GradeService.save_scores | Meta+{brp_id,entries:[{node_id,earned?}],source}→MutationResult | Semua leaf valid; lock BRP; satu source increment; tidak menulis actual final | INPUT_INVALID/STALE_REVISION; GRD-T-003/018 |
| GradeService.save_target | Meta+{enrollment_id,numeric? or letter?,policy_id?,source}→MutationResult | Numeric 0..100 atau letter unresolved; policy mismatch tidak diam-diam konversi | INPUT_INVALID/POLICY_SCOPE_MISMATCH; GRD-T-005/012 |
| GradeService.read_summary | {enrollment_id,mode:actual/scenario}→GradeSummary+TargetResult+ResultMeta | Snapshot valid; scenario stale menghasilkan stale view tanpa recalculation current | missing BRP domain state; GRD-T-004–007/014/016 |
| GradeService.preview_actual / confirm_actual | Preview{explicit final,source,expected,reason?}→Preview{payload_hash,token,impact}; confirm{same payload,proof,Meta}→MutationResult | Preview nol write; signed proof diverifikasi adapter; service revalidasi revision/payload/outcome; append history | STALE_PREVIEW/CONFIRMATION_REQUIRED/INPUT_CONFLICT; GRD-T-010,DDP-T-07 |
| RoadmapService.read | {curriculum_id?,term_id?,mode}→RoadmapResult+ResultMeta | Actual mode tidak mengakses overlay sebagai evidence | unknown scope normal; MAP-T-001/002/003/008/009 |
| ScenarioService.save | Meta+{plan,score_overlay,target_overlay,assumptions}→MutationResult | Maksimum satu; create base current; edit membutuhkan base current; validator kedua domain | STALE_SCENARIO/SCOPE_MISMATCH; MAP-T-004/005,GRD-T-011 |
| ScenarioService.reset | Meta+{scenario_id}→MutationResult | Stale boleh reset, current workspace token tetap wajib; clear semua overlay; actual/source revision tidak berubah | STALE_REVISION; MAP-T-006/011,INT-T-003 |
| DashboardService.read | {term_id?}→DashboardVM | Snapshot sekali, panggil summarize_grade/evaluate_eligibility/summarize_credits dari input yang sama | Partial per-card known/unknown; no invented metrics; UX-T-002,CORE-T-002/007 |
| WorkspaceService.export | current request→ExportDocument{schema,source,revisions,records} | Read-only snapshot; no secrets/receipts/log; download lokal | READ_FAILED; AUTH-T-015,INT-T-014 |
| WorkspaceService.preview_reset / reset | Preview read→counts/hash/token; Meta+confirmed proof→MutationResult | Cancel no write; confirmed destructive reset sesuai ARCH-02§6 | CONFIRMATION_REQUIRED/STALE_PREVIEW; AUTH-T-015,DDP-T-09 |

Preview history untuk attempt baru hanya menampilkan proposed identity dan payload; belum membuat enrollment. Confirm memeriksa duplicate attempt sekali lagi lalu membuat enrollment dan final dalam satu commit. Bila load-demo bertabrakan dengan term/binding yang sudah ada, tolak seluruh operasi dengan penjelasan; jangan mengubah profile atau melakukan reset otomatis.

Shared unit of work adalah parameter/internal coordinator, bukan setiap service membuat commit tersendiri. `record_history` menggunakan helper actual writer yang sama dengan confirm biasa; tak ada salinan algoritma. Tidak diperlukan kelas “User” dengan login untuk memenuhi owner_scope lokal.

## 4. Error dan hasil domain

| Kategori | Transport Flask usulan | State UI / pemulihan |
| --- | --- | --- |
| INPUT_INVALID, INVALID_TREE, GRAPH_INVALID, SOURCE_SCOPE_MISMATCH |422|Ringkasan error + field errors; jangan kehilangan draft atau mengganti data aktif |
| DUPLICATE_ATTEMPT, STRUCTURE_LOCKED, OPERATION_ID_REUSED |409|Jelaskan konflik; jangan retry otomatis dengan ID baru yang menggandakan operasi |
| STALE_REVISION, STALE_EPOCH, STALE_PREVIEW, STALE_SCENARIO |409|Lihat perubahan; preview ulang/reset scenario; input lama boleh ditinjau tanpa auto-overwrite |
| CSRF/Host validation failure |403/400|Request ditolak sebelum write; pesan umum, reload form lokal |
| Entity ID tidak ada |404|Tautan kembali; bedakan record hilang dari data akademik unknown |
| WRITE_FAILED / DB_BUSY |503|Input tetap; retry op_id sama; tidak menyatakan saved |
| Unknown prerequisite, policy_unresolved, missing BRP, impossible target |200 (read/preview)|Outcome domain dengan reason/action; bukan exception generic atau angka 0 |

Tidak semua ketidakpastian adalah “error”; pending/saved/failed/stale adalah status operasi, sedangkan unmet/unknown adalah hasil akademik. Template menerima message_key dan field paths yang aman, tidak SQL exception mentah.

## 5. Dashboard read model

`DashboardVM = {context:{term,profile_status,dataset_mode,independent_label}, meta:ResultMeta, grade_cards:[{enrollment_id,course_label,summary,target,source_link}], roadmap:{credits,eligibility_counts,plan_state,warnings,source_link}, notices:[{reason,source_link}], capability_manifest}`.

Aggregation read-only: (a) ambil input satu snapshot, (b) baca profile/binding, (c) panggil GRD untuk setiap offering dan MAP sekali untuk catalog, (d) ubah output jadi DTO presentasi, (e) bentuk navigasi berdasarkan capabilities. `notices` adalah daftar masalah data/warning engine dengan tautan langsung, bukan ranking guidance baru. Dashboard tidak membuat target, mengubah course status, atau melakukan write “refresh”. Urutan deterministik: input invalid/unknown, target impossible, warning plan; tanpa klaim rekomendasi akademik cerdas.

| Kondisi | Tampilan | Aksi |
| --- | --- | --- |
| Workspace kosong | Petunjuk profil/masukkan matkul/pilih contoh; tidak ada IPK/tren | Onboarding/manual offering |
| Skor parsial | K, coverage O, observed jika ada, bounds; label jenis hasil | Ke form skor sumber |
| Semua unknown | Coverage 0, observed “belum tersedia”, bounds 0–100 jika BRP sah | Lengkapi skor |
| Policy huruf missing | Target A belum dapat dikonversi, numeric tetap tersedia | Pilih target angka/source policy |
| Scenario current | Actual dan what-if dipisah, banner dan base revision | Buka scenario/reset |
| Scenario stale | Badge perlu diperbarui + changed source; hasil lama bukan current | Reset/pilih ulang |
| Actual confirmed/corrected | Label user-reported+sintetis+revision; eligibility dihitung ulang saat baca | Lihat history/input aktual |
| Missing/unsupported scope | Unknown + alasan; tidak mengisi angka placeholder | Lengkapi binding/sumber |
| Read/write failure | Error spesifik card atau halaman, tanpa sukses palsu | Retry aman/reload |

Dua halaman pada snapshot yang sama harus menghasilkan angka exact sama sebelum formatting. Karena model read-only tidak cached persisted, invalidasi berarti revision check dan hitung saat read; tidak perlu background worker. Scenario stale tetap dapat ditampilkan sebagai draft lama tetapi hasil derived tidak current.

## 6. Route mapping usulan

GET `/`→Dashboard; GET/POST `/profile`; POST `/terms`; GET/POST `/enrollments/new`; GET/POST `/history/new` (preview/confirm tahap jelas); GET `/roadmap`; GET/POST `/scenario`; POST `/scenario/reset`; GET `/grades/<enrollment_id>`; POST suffix `/brp`, `/scores`, `/target`, `/actual/preview`, `/actual/confirm`; GET `/workspace`; POST `/workspace/export`, `/workspace/reset/preview`, `/workspace/reset/confirm`, `/workspace/load-demo`. Semua mutasi POST+CSRF. GET tidak boleh memicu seed/reset. POST sukses menggunakan redirect atau response saved dari commit yang sudah selesai; request export read-only tetap POST agar token diperlukan. Path hanya rekomendasi internal local adapter, bukan API publik stabil.

Alternatif Dashboard memanggil HTTP engine lain, menyimpan duplikat derived values, atau membuat event bus ditolak. Frontend hanya menerima schema read model dan error; formula kanonik tetap satu tempat.

## Risiko, dependensi, dan bukti terbuka

Read model yang membaca tanpa snapshot dapat mencampur revision; actual history via PRO raw write dapat menduplikasi writer. Keduanya dicegah oleh unit of work bersama dan contract tests. Metadata provenance harus dipertahankan saat formatting.

**Traceability:** CORE-AC/T-002/003/004/005/007; UX-AC/T-001/002/006/007; PRO-AC/T-001–005; INT-T-001/003/010/013/014. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** OD-01 adapter final dan OD-04 transaction/API review; fallback Streamlit wajib memetakan operasi yang sama, bukan melewati service. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
