# PRD-04 — Academic Schedule & Academic Stress Radar

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-04 / v0.2 DDP1 Draft |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | Product Owner Schedule |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | Stress Radar adalah nama fitur beban akademik, bukan asesmen klinis. Kapasitas waktu adalah input pengguna; nilai default durasi tidak diisi diam-diam. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). |

## 2. Executive Summary & Problem

Modul menyatukan pertemuan kelas, tenggat assessment dan estimasi kerja agar kepadatan terlihat lebih awal. Estimasi menggunakan jam tersisa dan bobot assessment sebagai indikator salience terpisah; jam dan persen tidak dijumlahkan sebagai besaran yang sama.

## 3. Goals, Non-Goals & Success Metrics

Pengguna mengenali tabrakan, melihat pekerjaan yang belum diperkirakan, dan menyusun blok persiapan yang bisa ditolak atau diubah.

**Non-goals:** Diagnosis stres, skor kesehatan mental, deteksi kondisi psikologis atau sinkronisasi kalender pribadi tanpa izin.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Kebenaran konflik | Fixture interval bertumpuk dan back-to-back | 100% cocok oracle |
| Coverage estimasi | Assessment bertenggat dengan remaining_hours / seluruh assessment bertenggat | Ditampilkan sebagai pecahan; bukan target wajib pengguna |
| Actionability | Peserta menemukan minggu padat dan mengubah blok kerja | Usulan ≥4/5 peserta |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Mahasiswa dengan jam kuliah tetap, deadline banyak dan durasi tugas belum pasti.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Student | Jadwal, durasi dan kapasitas sendiri | Melihat beban orang lain |
| Guest/moderator | Penjelasan metode publik | Jadwal dan deadline personal |
| Adapter future | Jadwal sesuai izin eksplisit | Akses nilai hanya karena login |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Tidak ada fitur modul ini yang wajib dibangun untuk P0 | Pertemuan satu per satu, overlap, deadline canon, weekly demand/capacity dan coverage | Recurrence, preparation blocks, salience lanjutan, auto-allocation dan review blok |

**Slice rilis:** Jika P1 diaktifkan: input interval, dua durasi 6+4 jam dan kapasitas 8 → overlap terukur dan rasio 1,25. Beban adalah perkiraan akademik, bukan diagnosis.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

Alur rilis DDP1 yang berlaku: Jika P1 diaktifkan: input interval, dua durasi 6+4 jam dan kapasitas 8 → overlap terukur dan rasio 1,25. Beban adalah perkiraan akademik, bukan diagnosis. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1.** Jadwal → Tambah pertemuan → hari/jam/rentang aktif → preview bentrok → simpan. Bentrok memberi warning dan tetap dapat disimpan dengan catatan; meeting berakhir tepat saat berikutnya mulai tidak bentrok.

**J2.** Tracker → isi deadline assessment → Jadwal menampilkan deadline yang sama → isi remaining_hours → radar mingguan. Jika kapasitas belum ada, lihat total jam tanpa label kapasitas terlampaui.

**J3.** Pekan padat → buka rincian → tambah blok persiapan lebih awal → review jam yang masih belum dialokasikan. Cancel tidak mengubah deadline; kembali ke tracker tetap membaca assessment yang sama.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| SCH-US-001 | As a student, I want memasukkan kelas dan deadline sekali, so that jadwal saya konsisten. | P1 | SCH-FR-001, SCH-FR-002, SCH-FR-003 |
| SCH-US-002 | As a student, I want melihat jam kerja dan ketidakpastiannya, so that saya dapat mengatur waktu. | P1 | SCH-FR-004, SCH-FR-005, SCH-FR-006 |
| SCH-US-003 | As a student, I want membagi persiapan lebih awal, so that pekan tenggat lebih terkendali. | P2 | SCH-FR-007, SCH-FR-008, SCH-FR-009 |
| SCH-US-004 | As a student, I want memasukkan estimasi yang konsisten, so that ringkasan jam dapat dipercaya. | P1 / P2 (per FR) | SCH-FR-011, SCH-FR-012 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SCH-FR-001 | P1 | Tambah deadline dari jadwal | Enrollment dengan assessment | assessment_id, due_at | Tulis deadline ke record assessment canon GRD; jika belum ada pilih/buat assessment personal tanpa bobot | Tracker dan jadwal membaca satu deadline yang sama | SCH-AC-001 |
| SCH-FR-002 | P1 | Simpan pertemuan | Zona waktu dipilih | start/end dan timezone; recurrence hanya P2 | Validasi end>start dan tampilkan zona waktu; P1 memasukkan pertemuan satu per satu; editor recurrence dipertahankan sebagai P2 | 09.00–10.00 WIB diterima; 10.00–09.00 pada hari sama ditolak | SCH-AC-002 |
| SCH-FR-003 | P1 | Deteksi konflik | Dua interval pada hari sama | A09–10,B10–11; lalu B09.30–11 | Gunakan interval half-open [start, end) | Kasus pertama tidak bentrok; kedua bentrok 30 menit | SCH-AC-003 |
| SCH-FR-004 | P1 | Hitung weekly demand | Dua assessment di minggu sama | Remaining hours 6 dan 4; kapasitas 8 | Jumlahkan jam yang jatuh pada minggu deadline bila belum dialokasikan | Demand=10 jam; rasio=1,25; status di atas kapasitas | SCH-AC-004 |
| SCH-FR-005 | P1 | Hitung coverage | Tiga assessment jatuh minggu itu | Durasi 6,4,unknown | Keluarkan unknown dari total numerik tetapi hitung coverage | Known=10 jam; coverage=2/3; label estimasi parsial | SCH-AC-005 |
| SCH-FR-006 | P1 | Tampilkan beban tanpa kapasitas | Known hours=10 | capacity unknown atau 0 | Bedakan belum diisi dari nol ketersediaan eksplisit | Unknown: tanpa rasio; 0: tidak ada waktu tersedia, rasio tidak dihitung | SCH-AC-006 |
| SCH-FR-007 | P2 | Simpan blok persiapan | Tugas 6 jam due minggu 2 | Alokasi 2 jam minggu 1 dan 4 jam minggu 2 | Alokasikan remaining work tanpa menghitung tugas dua kali | Total lintas minggu tetap 6 jam; deadline tidak berubah | SCH-AC-007 |
| SCH-FR-008 | P2 | Tampilkan salience assessment | Bobot 10% dan 40% pada offering berbeda | 2 assessment minggu sama | Tampilkan bucket bobot per assessment terpisah dari jam | Tidak menampilkan 50% sebagai total lintas offering atau menambah ke jam | SCH-AC-008 |
| SCH-FR-009 | P2 | Geser deadline | Assessment punya blok persiapan | Deadline baru sebelum satu blok yang ada | Tandai blok setelah deadline sebagai perlu ditinjau | Tidak memindahkan blok otomatis; radar memakai revision baru | SCH-AC-009 |
| SCH-FR-010 | P2 | Minta saran persiapan | Kapasitas per hari tersedia | Durasi tersisa dan deadline | Usulkan alokasi di slot kosong terdekat sebelum deadline lalu minta apply | Saran belum menjadi meeting sampai disetujui | SCH-AC-010 |
| SCH-FR-011 | P2 | Validasi alokasi | Tugas remaining 6 jam | Blok 4+3 jam, estimasi−1, kapasitas−2 | Tolak total alokasi>remaining dan input negatif/nonfinite | 4+3 ditolak; tidak ada double-count atau jam negatif | SCH-AC-011 |
| SCH-FR-012 | P1 | Input deadline hanya tanggal | User tidak tahu jam | 10 Desember 2026 tanpa waktu | Simpan due_date dan label jam belum ditentukan | Tidak dibuat 23.59; tidak memicu bentrok interval palsu | SCH-AC-012 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| SCH-BR-001 | Tanggal-waktu disimpan sebagai instant dengan timezone sumber. Date-only deadline tetap date-only, bukan dibuat pukul 23.59 tanpa konfirmasi. Minggu = Senin 00.00 sampai Senin berikutnya di timezone pengguna. | SCH-FR-001, SCH-FR-002, SCH-FR-012 |
| SCH-BR-002 | Overlap bila max(startA,startB)<min(endA,endB). Deadline titik bukan durasi pertemuan; coincidence deadline bukan bentrok waktu kuliah. | SCH-FR-003 |
| SCH-BR-003 | Remaining_hours ≥0; completed task memiliki 0. Jangan menurunkan jam hanya karena waktu kalender berlalu. Estimasi kerja mandiri terpisah dari jam kelas. | SCH-FR-004, SCH-FR-005 |
| SCH-BR-004 | Default demand-by-deadline menempatkan seluruh jam tersisa di minggu jatuh tempo. Ini proxy kepadatan, bukan rekomendasi mulai pada minggu itu. Allocation mode memindahkan jam, bukan menggandakan. | SCH-FR-004, SCH-FR-007 |
| SCH-BR-005 | Weekly demand = allocated hours pada minggu + unallocated remainder tugas yang deadline-nya di minggu itu. Allocation total tidak boleh melebihi remaining hours; blok setelah due perlu review. | SCH-FR-007, SCH-FR-009, SCH-FR-011 |
| SCH-BR-006 | Jika C>0, ratio=D/C: D=0 → tidak ada beban diketahui, 0<ratio<0,8 → di bawah kapasitas, 0,8≤ratio≤1 → mendekati kapasitas, ratio>1 → di atas kapasitas. Threshold produk usulan, bukan indeks medis. | SCH-FR-004, SCH-FR-006 |
| SCH-BR-007 | Kualitas input = durasi tersedia n/N; tidak memakai istilah confidence statistik. Jika n=0, total tidak ditampilkan sebagai nol beban nyata. Kapasitas kosong menahan ratio. | SCH-FR-005, SCH-FR-006 |
| SCH-BR-008 | Salience bobot menggunakan metadata assessment dan BRP version: <10 rendah, 10–<30 menengah, ≥30 tinggi; bobot unknown diberi unknown. Ini urutan perhatian produk, bukan prediksi nilai atau stres. | SCH-FR-008 |

**Fixture mingguan:** tugas A sisa 6 jam due minggu 2; tugas B 4 jam due minggu 2; kapasitas minggu 2=8 jam. Tanpa alokasi, demand 10 dan ratio 1,25. Setelah A dialokasikan 2 jam minggu 1 dan 4 jam minggu 2, minggu 2 demand=4+4=8, ratio=1. Total dua minggu tetap 10.

**Data parsial:** tugas C due minggu 2 tetapi durasi kosong → known demand tetap 8 dan coverage 2/3; copy “8 jam dari 2 tugas yang memiliki estimasi; 1 tugas belum diestimasi”. Bobot A 40% dari course X dan B 10% dari course Y ditampilkan per baris, tidak dijumlahkan sebagai 50% semester.

**Deadline terlewat:** tugas overdue tidak otomatis bergeser deadline. Tampilkan backlog tersendiri beserta jam belum selesai, dan usulkan rencana kerja setelah pengguna mengonfirmasi status tugas; jangan menghilangkan pekerjaan dari radar.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| Meeting / meeting_id | owner, offering, start/end, timezone, recurrence, exception refs | Student | active/cancelled; audit revisi | Private |
| Assessment deadline | assessment_id,due_at atau due_date, timezone | GRD canon; SCH editor | Revisi memicu invalidasi turunan | Private |
| WorkEstimate / assessment_id+owner | remaining_hours nullable, estimated_at, completed flag | Student | Estimate diperbarui manual | Private |
| PreparationBlock / block_id | assessment_id,start/end,hours,status | Student / applied proposal | proposed/applied/done/cancelled | Private |
| Capacity / owner+week | available_hours, scope study-only | Student | Unknown ≠ zero | Private |
| WorkloadSummary / week | known hours, coverage, ratio, source_revision | SCH turunan | recomputable/stale | Private |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Agenda list P1 dapat dipakai tanpa kalender visual. Radar menampilkan total jam diketahui, kapasitas, jumlah deadline, coverage dan daftar penyebab. Pertemuan kuliah, deadline, serta blok persiapan memakai ikon/label berbeda. Microcopy utama: “Estimasi beban akademik dari data yang kamu masukkan.” Label peringatan tidak menggunakan “kamu stres berat”. Setiap ringkasan membuka daftar sumber; form deadline dapat diakses dari tracker maupun jadwal. Mobile tetap menampilkan timezone dan tanggal lengkap.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| No data | Tambah kelas atau tenggat | Tidak menyatakan pekan ringan |
| Unknown duration | CTA isi estimasi | Tidak mengarang durasi |
| Zero capacity | Tidak ada waktu tersedia | Tidak Infinity |
| Overdue | Backlog terlihat | Tidak auto-shift due date |
| Cancelled class | Occurrence hilang dari konflik | History audit tetap |
| Offline/stale | Data terakhir dengan timestamp | Tidak mengklaim sync berhasil |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** Seluruh jalur SCH opsional P1/P2; tidak boleh menjadi input wajib Dashboard P0. Recurrence, PreparationBlock dan GDE tetap P2. Deadline tunggal ditulis ke assessment GRD; estimasi tidak mengubah grade. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| GRD-FR-001/PRO-FR-004 → SCH-FR-001 | Assessment/offering scope | Shared ID, tidak copy skor |
| SCH-FR-004 → GDE-FR-003 | WorkloadChanged dengan hours,coverage,ratio | Low coverage → permintaan isi data |
| PRO-FR-007 → SCH-FR-002 | Timezone preference | Instant tetap; regroup week menurut timezone |
| AUTH-FR-009 → SCH-FR-002 | Future ScheduleSyncResult | Manual selalu tersedia; edit manual menang sampai konflik disetujui |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Tidak mengumpulkan suasana hati, diagnosis, lokasi real-time atau kalender pihak lain. Jadwal hanya personal. Analytics tidak merekam judul tugas atau tanggal per individu.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| SCH-NFR-001 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | SCH-AC-101 |
| SCH-NFR-002 | P0 | Tampilan utama p95 ≤2 detik setelah data tersedia pada beban uji dasar. | SCH-AC-102 |
| SCH-NFR-003 | P0 | Ringkasan jam konservatif: jumlah lintas minggu sama sebelum dan sesudah alokasi. | SCH-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata. SCH-NFR-003 (konservasi alokasi) baru aktif bersama alokasi P2; pada P1 total jam deadline/coverage tetap mengikuti SCH-FR-004/005/006.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| SCH-AC-001 | Given Enrollment dengan assessment; assessment_id,due_at | When Tambah deadline dari jadwal | Then Tracker dan jadwal membaca satu deadline yang sama | SCH-FR-001 |
| SCH-AC-002 | Given Zona waktu dipilih; start/end dan timezone; recurrence hanya P2 | When Simpan pertemuan | Then 09.00–10.00 WIB diterima; 10.00–09.00 pada hari sama ditolak | SCH-FR-002 |
| SCH-AC-003 | Given Dua interval pada hari sama; A09–10,B10–11; lalu B09.30–11 | When Deteksi konflik | Then Kasus pertama tidak bentrok; kedua bentrok 30 menit | SCH-FR-003 |
| SCH-AC-004 | Given Dua assessment di minggu sama; Remaining hours 6 dan 4; kapasitas 8 | When Hitung weekly demand | Then Demand=10 jam; rasio=1,25; status di atas kapasitas | SCH-FR-004 |
| SCH-AC-005 | Given Tiga assessment jatuh minggu itu; Durasi 6,4,unknown | When Hitung coverage | Then Known=10 jam; coverage=2/3; label estimasi parsial | SCH-FR-005 |
| SCH-AC-006 | Given Known hours=10; capacity unknown atau 0 | When Tampilkan beban tanpa kapasitas | Then Unknown: tanpa rasio; 0: tidak ada waktu tersedia, rasio tidak dihitung | SCH-FR-006 |
| SCH-AC-007 | Given Tugas 6 jam due minggu 2; Alokasi 2 jam minggu 1 dan 4 jam minggu 2 | When Simpan blok persiapan | Then Total lintas minggu tetap 6 jam; deadline tidak berubah | SCH-FR-007 |
| SCH-AC-008 | Given Bobot 10% dan 40% pada offering berbeda; 2 assessment minggu sama | When Tampilkan salience assessment | Then Tidak menampilkan 50% sebagai total lintas offering atau menambah ke jam | SCH-FR-008 |
| SCH-AC-009 | Given Assessment punya blok persiapan; Deadline baru sebelum satu blok yang ada | When Geser deadline | Then Tidak memindahkan blok otomatis; radar memakai revision baru | SCH-FR-009 |
| SCH-AC-010 | Given Kapasitas per hari tersedia; Durasi tersisa dan deadline | When Minta saran persiapan | Then Saran belum menjadi meeting sampai disetujui | SCH-FR-010 |
| SCH-AC-011 | Given Tugas remaining6 jam; Blok4+3 jam, estimasi−1, kapasitas−2 | When Validasi alokasi | Then 4+3 ditolak; tidak ada double-count atau jam negatif | SCH-FR-011 |
| SCH-AC-012 | Given User tidak tahu jam; 10 Desember 2026 tanpa waktu | When Input deadline hanya tanggal | Then Tidak dibuat 23.59; tidak memicu bentrok interval palsu | SCH-FR-012 |
| SCH-AC-101 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | SCH-NFR-001 |
| SCH-AC-102 | Given Beban uji dasar dan data telah tersedia | When Buka tampilan utama 30 kali | Then p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | SCH-NFR-002 |
| SCH-AC-103 | Given Fixture 10 jam pada bagian 9 | When Alokasikan A 2+4 jam | Then Total tetap 10 dan tidak ada negatif; source revision terlacak | SCH-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| SCH-T-001 | integrasi | Enrollment dengan assessment; assessment_id, due_at | Tambah deadline dari jadwal | Tracker dan jadwal membaca satu deadline yang sama | P1 | SCH-FR-001 / SCH-AC-001 |
| SCH-T-002 | boundary | Zona waktu dipilih; start/end dan timezone; recurrence hanya P2 | Simpan pertemuan | 09.00–10.00 WIB diterima; 10.00–09.00 pada hari sama ditolak | P1 | SCH-FR-002 / SCH-AC-002 |
| SCH-T-003 | boundary | Dua interval pada hari sama; A09–10,B10–11; lalu B09.30–11 | Deteksi konflik | Kasus pertama tidak bentrok; kedua bentrok 30 menit | P1 | SCH-FR-003 / SCH-AC-003 |
| SCH-T-004 | numerik | Dua assessment di minggu sama; Remaining hours 6 dan 4; kapasitas 8 | Hitung weekly demand | Demand=10 jam; rasio=1,25; status di atas kapasitas | P1 | SCH-FR-004 / SCH-AC-004 |
| SCH-T-005 | edge | Tiga assessment jatuh minggu itu; Durasi 6,4,unknown | Hitung coverage | Known=10 jam; coverage=2/3; label estimasi parsial | P1 | SCH-FR-005 / SCH-AC-005 |
| SCH-T-006 | boundary | Known hours=10; capacity unknown atau 0 | Tampilkan beban tanpa kapasitas | Unknown: tanpa rasio; 0: tidak ada waktu tersedia, rasio tidak dihitung | P1 | SCH-FR-006 / SCH-AC-006 |
| SCH-T-007 | numerik | Tugas 6 jam due minggu 2; Alokasi 2 jam minggu 1 dan 4 jam minggu 2 | Simpan blok persiapan | Total lintas minggu tetap 6 jam; deadline tidak berubah | P2 | SCH-FR-007 / SCH-AC-007 |
| SCH-T-008 | negatif | Bobot 10% dan 40% pada offering berbeda; 2 assessment minggu sama | Tampilkan salience assessment | Tidak menampilkan 50% sebagai total lintas offering atau menambah ke jam | P2 | SCH-FR-008 / SCH-AC-008 |
| SCH-T-009 | integrasi | Assessment punya blok persiapan; Deadline baru sebelum satu blok yang ada | Geser deadline | Tidak memindahkan blok otomatis; radar memakai revision baru | P2 | SCH-FR-009 / SCH-AC-009 |
| SCH-T-010 | fungsional | Kapasitas per hari tersedia; Durasi tersisa dan deadline | Minta saran persiapan | Saran belum menjadi meeting sampai disetujui | P2 | SCH-FR-010 / SCH-AC-010 |
| SCH-T-011 | boundary | Tugas remaining 6 jam; Blok 4+3 jam, estimasi−1, kapasitas−2 | Validasi alokasi | 4+3 ditolak; tidak ada double-count atau jam negatif | P2 | SCH-FR-011 / SCH-AC-011 |
| SCH-T-012 | boundary | User tidak tahu jam; 10 Desember 2026 tanpa waktu | Input deadline hanya tanggal | Tidak dibuat 23.59; tidak memicu bentrok interval palsu | P1 | SCH-FR-012 / SCH-AC-012 |
| SCH-T-101 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | SCH-NFR-001 / SCH-AC-101 |
| SCH-T-102 | nonfungsional | Beban uji dasar dan data telah tersedia | Buka tampilan utama 30 kali | p95 ≤2 detik; kegagalan ditandai dan dicatat, bukan dibuang dari sampel | P0 | SCH-NFR-002 / SCH-AC-102 |
| SCH-T-103 | nonfungsional | Fixture 10 jam pada bagian 9 | Alokasikan A 2+4 jam | Total tetap 10 dan tidak ada negatif; source revision terlacak | P0 | SCH-NFR-003 / SCH-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| SCH-Q1 | Estimasi durasi subjektif | Rasio tampak presisi semu | Tampilkan coverage dan tanggal estimasi |
| SCH-Q2 | Tanggal dan jam tidak lengkap | Konflik palsu | Date-only tidak dijadikan instant |
| SCH-Q3 | API personal SLCM belum terbukti | Sync tidak dapat dibangun | Input manual P1; integrasi off |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Tidak ada diagnosis, wearable, skor mental health, atau scrape jadwal. Recurrence kompleks dan scheduling otomatis P2 setelah review.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: SCH-FR-007, SCH-FR-008, SCH-FR-009, SCH-FR-010, SCH-FR-011. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-01 brief. Algoritma jam, kapasitas dan bucket merupakan PRODUCT_ASSUMPTION D-06; bukan instrumen klinis. Akses API personal SLCM tetap NEEDS_VALIDATION.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-07 pada audit untuk alasan revisi.

