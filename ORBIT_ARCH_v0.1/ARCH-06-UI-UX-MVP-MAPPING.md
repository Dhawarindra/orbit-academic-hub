# ORBIT · ARCH-06 · UI UX MVP MAPPING

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Menerjemahkan identitas Orbit dan PRD-09 ke layar P0 yang dapat digunakan tanpa mengaktifkan fitur future dari mockup.

**Scope:** page inventory, Figma adaptation, state/form behavior, aksesibilitas dan responsive.  
**Non-goals:** mengedit Figma, pixel-perfect promise, dark mode, global search, data IPK/tren/insight rekaan.

**Sumber:** PRD-09 UX-FR-001–008, UX-BR-001–008, UX-NFR-001–003; PRD-11 PUB-FR-002/003; CORE-FR-007; Figma Dashboard 11:22/Roadmap 11:183. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. Bukti visual dan keputusan

Referensi [Dashboard 11:22](https://www.figma.com/design/uGYiD2ePUEiC7fu52Hp7uL?node-id=11-22) tersedia sebagai metadata frame 1440×980: navigation rail, wordmark, statistic cards, Course focus, Grade performance chart, Your priorities dan Academic community. Referensi [Roadmap 11:183](https://www.figma.com/design/uGYiD2ePUEiC7fu52Hp7uL?node-id=11-183) berhasil dilihat sebagai screenshot 1680×980: tema gelap, sidebar, judul, tab peta/daftar, filter semester, kolom course, legenda dan ajakan simulasi. Akses lanjutan terkena limit layanan; screenshot Dashboard dan inspeksi token/style rinci tidak dijadikan bukti terverifikasi pada tugas ini.

Status **VISUAL_REFERENCE_PARTIAL**: metadata Dashboard dan visual Roadmap cukup untuk adaptation map; detail style belum tervalidasi. Untuk detail Dashboard yang belum terbaca, pakai kontrak tekstual PRD-09, bukan klaim layer/color yang tidak diinspeksi. Tidak ada perubahan pada file Figma. Nama dan edge course dalam mockup tidak diimpor sebagai data kurikulum.

Keputusan baseline: tema terang di seluruh P0. Wordmark Orbit, aksen, hierarki navigasi, pola kartu dan bahasa produk dipertahankan. Hex final OPEN sampai contrast test; tidak menebak nilai warna dari screenshot. Alternatif dark per halaman ditolak karena tidak konsisten dan dark global P2. List Roadmap adalah implementasi wajib; graph interaktif opsional future, tidak dibutuhkan untuk semua relasi terlihat.

## 3. MVP visual adaptation map

| Referensi | Perlakuan P0 | Alasan / traceability |
| --- | --- | --- |
| Wordmark/navigation rail, Dashboard 11:23–55 | Pertahankan brand; beri teks label/accessible name; Ringkasan/Roadmap/Nilai & Target | UX-FR-001/004, UX-BR-002 |
| Global search 11:56–60 dan bell 11:61–64 | Sembunyikan control aktif | Search P1, notifikasi future; bukan dependency P0 |
| Avatar 11:65–66 | Label “Workspace demo lokal”, tanpa nama/foto orang rekaan | AUTH-FR-014, PUB-FR-003 |
| Semester control 11:70–74 | Pilih term explicit; unknown/default empty jelas | PRO-FR-001/004, UX-FR-001 |
| Tiny statistics 11:75/78/81/84 | Metrik P0 yang ada: course aktif, SKS terkonfirmasi dengan coverage, rencana dan target course; empty bila data tak ada | CORE-FR-007, UX-FR-002; tidak mengganti IPK dengan angka sintetis tanpa label |
| Course focus 11:87 | Offering list ke skor/target; search-in-focus dan Vault bar 11:119 dihilangkan dari P0 | GRD P0; tidak ada Vault/search implisit |
| Grade performance chart 11:124 | Ganti area dengan tabel ringkasan K/coverage/bounds/target per offering | UX-FR-002/005; tren GPA P1 nonaktif |
| Your priorities 11:155 | Daftar warning engine + tautan input asal; tanpa guidance ranking | UX-FR-002; GDE P2 off |
| Academic community 11:167 | Sembunyikan di alur core; visi tetap di dokumen future | SNR/VLT/CAR off |
| Roadmap judul/legenda/status | Pertahankan struktur bahasa dan penjelasan; light theme | MAP-FR-008, UX-BR-001 |
| Roadmap delapan kolom course | Ganti list grouped term untuk 6–12 course fixture; hanya term data yang ada | MAP-FR-001/008; tidak mengklaim delapan semester kurikulum resmi |
| Roadmap tabs/filters | List sebagai default, term/category sederhana jika tersedia; tidak menampilkan tombol graph kosong yang seolah aktif | UX-FR-003/005; tanpa scope renderer tambahan |
| “Simulasikan sebelum IRS” | Banner simulasi, form delay/chosen OR/cap; keterangan bukan persetujuan IRS | MAP-FR-004/005/006/011 |

Pilihan menyembunyikan future control membuat halaman tetap fokus; informasi visi lengkap ada di dokumen scope. Bila tim menampilkan label “Direncanakan”, jangan beri link/button operasional atau form palsu.

## 4. Page inventory dan field minimum

| Halaman | Fields/output wajib | Actions / source |
| --- | --- | --- |
| Onboarding/profile | program/cohort nullable, curriculum demo/unknown, term (pilih atau buat manual), checkpoint, scope badge | Simpan; Lewati dulu; lanjut dari checkpoint; PRO001–003 |
| Tambah offering/history | term, manual label atau course binding, attempt; history explicit final/source/outcome | Buat enrollment; history preview→confirm; PRO004/005,GRD010 |
| Nilai & Target | Offering picker, BRP group/leaf editor sebelum lock, score/max/source, target numeric/letter, K/O/U/bounds | Simpan BRP/skor/target; what-if; actual preview/confirm; GRD P0 |
| Roadmap list/detail | Course/SKS/source, progress/planned/eligibility terpisah; setiap leaf reason, downstream | Pilih course/term; keyboard buka detail; MAP001–009/012 |
| Scenario | Banner; plan/score overlays; chosen OR; cap personal; assumptions; base revision | Simpan; tunda; reset/pilih ulang; MAP006/011,GRD011 |
| Ringkasan | DashboardVM persis ARCH-05; source links | Navigasi ke input, tidak ada edit data tersembunyi |
| Data lokal | Owner/demo label, data counts, export, reset consequences, integrasi unavailable | Export; preview/confirm reset; load demo eksplisit; AUTH010/014/015 |

Semua halaman menampilkan status produk independen mahasiswa dan data sintetis sebelum input. Tidak ada password kampus, email/login palsu, atau klaim API tersedia. Two offerings hanya target fixture demonstrasi; form tetap menangani empty workspace.

## 5. State/form contract

Empty: instruksi tindakan pertama, bukan kartu berisi nilai contoh otomatis. Unknown: tampil “belum diketahui” beserta reason; jangan dash tanpa label atau 0. Not applicable: jelaskan mengapa metrik tak berlaku. Invalid: summary di awal form berisi link ke field, label terhubung melalui id/aria-describedby; simpan draft field lain di response 422. Pending: teks “Menyimpan…” jika JS dipakai; disable double-submit membantu UX tetapi idempotency tetap server. Saved hanya sesudah commit. Failed: retry mempertahankan operation_id/payload. Stale: banner dan action refresh/preview ulang, tidak menimpa input lama diam-diam.

Confirm actual adalah halaman/form review eksplisit (tidak harus modal), menampilkan nilai yang pengguna masukkan, provenance, outcome, dampak MAP dan revision. Koreksi mencantumkan alasan serta final sebelumnya. Cancel kembali tanpa write. Confirm reset workspace menyebut semua runtime termasuk histori akan dihapus, seed dan ekspor yang sudah diunduh tidak dihapus. Reset scenario menyebut hanya overlay dibersihkan. Dua tindakan ini tidak memakai label “Reset” tanpa objek.

## 6. Responsive dan accessibility

Baseline test viewports 360/768/1280 px ditambah NFR reflow 320 CSSpx dan zoom 200%. Satu kolom di sempit, rail menjadi navigation yang tetap berlabel; tidak ada horizontal **page** scroll. Tabel kompleks boleh punya region overflow berlabel tetapi seluruh data/action memiliki alternatif list. Filter term tidak hilang saat pindah halaman.

Gunakan native label/input/button/select, heading berurutan, skip link, focus ring terlihat. Tab/Shift+Tab/Enter berfungsi; Escape menutup dialog jika memakai dialog dan fokus kembali ke trigger. Halaman konfirmasi biasa lebih sederhana daripada custom modal. Status mempunyai teks/ikon selain warna; alasan prasyarat tidak bergantung hover. Tampilan grayscale masih membedakan passed/planned/unknown.

Token semantik: canvas/surface/text-primary/text-muted/border/accent/success/warning/danger. Body 16 px, caption≥12 px, heading 24–36 px, line-height 1.4–1.6, spacing 4/8/12/16/24/32 dan touch target utama 44×44 CSSpx adalah target produk. Contrast target normal≥4.5:1, large≥3:1, nontext essential≥3:1. Ukur pasangan computed foreground/background aktual (termasuk alpha), catat ratio dan states; screenshot saja tidak membuktikan contrast. Reduced-motion menonaktifkan animasi nonesensial; UI boleh tanpa animasi.

## 7. Acceptance dan batas bukti

Review dengan keyboard dari profile→offering→BRP invalid→score/target→scenario→actual preview/cancel/confirm→export/reset. Periksa label unknown/current/actual/scenario dan source links di setiap langkah. Test fallback Streamlit wajib menjalankan checklist yang sama pada widget aktual; tidak menganggap framework otomatis lulus WCAG.

Tidak ada layout aplikasi yang dibuat atau browser test dijalankan pada tahap ini. Keputusan visual mengurangi control future, tidak mengganti identitas Orbit. Saat data atau hasil salah, perbaiki engine/contract dahulu; jangan menutupnya dengan angka statis di UI.

## Risiko, dependensi, dan bukti terbuka

Batas akses Figma membuat token/style detail tetap open. WCAG adalah target baseline, bukan sertifikasi. Fidelity visual tidak boleh menyerap waktu engine/persistence atau menjadi alasan menambahkan P1/P2.

**Traceability:** UX-AC/T-001–008/101–103; MAP-AC/T-008/101; PRO/CORE/PUB keyboard NFR; PUB-AC/T-002/003; DDP-T-10. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** RV-12 pengukuran UX/latency dan OD-05 token/visual review. Source Figma tidak memberikan izin scope baru; acceptance numerik tetap dari PRD. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
