# ORBIT · ARCH-08 · REPOSITORY AND CODEX HANDOFF

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Memberi blueprint file dan aturan kerja agar implementasi berikutnya tetap modular, dapat dipahami, dan terikat requirement P0.

**Scope:** struktur repository usulan, import boundaries, coding conventions, AGENTS template, workflow dan teach-back.  
**Non-goals:** membuat repository/kode aplikasi sekarang, mengisi identitas anggota rekaan, atau memberi izin deploy publik.

**Sumber:** CORE-FR-008/CORE-NFR-003; seluruh FR P0; panduan hlm 2–4 kontribusi/pemahaman/GitHub publik; ADR-01–10. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. File tree usulan dan tanggung jawab

Tabel berindentasi path ini adalah **file-by-file blueprint**, bukan inventaris file aplikasi yang sudah dibuat. Hindari package/framework tambahan jika satu file cukup. Pisahkan file setelah ada alasan, bukan membuat satu class untuk setiap tabel.

| Path usulan | Tanggung jawab / batas |
| --- | --- |
| `README.md` | Masalah/bukti, scope active/future, setup/run/test aktual, diagram, synthetic provenance, anggota/kontribusi, video; tidak klaim fitur belum ada |
| `AGENTS.md` | Instruksi Codex di §5; wajib dibaca sebelum implementasi |
| `requirements.txt` | Hanya dependency runtime yang dipilih dan diverifikasi; pin sesudah smoke |
| `requirements-dev.txt` | Opsional bila tim memilih tooling selain unittest; tidak perlu file kosong |
| `.gitignore` | Environment, secret, instance DB/journal/WAL/SHM, export/backup, cache/log runtime |
| `orbit/__init__.py` | Composition root/factory; inject services/repository, register P0 routes, safe config |
| `orbit/__main__.py` | Runner lokal dengan guard host/debug/schema, startup errors; satu entry resmi |
| `orbit/config.py` | Capability manifest, data directory, mode local-demo, allowed hosts; no academic constants |
| `orbit/domain/__init__.py` | Namespace domain; tidak import Flask/sqlite3 |
| `orbit/domain/models.py` | Typed DTO/enums/value types, SourceMeta/RevisionToken/ResultMeta |
| `orbit/domain/errors.py` | Domain error codes/field paths; tidak tahu HTTP status |
| `orbit/domain/numbers.py` | Decimal parsing, rational serialization, half-up/ceil formatter; satu numeric canon |
| `orbit/domain/roadmap.py` | AST/graph validation, truth values/reasons, eligibility, credits, delay |
| `orbit/domain/grades.py` | BRP validation/flatten, summary/target/policy; no database writes |
| `orbit/services/__init__.py` | Namespace, tanpa side effect |
| `orbit/services/workspace.py` | Open/profile/enrollment/history coordinator, export/reset/demo load; reuse actual writer |
| `orbit/services/academic.py` | Catalog/Grade/Scenario command and read services; UoW dan source binding |
| `orbit/services/dashboard.py` | One snapshot aggregation dan source notices, no duplicated math |
| `orbit/repositories/__init__.py` | Namespace |
| `orbit/repositories/sqlite_store.py` | Connection/UoW, parameterized reads/writes, FK setup, receipt/histori; no academic decisions |
| `orbit/repositories/schema.sql` | 17 tabel/constraints/index; schema_version guard; dibuat setelah review |
| `orbit/web/__init__.py` | Namespace adapter |
| `orbit/web/routes.py` | Parse forms, CSRF/preview proof check, map errors/status, redirect; calls services only |
| `orbit/web/security.py` | Host/origin/CSRF/local request guards; secret from runtime; no campus credentials |
| `orbit/templates/base.html` | Brand/nav/term/source/independence/synthetic banner; capabilities |
| `orbit/templates/dashboard.html` | Render DashboardVM; no math |
| `orbit/templates/profile.html` | Profile/checkpoint/unknown scope form |
| `orbit/templates/enrollment.html` | Manual offering/attempt creation dan history input path |
| `orbit/templates/roadmap.html` | Accessible list/detail/prerequisite reasons |
| `orbit/templates/grade.html` | BRP/score/target form dan exact-result labels |
| `orbit/templates/scenario.html` | Overlay controls, chosen OR, stale/reset; no actual fields |
| `orbit/templates/confirm.html` | Actual atau destructive reset review yang dibedakan eksplisit |
| `orbit/templates/workspace.html` | Export/reset/demo-load/integration-unavailable |
| `orbit/templates/macros.html` | Shared labels/errors/status; presentation-only |
| `orbit/static/orbit.css` | Light semantic tokens, responsive/focus/reduced-motion; self-host assets |
| `orbit/static/forms.js` | Opsional hanya focus/pending state; form tetap berfungsi tanpa JS |
| `fixtures/demo/catalog.json` |8 course sintetis dan rules/availability/source version |
| `fixtures/demo/offerings.json` |2 offering, term/binding, assessment templates/scores demo jelas |
| `fixtures/demo/policy.json` | Threshold/assumptions sintetis; bukan aturan UI |
| `fixtures/demo/README.md` | Label, source/versions, expected golden, cara load/reset, tanpa data pribadi |
| `tests/__init__.py` | unittest discovery |
| `tests/helpers.py` | Temp DB/factory/snapshot assertions; oracle bukan memanggil fungsi yang diuji |
| `tests/test_map_domain.py` | MAP pure unit/negative/three-values/availability |
| `tests/test_grade_domain.py` | GRD exact math/boundary/target/tree |
| `tests/test_integration.py` | Services+DB, restart/conflict/rollback/receipts, INT and active P0 service tests |
| `tests/test_web.py` | Flask client, forms/error/capabilities/read models; manual UX counterpart |
| `tests/test_local_safety.py` | Loopback/Host/CSRF/debug/export/secrets safety |
| `tests/test_documentation.py` | ID/capability/config/docs invariants, CORE-T-008 |
| `tests/fixtures/negative.json` | Invalid graphs/tree/numeric payload, bukan active seed |
| `docs/architecture/` |14 Markdown dari paket ini, sumber baseline/link/hash; update changelog |
| `docs/qa/manual-ux.md` | Checklist UI dengan ID asli, build/evidence aktual |
| `docs/qa/evidence.md` | Hasil aplikasi aktual; initial NOT_RUN |
| `docs/team/teach-back.md` | Semua anggota × semua area, evidence pemahaman |
| `.github/workflows/tests.yml` | Opsional unittest CI; local command tetap independen |
| `instance/` | Runtime DB/secret/exports, **untracked**, bukan seed |

Nama conceptual service di ARCH-05 boleh berupa fungsi di `workspace.py/academic.py`, tidak harus belasan class. Penggunaan dataclass/typing seperlunya membantu kontrak, bukan generic repository framework. Fallback Streamlit akan mengganti `web/templates/static` dengan adapter yang direview; jangan membuatnya bersamaan.

## 3. Dependency direction dan konvensi

Domain hanya stdlib+domain. Services→domain+repository interface/store; web→services+DTO; repository→sqlite3+DTO serialization, tidak mengimpor web atau memanggil engine. Composition root saja mengetahui semua concrete adapters. Dashboard reuse domain functions pada satu snapshot, tidak mengimpor Flask route atau HTTP client.

snake_case fungsi/kolom, PascalCase DTO bila class, constant error enums. Type annotations pada batas service/domain; hindari dynamic dict bebas untuk state inti. Decimal strings dan UTC timestamp format dikendalikan satu serializer. Query values di-bind; nama table/column whitelist statis. Error exceptions ditangkap di adapter, domain outcomes unknown/impossible dikembalikan sebagai result. Logging: operation type/code/correlation_id saja; tidak dump forms/DB rows/score/token/secret/source document privat.

One public service write boundary per command. Tidak ada module-level global connection, mutable cache akademik atau side-effect seeding saat import. Konfigurasi local-demo strict; fixture load explicit+transaction. Commit mencakup code, meaningful tests dan docs perubahan yang relevan; bukan artifact runtime.

## 4. Vertical slice handoff

Urutan setelah approval: (0) environment spike + fixture/schema review; (1) pure MAP/GRD + golden tests; (2) workspace/DB dan service transactions; (3) one offering end-to-end + actual/scenario; (4) complete P0 UI/Dashboard + restart/export/reset; (5) quality/fresh-clone/teach-back/video. Detail estimates/dates di ARCH-10. Dua engine bisa dibagi anggota, tetapi DTO/revision/error contract disepakati bersama sebelum coding supaya integrasi bukan pekerjaan terakhir.

## 5. Draft AGENTS.md untuk repository nanti

Blok ini instruksi yang diusulkan untuk Codex pada tahap implementasi berikutnya; **tidak menjadi izin melakukan coding pada tugas dokumentasi sekarang**.

```markdown
# Orbit development contract

Read ARCH-INDEX.md, ARCH-11 approval evidence, ARCH-02 state contract,
ARCH-03/04 domain contracts and ARCH-07 traceability before any change.
Baseline is ORBIT PRD v0.2.1. Preserve original FR/BR/NFR/AC/test IDs.
Implement only the 48 P0 FR and active quality gates. All P1/P2 stay off,
including full rebase, GPA/trends, search, GDE/closeout, SSO and public hosting.

Do not start implementation until the human has reviewed this architecture
and recorded scope/stack, RV-14 capacity, RV-15 novelty, runtime and fixture
approval or an explicit bounded spike authorization. Do not treat silence as approval.
For an authorized slice, complete the work and checks without repeated permission
requests; request a decision only for a material scope/contract change.

Python owns graph/tree/math/validation/state/aggregation. Domain imports no
Flask/sqlite3; routes call services; repositories do not infer academic outcomes.
Use exact numeric contracts, parameterized queries, atomic UoW, revision checks
and operation receipts. Never turn a projection into actual automatically.
Do not bypass stale rejection or BRP structure lock to make a demo work.

Write meaningful golden/negative/boundary tests for the chosen slice first.
Use original test IDs in test names or explicit mapping. Run relevant checks,
record actual results, and never claim tests passed without execution evidence.
Preserve valid form input on errors and provide keyboard/unknown/empty states.

Use synthetic fixtures with provenance. Do not invent university rules, identities,
API availability or permission. No secrets, campus passwords, runtime DB/exports
or personal academic records in GitHub. Bind loopback only, debug off for demo;
no public deployment, tunnel, SSO integration or speculative feature.

Each PR explains requirement IDs, behavior, tests and remaining limitations.
Human code review and cross-module teach-back are required before merge/release.
Do not merge or publish merely because code generation completed.
If a source/requirement conflicts, document the conflict and affected tests;
do not silently change priorities or academic semantics.
```

Human review before merge/release is rekomendasi workflow tim dalam paket ini, bukan aturan eksplisit dosen tentang pull request. Kewajiban dosen adalah kontribusi aktif dan pemahaman mendalam seluruh kode.

## 6. Git workflow dan change control

Gunakan branch pendek `map/...`, `grade/...`, `data/...`, `ui/...` dengan issue/PR menyebut requirement IDs. Reviewer lintas area mengecek invariants/test, bukan hanya style. Merge workflow harus mempertahankan atribusi kontribusi jujur; jangan satu unggahan akhir dari satu akun atau commit kosong mengejar angka. Panduan tidak menentukan minimum commit. Pair programming boleh dengan attribution yang benar dan tiap anggota tetap punya kontribusi aktif yang dapat ditelusuri.

Sebelum menyelesaikan conflict: baca kontrak canon, diskusikan perubahan semantic dengan reviewer, rerun test terkait lalu integration. Jangan resolve conflict dengan membuang test/revision guards. Scope change mencatat alasan, FR/BR/AC/test terdampak, capability, effort dan approval manusia di changelog; perbarui RTM dan ADR sebelum implementasi fitur itu. CORE-FR-008 berlaku juga pada dokumen ini.

## 7. Teach-back seluruh kode

Peran A MAP, B GRD, C data/UI; bila 4 anggota D mengambil integration/service/test dan sebagian UI, bukan video saja. Rotasi reviewer A↔B dan C↔D (atau C mereview kedua engine pada tim 3). Semua anggota menjelaskan: truth table/cycle/delay; K36/target 78/rounding; transaction/stale/reset/history; route→service→repository→view; negative test dan fresh-clone run. Catat demo/pertanyaan/bug kecil yang diperbaiki, bukan hanya tanda hadir. Sisihkan sesi bersama untuk membaca setiap file; area spesialisasi tidak menjadi silo pemahaman.

Alternatif satu orang mengintegrasikan seluruhnya menjelang deadline ditolak karena risiko teknis dan kontribusi. Review/teach-back termasuk estimates, tidak dibebankan sebagai waktu tak terlihat.

## Risiko, dependensi, dan bukti terbuka

Blueprint memiliki banyak file karena tanggung jawab/test/presentation dipisah, tetapi satu proses dan satu store. Tim boleh menggabungkan file kecil tanpa merusak boundary dan traceability. Tidak ada GitHub repo/anggota nyata yang telah diperiksa.

**Traceability:** CORE-AC/T-008/103; INT-T-010; seluruh test paths ARCH-07 direncanakan di tree ini; DDP ketentuan kontribusi/pemahaman. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** RV-11 identitas tim/Asdos, RV-14 jam/skill, RV-15 konsep; nama/peran aktual diisi tim, bukan diasumsikan. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
