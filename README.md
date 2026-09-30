# Starhemberg–Kaunitz cipher, 1758

**The codebook is identified as DECODE R1588/R1589. The complete decipherment remains unfinished.** This repository contains the current key, reviewed ciphertext and provisional German/English reading.

| File | Contents |
| --- | --- |
| [READING.md](READING.md) | German working text and English translation, with unresolved readings marked. |
| [ciphertext.txt](ciphertext.txt) | Current reviewed transcription: 52 labelled rows across four pages. |
| [working_key.csv](working_key.csv) | Current key and review information, including Norbert’s manuscript checks. |
| [Review table](output/key_review_table.md) | Code, value, qualitative probability and named human confirmation. |
| [Literal replay](output/historical_reading.md) | Reproducible partial reading, with missing entries and explicit stopping points. |
| [EVIDENCE.md](EVIDENCE.md) | Source identification, confirmed corrections, rules and remaining work. |

The key contains **322 source entries and 62 separately labelled, unconfirmed supplied guesses**. The latter remain in the review table for investigation and are excluded from the replay. Read `code` as text to preserve leading zeros; Prima and Secunda are separate tables. `source_read` means an accepted source transcription, not necessarily human confirmation. Alternatives and abbreviated endings are not fully expanded.

Norbert’s 73 Prima IMG readings and all 48 Secunda manuscript readings are incorporated with their stated uncertainty. Robert confirmed that Secunda’s lack of IMG markers does not mean those entries are unreviewed. `049` remains illegible; `1118` is partial; `005`, `248`, `5512` and `3337` retain explicit uncertainty. His latest readings take priority. The corrections `629` → `621` at P1-R03 and `3337,768` → `3333,7768` at P1-R05 are applied. The replay now frames 90 groups into P2-R01; an independent local probe also supports Graf Stainville using Secunda `2215 = f`. The full reading remains provisional. Probability labels are qualitative evidence categories, not decipherment percentages.

## Check or update

Python 3.9+, standard library only:

```sh
python3 audit.py
python3 -m unittest -v
```

After a reviewed change to `working_key.csv` or `ciphertext.txt`, run `python3 audit.py --build` to refresh the two Markdown tables. Edit the bilingual working text in `READING.md` separately and check its wording against the literal replay. Software checks establish consistency, not handwriting accuracy or a complete decipherment.

Prepared by Robert Pitt, with manuscript reviews and contributions from Norbert, Satoshi and Alexandre. No manuscript images or OCR working files are distributed here. For corrections, give the table, exact code, source location, literal reading and uncertainty.

Code: [MIT](LICENSE-CODE). Robert Pitt’s original research contributions: [CC BY 4.0](LICENSE-RESEARCH.md). Cite this repository and the commit used; third-party rights are unaffected.
