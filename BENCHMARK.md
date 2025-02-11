# Benchmarks FernetStore

Tests done with autoflush, with or without open_secure.

WT -1, ... are the last store.add time in store

WTime is the total write time. RTime the time spent to read

| Data              | NbDocs | Op sec | Orig size | Crypt size | C Ratio | WTime | Rtime | WT -1 | WT -2 | WT -3 | WT -4 |
|:------------------|-------:|-------:|----------:|-----------:|--------:|------:|------:|------:|------:|------:|------:|
|genindex-all.html  |      5 | None   |      8775 |        325 |    3.70 |  0.11 |  0.04 |  0.02 |  0.02 |  0.02 |  0.02 |
|genindex-all.html  |      5 | frnz   |      8775 |       1625 |   18.51 |  0.15 |  0.07 |  0.03 |  0.03 |  0.03 |  0.03 |
|genindex-all.html  |      5 | frnt   |      8775 |      11772 |  134.15 |  0.71 |  0.17 |  0.15 |  0.14 |  0.12 |  0.10 |
|genindex-all.html  |      5 | nacz   |      8775 |       1630 |   18.57 |  0.14 |  0.06 |  0.03 |  0.02 |  0.02 |  0.02 |
|genindex-all.html  |      5 | nacl   |      8775 |      11745 |  133.85 |  0.54 |  0.12 |  0.12 |  0.10 |  0.09 |  0.07 |
|genindex-all.html  |     20 | None   |     35100 |        328 |    0.93 |  0.63 |  0.15 |  0.04 |  0.04 |  0.04 |  0.04 |
|genindex-all.html  |     20 | frnz   |     35100 |       6499 |   18.51 |  1.15 |  0.30 |  0.08 |  0.08 |  0.08 |  0.07 |
|genindex-all.html  |     20 | frnt   |     35100 |      47090 |  134.16 |  6.23 |  0.71 |  0.50 |  0.46 |  0.41 |  0.39 |
|genindex-all.html  |     20 | nacz   |     35100 |       6519 |   18.57 |  1.04 |  0.24 |  0.08 |  0.08 |  0.07 |  0.07 |
|genindex-all.html  |     20 | nacl   |     35100 |      46980 |  133.85 |  5.21 |  0.48 |  0.40 |  0.37 |  0.36 |  0.35 |
|searchindex.js     |      5 | None   |     19295 |       5906 |   30.61 |  0.70 |  0.14 |  0.17 |  0.14 |  0.11 |  0.08 |
|searchindex.js     |      5 | frnz   |     19295 |       5923 |   30.70 |  0.49 |  0.18 |  0.11 |  0.09 |  0.07 |  0.07 |
|searchindex.js     |      5 | frnt   |     19295 |      25882 |  134.14 |  3.14 |  0.47 |  0.69 |  0.70 |  0.46 |  0.37 |
|searchindex.js     |      5 | nacz   |     19295 |       5917 |   30.67 |  0.51 |  0.16 |  0.12 |  0.09 |  0.08 |  0.08 |
|searchindex.js     |      5 | nacl   |     19295 |      25815 |  133.79 |  2.05 |  0.25 |  0.41 |  0.38 |  0.34 |  0.35 |
|searchindex.js     |     20 | None   |     77181 |      23627 |   30.61 |  7.41 |  0.54 |  0.72 |  0.61 |  0.55 |  0.56 |
|searchindex.js     |     20 | frnz   |     77181 |      23693 |   30.70 |  3.13 |  0.61 |  0.24 |  0.23 |  0.22 |  0.22 |
|searchindex.js     |     20 | frnt   |     77181 |     103528 |  134.14 | 16.50 |  1.50 |  1.40 |  1.21 |  1.07 |  1.06 |
|searchindex.js     |     20 | nacz   |     77181 |      23670 |   30.67 |  2.89 |  0.51 |  0.24 |  0.26 |  0.21 |  0.19 |
|searchindex.js     |     20 | nacl   |     77181 |     103257 |  133.78 | 13.55 |  0.92 |  0.97 |  0.98 |  0.92 |  0.94 |
|library.pdf        |      5 | None   |     56679 |      73784 |  130.18 |  3.43 |  0.59 |  0.84 |  0.66 |  0.50 |  0.36 |
|library.pdf        |      5 | frnz   |     56679 |      74138 |  130.80 |  4.04 |  1.06 |  0.96 |  0.77 |  0.62 |  0.55 |
|library.pdf        |      5 | frnt   |     56679 |      76022 |  134.13 | 15.48 |  0.99 |  2.69 |  2.66 |  2.84 |  2.55 |
|library.pdf        |      5 | nacz   |     56679 |      73926 |  130.43 |  2.95 |  0.68 |  0.70 |  0.58 |  0.48 |  0.36 |
|library.pdf        |      5 | nacl   |     56679 |      75806 |  133.75 | 10.42 |  0.74 |  2.44 |  1.97 |  1.82 |  1.91 |
|library.pdf        |     20 | None   |    226714 |     295162 |  130.19 | 41.96 |  2.70 |  3.52 |  3.46 |  2.98 |  2.96 |
|library.pdf        |     20 | frnz   |    226714 |     296549 |  130.80 | 34.60 |  4.22 |  2.83 |  2.90 |  2.67 |  2.61 |
|library.pdf        |     20 | frnt   |    226714 |     304090 |  134.13 | 77.72 |  4.12 |  5.16 |  5.08 |  4.89 |  4.94 |
|library.pdf        |     20 | nacl   |    226714 |     303226 |  133.75 | 59.31 |  2.82 |  3.89 |  3.94 |  3.77 |  3.64 |
|library.pdf        |     20 | nacz   |    226714 |     295705 |  130.43 | 30.00 |  2.82 |  2.54 |  2.50 |  2.38 |  2.13 |


# Benchmarks ZstdFernetFile

Tests with different compression level and workers

| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|
| ZstdFernetFile       | genindex-all.html    |   9 |    2 |        1755 |        258 |      14.68% |   0.04 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |   9 |    8 |        1755 |        258 |      14.68% |   0.04 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |   9 |   12 |        1755 |        258 |      14.68% |   0.03 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |    2 |        1755 |        217 |      12.34% |   0.80 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |    8 |        1755 |        217 |      12.34% |   0.79 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |   12 |        1755 |        217 |      12.34% |   0.80 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |    2 |        3859 |        964 |      24.99% |   0.09 |   0.02 |
| ZstdFernetFile       | searchindex.js       |   9 |    8 |        3859 |        964 |      24.99% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |   12 |        3859 |        964 |      24.99% |   0.09 |   0.02 |
| ZstdFernetFile       | searchindex.js       |  19 |    2 |        3859 |        836 |      21.67% |   1.58 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    8 |        3859 |        836 |      21.67% |   1.55 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |   12 |        3859 |        836 |      21.67% |   1.58 |   0.01 |
| ZstdFernetFile       | library.pdf          |   9 |    2 |       11336 |      14659 |     129.32% |   0.36 |   0.08 |
| ZstdFernetFile       | library.pdf          |   9 |    8 |       11336 |      14659 |     129.32% |   0.25 |   0.07 |
| ZstdFernetFile       | library.pdf          |   9 |   12 |       11336 |      14659 |     129.32% |   0.26 |   0.07 |
| ZstdFernetFile       | library.pdf          |  19 |    2 |       11336 |      14617 |     128.95% |   2.64 |   0.08 |
| ZstdFernetFile       | library.pdf          |  19 |    8 |       11336 |      14617 |     128.95% |   2.62 |   0.08 |
| ZstdFernetFile       | library.pdf          |  19 |   12 |       11336 |      14617 |     128.95% |   2.63 |   0.08 |


# General benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.34% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2354 |     134.13% |   0.16 |   0.02 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5176 |     134.13% |   0.79 |   0.03 |
| FernetFile           | library.pdf          |          16 |       11336 |      15205 |     134.13% |   7.11 |   0.09 |
| NaclFile             | download.html        |          16 |          11 |         11 |     100.64% |   0.00 |   0.00 |
| NaclFile             | genindex-all.html    |          16 |        1755 |       1763 |     100.44% |   0.08 |   0.01 |
| NaclFile             | searchindex.js       |          16 |        3859 |       3876 |     100.44% |   0.67 |   0.01 |
| NaclFile             | library.pdf          |          16 |       11336 |      11386 |     100.44% |   5.32 |   0.03 |
| AesFile              | download.html        |          16 |          11 |         11 |     100.29% |   0.17 |   0.00 |
| AesFile              | genindex-all.html    |          16 |        1755 |       1758 |     100.20% |   0.11 |   0.06 |
| AesFile              | searchindex.js       |          16 |        3859 |       3867 |     100.20% |   0.63 |   0.12 |
| AesFile              | library.pdf          |          16 |       11336 |      11358 |     100.20% |   5.47 |   0.34 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.37% |   0.02 |   0.01 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        210 |      11.95% |   0.16 |   0.04 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        826 |      21.40% |   0.27 |   0.10 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14909 |     131.52% |   6.93 |   1.90 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      36.15% |   0.02 |   0.01 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        220 |      12.51% |   0.37 |   0.02 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        798 |      20.69% |   1.42 |   0.05 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14777 |     130.36% |  10.75 |   1.93 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.80% |   0.01 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1755 |        325 |      18.51% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |          16 |        3859 |       1185 |      30.70% |   0.04 |   0.02 |
| ZstdFernetFile       | library.pdf          |          16 |       11336 |      14833 |     130.85% |   0.19 |   0.09 |
| ZstdNaclFile         | download.html        |          16 |          11 |          3 |      28.92% |   0.00 |   0.00 |
| ZstdNaclFile         | genindex-all.html    |          16 |        1755 |        243 |      13.86% |   0.01 |   0.01 |
| ZstdNaclFile         | searchindex.js       |          16 |        3859 |        887 |      22.99% |   0.03 |   0.01 |
| ZstdNaclFile         | library.pdf          |          16 |       11336 |      11106 |      97.97% |   0.11 |   0.03 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.34% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.38% |   0.02 |   0.01 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.39% |   0.08 |   0.03 |
| FernetFile           | library.pdf          |         256 |       11336 |      15120 |     133.38% |   0.51 |   0.07 |
| NaclFile             | download.html        |         256 |          11 |         11 |     100.64% |   0.00 |   0.00 |
| NaclFile             | genindex-all.html    |         256 |        1755 |       1756 |     100.03% |   0.01 |   0.01 |
| NaclFile             | searchindex.js       |         256 |        3859 |       3860 |     100.03% |   0.06 |   0.01 |
| NaclFile             | library.pdf          |         256 |       11336 |      11339 |     100.03% |   0.40 |   0.03 |
| AesFile              | download.html        |         256 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| AesFile              | genindex-all.html    |         256 |        1755 |       1755 |     100.01% |   0.06 |   0.05 |
| AesFile              | searchindex.js       |         256 |        3859 |       3860 |     100.01% |   0.16 |   0.11 |
| AesFile              | library.pdf          |         256 |       11336 |      11337 |     100.01% |   0.67 |   0.34 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.37% |   0.01 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.15 |   0.04 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.26 |   0.10 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14826 |     130.79% |   1.51 |   1.69 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      36.15% |   0.02 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.36 |   0.02 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.42 |   0.05 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14695 |     129.64% |   4.90 |   1.70 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.80% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |         256 |        3859 |       1178 |      30.52% |   0.03 |   0.02 |
| ZstdFernetFile       | library.pdf          |         256 |       11336 |      14741 |     130.04% |   0.14 |   0.08 |
| ZstdNaclFile         | download.html        |         256 |          11 |          3 |      28.92% |   0.01 |   0.00 |
| ZstdNaclFile         | genindex-all.html    |         256 |        1755 |        242 |      13.80% |   0.01 |   0.01 |
| ZstdNaclFile         | searchindex.js       |         256 |        3859 |        883 |      22.88% |   0.03 |   0.02 |
| ZstdNaclFile         | library.pdf          |         256 |       11336 |      11055 |      97.52% |   0.10 |   0.03 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.34% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.35% |   0.02 |   0.02 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.35% |   0.04 |   0.03 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15116 |     133.35% |   0.24 |   0.10 |
| NaclFile             | download.html        |        1024 |          11 |         11 |     100.64% |   0.01 |   0.00 |
| NaclFile             | genindex-all.html    |        1024 |        1755 |       1755 |     100.01% |   0.01 |   0.01 |
| NaclFile             | searchindex.js       |        1024 |        3859 |       3859 |     100.01% |   0.02 |   0.02 |
| NaclFile             | library.pdf          |        1024 |       11336 |      11337 |     100.01% |   0.14 |   0.04 |
| AesFile              | download.html        |        1024 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| AesFile              | genindex-all.html    |        1024 |        1755 |       1755 |     100.00% |   0.06 |   0.06 |
| AesFile              | searchindex.js       |        1024 |        3859 |       3859 |     100.00% |   0.13 |   0.13 |
| AesFile              | library.pdf          |        1024 |       11336 |      11336 |     100.00% |   0.47 |   0.34 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.37% |   0.01 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.16 |   0.04 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.27 |   0.10 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14822 |     130.75% |   1.29 |   1.83 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      36.15% |   0.02 |   0.01 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.39 |   0.02 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   1.38 |   0.05 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   4.39 |   1.79 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.80% |   0.01 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3859 |       1177 |      30.51% |   0.04 |   0.02 |
| ZstdFernetFile       | library.pdf          |        1024 |       11336 |      14737 |     130.00% |   0.18 |   0.11 |
| ZstdNaclFile         | download.html        |        1024 |          11 |          3 |      28.92% |   0.01 |   0.00 |
| ZstdNaclFile         | genindex-all.html    |        1024 |        1755 |        242 |      13.80% |   0.01 |   0.01 |
| ZstdNaclFile         | searchindex.js       |        1024 |        3859 |        883 |      22.88% |   0.03 |   0.01 |
| ZstdNaclFile         | library.pdf          |        1024 |       11336 |      11052 |      97.50% |   0.14 |   0.07 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15963 |      94.12% |   1.81 |   2.75 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15873 |      93.59% |   1.64 |   2.42 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15868 |      93.56% |   1.65 |   2.12 |
| TarZstdNaclFile      | html,js and pdf      |          16 |       16961 |      12232 |      72.12% |   0.15 |   0.08 |
| TarZstdNaclFile      | html,js and pdf      |         256 |       16961 |      12180 |      71.81% |   0.13 |   0.08 |
| TarZstdNaclFile      | html,js and pdf      |        1024 |       16961 |      12178 |      71.80% |   0.14 |   0.12 |
| TarZstdFernetFile    | html,js and pdf      |          16 |       16961 |      16260 |      95.87% |   0.20 |   0.13 |
| TarZstdFernetFile    | html,js and pdf      |         256 |       16961 |      16260 |      95.87% |   0.19 |   0.13 |
| TarZstdFernetFile    | html,js and pdf      |        1024 |       16961 |      16260 |      95.87% |   0.20 |   0.12 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15786 |      93.07% |   6.38 |   2.11 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15693 |      92.52% |   6.18 |   1.93 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.50% |   6.23 |   1.99 |
| TarFile              | html,js and pdf      |           0 |       16961 |      16970 |     100.05% |   0.02 |   0.04 |
