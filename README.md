# STUDI KASUS

Sistem pakar ini digunakan untuk mendeteksi tingkat **burnout mahasiswa** berdasarkan gejala yang dialami pada aspek akademik, fisik, dan emosional.

Sistem bekerja dengan menerima fakta awal berupa gejala yang dipilih pengguna, kemudian melakukan proses penalaran menggunakan metode **Forward Chaining** untuk menentukan tingkat burnout yang dialami. Selanjutnya, metode **Certainty Factor** digunakan untuk menghitung tingkat keyakinan terhadap hasil diagnosis yang diperoleh.

# METODE

## 1. Forward Chaining

Forward Chaining merupakan metode penalaran yang bekerja berdasarkan pendekatan **data-driven**, yaitu proses inferensi dimulai dari fakta atau gejala yang diberikan pengguna menuju suatu kesimpulan.

## 2. Certainty Factor

Certainty Factor (CF) merupakan metode yang digunakan untuk mengukur tingkat keyakinan suatu diagnosis.

# GEJALA / FAKTA AWAL

| Kode | Gejala                      |
| ---- | --------------------------- |
| G1   | Sering Begadang             |
| G2   | Tugas Menumpuk              |
| G3   | Sulit Berkonsentrasi        |
| G4   | Kehilangan Motivasi Belajar |
| G5   | Mudah Lelah                 |
| G6   | Sulit Tidur                 |
| G7   | Mudah Marah                 |
| G8   | Menarik Diri dari Pergaulan |

# FAKTA ANTARA

| Kode | Keterangan         |
| ---- | ------------------ |
| F1   | Kelelahan Fisik    |
| F2   | Gangguan Akademik  |
| F3   | Gangguan Emosional |
| F4   | Burnout Awal       |
| F5   | Burnout Menengah   |

# HASIL AKHIR (GOAL)

| Kode | Diagnosis      |
| ---- | -------------- |
| P1   | Burnout Ringan |
| P2   | Burnout Sedang |
| P3   | Burnout Berat  |

# RULE BASE SISTEM

| Rule | Bobot CF | Aturan                                    |
| ---- | -------- | ----------------------------------------- |
| R1   | 0.90     | IF G1 AND G5 THEN F1 (Kelelahan Fisik)    |
| R2   | 0.85     | IF G3 AND G4 THEN F2 (Gangguan Akademik)  |
| R3   | 0.90     | IF G7 AND G8 THEN F3 (Gangguan Emosional) |
| R4   | 0.90     | IF F1 AND F2 THEN F4 (Burnout Awal)       |
| R5   | 0.85     | IF F4 AND G6 THEN P1 (Burnout Ringan)     |
| R6   | 0.90     | IF P1 AND F3 THEN F5 (Burnout Menengah)   |
| R7   | 0.95     | IF F5 AND G2 THEN P2 (Burnout Sedang)     |
| R8   | 0.95     | IF P2 AND G6 THEN P3 (Burnout Berat)      |

# ALUR PENALARAN FORWARD CHAINING

```text
Fakta Awal (G1 - G8)
        ↓
R1, R2, R3
        ↓
F1, F2, F3
        ↓
R4
        ↓
F4 (Burnout Awal)
        ↓
R5
        ↓
P1 (Burnout Ringan)
        ↓
R6
        ↓
F5 (Burnout Menengah)
        ↓
R7
        ↓
P2 (Burnout Sedang)
        ↓
R8
        ↓
P3 (Burnout Berat)
```
