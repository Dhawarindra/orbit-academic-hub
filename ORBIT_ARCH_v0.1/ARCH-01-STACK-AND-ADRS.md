# ORBIT · ARCH-01 · STACK AND ADRS

Versi **0.1** · **REVIEW** · 18 November 2026, Asia/Jakarta  
Baseline produk: **PRD v0.2.1**. Ini kontrak rancangan untuk review manusia; belum ada aplikasi, benchmark atau test aplikasi yang dijalankan.

## 1. Tujuan dan batas

Merekam pilihan teknologi dan konsekuensinya agar Codex/tim tidak mengubah arsitektur melalui keputusan implisit.

**Scope:** default Flask/Jinja/sqlite3, fallback Streamlit, 10 ADR yang diusulkan untuk P0.  
**Non-goals:** pin versi yang belum diuji, pemilihan hosting, atau menganggap framework sebagai ketentuan dosen.

**Sumber:** PRD-00/02/03/09/10; MVP-SCOPE-AND-PRIORITIES dan Readiness; RV-14/RV-15; CORE-FR-005/008, AUTH-FR-014/015. Sumber lengkap dan hasil audit input ada di [ARCH-INDEX](ARCH-INDEX.md). Label **DOSEN** berarti ketentuan PDF resmi; **BASELINE** berarti keputusan PRD; **REKOMENDASI** berarti rancangan paket ini; **OPEN** berarti bukti/keputusan belum tersedia. Rekomendasi bukan kewajiban dosen.

## 2. Perbandingan stack

| Aspek | A · Flask + Jinja + sqlite3 + HTML/CSS | B · Streamlit + SQLite |
| --- | --- | --- |
| Belajar | Perlu HTTP/form/template/CSS; domain tetap Python | Form awal lebih singkat; perlu memahami rerun dan session state |
| Identitas Figma | Kontrol layout, semantic HTML, fokus dan token lebih besar | Layout mengikuti widget; fidelity lebih terbatas |
| Validasi | Route parse → service → error per field; POST-redirect-GET | Form batch submit → service; jangan write pada setiap rerun |
| Konsistensi | DB transaksi + token revisi, terpisah dari session | DB dan token yang sama; session state bukan persistence |
| Test | Domain unittest, repository temp-file, Flask test client | Domain/repository sama; adapter/UI test perlu direncanakan ulang |
| Lokal | Satu server loopback, browser lokal | Satu server loopback; runtime Streamlit perlu smoke gate tersendiri |
| Waktu | Lebih banyak pekerjaan UI, lebih sedikit kompromi UX | Potensi mengurangi UI; penghematan belum diukur |
| Keputusan | **Default conditional** | **Fallback conditional**, bukan dua aplikasi yang dibangun bersama |

Framework tidak menghilangkan kewajiban validasi, transaksi, CSRF/host protection, accessible states, dan teach-back. [Streamlit session state](https://docs.streamlit.io/develop/concepts/architecture/session-state) menjelaskan rerun serta state per sesi; state durable Orbit tetap SQLite. [Flask testing](https://flask.palletsprojects.com/en/stable/testing/) menyediakan client/factory untuk pengujian adapter. Penggunaan unittest tetap rekomendasi minimal; pytest opsional bila disepakati tim.

## 3. ADR

Semua ADR berstatus **PROPOSED FOR REVIEW**, belum disetujui manusia. Alasan perbandingan adalah analisis arsitek, bukan hasil benchmark atau penelitian tim.

| ADR | Keputusan dan alasan | Alternatif ditolak / trade-off | Verifikasi dan pemicu revisi |
| --- | --- | --- | --- |
| ADR-01 Stack | Flask/Jinja default; Python memegang seluruh keputusan produk | Streamlit fallback jika spike/perangkat/kemampuan membuktikan UI Flask terlalu mahal; SPA ditolak | OD-01: semua perangkat menjalankan form→service→DB→restart setelah tahap implementasi diizinkan |
| ADR-02 Persistence | SQLite via stdlib sqlite3; schema eksplisit, transaksi pendek, tanpa ORM | JSON file sulit menjamin atomic multi-record; server DB berlebihan | AUTH-T-015, INT-T-014; cek sqlite3 benar-benar tersedia |
| ADR-03 Actual vs scenario | ActualFinalGrade append-only; overlay terpisah; numeric projection tidak dapat menulis actual | Satu kolom nilai dengan mode flag mudah mencampur sumber | GRD-T-010/011, MAP-T-002, INT-T-003/013 |
| ADR-04 Revision | Satu workspace `epoch/state_revision/source_revision`; satu scenario dengan `base_source_revision` | Per-field merge/event bus tidak perlu; global write conflict lebih konservatif | Dua tab dari revision sama: tepat satu commit; reset memutus token lama |
| ADR-05 Fixture/provenance | Katalog kecil sintetis immutable + source metadata; tanpa klaim verified official | Mengambil aturan dari nama Figma atau scraping ditolak | CORE-T-004, MAP-T-001/012, PUB-T-003 |
| ADR-06 Local access | Satu owner lokal tanpa login; loopback literal, Host allowlist, CSRF, debug off | Public link/tunnel bukan cara berbagi build tanpa auth | AUTH-T-014, DDP-T-09, AUTH-T-103 |
| ADR-07 Capabilities | Konstanta P0 di composition root; future routes tidak ada | Toggle bebas berisiko mengaktifkan scope tanpa test | CORE-T-005/101, INT-T-010 |
| ADR-08 UX | Tema terang, list setara penuh, form HTML; brand/struktur navigasi tetap | Pixel-perfect dan graph drag/drop tidak dipilih | UX-T-001–008/101–103; review Figma adaptation |
| ADR-09 Numeric | Input Decimal dari string, bobot integer bp, aritmetika rasional exact untuk rasio; format half-up di batas presentasi Python | float/SQLite REAL ditolak; Decimal context saja dapat membulatkan pecahan berulang dekat threshold | GRD-T-002/004/005/016/018; DDP-T-03/04/05 |
| ADR-10 Delivery/test | Pure-domain unittest + service/temp-file integration + manual browser checks; CI ringan opsional | Semua test hanya via browser lambat dan sulit mengisolasi formula | ARCH-07 gates, RV-14/15; tidak menambah Hypothesis wajib |

## 4. Detail yang harus konsisten

**ADR-02/04:** service adalah pemilik transaksi. Connection mengaktifkan foreign keys sebelum BEGIN. Gunakan binding parameter, tidak string interpolation SQL. Mode transaksi eksplisit harus diuji pada runtime terpilih; jangan bergantung default autocommit yang berbeda antar versi Python. Desain memakai BEGIN IMMEDIATE untuk write dan BEGIN read untuk snapshot. Tidak share connection antar request/thread. Lihat [Python sqlite3](https://docs.python.org/3/library/sqlite3.html), [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html), [transaction](https://www.sqlite.org/lang_transaction.html), dan [isolation](https://www.sqlite.org/isolation.html).

**ADR-09:** Decimal dipakai untuk parsing finite exact dan validasi rentang; bobot disimpan integer 10000 bp. Fraction dari Decimal/rasio integer menjaga pembagian earned/max dan threshold exact; tidak pernah membuat Fraction dari float. Ini satu model angka, bukan dua oracle yang berbeda. SQLite menyimpan angka skor sebagai string kanonik; hasil exact serialized numerator/denominator. Rounding dua desimal dilakukan oleh formatter Python dengan integer quotient/remainder half-up, lalu string ditampilkan Jinja. [Decimal](https://docs.python.org/3/library/decimal.html) dan [Fraction](https://docs.python.org/3/library/fractions.html) mendukung dasar ini; kontrak aplikasi dan batas input ada di ARCH-04. Tambahan konsep ini harus dapat dijelaskan tim, dan tidak otomatis dianggap materi baru di luar kelas.

**ADR-06:** local-only tetap membutuhkan perlindungan request. Flask tidak otomatis memberi CSRF untuk formulir; Jinja autoescape tidak membuat semua URL aman. Bentuk token/Host checks dijelaskan ARCH-09, bersumber pada [Flask security](https://flask.palletsprojects.com/en/stable/web-security/). Server pengembangan hanya untuk demo lokal, bukan produksi ([Flask development server](https://flask.palletsprojects.com/en/stable/server/)).

## 5. Gate pilihan default/fallback

Pada 18–19 Nov (target internal), inventaris Python/OS/sqlite3, kemampuan Git/HTML/Flask, dan slot kerja aktual. Setelah manusia mengizinkan spike kecil, ukur setup + satu form + persistence/restart pada perangkat tim. Bila A layak, catat versi tepat dan dependency file dari lingkungan yang benar-benar diuji. Bila B lebih masuk akal, revisi ARCH-05 adapter, ARCH-06 page mapping, ARCH-08 file tree dan ARCH-09 runner **sebelum** implementasi lanjut. Unit/domain dan golden results tidak berubah. Jangan mempertahankan dua frontend.

Tidak ada versi `latest`/pin yang dianggap final dalam paket ini. Input teknis dari dokumentasi resmi dibaca 18 Nov 2026; verifikasi kembali dokumentasi sesuai versi runtime yang akhirnya dipilih.

## Risiko, dependensi, dan bukti terbuka

Fallback dapat menghemat UI tetapi tidak mengurangi kompleksitas domain/state. Module sqlite3 dapat tidak tersedia pada suatu distribusi Python. CSRF/Host integration dan numeric teach-back harus dibuktikan, bukan diasumsikan aman.

**Traceability:** CORE-T-005/008/101; AUTH-T-014/015/103; GRD-T-016; DDP-T-05/08/09/10. Semua skenario aplikasi berstatus **SPECIFIED / NOT EXECUTED**; cakupan lengkap ada di [ARCH-07](ARCH-07-TEST-STRATEGY-AND-TRACEABILITY.md).

**OPEN:** OD-01 runtime/stack, OD-03 numeric teach-back dan RV-14/15; perubahan ADR memerlukan alasan, dampak AC/test, dan review manusia. Owner, tenggat, dan kriteria penutupan terpusat di [ARCH-11](ARCH-11-OPEN-DECISIONS-AND-APPROVAL-CHECKLIST.md).
