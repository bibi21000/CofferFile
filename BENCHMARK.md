

# General benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| DummyFile            | download.html        |          16 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| DummyFile            | genindex-all.html    |          16 |        1755 |       1758 |     100.20% |   0.09 |   0.00 |
| DummyFile            | searchindex.js       |          16 |        3859 |       3867 |     100.20% |   0.37 |   0.01 |
| DummyFile            | library.pdf          |          16 |       11336 |      11358 |     100.20% |   3.68 |   0.02 |
| FernetFile           | download.html        |          16 |          11 |         15 |     134.34% |   0.01 |   0.01 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2354 |     134.13% |   0.09 |   0.02 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5176 |     134.13% |   0.34 |   0.04 |
| FernetFile           | library.pdf          |          16 |       11336 |      15205 |     134.13% |   5.02 |   0.09 |
| NaclFile             | download.html        |          16 |          11 |         11 |     100.64% |   0.01 |   0.01 |
| NaclFile             | genindex-all.html    |          16 |        1755 |       1763 |     100.44% |   0.03 |   0.01 |
| NaclFile             | searchindex.js       |          16 |        3859 |       3876 |     100.44% |   0.22 |   0.02 |
| NaclFile             | library.pdf          |          16 |       11336 |      11386 |     100.44% |   1.60 |   0.04 |
| AesFile              | download.html        |          16 |          11 |         11 |     100.56% |   0.21 |   0.01 |
| AesFile              | genindex-all.html    |          16 |        1755 |       1762 |     100.39% |   0.06 |   0.03 |
| AesFile              | searchindex.js       |          16 |        3859 |       3874 |     100.39% |   0.25 |   0.05 |
| AesFile              | library.pdf          |          16 |       11336 |      11379 |     100.38% |   1.65 |   0.14 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.37% |   0.01 |   0.01 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        210 |      11.95% |   0.18 |   0.05 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        826 |      21.40% |   0.32 |   0.13 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14909 |     131.52% |   3.33 |   2.52 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      36.15% |   0.02 |   0.01 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        220 |      12.51% |   0.49 |   0.02 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        798 |      20.69% |   1.73 |   0.06 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14777 |     130.36% |   7.30 |   2.19 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.80% |   0.01 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1755 |        325 |      18.51% |   0.02 |   0.01 |
| ZstdFernetFile       | searchindex.js       |          16 |        3859 |       1185 |      30.70% |   0.05 |   0.03 |
| ZstdFernetFile       | library.pdf          |          16 |       11336 |      14833 |     130.85% |   0.24 |   0.11 |
| ZstdNaclFile         | download.html        |          16 |          11 |          3 |      28.92% |   0.01 |   0.01 |
| ZstdNaclFile         | genindex-all.html    |          16 |        1755 |        243 |      13.86% |   0.02 |   0.01 |
| ZstdNaclFile         | searchindex.js       |          16 |        3859 |        887 |      22.99% |   0.06 |   0.02 |
| ZstdNaclFile         | library.pdf          |          16 |       11336 |      11106 |      97.97% |   0.15 |   0.05 |
| ZstdAesFile          | download.html        |          16 |          11 |          3 |      28.84% |   0.01 |   0.01 |
| ZstdAesFile          | genindex-all.html    |          16 |        1755 |        243 |      13.85% |   0.02 |   0.02 |
| ZstdAesFile          | searchindex.js       |          16 |        3859 |        887 |      22.98% |   0.06 |   0.02 |
| ZstdAesFile          | library.pdf          |          16 |       11336 |      11099 |      97.91% |   0.31 |   0.17 |
| DummyFile            | download.html        |          64 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| DummyFile            | genindex-all.html    |          64 |        1755 |       1756 |     100.05% |   0.02 |   0.00 |
| DummyFile            | searchindex.js       |          64 |        3859 |       3861 |     100.05% |   0.07 |   0.01 |
| DummyFile            | library.pdf          |          64 |       11336 |      11341 |     100.05% |   0.39 |   0.01 |
| FernetFile           | download.html        |          64 |          11 |         15 |     134.34% |   0.01 |   0.01 |
| FernetFile           | genindex-all.html    |          64 |        1755 |       2344 |     133.54% |   0.04 |   0.02 |
| FernetFile           | searchindex.js       |          64 |        3859 |       5153 |     133.53% |   0.10 |   0.03 |
| FernetFile           | library.pdf          |          64 |       11336 |      15137 |     133.53% |   0.63 |   0.09 |
| NaclFile             | download.html        |          64 |          11 |         11 |     100.64% |   0.01 |   0.01 |
| NaclFile             | genindex-all.html    |          64 |        1755 |       1757 |     100.11% |   0.03 |   0.01 |
| NaclFile             | searchindex.js       |          64 |        3859 |       3863 |     100.11% |   0.09 |   0.02 |
| NaclFile             | library.pdf          |          64 |       11336 |      11348 |     100.11% |   0.45 |   0.03 |
| AesFile              | download.html        |          64 |          11 |         11 |     100.56% |   0.01 |   0.01 |
| AesFile              | genindex-all.html    |          64 |        1755 |       1757 |     100.10% |   0.03 |   0.02 |
| AesFile              | searchindex.js       |          64 |        3859 |       3863 |     100.10% |   0.09 |   0.03 |
| AesFile              | library.pdf          |          64 |       11336 |      11347 |     100.10% |   0.57 |   0.09 |
| Bz2FernetFile        | download.html        |          64 |          11 |          4 |      39.37% |   0.01 |   0.01 |
| Bz2FernetFile        | genindex-all.html    |          64 |        1755 |        209 |      11.90% |   0.19 |   0.09 |
| Bz2FernetFile        | searchindex.js       |          64 |        3859 |        822 |      21.30% |   0.32 |   0.13 |
| Bz2FernetFile        | library.pdf          |          64 |       11336 |      14842 |     130.94% |   1.97 |   2.30 |
| LzmaFernetFile       | download.html        |          64 |          11 |          4 |      36.15% |   0.02 |   0.01 |
| LzmaFernetFile       | genindex-all.html    |          64 |        1755 |        219 |      12.46% |   0.44 |   0.02 |
| LzmaFernetFile       | searchindex.js       |          64 |        3859 |        795 |      20.59% |   1.68 |   0.05 |
| LzmaFernetFile       | library.pdf          |          64 |       11336 |      14712 |     129.78% |   5.58 |   2.24 |
| ZstdFernetFile       | download.html        |          64 |          11 |          4 |      38.80% |   0.01 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |          64 |        1755 |        323 |      18.42% |   0.02 |   0.01 |
| ZstdFernetFile       | searchindex.js       |          64 |        3859 |       1179 |      30.56% |   0.06 |   0.03 |
| ZstdFernetFile       | library.pdf          |          64 |       11336 |      14762 |     130.23% |   0.25 |   0.09 |
| ZstdNaclFile         | download.html        |          64 |          11 |          3 |      28.92% |   0.01 |   0.01 |
| ZstdNaclFile         | genindex-all.html    |          64 |        1755 |        242 |      13.81% |   0.02 |   0.01 |
| ZstdNaclFile         | searchindex.js       |          64 |        3859 |        884 |      22.91% |   0.04 |   0.01 |
| ZstdNaclFile         | library.pdf          |          64 |       11336 |      11067 |      97.63% |   0.17 |   0.03 |
| ZstdAesFile          | download.html        |          64 |          11 |          3 |      28.84% |   0.01 |   0.01 |
| ZstdAesFile          | genindex-all.html    |          64 |        1755 |        242 |      13.81% |   0.02 |   0.01 |
| ZstdAesFile          | searchindex.js       |          64 |        3859 |        884 |      22.90% |   0.04 |   0.02 |
| ZstdAesFile          | library.pdf          |          64 |       11336 |      11065 |      97.61% |   0.22 |   0.10 |
| DummyFile            | download.html        |         256 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| DummyFile            | genindex-all.html    |         256 |        1755 |       1755 |     100.01% |   0.00 |   0.00 |
| DummyFile            | searchindex.js       |         256 |        3859 |       3860 |     100.01% |   0.03 |   0.00 |
| DummyFile            | library.pdf          |         256 |       11336 |      11337 |     100.01% |   0.14 |   0.02 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.34% |   0.02 |   0.01 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.38% |   0.04 |   0.02 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.39% |   0.06 |   0.04 |
| FernetFile           | library.pdf          |         256 |       11336 |      15120 |     133.38% |   0.25 |   0.10 |
| NaclFile             | download.html        |         256 |          11 |         11 |     100.64% |   0.01 |   0.01 |
| NaclFile             | genindex-all.html    |         256 |        1755 |       1756 |     100.03% |   0.02 |   0.02 |
| NaclFile             | searchindex.js       |         256 |        3859 |       3860 |     100.03% |   0.04 |   0.02 |
| NaclFile             | library.pdf          |         256 |       11336 |      11339 |     100.03% |   0.19 |   0.05 |
| AesFile              | download.html        |         256 |          11 |         11 |     100.56% |   0.01 |   0.01 |
| AesFile              | genindex-all.html    |         256 |        1755 |       1755 |     100.02% |   0.02 |   0.02 |
| AesFile              | searchindex.js       |         256 |        3859 |       3860 |     100.03% |   0.05 |   0.03 |
| AesFile              | library.pdf          |         256 |       11336 |      11338 |     100.02% |   0.23 |   0.10 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.37% |   0.01 |   0.01 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.23 |   0.06 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.33 |   0.13 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14826 |     130.79% |   1.79 |   2.40 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      36.15% |   0.02 |   0.01 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.42 |   0.02 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.68 |   0.06 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14695 |     129.64% |   5.11 |   2.35 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.80% |   0.01 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.02 |   0.01 |
| ZstdFernetFile       | searchindex.js       |         256 |        3859 |       1178 |      30.52% |   0.05 |   0.02 |
| ZstdFernetFile       | library.pdf          |         256 |       11336 |      14741 |     130.04% |   0.20 |   0.09 |
| ZstdNaclFile         | download.html        |         256 |          11 |          3 |      28.92% |   0.01 |   0.01 |
| ZstdNaclFile         | genindex-all.html    |         256 |        1755 |        242 |      13.80% |   0.01 |   0.01 |
| ZstdNaclFile         | searchindex.js       |         256 |        3859 |        883 |      22.88% |   0.05 |   0.02 |
| ZstdNaclFile         | library.pdf          |         256 |       11336 |      11055 |      97.52% |   0.17 |   0.05 |
| ZstdAesFile          | download.html        |         256 |          11 |          3 |      28.84% |   0.01 |   0.01 |
| ZstdAesFile          | genindex-all.html    |         256 |        1755 |        242 |      13.80% |   0.02 |   0.01 |
| ZstdAesFile          | searchindex.js       |         256 |        3859 |        883 |      22.88% |   0.05 |   0.02 |
| ZstdAesFile          | library.pdf          |         256 |       11336 |      11054 |      97.52% |   0.21 |   0.09 |
| DummyFile            | download.html        |        1024 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| DummyFile            | genindex-all.html    |        1024 |        1755 |       1755 |     100.00% |   0.00 |   0.00 |
| DummyFile            | searchindex.js       |        1024 |        3859 |       3859 |     100.00% |   0.01 |   0.01 |
| DummyFile            | library.pdf          |        1024 |       11336 |      11336 |     100.00% |   0.07 |   0.04 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.34% |   0.01 |   0.01 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.35% |   0.02 |   0.02 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.35% |   0.05 |   0.04 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15116 |     133.35% |   0.15 |   0.10 |
| NaclFile             | download.html        |        1024 |          11 |         11 |     100.64% |   0.01 |   0.01 |
| NaclFile             | genindex-all.html    |        1024 |        1755 |       1755 |     100.01% |   0.02 |   0.02 |
| NaclFile             | searchindex.js       |        1024 |        3859 |       3859 |     100.01% |   0.04 |   0.03 |
| NaclFile             | library.pdf          |        1024 |       11336 |      11337 |     100.01% |   0.12 |   0.05 |
| AesFile              | download.html        |        1024 |          11 |         11 |     100.56% |   0.01 |   0.01 |
| AesFile              | genindex-all.html    |        1024 |        1755 |       1755 |     100.01% |   0.02 |   0.02 |
| AesFile              | searchindex.js       |        1024 |        3859 |       3859 |     100.01% |   0.05 |   0.04 |
| AesFile              | library.pdf          |        1024 |       11336 |      11336 |     100.01% |   0.14 |   0.08 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.37% |   0.01 |   0.01 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.19 |   0.05 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.32 |   0.16 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14822 |     130.75% |   1.35 |   2.32 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      36.15% |   0.02 |   0.01 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.47 |   0.02 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   1.66 |   0.05 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   5.10 |   2.06 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.80% |   0.01 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.02 |   0.01 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3859 |       1177 |      30.51% |   0.05 |   0.03 |
| ZstdFernetFile       | library.pdf          |        1024 |       11336 |      14737 |     130.00% |   0.24 |   0.13 |
| ZstdNaclFile         | download.html        |        1024 |          11 |          3 |      28.92% |   0.01 |   0.01 |
| ZstdNaclFile         | genindex-all.html    |        1024 |        1755 |        242 |      13.80% |   0.01 |   0.01 |
| ZstdNaclFile         | searchindex.js       |        1024 |        3859 |        883 |      22.88% |   0.04 |   0.02 |
| ZstdNaclFile         | library.pdf          |        1024 |       11336 |      11052 |      97.50% |   0.15 |   0.08 |
| ZstdAesFile          | download.html        |        1024 |          11 |          3 |      28.84% |   0.01 |   0.01 |
| ZstdAesFile          | genindex-all.html    |        1024 |        1755 |        242 |      13.80% |   0.02 |   0.01 |
| ZstdAesFile          | searchindex.js       |        1024 |        3859 |        883 |      22.88% |   0.05 |   0.02 |
| ZstdAesFile          | library.pdf          |        1024 |       11336 |      11052 |      97.50% |   0.16 |   0.15 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15963 |      94.12% |   2.01 |   3.10 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15873 |      93.59% |   1.91 |   2.85 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15868 |      93.56% |   2.02 |   2.81 |
| TarZstdNaclFile      | html,js and pdf      |          16 |       16961 |      12232 |      72.12% |   0.21 |   0.10 |
| TarZstdNaclFile      | html,js and pdf      |         256 |       16961 |      12180 |      71.81% |   0.18 |   0.09 |
| TarZstdNaclFile      | html,js and pdf      |        1024 |       16961 |      12178 |      71.80% |   0.20 |   0.13 |
| TarZstdAesFile       | html,js and pdf      |          16 |       16961 |      12189 |      71.87% |   0.25 |   0.14 |
| TarZstdAesFile       | html,js and pdf      |         256 |       16961 |      12189 |      71.87% |   0.25 |   0.15 |
| TarZstdAesFile       | html,js and pdf      |        1024 |       16961 |      12189 |      71.87% |   0.29 |   0.16 |
| TarZstdFernetFile    | html,js and pdf      |          16 |       16961 |      16260 |      95.87% |   0.24 |   0.17 |
| TarZstdFernetFile    | html,js and pdf      |         256 |       16961 |      16260 |      95.87% |   0.28 |   0.15 |
| TarZstdFernetFile    | html,js and pdf      |        1024 |       16961 |      16260 |      95.87% |   0.25 |   0.14 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15786 |      93.07% |   7.29 |   2.50 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15693 |      92.52% |   7.06 |   2.18 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.50% |   7.17 |   2.28 |
| TarFile              | html,js and pdf      |           0 |       16961 |      16970 |     100.05% |   0.02 |   0.05 |


# Benchmarks ZstdFernetFile

Tests with different compression level and workers

| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|
| ZstdFernetFile       | genindex-all.html    |   9 |    2 |        1755 |        258 |      14.68% |   0.05 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |   9 |    8 |        1755 |        258 |      14.68% |   0.04 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |   9 |   12 |        1755 |        258 |      14.68% |   0.05 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |    2 |        1755 |        217 |      12.34% |   0.94 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |    8 |        1755 |        217 |      12.34% |   0.88 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |   12 |        1755 |        217 |      12.34% |   0.88 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |    2 |        3859 |        964 |      24.99% |   0.12 |   0.02 |
| ZstdFernetFile       | searchindex.js       |   9 |    8 |        3859 |        964 |      24.99% |   0.11 |   0.02 |
| ZstdFernetFile       | searchindex.js       |   9 |   12 |        3859 |        964 |      24.99% |   0.11 |   0.02 |
| ZstdFernetFile       | searchindex.js       |  19 |    2 |        3859 |        836 |      21.67% |   1.89 |   0.02 |
| ZstdFernetFile       | searchindex.js       |  19 |    8 |        3859 |        836 |      21.67% |   1.87 |   0.02 |
| ZstdFernetFile       | searchindex.js       |  19 |   12 |        3859 |        836 |      21.67% |   1.93 |   0.02 |
| ZstdFernetFile       | library.pdf          |   9 |    2 |       11336 |      14659 |     129.32% |   0.29 |   0.11 |
| ZstdFernetFile       | library.pdf          |   9 |    8 |       11336 |      14659 |     129.32% |   0.30 |   0.09 |
| ZstdFernetFile       | library.pdf          |   9 |   12 |       11336 |      14659 |     129.32% |   0.29 |   0.13 |
| ZstdFernetFile       | library.pdf          |  19 |    2 |       11336 |      14617 |     128.95% |   3.30 |   0.10 |
| ZstdFernetFile       | library.pdf          |  19 |    8 |       11336 |      14617 |     128.95% |   3.29 |   0.10 |
| ZstdFernetFile       | library.pdf          |  19 |   12 |       11336 |      14617 |     128.95% |   3.17 |   0.09 |
