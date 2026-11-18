# ORBIT — Modular PRD, revisi DDP1 v0.2.1

Tanggal: **18 November 2026 (Asia/Jakarta)**. Ini revisi terarah atas baseline v0.1, bukan regenerasi PRD atau implementasi aplikasi. Nama 13 PRD, 20 bagian per PRD dan seluruh requirement ID lama dipertahankan. Folder dokumen historis bernama `ORBIT_PRD_v0.1`; nama itu tidak menyatakan akar folder arsip. ZIP v0.2 berakar di `ORBIT_PRD_v0.2/`, sedangkan paket errata **v0.2.1** berakar di **`ORBIT_PRD_v0.2.1/`**. Untuk otomatisasi, gunakan nilai `archive_root` pada manifest. Dokumen yang tidak terdampak tetap versi v0.2; empat PRD yang dikoreksi ditandai v0.2.1.

**Status: CONDITIONAL GO untuk desain arsitektur.** Kapasitas anggota (RV-14), kebaruan konsep di luar kelas (RV-15), dan kesiapan stack pada perangkat tim belum terbukti. Hanya FR P0 dan gate terkait menjadi scope awal; P1/P2 membutuhkan aktivasi eksplisit melalui perubahan scope tercatat. Lihat [PRD-v0.2.1-ERRATA.md](docs/00-governance/PRD-v0.2.1-ERRATA.md).

## Mulai dari laporan revisi

1. [PRD-AUDIT-REPORT.md](docs/00-governance/PRD-AUDIT-REPORT.md) — audit seluruh PRD, gap dan disposisi setiap FR.
2. [DDP1-COMPLIANCE-MATRIX.md](docs/00-governance/DDP1-COMPLIANCE-MATRIX.md) — ketentuan resmi dan enam bobot rubrik, terpisah dari rekomendasi/asumsi.
3. [MVP-SCOPE-AND-PRIORITIES.md](docs/00-governance/MVP-SCOPE-AND-PRIORITIES.md) — kelayakan, scope, Python stack, kapasitas dan jadwal.
4. [PRD-REVISION-CHANGELOG.md](docs/00-governance/PRD-REVISION-CHANGELOG.md) — perubahan per-ID, alasan dan tautan diff.
5. [IMPLEMENTATION-READINESS-REPORT.md](docs/00-governance/IMPLEMENTATION-READINESS-REPORT.md) — keputusan terbuka, risiko, test plan dan checklist repo/video/submission.

## Dokumen produk

Gunakan [Product Document Index](docs/00-governance/PRODUCT-DOC-INDEX.md) untuk 13 PRD dan governance, [glossary/decisions](docs/00-governance/GLOSSARY-AND-DECISION-LOG.md), [RTM](docs/00-governance/REQUIREMENTS-TRACEABILITY-MATRIX.md), [source/validation register](docs/00-governance/RESEARCH-AND-VALIDATION-REGISTER.md), dan [QA dokumentasi](docs/00-governance/QA-DOCUMENTATION-REPORT.md).

Jumlah requirement tetap sejak v0.2: **143 FR (48 P0, 27 P1, 68 P2),102 BR, 39 NFR, 182 AC/test primer, 14 test integrasi**. Semua 141 FR lama tetap; dua FR baru membatasi demo lokal dan export/reset. Seluruh test aplikasi berstatus belum dieksekusi. P2 tetap Future Development; P1 opsional setelah gate kapasitas. Teks visi lengkap tidak berarti semua kemampuan wajib dibangun pada rilis ini.

## Arah rilis

Roadmap + Grade Rescue + Dashboard, dengan profil/persistensi minimum, direkomendasikan sebagai demo lokal sintetis berbasis Python. Flask/Jinja dan SQLite adalah rekomendasi teknis; versi runtime/kapasitas aktual tim masih perlu diputuskan. Tidak mengasumsikan SSO UI/SLCM tersedia. Visi fitur komunitas, career, guidance, closeout dan UI Orbit dipertahankan.

Deadline resmi **10 Desember 2026 pukul 23.59 WIB**. Tim 3–4 orang; setiap anggota aktif di GitHub dan memahami seluruh kode. Pengumpulan resmi: GitHub publik dan tautan video YouTube maksimal 15 menit yang memuat masalah, demo serta arsitektur/solusi. Rencana internal memberi waktu testing/video sebelum deadline; tidak ada janji nilai tertentu.

## Jejak revisi

Baseline v0.1 diperiksa melalui 19 checksum sebelum perubahan. [Diff v0.1→v0.2](docs/00-governance/PRD-v0.1-to-v0.2.patch) menyimpan perubahan literal pada berkas baseline (manifest checksum dikecualikan untuk menghindari referensi hash berputar). [MANIFEST.json](MANIFEST.json) berisi hash artefak versi sekarang. Arsip v0.1 lama tetap menjadi snapshot historis; arsip **ORBIT_PRD_v0.2-DDP1-Audit.zip** mempertahankan snapshot sebelum errata. Paket sekarang adalah **ORBIT_PRD_v0.2.1-DDP1-Errata.zip**. [Diff v0.2→v0.2.1](docs/00-governance/PRD-v0.2-to-v0.2.1.patch) mencatat koreksi terbaru.

Tidak ada kode aplikasi, deployment, video atau pengumpulan tugas yang dilakukan pada tahap audit ini.
