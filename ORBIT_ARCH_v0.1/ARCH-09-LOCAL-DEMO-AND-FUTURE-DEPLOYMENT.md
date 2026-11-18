# ORBIT · ARCH-09 · LOCAL DEMO AND FUTURE DEPLOYMENT

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Menetapkan cara menjalankan dan mendemonstrasikan P0 dengan aman serta memisahkan rencana hosting future.

**Scope:** localhost, request guards, offline assets/fixture, persistence, backup manual, video/release run contract.  
**Non-goals:** public hosting/tunnel, multiuser auth, data nyata, campus API, atau menjadikan GitHub publik sebagai izin membuka server.

**Sumber:** AUTH-FR-010/014/015, AUTH-NFR-003; PUB-FR-002/003; CORE-NFR-001; Readiness DDP-T-09 dan ADR-06. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. Startup dan request contract

Mode tunggal `local-demo`, bind literal `127.0.0.1` (default) atau `::1` jika smoke test perangkat mendukung. Jangan resolve hostname bebas sebagai dasar keputusan bind. Tolak `0.0.0.0`, `::`, alamat LAN/public dan public-host mode. `localhost` boleh label URL browser, tetapi runner bind menggunakan literal allowlist. Guard memeriksa konfigurasi efektif saat start; request remote peer nonloopback juga ditolak. Tidak menganggap Host header atau CORS sebagai pengganti socket bind.

Runner resmi kelak `python -m orbit` (belum tersedia). Config debug/reloader wajib false untuk demo; environment yang mencoba mengaktifkannya pada local-demo ditolak, bukan quietly ignored. Schema version/foreign keys harus benar; DB rusak/incompatible gagal start tanpa overwrite. File DB dan secret berada di instance directory, seed di fixtures terpisah. Fresh start membuat owner stabil dan workspace kosong; tidak seed setiap import/start. Semua assets lokal; tidak butuh CDN/webfont/cloud untuk menjalankan core.

| Surface | Proteksi rancangan | Test negatif |
| --- | --- | --- |
| Socket bind | Literal loopback allowlist, no proxy/tunnel recipe | Public/LAN/wildcard config rejected before listen |
| Host header | Allow `127.0.0.1`, `localhost`, `[::1]` pada port aplikasi; jangan percaya forwarded headers | Foreign Host/DNS-rebinding hostname rejected |
| Mutating requests | CSRF token dari server, cookie HttpOnly+SameSite=Strict, no write via GET | Missing/wrong token/cross-origin POST no write |
| Origin | Untuk request yang membawa Origin, cocokkan exact local scheme/host/port; no permissive CORS | Origin asing ditolak walau target localhost |
| Preview proof | HMAC/signature atas operation type+payload hash+epoch/revision; secret random runtime | Tampered actual/reset payload atau stale preview rejected |
| Templates/inputs | Jinja autoescape, no raw safe markup dari input, quoted attributes; source URL jika ditampilkan hanya scheme aman | Script/title/URL injection tidak dieksekusi |
| Logging/export | Allowlisted metadata, no form dumps; exports exclude token/secret/receipt | Secret marker tidak muncul di log/export/error response |

CSRF token disimpan session server-signed; session cookie hanya metadata request/nonce, **tidak** nilai/grades. Satu runtime signing secret dibuat acak dan disimpan untracked dengan izin file terbatas; bukan password owner dan bukan field database yang diekspor. Cookie `Secure` membutuhkan HTTPS, sehingga tidak diklaim aktif pada loopback HTTP; local-only bukan desain untuk internet. Token invalid setelah secret rotation meminta reload form, bukan reset data. Hash/signature menggunakan primitive stdlib/framework yang tersedia; jangan menciptakan algoritma crypto sendiri. Detail integrasi API harus diperiksa pada runtime terpilih.

Pemilik laptop/proses lokal lain dapat mengakses file lokal; P0 tidak mengklaim account isolation, enkripsi at rest, atau keamanan multiuser. Karena itu hanya data sintetis. Kehadiran no-login tidak boleh dijadikan alasan menonaktifkan CSRF: browser dapat mengirim request ke localhost dari halaman lain.

## 3. Kontrak runbook yang akan diisi setelah implementasi

README harus mencatat OS/Python/dependency versions yang benar-benar diuji; pembuatan environment lokal, instalasi dependency, runner resmi, cara memuat fixture secara eksplisit, test command dan stop/restart. Calon command test `python -m unittest discover -s tests -v`; ini instruksi blueprint, bukan klaim file sudah ada. Tidak ada command public deployment/tunnel dalam paket P0.

Smoke gate perangkat: fresh clone → setup → start loopback debugoff → workspace kosong → load fixture → score/target/roadmap → stop → start → owner dan input sama → export → cancel reset → confirm reset → empty, seed hash sama. Uji di semua perangkat anggota atau catat keterbatasan dan satu perangkat demo beserta cadangan yang benar-benar telah dicoba. Kondisi offline diuji setelah dependency terpasang; instalasi dependency dan upload GitHub/YouTube tentu membutuhkan akses jaringan.

## 4. Backup, recovery dan file lifecycle

DB runtime bukan fixture. `.gitignore` meliputi instance/*.sqlite*, journals/WAL/SHM, exports/backups, secret files dan logs. Review staged diff sebelum push; jangan menambah ekspor agar penilai mendapat demo—fixture sintetis cukup. Export user adalah snapshot JSON portable untuk inspeksi/backup data, bukan fitur import yang sudah dijanjikan.

Backup P0 operasional sederhana: stop proses dengan bersih, pastikan semua connection tutup, salin DB konsisten ke folder lokal untracked dan catat schema/build/epoch/tanggal. Bila memakai backup saat aplikasi hidup, harus memakai mekanisme SQLite backup yang teruji; jangan menyalin hanya main file saat journal/WAL aktif. Restore manual hanya untuk kegagalan teknis: stop, amankan file rusak, verifikasi versi/schema/integrity backup, ganti DB secara eksplisit, restart dan cek owner/histori. Ini bukan akun restore P2 dan bukan auto-restore. Jangan mengembalikan backup pra-reset tanpa keputusan eksplisit pengguna; reset bertujuan menghapus runtime, bukan trigger restore seed/history otomatis.

Export dari service mencakup schema_version/source/revisions/decimals strings/history dan stale marker; tidak memuat secret, cookies, receipt hashes atau internal logs. File tidak ditawarkan lewat public URL. Reset preview menjelaskan ekspor/backup yang telah disalin tetap ada; aplikasi hanya menghapus DB domain runtime pada confirmed reset. File seed read-only dipertahankan hash-nya.

## 5. Demo dan kebutuhan video

Sebelum merekam, gunakan build yang telah melewati gate dan fixture hash tercatat; restart untuk menunjukkan persistence. Demo mencakup empty/unknown, golden grade, impossible target, what-if terpisah, actual confirm yang memperbarui MAP, stale scenario reset dan export. Script video target 14 menit di ARCH-10 mencakup masalah/demo/arsitektur. GitHub publik bukan berarti file DB runtime dibagikan. YouTube link harus dapat diakses penilai, durasi≤15 menit; verifikasi link setelah upload sebelum deadline.

Tidak ada video, repository publik atau live app yang dibuat pada tahap arsitektur ini. Placeholder URL tidak boleh masuk README sebagai seolah tautan akhir. SSO/SLCM hanya status “belum tersedia” dan manual fallback; no campus credentials atau scraping.

## 6. Future public-deployment gate

Public hosting adalah perubahan capability P2 dengan desain/review terpisah. Jalur konseptual future: browser→HTTPS application server→authentication/authorization→services→persistent storage/backups. Bukan cukup mengganti bind localhost menjadi wildcard.

Gate yang harus punya evidence: akun+ownership A/B pada read/edit/list/export; secret management/session/CSRF/rate limiting/recovery; HTTPS dan production server; retention/delete/restore, data consent/provenance dan operator; monitoring/incident/backup/access control; deployment config, threat review dan test; izin institusi bila mengakses data/API universitas. AUTH dan RV-05/06/10 menentukan scope future. Tidak ada provider/endpoint/izin yang diasumsikan tersedia. Bagian ini mempertahankan visi tanpa membuat dependency publik untuk P0.

Alternatif hosting build no-auth atau menggunakan link tunnel untuk memenuhi GitHub/YouTube deliverable ditolak; panduan tidak memintanya. Local demo sudah sesuai bentuk aplikasi yang diperbolehkan, dengan Python sebagai komponen utama.

## Risiko, dependensi, dan bukti terbuka

Loopback guard dapat terlewati jika tim menjalankan server manual dengan opsi berbeda; runner/config/request checks harus diuji bersama dan README memberi satu jalur resmi. Security plan belum implementation evidence.

**Traceability:** AUTH-AC/T-010/014/015/103; PUB-AC/T-002/003; CORE-AC/T-101; DDP-T-09; INT-T-014. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** OD-01 runner/runtime, OD-04 reset/backup safety, RV-10 public operations future; tidak ada public deployment yang disetujui. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
