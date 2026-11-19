# Orbit Academic Hub

Orbit adalah proyek independen mahasiswa DDP1, Fakultas Ilmu Komputer Universitas Indonesia. **Grade Rescue** sudah dapat digunakan untuk mencatat komponen penilaian, menghitung target dan mencoba skenario pada data sintetis. Academic Roadmap masih direncanakan.

## Menjalankan dari checkout baru

Pasang **Python 3.12** dengan modul bawaan `venv`, `sqlite3`, dan `unittest`. Dari checkout repositori, buka terminal di direktori yang memuat README ini. Flask menangani HTTP dan Jinja merender HTML. Instal dependensi sekali saat terhubung ke internet. Halaman dan CSS selanjutnya dapat digunakan secara luring.

**Windows (PowerShell).** Perintah menggunakan interpreter virtual environment secara langsung sehingga tidak perlu mengubah execution policy.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m orbit
```

**Linux, macOS, atau lingkungan cloud baru**

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m orbit
```

Di Codex Cloud yang sudah disiapkan, jalankan dari `/workspace/orbit-academic-hub`:

```sh
/workspace/.orbit-venv/bin/python -m pip install -r requirements.txt
/workspace/.orbit-venv/bin/python -m orbit
```

Buka `http://127.0.0.1:5000/` di browser pada perangkat yang menjalankan server, lalu pilih **Buka Grade Rescue**. Alamat langsungnya `http://127.0.0.1:5000/grades/`. Gunakan Ctrl+C untuk menghentikan server dan ulangi perintah terakhir untuk memulai kembali.

### Mencoba Grade Rescue

1. Pilih **Coba contoh sintetis** di beranda untuk membuka formulir kuis bertingkat, UTS, dan UAS. Tinjau nama, periode, dan bobot, kemudian pilih **Simpan struktur**. Untuk struktur sendiri, gunakan **Tambah mata kuliah**. Simpan struktur dengan semua skor kosong jika masih ingin mengeditnya.
2. Contoh menghasilkan rerata teramati 72 dan rentang akhir 36–86 dengan 50% bobot terisi. Masukkan target 75 untuk melihat kebutuhan UAS 78. Target 90 menampilkan kebutuhan 108 dan status tidak dapat dicapai.
3. Di **Simulasi what-if**, masukkan UAS 90 untuk melihat proyeksi 81. Skor UAS aktual tetap kosong. Perubahan sumber membuat simulasi lama perlu direset.
4. Untuk mencatat hasil final yang dilaporkan, buka **Catat hasil final**, isi hasil dan sumber sintetis, lalu tinjau sebelum konfirmasi. Koreksi berikutnya menyimpan riwayat dan memerlukan alasan.

## Konfigurasi dan SQLite

| Variabel | Default | Penggunaan |
| --- | --- | --- |
| `ORBIT_DATABASE` | `instance/orbit.sqlite3` di root checkout | Path file SQLite. Path relatif dihitung dari direktori kerja. Untuk path kustom, gunakan direktori data privat di luar Git dan direktori static. |
| `ORBIT_PORT` | `5000` | Port lokal 1–65535. Jika port sibuk, pilih port lain dan sesuaikan URL browser. |
| `ORBIT_HOST` | `127.0.0.1` | Runner M0 hanya menerima alamat loopback IPv4 ini. |

Untuk database contoh terpisah di PowerShell, gunakan `$env:ORBIT_DATABASE = Join-Path $env:TEMP "orbit-grade-demo.sqlite3"`. Di Bash gunakan `export ORBIT_DATABASE=/tmp/orbit-grade-demo.sqlite3`. Startup memeriksa integritas dan menyiapkan skema Grade Rescue versi 1 dalam satu transaksi pada database versi 0 milik M0. File lama tidak perlu dihapus. Jika pemeriksaan gagal, simpan file lama dan periksa path, izin, atau pilih file demo baru.

Mode debug dan reloader dinonaktifkan. Konfigurasi `FLASK_DEBUG=1` ditolak. Gunakan runner modul di atas. Aplikasi membuat kunci penandatanganan lokal di `instance/` untuk melindungi formulir dan konfirmasi. Direktori ini diabaikan Git. Gunakan hanya data sintetis.

## Struktur

| Lokasi | Peran |
| --- | --- |
| `orbit/__init__.py`, `__main__.py`, `config.py` | Membuat aplikasi, membaca konfigurasi, dan menjalankan server lokal. |
| `orbit/web/` | Pemeriksaan request lokal, proteksi formulir, dan route Grade Rescue. |
| `orbit/domain/grades.py`, `orbit/services/gradebook.py` | Validasi dan perhitungan presisi penuh, transaksi nilai, serta isolasi simulasi. |
| `orbit/templates/`, `orbit/static/` | Template Jinja dan CSS lokal. |
| `orbit/repositories/` | Membuka, memeriksa, dan menutup koneksi SQLite. |
| `tests/` | Pengujian fondasi, traceability, domain nilai, dan alur formulir/SQLite. |
| `ORBIT_PRD_v0.2.1/`, `ORBIT_ARCH_v0.1/` | Baseline produk dan rancangan arsitektur. |
| `instance/` | Data runtime lokal yang diabaikan Git. |

Target huruf memerlukan kebijakan yang cocok. Pilihan kebijakan A/B/C adalah contoh sintetis yang terikat pada kelas tersebut. Aturan tambahan ditampilkan sebagai catatan di luar model linear.

## Pengujian

Dari root checkout dengan virtual environment aktif:

```sh
python -m unittest discover -s tests -v
```

Di PowerShell tanpa aktivasi, gunakan `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`. Di Linux gunakan `.venv/bin/python`, atau di cloud gunakan `/workspace/.orbit-venv/bin/python`, dengan argumen yang sama. Tes memakai database sementara terpisah. Runtime referensi cloud adalah Linux, Python 3.12.14, Flask 3.1.3, Jinja 3.1.6, dan SQLite 3.53.1. Reproduksi di perangkat anggota dan teach-back anggota kedua berstatus **PENDING**.

## Jejak keputusan M0

Otorisasi awal mencakup fondasi M0 dengan Flask/Jinja dan SQLite. Baseline produk adalah PRD v0.2.1 dan rancangan teknis v0.1. Target perencanaan tim adalah sekitar 8 dari 94 jam-orang untuk M0. Build Phase 1 mengotorisasi Grade Rescue sebagai fitur pertama.

`CORE-FR-008` → `CORE-AC-008` → `CORE-T-008` mengharuskan perubahan scope dapat ditelusuri hingga keputusan dan pengujian terkait. Contoh baseline: keputusan D-21 membatasi `MAP-FR-006` pada tinjau perubahan dan reset/pilih ulang. Rebase yang mempertahankan pilihan ditunda ke P2. Pengujian dokumentasi menelusuri keputusan, changelog, dan pasangan `MAP-AC-006` / `MAP-T-006`. Hasilnya memeriksa jejak dokumen. Perilaku aplikasi Roadmap menunggu implementasi.

[Decision log](ORBIT_PRD_v0.2.1/docs/00-governance/GLOSSARY-AND-DECISION-LOG.md) · [Changelog](ORBIT_PRD_v0.2.1/docs/00-governance/PRD-REVISION-CHANGELOG.md) · [Traceability matrix](ORBIT_PRD_v0.2.1/docs/00-governance/REQUIREMENTS-TRACEABILITY-MATRIX.md) · [Instruksi kontributor](AGENTS.md)
