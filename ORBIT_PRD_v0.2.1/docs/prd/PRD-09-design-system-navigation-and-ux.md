# PRD-09 — UI/UX Design System & Navigation

## 1. Document Control

| Field | Isi |
| --- | --- |
| ID / versi | PRD-09 / v0.2.1 DDP1 Errata |
| Status | Draft untuk review manusia; bukan bukti implementasi |
| Owner | UX Lead / Accessibility Reviewer |
| Tanggal | 18 November 2026 (Asia/Jakarta) |
| Asumsi | Dua screenshot Figma telah diamati; interaksi, layer properties, responsivitas dan contrast belum diuji. Token di sini usulan konseptual. |
| Acuan canon | [PRD-00](PRD-00-master-product-overview.md), [glossary](../00-governance/GLOSSARY-AND-DECISION-LOG.md) |
| Change log | v0.1 dipertahankan sebagai baseline; v0.2: audit DDP1, prioritas dan kontrak rilis direvisi terarah. Lihat [changelog](../00-governance/PRD-REVISION-CHANGELOG.md). v0.2.1: errata prioritas/journey dari review independen; FR dan ID tetap. |

## 2. Executive Summary & Problem

Desain Orbit harus membuat angka, sumber dan tindakan mudah dipindai. Referensi visual memiliki identitas orbit, sidebar ringkas dan ruang kosong yang tenang; spesifikasi ini melengkapi perilaku, state dan aksesibilitas yang tidak dapat dibuktikan oleh gambar statis.

## 3. Goals, Non-Goals & Success Metrics

Navigasi konsisten lintas modul; data aktual dan simulasi dapat dibedakan; semua aksi utama dapat diakses lewat keyboard dan layar kecil.

**Non-goals:** Menyatakan Figma sudah fungsional/accessible, menyelesaikan logo final atau mengunci implementasi framework.

| Metrik usulan | Definisi / pengukuran | Target / batas |
| --- | --- | --- |
| Task navigation | Peserta menemukan Nilai/Roadmap; Jadwal/Vault hanya jika P1 aktif | Usulan ≥4/5 tanpa bantuan |
| Accessibility release gates | Keyboard, contrast, reflow dan chart alternative | Nol blocker P0 sebelum demo |
| State comprehension | Peserta mengenali loading/empty/error/stale | Usulan ≥4/5 pada fixture |

Semua target merupakan PRODUCT_ASSUMPTION untuk evaluasi prototipe; belum ada baseline pengguna atau hasil pengukuran. Jangan mengklaim dampak akademik kausal dari penggunaan fitur.

## 4. Personas & Permissions

Mahasiswa desktop/mobile, pengguna keyboard/screen reader, dan moderator dengan kebutuhan kepadatan informasi.

| Aktor | Boleh | Tidak boleh |
| --- | --- | --- |
| Guest | Public navigation | Personal counters |
| Student | Workspace navigation sesuai scope | Role controls yang tidak diizinkan |
| Moderator/admin | Navigation sesuai role | Tidak melihat nilai privat melalui menu admin |

Hak dibatasi juga oleh kepemilikan record dan status publikasi, bukan role saja. Matriks keamanan canon ada pada PRD-10.

## 5. Scope & Minimum Vertical Slice

**Batas rilis v0.2:** panduan DDP1 (SRC-11) mengatur tugas, bukan daftar fitur Orbit. Prioritas di bawah adalah rekomendasi hasil analisis kelayakan. Bagian persona, perjalanan, model data dan UI menyimpan visi lengkap; suatu alur/role hanya aktif bila FR terkait diaktifkan. P2 berarti **Future Development**, bukan requirement dihapus. Pada P0, istilah pemilik/user merujuk owner_scope demo lokal AUTH-FR-014; login, moderator dan komunitas hanya untuk mode future. BR/AC/test mengikuti kemampuan aktif, sehingga tidak membuat dependensi P2 wajib secara tersirat.

| P0 — MVP DDP1 | P1 — opsional setelah gate | P2 — Future Development |
| --- | --- | --- |
| Shell Orbit, tema terang, navigasi inti, dashboard, forms/states, label sumber dan aksesibilitas | Tren akademik hanya bila data/GPA P1 tersedia | Tema gelap, motion/density lanjutan dan native app |

**Slice rilis:** Workspace → dashboard → roadmap list atau Grade Rescue → hasil → dashboard. Warna, tipografi, orbit motif dan struktur visual baseline dipertahankan; hanya menu/capability aktif dibatasi.

Setiap FR tetap berada di bagian 8 dengan ID lama; daftar disposisi lengkap dan estimasi ada di [MVP Scope](../00-governance/MVP-SCOPE-AND-PRIORITIES.md). Batas resmi: 10 Desember 2026 pukul 23.59 WIB, tim 3–4 orang, GitHub publik dan video YouTube maksimal 15 menit (SRC-11 hlm. 1–5). Stack rekomendasi: monolit Python + Flask/Jinja + SQLite; bukan framework yang diwajibkan dosen.

## 6. Entry Points & User Journeys

**Batas handoff arsitektur/implementasi:** hanya FR P0 beserta BR, NFR, AC dan test yang relevan untuk kemampuan aktif. P1/P2 serta subkemampuan future di dalam FR campuran tetap nonaktif sampai ada keputusan perubahan scope eksplisit dan tercatat. Journey berlabel future tidak menjadi kontrak coding P0.

Alur rilis DDP1 yang berlaku: Workspace → dashboard → roadmap list atau Grade Rescue → hasil → dashboard. Warna, tipografi, orbit motif dan struktur visual baseline dipertahankan; hanya menu/capability aktif dibatasi. Alur lengkap di bawah disimpan untuk kemampuan yang prioritasnya sesuai bagian 5/8; bukan kewajiban menyelesaikan seluruhnya pada P0.

**J1 — P0 aktif.** Buka workspace demo lokal → dashboard menampilkan semester aktif dan hasil MAP/GRD → pilih course → edit nilai → kembali dengan semester/filter tetap. Jika data kosong, CTA isi data menggantikan angka ilustrasi. Varian login akun Orbit tetap P2 dan tidak diperlukan pada P0.

**J2 — P0 aktif.** User keyboard membuka sidebar → pilih Roadmap → pilih tampilan list → buka detail → tutup dialog dengan Escape. Fokus kembali ke tombol pemicu; tidak perlu drag.

**J3 — P1 opsional, hanya bila search dan Vault diaktifkan.** User mobile membuka global search → hasil berlabel tipe → pilih resource → kembali. Header tidak menutup content/focus; tabel punya tampilan list alternatif.

## 7. User Stories

| ID | Story | Prioritas | Requirement |
| --- | --- | --- | --- |
| UX-US-001 | As a student, I want memakai navigasi konsisten, so that saya tidak kehilangan konteks. | P0 | UX-FR-001, UX-FR-002, UX-FR-003 |
| UX-US-002 | As a keyboard user, I want mengakses semua interaksi, so that saya tidak bergantung pada pointer. | P0 | UX-FR-004, UX-FR-005, UX-FR-006 |
| UX-US-003 | As a student, I want memahami state dan nilai, so that saya tidak mengira data ilustratif aktual. | P0 / P1 (per FR) | UX-FR-007, UX-FR-008, UX-FR-009 |

## 8. Functional Requirements

| ID | P | Trigger | Precondition | Input | Expected behavior | Output / postcondition | AC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UX-FR-001 | P0 | Buka modul personal | Workspace dan term aktif; akun hanya untuk mode multiuser P2 | Route ke modul lain | Pertahankan term scope dan tampilkan breadcrumb | Term sama kecuali user menggantinya | UX-AC-001 |
| UX-FR-002 | P0 | Buka dashboard | Ada data parsial atau kosong | Summary GRD (K, bounds, target) dan MAP (eligibility, rencana, peringatan SKS) | Baca hasil Python GRD/MAP langsung dengan revision dan provenance; tampilkan tautan ke input/peringatan asal; jangan mensyaratkan GDE, SCH atau GPA P1 | Dashboard konsisten dengan hasil GRD/MAP; unknown berlabel; seluruh P1/P2 off tetap dapat dibuka; tidak ada angka atau tren fiktif | UX-AC-002 |
| UX-FR-003 | P0 | Resize viewport | Konten course/grade table | Lebar 360,768,1280 px | Adaptasi satu kolom/list tanpa hilang aksi atau field wajib | Tidak ada horizontal page scroll; graf/table kompleks punya alternatif | UX-AC-003 |
| UX-FR-004 | P0 | Navigasi keyboard | Dialog dan menu terbuka | Tab,Shift+Tab,Enter,Escape | Kelola fokus, label dan urutan yang sesuai tindakan | Modal tidak menjebak tanpa exit; fokus kembali ke trigger | UX-AC-004 |
| UX-FR-005 | P0 | Buka chart/roadmap | Data tersedia | Grafik/tren dan node edges | Sediakan tabel/list dengan data dan alasan ekuivalen | Semua nilai dan relasi tersedia tanpa warna/hover | UX-AC-005 |
| UX-FR-006 | P0 | Submit form invalid | BRP weight salah | Total 90% | Hubungkan error ke field dan rangkum kesalahan di atas form | Fokus ke ringkasan; input valid lain tidak hilang | UX-AC-006 |
| UX-FR-007 | P0 | Operasi tertunda/gagal | Save berlangsung | Loading lalu network failure | Bedakan pending, failed, saved dan stale dengan teks | Tidak muncul toast berhasil sebelum konfirmasi simpan | UX-AC-007 |
| UX-FR-008 | P0 | Ganti tampilan status | Passed/planned/unknown | Status berbeda | Gunakan label dan ikon selain warna | Status tetap dapat dibedakan dalam grayscale | UX-AC-008 |
| UX-FR-009 | P1 | Buka tren akademik | Hanya dua term punya nilai | Series aktual dua titik | Render hanya data yang tersedia dengan gap untuk missing; proyeksi berlabel | Tidak menggambar tren 8 semester fiktif | UX-AC-009 |
| UX-FR-010 | P2 | Pilih tema gelap | Tema gelap selesai diuji | Preference dark | Terapkan token semantik seluruh modul secara konsisten | Roadmap tidak berganti tema sendiri karena frame contoh | UX-AC-010 |

## 9. Business Rules & Algorithms

| ID | Aturan normatif produk | Diverifikasi melalui |
| --- | --- | --- |
| UX-BR-001 | Source visual hanya arah: Dashboard v2 terang, Roadmap v2 gelap. P0 memilih tema terang lintas halaman; dark mode P2 harus berlaku global dan diuji sendiri, serta hanya tampil aktif bila capability tema gelap diaktifkan. | UX-FR-010, UX-FR-001 |
| UX-BR-002 | Navigasi mengikuti capability manifest, bukan label prioritas saja. P0 menampilkan Ringkasan, Roadmap dan Nilai & Target serta akses ekspor/reset lokal. Jadwal, Vault dan search P1 hanya aktif setelah keputusan scope tercatat; Playbook dan Minat & Jalur adalah P2 dan hanya tampil aktif bila capability terkait diaktifkan. Pengelompokan Komunitas tetap bagian desain. Menu fitur nonaktif disembunyikan atau berlabel direncanakan, tanpa aksi aktif; bantuan lanjutan mengikuti capability, sedangkan petunjuk menjalankan demo tersedia pada README. | UX-FR-001, UX-FR-003 |
| UX-BR-003 | Hierarki angka: label jenis hasil → angka → coverage/provenance → action. Jangan menampilkan IPK prediksi tanpa label di area yang terbaca sebagai aktual. | UX-FR-002, UX-FR-009 |
| UX-BR-004 | Desain komponen: tombol utama satu per tindakan lokal, secondary untuk kembali/batal, destructive diberi konsekuensi konkret; penghapusan permanen melalui dialog AUTH. | UX-FR-004, UX-FR-006 |
| UX-BR-005 | Token semantik: canvas, surface, text-primary, text-muted, border, accent, success, warning, danger; status tidak dikodekan warna saja. Hex final diputus setelah contrast test. | UX-FR-008 |
| UX-BR-006 | Typography usulan: body 16px, caption minimal 12px, heading 24–36px, line-height 1,4–1,6. Spacing grid 4/8/12/16/24/32; radius 8–16. Target sentuh produk 44×44 CSS px untuk aksi utama. | UX-FR-003, UX-FR-004 |
| UX-BR-007 | Animasi hanya membantu perubahan state, 120–200ms usulan; prefers-reduced-motion menghilangkan gerakan nonesensial. Tidak ada confetti untuk nilai atau consent. | UX-FR-007 |
| UX-BR-008 | Grafik nilai menggunakan titik term diskrit; interpolation tidak menyatakan capaian di waktu tanpa data. Tooltip memiliki padanan focus/tabel. | UX-FR-005, UX-FR-009 |

### Observasi Figma, 18 November 2026

**Dashboard v2, node 11:22, 1440×980:** sidebar ikon, header orbit., search, notifikasi dan avatar; judul “Semestermu, lebih terarah”; pemilih semester; empat metric tiles; daftar fokus course di kiri; tren akademik dan daftar tindakan/insight di kanan. Footer menandai data ilustratif dan belum terhubung SLCM/SSO. Angka di frame tidak menjadi data produk.

**Roadmap v2, node 11:183, 1680×980:** tema navy gelap, kontrol program, tab Peta jalur/Daftar matkul, filter semester/kategori, kolom semester 1–8, legenda dan CTA simulasi. Frame menyebut nama dan hubungan sebagai contoh desain. Pengamatan gambar tidak memverifikasi click behavior, ukuran token exact, font family, kontras atau mobile.

**Perbaikan spesifikasi:** sidebar ikon diberi accessible names dan label saat dibutuhkan; tren menyertakan tabel; tampilan mobile default list; tema tidak berubah antar halaman; angka ilustrasi diganti empty state hingga data tersedia. Dashboard mengurangi card dekoratif dengan section heading dan list yang membantu tindakan.

## 10. Conceptual Data Model & Ownership

| Entitas / ID | Atribut dan relasi penting | Sumber / owner | Lifecycle / audit | Sensitivitas |
| --- | --- | --- | --- | --- |
| NavigationContext / user/session | active_term, route, filter state, scenario_id | UX from PRO/MAP | Transient; safe resume per account | Private |
| DesignTokenSet / version | semantic roles, type/space/motion; no hard stack | UX Lead | draft/reviewed; contrast evidence | Public specification |
| UIState / view | loading/empty/partial/error/stale/saved | Module state owner → UX | Derived; no duplicated source grade | Private where payload personal |
| AccessibilityEvidence / test_id | viewport, input mode, screen reader, findings | QA | Recorded at implementation | Internal non-sensitive |

Identitas berupa ID internal stabil, bukan nama tampilan. Setiap perubahan memiliki revision, updated_at, actor dan source_ref yang sesuai; hapus atau koreksi mengikuti PRD-10. Kontrak ini konseptual, tidak menentukan tabel fisik, ORM, atau endpoint.

## 11. UI/UX Specification

Komponen wajib sesuai kemampuan yang diaktifkan (chart/resource row hanya jika datanya dan fitur terkait aktif): app shell, semester switcher, course list item, source badge, scenario banner, BRP tree editor, validated field, result summary, chart+table, skeleton, empty panel, inline error, destructive confirmation, resource row dan reason disclosure. Setiap komponen memiliki focus, disabled, pending, error, success state yang relevan. Tombol disabled disertai alasan; error tidak hanya warna. Icon-only diberi accessible label; status save diumumkan tanpa memindahkan fokus. Notifikasi lonceng di Figma tidak wajib berfungsi sebagai inbox sebelum fitur tersedia.

## 12. States & Edge Cases

| State / kasus | Respons yang terlihat | Pemulihan / invariant |
| --- | --- | --- |
| Loading | Skeleton sesuai struktur tanpa angka palsu | Tidak dianggap empty |
| Empty | Sebab + satu CTA relevan | Tidak blame user |
| Partial | Apa yang belum tersedia | Angka diberi coverage |
| Error | Pesan manusiawi + retry | Input tetap |
| Stale | Data terakhir dan refresh | Bukan terkini |
| Reduced motion | Transition nonesensial mati | Semua informasi tetap ada |

## 13. Module Interfaces & Dependencies

**Kontrak rilis v0.2:** Dashboard P0 membaca hanya PRO/MAP/GRD dan capability manifest AUTH-FR-014. Search entry P1 dan authorization akun AUTH-FR-004 P2 tidak menjadi dependency core. Status/error/informasi sumber tetap mengikuti design system yang sama. Tabel berikut menyimpan kontrak produk lengkap dan berlaku hanya pada kemampuan yang diaktifkan.

| Dari → ke / requirement | Kontrak / trigger | Konflik, retry, fallback |
| --- | --- | --- |
| PRD-01 sampai PRD-08 → UX-FR-002 | Domain view model + state/provenance | UX tidak menghitung GPA sendiri |
| UX-FR-001 → SUP-FR-001 | Search entry dan contextual filters | Permission scope dari AUTH |
| AUTH-FR-004 → UX-FR-001 | Allowed actions per role+ownership | UI hide bukan pengganti authorization |
| MAP-FR-008/GRD-FR-004 → UX-FR-005 | Data ekuivalen untuk graph/list/table | Tidak menyederhanakan uncertainty hilang |

Envelope perubahan canon: event_id, entity_id, revision, occurred_at, owner_scope, source_ref, scenario_id nullable. Konsumen memeriksa izin sebelum membaca payload; event berulang tidak menggandakan hasil. MVP boleh menghitung ulang saat halaman dibuka tanpa broker/event bus. Tidak ada endpoint final pada tahap ini.

## 14. Privacy, Security & Trust

Dashboard tidak membocorkan nilai pada preview publik, error page atau metadata search publik. Preferensi tema tidak membutuhkan profil sensitif. Jangan memakai dark pattern untuk consent. Sumber desain Figma tidak digunakan sebagai sumber data mahasiswa.

Data personal tidak masuk telemetri mentah. Error hanya mencatat jenis operasi, status dan correlation_id terbatas; akses dukungan tidak otomatis membuka nilai. Consent kontribusi dipisahkan dari persetujuan memakai layanan.

## 15. Non-Functional Requirements

| ID | P | Kriteria terukur | AC |
| --- | --- | --- | --- |
| UX-NFR-001 | P0 | Target WCAG 2.2 AA pada alur P0; teks normal contrast ≥4,5:1, teks besar ≥3:1; komponen nonteks esensial ≥3:1. | UX-AC-101 |
| UX-NFR-002 | P0 | Reflow 320 CSS px dan zoom 200% tetap mempertahankan fungsi; graf/tabel punya alternatif list. | UX-AC-102 |
| UX-NFR-003 | P0 | Seluruh aksi utama dapat diselesaikan dengan keyboard; fokus terlihat dan tidak terjebak. | UX-AC-103 |

NFR P0 adalah gate kualitas untuk kemampuan yang diaktifkan. Jika kemampuan terkait P1/P2 ditunda, gate tersebut tidak mewajibkan pembangunan fitur itu; statusnya deferred bersama fitur.

Beban uji dasar: satu pengguna aktif pada perangkat laptop referensi yang dicatat QA, 100 course, 300 assessment dan 1.000 metadata resource; bukan klaim kapasitas produksi. Ukur 30 pengulangan untuk p95; setup, perangkat dan hasil dicatat saat implementasi. Semua target di atas belum diuji pada aplikasi.

Target latency dan accessibility tetap target produk, bukan kewajiban angka dari dosen. Benchmark sintetis terpisah dari fixture demo 6–12 course; tidak membutuhkan kurasi 100 course nyata.

## 16. Acceptance Criteria

| ID | Given | When | Then | Requirement |
| --- | --- | --- | --- | --- |
| UX-AC-001 | Given Workspace dan term aktif; akun hanya untuk mode multiuser P2; Route ke modul lain | When Buka modul personal | Then Term sama kecuali user menggantinya | UX-FR-001 |
| UX-AC-002 | Given Ada data parsial atau kosong; Summary GRD (K, bounds, target) dan MAP (eligibility, rencana, peringatan SKS) | When Buka dashboard | Then Dashboard konsisten dengan hasil GRD/MAP; unknown berlabel; seluruh P1/P2 off tetap dapat dibuka; tidak ada angka atau tren fiktif | UX-FR-002 |
| UX-AC-003 | Given Konten course/grade table; Lebar 360,768,1280 px | When Resize viewport | Then Tidak ada horizontal page scroll; graf/table kompleks punya alternatif | UX-FR-003 |
| UX-AC-004 | Given Dialog dan menu terbuka; Tab,Shift+Tab,Enter,Escape | When Navigasi keyboard | Then Modal tidak menjebak tanpa exit; fokus kembali ke trigger | UX-FR-004 |
| UX-AC-005 | Given Data tersedia; Grafik/tren dan node edges | When Buka chart/roadmap | Then Semua nilai dan relasi tersedia tanpa warna/hover | UX-FR-005 |
| UX-AC-006 | Given BRP weight salah; Total 90% | When Submit form invalid | Then Fokus ke ringkasan; input valid lain tidak hilang | UX-FR-006 |
| UX-AC-007 | Given Save berlangsung; Loading lalu network failure | When Operasi tertunda/gagal | Then Tidak muncul toast berhasil sebelum konfirmasi simpan | UX-FR-007 |
| UX-AC-008 | Given Passed/planned/unknown; Status berbeda | When Ganti tampilan status | Then Status tetap dapat dibedakan dalam grayscale | UX-FR-008 |
| UX-AC-009 | Given Hanya dua term punya nilai; Series aktual dua titik | When Buka tren akademik | Then Tidak menggambar tren 8 semester fiktif | UX-FR-009 |
| UX-AC-010 | Given Tema gelap selesai diuji; Preference dark | When Pilih tema gelap | Then Roadmap tidak berganti tema sendiri karena frame contoh | UX-FR-010 |
| UX-AC-101 | Given Token final tiap state dan tema aktif | When Ukur contrast dan review keyboard/screen reader | Then Semua kombinasi esensial lolos; status kepatuhan hanya setelah audit, bukan dari screenshot | UX-NFR-001 |
| UX-AC-102 | Given Alur P0 dengan error dan label panjang | When Ubah viewport 320 px, lalu zoom 200% | Then Tidak ada konten/aksi terpotong atau focus tertutup | UX-NFR-002 |
| UX-AC-103 | Given Satu record valid dan viewport 360 px serta desktop | When Jalankan journey utama dengan Tab, Enter, Escape | Then Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | UX-NFR-003 |

## 17. Test Matrix

| ID | Jenis | Input / setup | Langkah | Expected result | P | Kaitan |
| --- | --- | --- | --- | --- | --- | --- |
| UX-T-001 | fungsional | Workspace dan term aktif; akun hanya untuk mode multiuser P2; Route ke modul lain | Buka modul personal | Term sama kecuali user menggantinya | P0 | UX-FR-001 / UX-AC-001 |
| UX-T-002 | negatif | Ada data parsial atau kosong; Summary GRD (K, bounds, target) dan MAP (eligibility, rencana, peringatan SKS) | Buka dashboard | Dashboard konsisten dengan hasil GRD/MAP; unknown berlabel; seluruh P1/P2 off tetap dapat dibuka; tidak ada angka atau tren fiktif | P0 | UX-FR-002 / UX-AC-002 |
| UX-T-003 | responsif | Konten course/grade table; Lebar 360,768,1280 px | Resize viewport | Tidak ada horizontal page scroll; graf/table kompleks punya alternatif | P0 | UX-FR-003 / UX-AC-003 |
| UX-T-004 | aksesibilitas | Dialog dan menu terbuka; Tab,Shift+Tab,Enter,Escape | Navigasi keyboard | Modal tidak menjebak tanpa exit; fokus kembali ke trigger | P0 | UX-FR-004 / UX-AC-004 |
| UX-T-005 | aksesibilitas | Data tersedia; Grafik/tren dan node edges | Buka chart/roadmap | Semua nilai dan relasi tersedia tanpa warna/hover | P0 | UX-FR-005 / UX-AC-005 |
| UX-T-006 | negatif | BRP weight salah; Total 90% | Submit form invalid | Fokus ke ringkasan; input valid lain tidak hilang | P0 | UX-FR-006 / UX-AC-006 |
| UX-T-007 | edge | Save berlangsung; Loading lalu network failure | Operasi tertunda/gagal | Tidak muncul toast berhasil sebelum konfirmasi simpan | P0 | UX-FR-007 / UX-AC-007 |
| UX-T-008 | aksesibilitas | Passed/planned/unknown; Status berbeda | Ganti tampilan status | Status tetap dapat dibedakan dalam grayscale | P0 | UX-FR-008 / UX-AC-008 |
| UX-T-009 | negatif | Hanya dua term punya nilai; Series aktual dua titik | Buka tren akademik | Tidak menggambar tren 8 semester fiktif | P1 | UX-FR-009 / UX-AC-009 |
| UX-T-010 | fungsional | Tema gelap selesai diuji; Preference dark | Pilih tema gelap | Roadmap tidak berganti tema sendiri karena frame contoh | P2 | UX-FR-010 / UX-AC-010 |
| UX-T-101 | nonfungsional | Token final tiap state dan tema aktif | Ukur contrast dan review keyboard/screen reader | Semua kombinasi esensial lolos; status kepatuhan hanya setelah audit, bukan dari screenshot | P0 | UX-NFR-001 / UX-AC-101 |
| UX-T-102 | nonfungsional | Alur P0 dengan error dan label panjang | Ubah viewport 320 px, lalu zoom 200% | Tidak ada konten/aksi terpotong atau focus tertutup | P0 | UX-NFR-002 / UX-AC-102 |
| UX-T-103 | nonfungsional | Satu record valid dan viewport 360 px serta desktop | Jalankan journey utama dengan Tab, Enter, Escape | Tidak ada aksi wajib yang hanya bisa diklik/di-drag; fokus kembali ke pemicu dialog | P0 | UX-NFR-003 / UX-AC-103 |

**Status seluruh test aplikasi: SPECIFIED — NOT EXECUTED.** Pemeriksaan aritmetika independen dan audit dokumen, bila dilakukan, dicatat terpisah di QA-DOCUMENTATION-REPORT.md. Lulus audit dokumentasi tidak berarti aplikasi telah lolos uji.

## 18. Risks, Assumptions, Open Questions & Decision Log

| ID | Risiko / pertanyaan | Dampak | Default aman / owner |
| --- | --- | --- | --- |
| UX-Q1 | Tema Figma berbeda | Inconsistency | Satu tema P0; global dark P2 |
| UX-Q2 | Desain desktop lebar | Sulit mobile | Default list dan progressive disclosure |
| UX-Q3 | Belum ada uji aksesibilitas | Klaim berlebihan | Target, bukan status lulus |

Keputusan lokal tunduk pada [decision log canon](../00-governance/GLOSSARY-AND-DECISION-LOG.md). Perubahan aturan global harus memperbarui dokumen konsumen dan traceability sebelum versi baru disetujui.

## 19. Explicit Out-of-Scope & Future Work

Logo/brand final, dark theme lengkap, microanimation lanjutan dan native app tidak diperlukan untuk P0. Tidak ada redesign Figma dalam pekerjaan dokumentasi ini.

### Disposisi Future Development v0.2

Requirement ditunda, tidak dihapus: UX-FR-010. Semua perilaku, aturan, AC dan test tetap tersedia pada dokumen ini.

Fitur P1 yang tidak lolos gate kapasitas juga tetap terdokumentasi untuk rilis setelah DDP1. Prioritas bukan status implementasi; seluruh fitur masih spesifikasi.

## 20. Sources & Verification Register

SRC-06/07: screenshot frame dibaca melalui Figma; observasi di atas terverifikasi sebagai pengamatan visual saja. SRC-08 WCAG 2.2 untuk target aksesibilitas. Seluruh token detail adalah proposal produk D-11.

Daftar sumber, batas verifikasi, tanggal akses, dan tindak lanjut ada di [Research Register](../00-governance/RESEARCH-AND-VALIDATION-REGISTER.md). Fakta dari sumber tidak otomatis menjadi aturan aktif aplikasi; binding ke program, angkatan, versi kurikulum dan periode harus tercatat. Semua skenario numerik berlabel sintetis dan bukan data mahasiswa.

**SRC-11 — VERIFIED_OFFICIAL untuk aturan tugas:** Panduan Proyek Kelompok DDP1 Gasal 2026/2027, versi 1 (4 Nov 2026 16.00), seluruh 5 halaman diperiksa 18 Nov 2026. Hlm. 2: Python, konsep baru dan pemahaman kode/kontribusi; hlm. 3–4: tim/bimbingan/deliverables; hlm. 1/5: deadline/rubrik. Panduan tidak memverifikasi kurikulum, BRP atau API UI. Lihat [Compliance Matrix](../00-governance/DDP1-COMPLIANCE-MATRIX.md) dan AUD-12 pada audit untuk alasan revisi.

