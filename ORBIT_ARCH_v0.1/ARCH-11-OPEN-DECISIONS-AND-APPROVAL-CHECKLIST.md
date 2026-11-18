# ORBIT · ARCH-11 · OPEN DECISIONS AND APPROVAL CHECKLIST

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Menyajikan keputusan yang masih perlu bukti manusia dengan konsekuensi yang jelas, sehingga arsitektur dapat ditinjau tanpa klaim siap implementasi.

**Scope:** open register, approval scope, source conflicts, change control dan Engineering Readiness Verdict.  
**Non-goals:** menganggap dokumen sebagai persetujuan dosen, mengisi evidence fiktif, meminta izin ulang untuk pekerjaan dokumentasi yang sudah diotorisasi.

**Sumber:** RESEARCH-AND-VALIDATION-REGISTER RV-01–16; errata handoff; seluruh ADR; CORE-FR-008; Panduan DDP1 dan Prompt 02. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. Register keputusan/evidence

Owner adalah **peran sementara**, bukan identitas anggota yang belum diketahui. Semua tenggat di bawah target internal WIB; aturan tugas tetap deadline 10 Des 23.59. “Sebelum implementasi” tidak menutup kemungkinan bounded spike yang diotorisasi manusia untuk memperoleh bukti runtime.

| ID | Pertanyaan/keputusan | Status dan dampak | Owner / target internal | Evidence untuk menutup |
| --- | --- | --- | --- | --- |
|RV-14|Berapa jam/tanggal dan skill Python/Git/web aktual 3–4 anggota?|OPEN; mencegah komitmen 86–116 jam tanpa kapasitas|Semua anggota,19 Nov sebelum komitmen delivery|Daftar availability per tanggal, total usable 75%, skills dan pembagian/review; estimasi hasil spike |
|RV-15|Konsep berguna mana benar-benar di luar kelas?|OPEN; novelty rubrik belum terbukti|Tim+Asdos,19 Nov atau bimbingan terdekat sebelum claim|Silabus/lab yang dibandingkan, konsep terpilih dan catatan bimbingan; semua dapat menjelaskan |
|OD-01|Flask default atau Streamlit fallback, versi/runtime/device?|OPEN; adapter/pin final belum ditetapkan|C+reviewer,19 Nov / setelah bounded spike diizinkan|Versi OS/Python/sqlite3/dependency, setup/form/store/restart smoke pada perangkat tim, alasan pilihan |
|OD-02|Fixture 6–12 course/2 offering, policy/BRP/availability/attempt rule sintetis disepakati?|OPEN; oracle implementasi belum materialized/reviewed|A+B,19–20 Nov|JSON fixture/hash, source labels, review golden math/graph, unknown/unsupported cases; tanpa data nyata |
|OD-03|Exact numeric model, limit 24 digit/12 desimal/depth 16 dan granularity dapat dipahami?|OPEN; arsitektur merekomendasikan, belum hasil teach-back|B+reviewer A,20 Nov|Penjelasan integer bp/Decimal/Fraction/half-up/ceil, golden 84.995/75.01 dan batas input; ubah ADR bila perlu |
|OD-04|Schema/revision/reset/preview security diterima dan bisa diuji?|OPEN; desain tersedia, feasibility belum diuji|C dengan A/B,20 Nov review;28 Nov bukti integrasi|Review 17 tabel, satu writer/UoW, stale/rollback/idempotency/restart/reset test evidence setelah implementasi |
|OD-05|Adaptasi Figma light/list dan token final?|OPEN detail style; struktur P0 jelas|C+reviewer,25–28 Nov|Review layar aktual terhadap PRD-09, contrast/keyboards 320/zoom 200, label future off |
|RV-11|Identitas kelompok resmi 3–4 orang dan Asdos?|OPEN; role placeholders saja|Koordinator tim,19 Nov|Daftar resmi; izin publikasi nama/link tim bila diperlukan |
|RV-12|UX/performance pada perangkat referensi?|OPEN, release gate bukan startup gate|QA lintas anggota,2 Des|30 samples/raw timings dan manual UX/contrast build aktual |
|RV-16|Masalah pengguna terbukti dari kebutuhan nyata?|OPEN; membatasi klaim manfaat|Product role,20–24 Nov|Catatan kebutuhan sukarela tanpa data sensitif, ringkasan painpoint dan batas sampel |
|RV-02/03/04|Kurikulum, BRP, kebijakan nilai nyata applicable?|OPEN; blok klaim resmi/data nyata, bukan demo sintetis|Academic curator, sebelum future real-data mode|Dokumen resmi/versi/kelas/term/izin yang relevan; tidak mengarang mapping |
|RV-05/06|SSO/SLCM contract dan izin?|OPEN FUTURE; integrasi off|Tim+institusi, sebelum integrasi future|Izin dan API/protocol contract yang benar-benar tersedia |
|RV-07/08/09/10|Privacy/rights/community/career/production operations?|OPEN FUTURE; P0 tanpa dependency ini|Owner future, sebelum feature activation|Review sumber/hak/consent/operator dan test capability terkait |
|RV-13|Perubahan aturan/sumber berikutnya?|OPEN MONITORING; tidak ada auto-update|Product role, setiap perubahan sumber|Diff source/version+impact FR/BR/AC/test; approval baseline berikutnya |

RV-01 aturan tugas telah terverifikasi dari PDF 5 halaman; ini closure dokumentasi, bukan bukti submission atau persetujuan scope oleh Asdos. Official release date 5 Nov bukan 18 Nov; tanggal paket ini adalah tanggal arsitektur.

## 3. Ambiguitas yang ditangani tanpa mengubah baseline

| Isu | Penyelesaian dalam arsitektur | Perlu revisi PRD? |
| --- | --- | --- |
|Prompt memakai frasa K/O/U seolah O=observed average|Canon GRD-BR-004:O adalah observed weight, observed average=K/O; formula/golden tetap|Tidak; klarifikasi istilah |
|P0 FR campuran menyebut rebase/migrasi/visi lengkap|Hanya stale/reset P0 pada MAP006; lock struktur GRD001; full rebase/migration future|Tidak; mengikuti baseline/errata |
|PUB003 melarang demo menjadi actual user, sementara GRD demo mencatat actual|Namespace demo terpisah, is_synthetic=true di semua record/UI/export; “actual” hanya status input dalam demo, tidak catatan nyata|Tidak; penjelasan invariant provenance |
|Retake atau rule unsupported tidak punya policy jelas|Unknown+reason, tidak memilih highest/latest otomatis; fixture rule sintetis eksplisit jika diperlukan|Tidak untuk demo; OD-02 wajib review |
|Batas numeric/depth/rational belum ditentukan PRD|Rekomendasi implementasi terukur ADR-09/OD-03; tidak silently round/truncate|Review arsitektur; jika menolak input yang wajib didukung baseline, perubahan harus diselesaikan sebelum coding |
|Metadata Figma tersedia sebagian, style detail tidak|VISUAL_REFERENCE_PARTIAL, gunakan PRD-09; jangan klaim token/contrast diperiksa|Tidak; OD-05 untuk evidence visual |
|48 FR mungkin melebihi kapasitas|Estimasi baru 86–116; RV-14 terbuka, tidak menghapus requirement|Revisi scope hanya bila keputusan manusia berikutnya memang mengubah FR |

Tidak ditemukan kontradiksi P0 fundamental yang memaksa dependency kampus/cloud/closeout. Keterbatasan saat ini adalah bukti kesiapan tim/perangkat/fixture dan keputusan detail, bukan izin mengubah prioritas diam-diam.

## 4. Checklist approval manusia

Checklist belum dicentang berarti belum ada bukti persetujuan pada percakapan ini; bukan permintaan agar pengguna mengonfirmasi setiap langkah dokumentasi.

- [ ] Review scope 48 FR P0 dan semua subcapability future yang tetap off.
- [ ] Pilih ADR-01 default/fallback berdasarkan RV-14 dan OD-01; catat versi setelah smoke, bukan sebelumnya.
- [ ] Konfirmasi RV-15 dari materi kelas/bimbingan dan rencana teach-back setiap anggota.
- [ ] Review fixture, precision/model/granularity, retake/unknown, source labels; tutup OD-02/03.
- [ ] Review schema/transaksi/history/idempotency/reset dan local-request protection OD-04.
- [ ] Sepakati effort/jadwal/review/video; tidak menganggap seluruh tanggal tersedia.
- [ ] Beri otorisasi tahap implementasi atau bounded spike dengan scope konkret, owner dan exit criteria.

Approval record yang kelak diisi: tanggal WIB, nama reviewer manusia, versi/hash paket, decisions accepted/modified, evidence refs, scope authorized, remaining conditions. Persetujuan tim untuk stack bukan otomatis persetujuan akademik Asdos; catat keduanya sesuai bukti nyata bila ada.

## 5. Instruksi handoff konkret setelah approval

Buka repository implementasi yang diberikan/dibuat pada tahap berikutnya, tempatkan 14 Markdown di `docs/architecture/`, simpan rujukan baseline v0.2.1/hash, dan buat AGENTS dari ARCH-08 setelah review. Mulai **Slice 0**: runtime/fixture/schema spike yang disetujui; laporkan environment dan hasil nyata, lalu update OD-01/02/04 serta estimasi. Lanjut pure-domain MAP/GRD dengan test ID asli sebelum wiring UI. Setiap PR merujuk FR/AC/test, human review, dan teach-back. Setelah integration/UX gates lulus, baru freeze/repo/video. Jangan menyertakan public deploy atau fitur future sebagai pekerjaan tersirat.

Jika hanya bounded spike yang disetujui, berhenti pada exit criteria spike dan laporkan keputusan berikutnya; jangan memperluas menjadi seluruh aplikasi. Jika implementasi P0 telah diotorisasi dan kondisi terpenuhi, kerjakan slice yang disetujui tanpa meminta izin berulang untuk perubahan rutin yang diperlukan.

## 6. Engineering Readiness Verdict

**READY FOR ARCHITECTURE REVIEW.** Paket mendefinisikan seluruh 48 P0, data/state/algoritma, service/UI contracts, test plan, blueprint dan delivery plan; baseline tetap utuh.

**CONDITIONAL FOR IMPLEMENTATION — NOT APPROVED.** RV-14/RV-15/runtime/fixture dan review manusia masih OPEN. Tidak ada code/app tests/benchmark/deploy/repo/video yang selesai pada tahap ini. Ini tidak sama dengan BLOCKED karena konflik produk fundamental; jika review berikutnya menemukan kontradiksi atau kapasitas tidak cukup, catat blocker dan revisi rencana sebelum mulai.

Alternatif menandai “ready” hanya karena dokumen lengkap ditolak. Evidence gate melindungi ketepatan komitmen, bukan alasan menghentikan pekerjaan arsitektur yang sudah diotorisasi.

## Risiko, dependensi, dan bukti terbuka

Pemilik keputusan nyata belum diketahui; tanggal target bukan komitmen anggota. Approval tidak boleh diisi oleh agen atas nama tim. Semua risiko kritis dan mitigasi berada di ARCH-10.

**Traceability:** CORE-AC/T-008/103; seluruh 48 FR P0; quality/release gates ARCH-07/10; dokumen ini menyediakan review checklist bukan hasil aplikasi. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** Semua rows OPEN di atas; tindak lanjut paling dekat adalah review paket dan evidence RV-14/RV-15/OD-01/02. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
