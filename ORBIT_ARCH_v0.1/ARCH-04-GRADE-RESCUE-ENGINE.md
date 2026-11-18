# ORBIT · ARCH-04 · GRADE RESCUE ENGINE

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Menentukan matematika nilai, target, precision, dan jalur actual confirmation yang dapat diuji secara deterministik.

**Scope:** BRP bertingkat, skor leaf, K/O/U, bounds, target, what-if dan final aktual per course.  
**Non-goals:** IPS/IPK/tren, nonlinear policy solver, migrasi BRP berskor, atau auto-finalization dari proyeksi.

**Sumber:** PRD-03 GRD-FR-001–007/010/011/012/014/016/018; GRD-BR-001–007/010/011; GRD-NFR-001–003; Readiness DDP-T-03–07. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. Model angka dan input

Schema input numerik selalu string, bukan JSON number float. Parser menerima titik desimal kanonik; UI Indonesia boleh menormalkan satu koma sebagai desimal tanpa thousands separator. Ambigu seperti `1,000.5` ditolak. Tolak NaN/Infinity, negative score, earned>max, max≤0, target di luar 0..100, dan bobot di luar 0..100 atau lebih dari 2 desimal persen. Field kosong score→None; string 0→nilai 0 sah. Missing/absent bukan 0 tanpa pencatatan eksplisit dan provenance.

**Rekomendasi batas teknis:** maksimal 24 digit signifikan/12 desimal untuk earned/max/target; bobot tetap 2 desimal persen. Batas panjang form/AST disebut sebelum submit dan invalid tidak dipotong/round diam-diam. Ini batas input demo, bukan aturan penilaian akademik; bila fixture membutuhkan lebih, ubah ADR/test sebelum mengaktifkannya. Target granularity adalah asumsi unit skor yang mungkin diperoleh, terpisah dari precision nilai aktual yang dilaporkan.

Decimal dari string digunakan untuk validasi dan representasi exact. Weight persen→integer basis points: 20%=2000 bp, 50%=5000 bp. Proporsi efektif dan score normalization menggunakan Fraction dari integer/Decimal exact. Tidak memakai float, SQLite REAL, atau pembulatan ke 6 desimal untuk keputusan. Formatter Python mengubah rational ke 2 desimal **round-half-up** menggunakan quotient/remainder integer, sehingga pecahan berulang tidak berubah threshold karena context Decimal. Semua angka exact pada response disimpan `{numerator: string, denominator: string}`, denominator>0; formatted text berbeda field. Ini desain, belum fungsi yang diimplementasikan.

## 3. validate_brp dan effective weights

Input: `{brp_id,enrollment_id,source,rule_version,nodes:[{id,parent_id,kind,label,weight_bp,max_score?,granularity?}]}`. Satu root group weight 10000; every non-root punya satu parent group, semua node reachable, tidak cycle, tidak shared leaf identity, leaf tidak punya anak. Setiap group aktif punya anak dan sum bobot anak **tepat 10000 bp**; zero weight boleh tetapi tidak menyelesaikan sum group kosong. Parent tanpa distribusi anak tidak dibagi rata.

Traverse dari root membawa weight 1. Leaf weight adalah produk `(child.weight_bp/10000)` sepanjang jalur; hanya leaf masuk agregasi. Root kuis 20/UTS30/UAS50; kuis Q1/Q2 masing-masing 50→leaf 10/10/30/50%. Tidak menambah parent kuis 20 lagi.

Precondition edit struktur: belum ada score row yang disimpan. Setelah pertama save score, `locked=1` dan tidak dibuka kembali dengan mengosongkan skor. Edit earned diperbolehkan; edit parent/bobot/max/granularity/identitas struktur ditolak STRUCTURE_LOCKED dengan data lama utuh. Sebelum lock, simpan versi baru immutable dan pertahankan versi lama superseded. Migrasi ber-mapping adalah GRD-FR-020 P2. Jika source template berasal dari kelas/term lain, jangan mengikatnya sebagai verified. Pengguna dapat memilih copy eksplisit menjadi BRP personal draft pada enrollment tujuan, dengan source asal tetap terlihat dan label NEEDS_VALIDATION; validasi tree dilakukan ulang. Ini tidak memindahkan score lama dan tetap tunduk pada structure lock.

## 4. summarize_grade

Untuk leaf i, wᵢ proporsi efektif, eᵢ earned, mᵢ max>0, sᵢ=100 eᵢ/mᵢ. Set known berisi leaf dengan earned≠None (termasuk nol). Canon baseline:

\[
K=\sum_{known}w_i s_i,\quad O=\sum_{known}w_i,\quad U=1-O.
\]

**O adalah observed weight**, bukan observed average. Observed average=K/O jika O>0; unavailable bila O=0. Coverage ditampilkan O×100%. Bounds model linear tanpa syarat lain: `[K, K+100U]`. Bounds bukan confidence interval statistik atau prediksi bahwa semua unknown nol/100.

| Kasus | K | O / U | Observed | Bounds / makna |
| --- | --- | --- | --- | --- |
| Q1=80,Q2=100,UTS=60,UAS unknown |36|0.5 /0.5|72|36–86 |
| Semua unknown |0|0 /1|unavailable|0–100, tidak tampil rata-rata 0 |
| Semua known 0 |0|1 /0|0|0–0, berbeda unknown |
| Semua known, final model 75 |75|1 /0|75|75–75, tetap bukan actual final otomatis |
| UAS what-if 90 pada fixture |81|1 /0 pada overlay|81|81–81 pada overlay; actual tetap 36–86 |

Pada overlay, O adalah bobot input terisi untuk kalkulasi scenario; bukan seluruhnya observasi aktual. Sertakan `actual_coverage` dan `assumed_coverage` terpisah (golden: 0.5 dan 0.5). UI menamai angka 81 sebagai proyeksi what-if, bukan observed average aktual. Ringkasan actual tetap memakai O=0.5 dan observed=72.

Output `GradeSummary`: enrollment_id, brp_id/rule_version, K/O/U exact, observed nullable, bounds, missing_leaf_ids, nonlinear_unresolved[], result_kind (`actual_inputs_summary` atau `what_if_projection`), source refs dan input_revisions. Jika tree invalid, tidak ada ringkasan numerik baru. Tidak ada model prior/default prediction dari rata-rata observed.

## 5. solve_target

Input `{summary,target: numeric string | letter,policy_binding?,remaining_granularity?}`. Target huruf hanya dikonversi jika threshold policy cocok offering/kelas/term dan source binding; tidak ada fallback A=85. Policy unknown atau nonlinear rule unsupported mempertahankan target angka sebagai **numeric-only**, tanpa klaim kelulusan resmi. Threshold demo A≥85/B≥70<85/C<70 adalah policy sintetis, tidak otomatis aturan lulus.

Untuk target numeric T dan U>0, raw required remaining weighted average `R=(T−K)/U`. Jika R≤0→`already_met_in_model`; 0<R≤100→`conditionally_feasible`; R>100→`impossible_in_model`. Saat U=0, bandingkan K≥T: `met_in_model` atau `not_met_in_model`, required=null, tanpa pembagian nol. Impossible adalah hasil domain normal, bukan input error HTTP.

| Input dari golden | Oracle exact | Pesan/keputusan |
| --- | --- | --- |
| T75 |(75−36)/0.5=78|Perlu rata-rata sisa 78; karena hanya UAS unknown/max 100, skor UAS minimal 78 |
| T90 |108; upper 86|Tidak tercapai dengan model ini; jangan clamp required menjadi 100 |
| T75.01 |78.02|Granularity 1→79; granularity 0.01→78.02 |
| T30 |−12|Sudah memenuhi target numerik model; rekomendasi minimum 0, raw−12 tetap dapat ditelusuri |
| U0,K75,T75/T80 |met /not_met|required=null, bukanInfinity |
| Policy A85, x 84.995/x 85 |B /A|84.995 dapat berformat 85.00 tetapi klasifikasi tetapB; tampil catatan precision |

Jika hanya satu unknown leaf max m dengan quantum g pada skala earned: `earned_required = R*m/100`, `suggested = ceil(earned_required/g)*g`. Contoh granularity di tabel memakai max 100. Bila suggested>max, laporkan `infeasible_at_selected_granularity` walau model continuous feasible. Bounds tetap bounds continuous 0..100 yang dilabeli; jangan menyamakan feasible continuous dengan attainable discrete.

Jika lebih dari satu leaf unknown, R adalah **rata-rata berbobot sisa**, bukan minimum setiap ujian. Tanpa pembagian asumsi eksplisit, keluaran tidak menyatakan skor minimum per komponen. Pengguna boleh memasukkan what-if pada beberapa leaf dan menghitung ulang sisa. Tidak mencari kombinasi optimum. Granularity tidak mengubah actual input atau membulatkan actual 84.995 menjadi 85.

## 6. What-if dan actual confirmation

`calculate_what_if(snapshot,scenario)` menggabung overlay per node di memori. Unknown aktual tetap tersimpan None; score overlay 90 menghasilkan 81 tetapi tidak menulis assessment_score/actual_final_revision dan tidak mengeluarkan ActualFinalGradeChanged. Overlay scope harus BRP/node aktif milik enrollment yang sama; base revision berbeda→STALE_SCENARIO.

`preview_actual_final` menerima final numeric/letter/outcome yang **diketik/dipilih eksplisit**, source, enrollment, expected token dan correction_reason bila revisi. Tidak mengambil nilai predicted sebagai default field. Outcome passed/failed dapat dilaporkan eksplisit dengan source user_reported; bila policy applicable bertentangan dengan nilai/letter yang dimasukkan, tampil konflik dan tahan confirm. Tanpa rule konversi outcome, numeric saja memberi outcome unresolved; jangan menyimpulkan lulus dari angka.

Preview read-only mengembalikan payload kanonik, dampak (MAP/Dashboard refresh, scenario stale), source label dan token terikat hash. Adapter menandatangani preview; confirm wajib token valid + input sama + expected revision current. Pada confirm service append actual final, source_revision+1, histori lama tetap. Cancel nol write. Koreksi memerlukan reason; stale preview ditolak dan meminta preview ulang. Riwayat enrollment yang dibuat dari PRO-FR-005 memakai jalur confirm yang sama dalam satu transaksi, tidak service penulisan actual kedua.

## 7. Kontrak operasi dan error

| Fungsi konseptual / layer | Input → output | Invariant / error | Test |
| --- | --- | --- | --- |
| validate_brp · domain | Tree→ValidatedTree/errors by path | cycle/shared leaf/10000 exact; no partial tree | GRD-T-001/002/018; DDP-T-03/06 |
| normalize_score · domain | earned/max strings→rational or unknown | finite range; unknown≠0 | GRD-T-003/018; DDP-T-04 |
| summarize_grade · domain | Tree+scores→GradeSummary | leaves only; consistent exact outputs | GRD-T-004/014/101 |
| solve_target · domain | Summary+target+policy→TargetResult | U0 safe; unknown letter; ceil quantum; full precision threshold | GRD-T-005/006/007/012/016; DDP-T-05 |
| save_scores · service | command token/op_id + node inputs→MutationResult | active BRP leaf; atomic save/lock/revision; invalid field data retained | GRD-T-003/103 |
| save_grade_overlay · service | scenario + map node→earned→MutationResult | no actual write; stale rejected | GRD-T-011; INT-T-003 |
| preview/confirm_actual · service | explicit final→preview→confirmation result | stale rejection, append-only correction, no GDE | GRD-T-010; DDP-T-07; INT-T-013 |

All-or-nothing save berlaku untuk satu form batch skor; field sah dipertahankan di form saat satu field invalid, tetapi tidak disimpan separuh. Request format, DB errors dan domain unknown dibedakan oleh ARCH-05.

## 8. Kompleksitas dan pilihan minimal

N=jumlah assessment node; tree validation, flatten dan aggregation masing-masing O(N) kunjungan; ruang O(N), stack worst O(N). Kalkulasi target setelah summary O(1), lookup policy O(P) untuk P threshold kecil atau binary search bila terurut; tidak perlu optimasi untuk policy demo. Fraction memakai big integers: waktu bit-arithmetic tergantung digit/depth, sehingga O(N) adalah jumlah operasi dengan input size bounded, bukan klaim biaya aritmetika konstan untuk angka arbitrer. Batas teknis 24 digit/12 desimal dan tree depth 16 diusulkan; benchmark 300 leaf memakai depth wajar dan harus dicatat. Iterative DFS menghindari kegagalan rekursi pada input malformed.

Alternatif float+epsilon, SQL SUM atas REAL, dan menyimpan hasil formatted sebagai input ditolak. Pilihan exact menjaga golden contract, tetapi tim wajib memahami parsing, rational arithmetic dan rounding; jika terlalu berat, alternatif Decimal harus membawa pembuktian boundary yang setara sebelum ADR diubah.

## Risiko, dependensi, dan bukti terbuka

Kebijakan nyata/BRP belum tervalidasi. Hasil conditional numeric tidak boleh dijual sebagai prediksi lulus. Precision boundary dan nonlinear flags perlu test; quantum adalah asumsi eksplisit, bukan fakta ujian.

**Traceability:** Semua 13 GRD P0 dan AC/T pasangannya; GRD-AC/T-101–103; DDP-T-03–07; INT-T-003/013. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** OD-02 BRP/policy sintetis, OD-03 numeric model/limits dan teach-back; RV-03/04 memblokir klaim aturan nyata, bukan demo. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
