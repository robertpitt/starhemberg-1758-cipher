# Starhemberg–Kaunitz cipher, 1758

**The codebook is identified as DECODE R1588/R1589. The complete decipherment remains unfinished.** This repository contains the current key, reviewed ciphertext and provisional German/English reading.

| File | Contents |
| --- | --- |
| [READING.md](READING.md) | German working text and English translation, with unresolved readings marked. |
| [ciphertext.txt](ciphertext.txt) | Current reviewed transcription: 52 labelled rows across four pages. |
| [working_key.csv](working_key.csv) | Current key and review information, including Norbert’s manuscript checks. |
| [Review table](output/key_review_table.md) | Code, value, qualitative probability and named human confirmation. |
| [Literal replay](output/historical_reading.md) | Reproducible partial reading of the manuscript transcript, with explicit stopping points. |
| [Norbert comparison](output/norbert_comparison.md) | All 779 worksheet groups, literal key matches, notes and candidate manuscript differences. |
| [Norbert source extracts](sources/) | Completed worksheet key, grouped ciphertext, cached formulas/readings, provenance and email transcription. |
| [EVIDENCE.md](EVIDENCE.md) | Source identification, confirmed corrections, rules and remaining work. |

The key contains **530 source entries and six separately labelled, unconfirmed supplied guesses**. The latter remain in the review table for investigation and are excluded from the replay. Read `code` as text to preserve leading zeros; Prima and Secunda are separate tables. `source_read` means an accepted source transcription, not necessarily human confirmation. Alternatives and abbreviated endings are not fully expanded.

Norbert’s completed worksheet, retrieved on **4 October 2026**, supplies **445 readings** (267 Prima, 178 Secunda) and **779 grouped cipher entries**. All are imported with cell references; his latest values supersede the earlier partial import. Fifteen key readings remain provisional, including `049`, `248`, `5512` and `3337`. `005` and `1118` now have fuller readings. New values without stated confidence are Moderate; existing human confidence is retained for unchanged readings. Probability labels are qualitative evidence categories, not decipherment percentages.

The decoder replays all 779 worksheet groups continuously, agreeing with both table transitions. The separate manuscript transcript still frames 90 groups before stopping at P2-R01. The comparison lists 154 candidate edit spans between the two streams for review. Norbert’s worksheet now uses `2275`, rather than the manuscript’s `2215`, in the Stainville sequence. The full prose reading remains provisional until these differences and every phrase are verified. The email’s interlinear/ciphertext distinctions are preserved in [the original transcription](sources/norbert_interlinear.txt).

## Check or update

Python 3.9+, standard library only:

```sh
python3 audit.py
python3 -m unittest -v
```

After a reviewed change to `working_key.csv`, `ciphertext.txt` or the source extracts, run `python3 audit.py --build` to refresh all three Markdown outputs. Edit the bilingual working text in `READING.md` separately and check its wording against the literal replay and Norbert’s email. Software checks establish consistency, not handwriting accuracy or a complete decipherment.

To refresh from a new copy of Norbert’s worksheet, save the workbook locally and import it:

```sh
python3 norbert.py /tmp/norbert.xlsx --retrieved 2026-10-04
python3 audit.py --build
python3 -m unittest -v
```

Use the actual retrieval date. The importer records the workbook’s SHA-256, preserves leading-zero codes, literal alternatives, annotations, formula text and cached readings, and checks the worksheet’s table states before writing. It updates worksheet entries in the key, retaining entries absent from the workbook with their existing provenance. It leaves the manuscript transcript available for comparison. The workbook contains images; only text extracts are distributed here.

Prepared by Robert Pitt. No manuscript images or OCR working files are distributed here. For corrections, give the table, exact code, source location, literal reading and uncertainty.

## Acknowledgements

- [Prof. Norbert Biermann](https://www.udk-berlin.de/person/norbert-biermann/), Universität der Künste Berlin, for his support in reading the German manuscripts, reviewing the cipher tables and refining the decipherment.
- **Satoshi Tomokiyo and Alexandra**, from the [Cryptiana team](https://cryptiana.web.fc2.com/code/crypto.htm), for their research support and collaboration on the decipherment.

Code: [MIT](LICENSE-CODE). Robert Pitt’s original research contributions: [CC BY 4.0](LICENSE-RESEARCH.md). Cite this repository and the commit used; third-party rights are unaffected.
