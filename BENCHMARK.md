# Benchmarks FernetStore

Tests done with autoflush, with or without open_secure.

WT -1, ... are the last store.add time in store

WTime is the total write time. RTime the time spent to read

| Data              | NbDocs | Op sec | Orig size | Crypt size | C Ratio | WTime | Rtime | WT -1 | WT -2 | WT -3 | WT -4 |
|:------------------|-------:|-------:|----------:|-----------:|--------:|------:|------:|------:|------:|------:|------:|
|genindex-all.html  |      5 | None   |      8775 |        325 |    3.70 |  0.10 |  0.03 |  0.02 |  0.02 |  0.01 |  0.02 |
|genindex-all.html  |      5 | zstd   |      8775 |       1624 |   18.51 |  0.13 |  0.06 |  0.03 |  0.02 |  0.02 |  0.02 |
|genindex-all.html  |      5 | frnt   |      8775 |      11772 |  134.15 |  0.65 |  0.14 |  0.16 |  0.13 |  0.11 |  0.09 |
|genindex-all.html  |      5 | nacl   |      8775 |      11745 |  133.85 |  0.48 |  0.10 |  0.11 |  0.09 |  0.08 |  0.06 |
|genindex-all.html  |     20 | None   |     35100 |        328 |    0.94 |  0.46 |  0.14 |  0.03 |  0.03 |  0.03 |  0.03 |
|genindex-all.html  |     20 | zstd   |     35100 |       6498 |   18.51 |  0.92 |  0.22 |  0.07 |  0.07 |  0.07 |  0.06 |
|genindex-all.html  |     20 | frnt   |     35100 |      47089 |  134.16 |  5.18 |  0.54 |  0.44 |  0.40 |  0.37 |  0.37 |
|genindex-all.html  |     20 | nacl   |     35100 |      46980 |  133.85 |  4.18 |  0.38 |  0.35 |  0.32 |  0.31 |  0.29 |
|searchindex.js     |      5 | None   |     19295 |       5906 |   30.61 |  0.59 |  0.15 |  0.14 |  0.12 |  0.09 |  0.06 |
|searchindex.js     |      5 | zstd   |     19295 |       5923 |   30.70 |  0.37 |  0.13 |  0.08 |  0.07 |  0.06 |  0.05 |
|searchindex.js     |      5 | frnt   |     19295 |      25884 |  134.14 |  1.96 |  0.28 |  0.39 |  0.34 |  0.29 |  0.27 |
|searchindex.js     |      5 | nacl   |     19295 |      25815 |  133.79 |  1.41 |  0.20 |  0.30 |  0.28 |  0.25 |  0.21 |
|searchindex.js     |     20 | None   |     77181 |      23627 |   30.61 |  6.67 |  0.46 |  0.57 |  0.55 |  0.57 |  0.47 |
|searchindex.js     |     20 | zstd   |     77181 |      23693 |   30.70 |  2.83 |  0.49 |  0.22 |  0.21 |  0.20 |  0.19 |
|searchindex.js     |     20 | frnt   |     77181 |     103529 |  134.14 | 13.40 |  1.09 |  1.04 |  1.00 |  0.93 |  0.90 |
|searchindex.js     |     20 | nacl   |     77181 |     103257 |  133.78 | 11.04 |  0.76 |  0.86 |  0.83 |  0.79 |  0.73 |
|library.pdf        |      5 | None   |     56679 |      73784 |  130.18 |  3.17 |  0.49 |  0.79 |  0.61 |  0.46 |  0.32 |
|library.pdf        |      5 | zstd   |     56679 |      74138 |  130.80 |  3.12 |  0.84 |  0.74 |  0.60 |  0.49 |  0.39 |
|library.pdf        |      5 | frnt   |     56679 |      76023 |  134.13 | 11.46 |  0.85 |  2.05 |  1.90 |  1.78 |  1.66 |
|library.pdf        |      5 | nacl   |     56679 |      75806 |  133.75 |  7.36 |  0.59 |  1.57 |  1.46 |  1.36 |  1.25 |
|library.pdf        |     20 | None   |    226714 |     295162 |  130.19 | 36.00 |  1.92 |  3.10 |  2.93 |  2.88 |  2.66 |
|library.pdf        |     20 | zstd   |    226714 |     296551 |  130.80 | 31.47 |  3.33 |  2.59 |  2.47 |  2.36 |  2.20 |
|library.pdf        |     20 | frnt   |    226714 |     304091 |  134.13 | 57.33 |  3.31 |  3.96 |  3.91 |  3.66 |  3.56 |
|library.pdf        |     20 | nacl   |    226714 |     303226 |  133.75 | 45.93 |  2.45 |  3.18 |  3.02 |  2.92 |  2.75 |


# Benchmarks ZstdFernetFile

Tests with different compression level and workers

| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|
| ZstdFernetFile       | genindex-all.html    |   9 |    2 |        1755 |        258 |      14.68% |   0.04 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |   9 |    8 |        1755 |        258 |      14.68% |   0.04 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |   9 |   12 |        1755 |        258 |      14.68% |   0.03 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |    2 |        1755 |        217 |      12.34% |   0.78 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |    8 |        1755 |        217 |      12.34% |   0.79 |   0.01 |
| ZstdFernetFile       | genindex-all.html    |  19 |   12 |        1755 |        217 |      12.34% |   0.78 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |    2 |        3859 |        964 |      24.99% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |    8 |        3859 |        964 |      24.99% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |   12 |        3859 |        964 |      24.99% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    2 |        3859 |        836 |      21.67% |   1.54 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    8 |        3859 |        836 |      21.67% |   1.51 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |   12 |        3859 |        836 |      21.67% |   1.52 |   0.01 |
| ZstdFernetFile       | library.pdf          |   9 |    2 |       11336 |      14659 |     129.32% |   0.20 |   0.06 |
| ZstdFernetFile       | library.pdf          |   9 |    8 |       11336 |      14659 |     129.32% |   0.22 |   0.06 |
| ZstdFernetFile       | library.pdf          |   9 |   12 |       11336 |      14659 |     129.32% |   0.21 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |    2 |       11336 |      14617 |     128.95% |   2.57 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |    8 |       11336 |      14617 |     128.95% |   2.56 |   0.07 |
| ZstdFernetFile       | library.pdf          |  19 |   12 |       11336 |      14617 |     128.95% |   2.56 |   0.07 |


# General benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.34% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2354 |     134.13% |   0.13 |   0.02 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5176 |     134.13% |   0.70 |   0.03 |
| FernetFile           | library.pdf          |          16 |       11336 |      15205 |     134.13% |   5.29 |   0.07 |
| NaclFile             | download.html        |          16 |          11 |         11 |     100.64% |   0.00 |   0.00 |
| NaclFile             | genindex-all.html    |          16 |        1755 |       1763 |     100.44% |   0.06 |   0.01 |
| NaclFile             | searchindex.js       |          16 |        3859 |       3876 |     100.44% |   0.53 |   0.01 |
| NaclFile             | library.pdf          |          16 |       11336 |      11386 |     100.44% |   3.87 |   0.03 |
| AesFile              | download.html        |          16 |          11 |         11 |     100.29% |   0.10 |   0.00 |
| AesFile              | genindex-all.html    |          16 |        1755 |       1758 |     100.20% |   0.10 |   0.05 |
| AesFile              | searchindex.js       |          16 |        3859 |       3867 |     100.20% |   0.57 |   0.11 |
| AesFile              | library.pdf          |          16 |       11336 |      11358 |     100.20% |   4.25 |   0.40 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.37% |   0.01 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        210 |      11.95% |   0.18 |   0.04 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        826 |      21.40% |   0.27 |   0.10 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14909 |     131.52% |   5.72 |   1.70 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      36.15% |   0.02 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        220 |      12.51% |   0.39 |   0.02 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        798 |      20.69% |   1.53 |   0.05 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14777 |     130.36% |   9.39 |   1.58 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.80% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1755 |        325 |      18.51% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |          16 |        3859 |       1185 |      30.70% |   0.04 |   0.02 |
| ZstdFernetFile       | library.pdf          |          16 |       11336 |      14833 |     130.85% |   0.18 |   0.08 |
| ZstdNaclFile         | download.html        |          16 |          11 |          3 |      28.92% |   0.00 |   0.00 |
| ZstdNaclFile         | genindex-all.html    |          16 |        1755 |        243 |      13.86% |   0.01 |   0.01 |
| ZstdNaclFile         | searchindex.js       |          16 |        3859 |        887 |      22.99% |   0.03 |   0.01 |
| ZstdNaclFile         | library.pdf          |          16 |       11336 |      11106 |      97.97% |   0.11 |   0.03 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.34% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.38% |   0.02 |   0.01 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.39% |   0.07 |   0.03 |
| FernetFile           | library.pdf          |         256 |       11336 |      15120 |     133.38% |   0.51 |   0.08 |
| NaclFile             | download.html        |         256 |          11 |         11 |     100.64% |   0.01 |   0.01 |
| NaclFile             | genindex-all.html    |         256 |        1755 |       1756 |     100.03% |   0.02 |   0.01 |
| NaclFile             | searchindex.js       |         256 |        3859 |       3860 |     100.03% |   0.07 |   0.01 |
| NaclFile             | library.pdf          |         256 |       11336 |      11339 |     100.03% |   0.41 |   0.04 |
| AesFile              | download.html        |         256 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| AesFile              | genindex-all.html    |         256 |        1755 |       1755 |     100.01% |   0.08 |   0.08 |
| AesFile              | searchindex.js       |         256 |        3859 |       3860 |     100.01% |   0.22 |   0.16 |
| AesFile              | library.pdf          |         256 |       11336 |      11337 |     100.01% |   0.93 |   0.49 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.37% |   0.01 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.26 |   0.10 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.45 |   0.35 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14826 |     130.79% |   3.54 |   3.04 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      36.15% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.48 |   0.02 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.94 |   0.05 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14695 |     129.64% |   5.81 |   2.03 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.80% |   0.01 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.02 |   0.01 |
| ZstdFernetFile       | searchindex.js       |         256 |        3859 |       1178 |      30.52% |   0.05 |   0.02 |
| ZstdFernetFile       | library.pdf          |         256 |       11336 |      14741 |     130.04% |   0.21 |   0.09 |
| ZstdNaclFile         | download.html        |         256 |          11 |          3 |      28.92% |   0.00 |   0.00 |
| ZstdNaclFile         | genindex-all.html    |         256 |        1755 |        242 |      13.80% |   0.02 |   0.01 |
| ZstdNaclFile         | searchindex.js       |         256 |        3859 |        883 |      22.88% |   0.04 |   0.01 |
| ZstdNaclFile         | library.pdf          |         256 |       11336 |      11055 |      97.52% |   0.21 |   0.04 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.34% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.35% |   0.02 |   0.01 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.35% |   0.05 |   0.03 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15116 |     133.35% |   0.30 |   0.16 |
| NaclFile             | download.html        |        1024 |          11 |         11 |     100.64% |   0.01 |   0.01 |
| NaclFile             | genindex-all.html    |        1024 |        1755 |       1755 |     100.01% |   0.02 |   0.02 |
| NaclFile             | searchindex.js       |        1024 |        3859 |       3859 |     100.01% |   0.05 |   0.03 |
| NaclFile             | library.pdf          |        1024 |       11336 |      11337 |     100.01% |   0.33 |   0.07 |
| AesFile              | download.html        |        1024 |          11 |         11 |     100.29% |   0.00 |   0.00 |
| AesFile              | genindex-all.html    |        1024 |        1755 |       1755 |     100.00% |   0.08 |   0.08 |
| AesFile              | searchindex.js       |        1024 |        3859 |       3859 |     100.00% |   0.19 |   0.17 |
| AesFile              | library.pdf          |        1024 |       11336 |      11336 |     100.00% |   0.60 |   0.46 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.37% |   0.01 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.23 |   0.05 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.35 |   0.14 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14822 |     130.75% |   1.87 |   3.36 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      36.15% |   0.02 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.67 |   0.02 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   2.06 |   0.05 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   5.11 |   2.10 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.80% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3859 |       1177 |      30.51% |   0.04 |   0.02 |
| ZstdFernetFile       | library.pdf          |        1024 |       11336 |      14737 |     130.00% |   0.22 |   0.11 |
| ZstdNaclFile         | download.html        |        1024 |          11 |          3 |      28.92% |   0.00 |   0.00 |
| ZstdNaclFile         | genindex-all.html    |        1024 |        1755 |        242 |      13.80% |   0.01 |   0.01 |
| ZstdNaclFile         | searchindex.js       |        1024 |        3859 |        883 |      22.88% |   0.04 |   0.02 |
| ZstdNaclFile         | library.pdf          |        1024 |       11336 |      11052 |      97.50% |   0.15 |   0.07 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15963 |      94.12% |   2.20 |   3.04 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15874 |      93.59% |   1.95 |   2.86 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15869 |      93.56% |   2.04 |   2.80 |
| TarZstdNaclFile      | html,js and pdf      |          16 |       16961 |      12232 |      72.12% |   0.21 |   0.09 |
| TarZstdNaclFile      | html,js and pdf      |         256 |       16961 |      12180 |      71.81% |   0.15 |   0.08 |
| TarZstdNaclFile      | html,js and pdf      |        1024 |       16961 |      12178 |      71.80% |   0.19 |   0.12 |
| TarFile              | html,js and pdf      |          16 |       16961 |      16260 |      95.87% |   0.25 |   0.13 |
| TarFile              | html,js and pdf      |         256 |       16961 |      16260 |      95.87% |   0.23 |   0.13 |
| TarFile              | html,js and pdf      |        1024 |       16961 |      16260 |      95.87% |   0.25 |   0.13 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15786 |      93.07% |   8.34 |   2.78 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15692 |      92.52% |   7.06 |   2.25 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.50% |   7.33 |   2.55 |
