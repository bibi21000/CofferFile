# Benchmarks FernetStore

Tests done with autoflush, with or without open_secure.

WT -1, ... are the last store.add time in store

WTime is the total write time. RTime the time spent to read

| Data              | NbDocs | Op sec | Orig size | Crypt size | C Ratio | WTime | Rtime | WT -1 | WT -2 | WT -3 | WT -4 |
|:------------------|-------:|-------:|----------:|-----------:|--------:|------:|------:|------:|------:|------:|------:|
|genindex-all.html  |      5 | None   |      8775 |        324 |    3.70 |  0.12 |  0.03 |  0.02 |  0.02 |  0.02 |  0.01 |
|genindex-all.html  |      5 | frnz   |      8775 |       1625 |   18.51 |  0.13 |  0.06 |  0.03 |  0.02 |  0.02 |  0.02 |
|genindex-all.html  |      5 | frnt   |      8775 |      11772 |  134.15 |  0.63 |  0.14 |  0.14 |  0.12 |  0.10 |  0.08 |
|genindex-all.html  |      5 | nacz   |      8775 |       1630 |   18.57 |  0.12 |  0.05 |  0.02 |  0.02 |  0.02 |  0.02 |
|genindex-all.html  |      5 | nacl   |      8775 |      11745 |  133.85 |  0.48 |  0.10 |  0.11 |  0.10 |  0.07 |  0.06 |
|genindex-all.html  |     20 | None   |     35100 |        328 |    0.94 |  0.49 |  0.15 |  0.03 |  0.03 |  0.03 |  0.03 |
|genindex-all.html  |     20 | frnz   |     35100 |       6499 |   18.51 |  0.94 |  0.21 |  0.07 |  0.07 |  0.06 |  0.06 |
|genindex-all.html  |     20 | frnt   |     35100 |      47089 |  134.16 |  5.23 |  0.53 |  0.43 |  0.41 |  0.38 |  0.36 |
|genindex-all.html  |     20 | nacz   |     35100 |       6519 |   18.57 |  0.83 |  0.19 |  0.06 |  0.06 |  0.06 |  0.05 |
|genindex-all.html  |     20 | nacl   |     35100 |      46980 |  133.85 |  4.20 |  0.38 |  0.34 |  0.32 |  0.31 |  0.29 |
|searchindex.js     |      5 | None   |     19295 |       5906 |   30.61 |  0.62 |  0.11 |  0.14 |  0.11 |  0.09 |  0.06 |
|searchindex.js     |      5 | frnz   |     19295 |       5922 |   30.69 |  0.37 |  0.13 |  0.08 |  0.07 |  0.06 |  0.05 |
|searchindex.js     |      5 | frnt   |     19295 |      25884 |  134.14 |  2.00 |  0.28 |  0.39 |  0.35 |  0.31 |  0.27 |
|searchindex.js     |      5 | nacz   |     19295 |       5917 |   30.67 |  0.32 |  0.10 |  0.07 |  0.06 |  0.05 |  0.04 |
|searchindex.js     |      5 | nacl   |     19295 |      25815 |  133.79 |  1.44 |  0.20 |  0.32 |  0.28 |  0.25 |  0.21 |
|searchindex.js     |     20 | None   |     77181 |      23628 |   30.61 |  6.80 |  0.51 |  0.57 |  0.54 |  0.53 |  0.49 |
|searchindex.js     |     20 | frnz   |     77181 |      23694 |   30.70 |  2.89 |  0.51 |  0.22 |  0.21 |  0.20 |  0.19 |
|searchindex.js     |     20 | frnt   |     77181 |     103530 |  134.14 | 13.49 |  1.09 |  1.05 |  0.98 |  0.95 |  0.90 |
|searchindex.js     |     20 | nacz   |     77181 |      23670 |   30.67 |  2.54 |  0.45 |  0.20 |  0.19 |  0.18 |  0.17 |
|searchindex.js     |     20 | nacl   |     77181 |     103257 |  133.78 | 11.23 |  0.78 |  0.86 |  0.86 |  0.80 |  0.74 |
|library.pdf        |      5 | None   |     56679 |      73784 |  130.18 |  3.20 |  0.50 |  0.80 |  0.62 |  0.49 |  0.34 |
|library.pdf        |      5 | frnz   |     56679 |      74139 |  130.81 |  3.35 |  0.94 |  0.84 |  0.64 |  0.48 |  0.38 |
|library.pdf        |      5 | frnt   |     56679 |      76022 |  134.13 | 11.59 |  0.92 |  2.05 |  1.93 |  1.80 |  1.68 |
|library.pdf        |      5 | nacz   |     56679 |      73926 |  130.43 |  2.66 |  0.60 |  0.64 |  0.54 |  0.44 |  0.31 |
|library.pdf        |      5 | nacl   |     56679 |      75806 |  133.75 |  7.55 |  0.66 |  1.62 |  1.51 |  1.38 |  1.26 |
|library.pdf        |     20 | None   |    226714 |     295162 |  130.19 | 39.67 |  1.96 |  3.26 |  2.97 |  2.87 |  2.78 |
|library.pdf        |     20 | frnz   |    226714 |     296551 |  130.80 | 33.52 |  3.44 |  2.64 |  2.56 |  2.39 |  2.59 |
|library.pdf        |     20 | frnt   |    226714 |     304089 |  134.13 | 60.25 |  4.15 |  4.63 |  4.14 |  3.79 |  3.69 |
|library.pdf        |     20 | nacl   |    226714 |     303226 |  133.75 | 54.58 |  2.86 |  4.13 |  3.92 |  3.83 |  3.71 |
|library.pdf        |     20 | nacz   |    226714 |     295705 |  130.43 | 32.99 |  3.00 |  3.02 |  2.90 |  2.40 |  2.30 |


# Benchmarks ZstdFernetFile

Tests with different compression level and workers

| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|
| ZstdFernetFile       | genindex-all.html    |   9 |    2 |        1755 |        258 |      14.68% |   0.04 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |   9 |    8 |        1755 |        258 |      14.68% |   0.04 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |   9 |   12 |        1755 |        258 |      14.68% |   0.03 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |    2 |        1755 |        217 |      12.34% |   0.83 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |    8 |        1755 |        217 |      12.34% |   0.81 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |   12 |        1755 |        217 |      12.34% |   0.96 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |    2 |        3859 |        964 |      24.99% |   0.09 |   0.02 |
| ZstdFernetFile       | searchindex.js       |   9 |    8 |        3859 |        964 |      24.99% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |   12 |        3859 |        964 |      24.99% |   0.09 |   0.02 |
| ZstdFernetFile       | searchindex.js       |  19 |    2 |        3859 |        836 |      21.67% |   1.82 |   0.02 |
| ZstdFernetFile       | searchindex.js       |  19 |    8 |        3859 |        836 |      21.67% |   1.91 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |   12 |        3859 |        836 |      21.67% |   1.99 |   0.01 |
| ZstdFernetFile       | library.pdf          |   9 |    2 |       11336 |      14659 |     129.32% |   0.29 |   0.08 |
| ZstdFernetFile       | library.pdf          |   9 |    8 |       11336 |      14659 |     129.32% |   0.27 |   0.09 |
| ZstdFernetFile       | library.pdf          |   9 |   12 |       11336 |      14659 |     129.32% |   0.25 |   0.07 |
| ZstdFernetFile       | library.pdf          |  19 |    2 |       11336 |      14617 |     128.95% |   3.18 |   0.07 |
| ZstdFernetFile       | library.pdf          |  19 |    8 |       11336 |      14617 |     128.95% |   3.44 |   0.10 |
| ZstdFernetFile       | library.pdf          |  19 |   12 |       11336 |      14617 |     128.95% |   3.20 |   0.10 |


# General benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.34% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2354 |     134.13% |   0.25 |   0.02 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5176 |     134.13% |   0.97 |   0.03 |
| FernetFile           | library.pdf          |          16 |       11336 |      15205 |     134.13% |   6.61 |   0.07 |
| NaclFile             | download.html        |          16 |          11 |         11 |     100.64% |   0.00 |   0.00 |
| NaclFile             | genindex-all.html    |          16 |        1755 |       1763 |     100.44% |   0.06 |   0.01 |
| NaclFile             | searchindex.js       |          16 |        3859 |       3876 |     100.44% |   0.42 |   0.01 |
| NaclFile             | library.pdf          |          16 |       11336 |      11386 |     100.44% |   4.88 |   0.03 |
| AesFile              | download.html        |          16 |          11 |         11 |     100.29% |   0.12 |   0.00 |
| AesFile              | genindex-all.html    |          16 |        1755 |       1758 |     100.20% |   0.11 |   0.06 |
| AesFile              | searchindex.js       |          16 |        3859 |       3867 |     100.20% |   0.68 |   0.12 |
| AesFile              | library.pdf          |          16 |       11336 |      11358 |     100.20% |   5.40 |   0.34 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.37% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        210 |      11.95% |   0.19 |   0.05 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        826 |      21.40% |   0.31 |   0.12 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14909 |     131.52% |   7.90 |   2.54 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      36.15% |   0.02 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        220 |      12.51% |   0.41 |   0.01 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        798 |      20.69% |   1.63 |   0.06 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14777 |     130.36% |  10.33 |   1.91 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.80% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1755 |        325 |      18.51% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |          16 |        3859 |       1185 |      30.70% |   0.06 |   0.02 |
| ZstdFernetFile       | library.pdf          |          16 |       11336 |      14833 |     130.85% |   0.21 |   0.08 |
| ZstdNaclFile         | download.html        |          16 |          11 |          3 |      28.92% |   0.00 |   0.00 |
| ZstdNaclFile         | genindex-all.html    |          16 |        1755 |        243 |      13.86% |   0.01 |   0.01 |
| ZstdNaclFile         | searchindex.js       |          16 |        3859 |        887 |      22.99% |   0.03 |   0.01 |
| ZstdNaclFile         | library.pdf          |          16 |       11336 |      11106 |      97.97% |   0.17 |   0.05 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.34% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.38% |   0.03 |   0.01 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.39% |   0.08 |   0.02 |
| FernetFile           | library.pdf          |         256 |       11336 |      15120 |     133.38% |   0.51 |   0.07 |
| NaclFile             | download.html        |         256 |          11 |         11 |     100.64% |   0.00 |   0.00 |
| NaclFile             | genindex-all.html    |         256 |        1755 |       1756 |     100.03% |   0.01 |   0.01 |
| NaclFile             | searchindex.js       |         256 |        3859 |       3860 |     100.03% |   0.05 |   0.01 |
| NaclFile             | library.pdf          |         256 |       11336 |      11339 |     100.03% |   0.37 |   0.03 |
| AesFile              | download.html        |         256 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| AesFile              | genindex-all.html    |         256 |        1755 |       1755 |     100.01% |   0.07 |   0.06 |
| AesFile              | searchindex.js       |         256 |        3859 |       3860 |     100.01% |   0.16 |   0.13 |
| AesFile              | library.pdf          |         256 |       11336 |      11337 |     100.01% |   0.72 |   0.35 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.37% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.18 |   0.05 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.30 |   0.12 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14826 |     130.79% |   2.07 |   2.56 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      36.15% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.49 |   0.02 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.87 |   0.06 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14695 |     129.64% |   5.27 |   1.73 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.80% |   0.01 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |         256 |        3859 |       1178 |      30.52% |   0.04 |   0.02 |
| ZstdFernetFile       | library.pdf          |         256 |       11336 |      14741 |     130.04% |   0.17 |   0.07 |
| ZstdNaclFile         | download.html        |         256 |          11 |          3 |      28.92% |   0.00 |   0.00 |
| ZstdNaclFile         | genindex-all.html    |         256 |        1755 |        242 |      13.80% |   0.02 |   0.01 |
| ZstdNaclFile         | searchindex.js       |         256 |        3859 |        883 |      22.88% |   0.03 |   0.01 |
| ZstdNaclFile         | library.pdf          |         256 |       11336 |      11055 |      97.52% |   0.10 |   0.04 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.34% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.35% |   0.02 |   0.01 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.35% |   0.04 |   0.03 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15116 |     133.35% |   0.20 |   0.08 |
| NaclFile             | download.html        |        1024 |          11 |         11 |     100.64% |   0.00 |   0.00 |
| NaclFile             | genindex-all.html    |        1024 |        1755 |       1755 |     100.01% |   0.01 |   0.01 |
| NaclFile             | searchindex.js       |        1024 |        3859 |       3859 |     100.01% |   0.02 |   0.02 |
| NaclFile             | library.pdf          |        1024 |       11336 |      11337 |     100.01% |   0.15 |   0.04 |
| AesFile              | download.html        |        1024 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| AesFile              | genindex-all.html    |        1024 |        1755 |       1755 |     100.00% |   0.06 |   0.06 |
| AesFile              | searchindex.js       |        1024 |        3859 |       3859 |     100.00% |   0.17 |   0.15 |
| AesFile              | library.pdf          |        1024 |       11336 |      11336 |     100.00% |   0.50 |   0.38 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.37% |   0.01 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.19 |   0.05 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.29 |   0.11 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14822 |     130.75% |   1.61 |   1.72 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      36.15% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.42 |   0.02 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   1.63 |   0.05 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   4.83 |   1.67 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.80% |   0.01 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3859 |       1177 |      30.51% |   0.04 |   0.02 |
| ZstdFernetFile       | library.pdf          |        1024 |       11336 |      14737 |     130.00% |   0.23 |   0.10 |
| ZstdNaclFile         | download.html        |        1024 |          11 |          3 |      28.92% |   0.00 |   0.00 |
| ZstdNaclFile         | genindex-all.html    |        1024 |        1755 |        242 |      13.80% |   0.01 |   0.01 |
| ZstdNaclFile         | searchindex.js       |        1024 |        3859 |        883 |      22.88% |   0.03 |   0.01 |
| ZstdNaclFile         | library.pdf          |        1024 |       11336 |      11052 |      97.50% |   0.10 |   0.06 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15963 |      94.12% |   1.94 |   2.60 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15873 |      93.59% |   1.73 |   2.35 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15868 |      93.56% |   1.88 |   2.38 |
| TarZstdNaclFile      | html,js and pdf      |          16 |       16961 |      12232 |      72.12% |   0.18 |   0.08 |
| TarZstdNaclFile      | html,js and pdf      |         256 |       16961 |      12180 |      71.81% |   0.14 |   0.09 |
| TarZstdNaclFile      | html,js and pdf      |        1024 |       16961 |      12178 |      71.80% |   0.18 |   0.12 |
| TarFile              | html,js and pdf      |          16 |       16961 |      16260 |      95.87% |   0.23 |   0.14 |
| TarFile              | html,js and pdf      |         256 |       16961 |      16260 |      95.87% |   0.28 |   0.12 |
| TarFile              | html,js and pdf      |        1024 |       16961 |      16260 |      95.87% |   0.25 |   0.14 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15786 |      93.07% |   7.43 |   2.15 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15693 |      92.52% |   6.96 |   1.95 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.50% |   6.85 |   2.19 |
