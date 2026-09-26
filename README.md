# Starhemberg–Kaunitz cipher, 1758

**The codebook is identified as DECODE R1588/R1589.** R1588 is the alphabetically arranged key and instructions; R1589 supplies its numerical arrangement. This repository records a source-based key transcription and a reproducible partial replay of the letter. The full decipherment remains incomplete.

The source key currently contains **290 table-specific entries**: 226 lexical entries, 20 nulls, 30 punctuation entries, 12 indicators and two cancellation entries. Some readings are provisional and abbreviated alternatives are not fully expanded. `source_read` means an assistant visual transcription, not independent human authentication.

## Main files

| File | Purpose |
| --- | --- |
| [READING.md](READING.md) | Revised German/English working edition, source-aligned extracts and explicit unresolved readings. |
| [reading_edition.json](reading_edition.json) | Editorial text and translation anchors checked against the replay. |
| [ciphertext.txt](ciphertext.txt) | Unchanged supplied transcription: 52 rows, four pages. |
| [ciphertext_emendations.json](ciphertext_emendations.json) | Explicit human reviews and the authorized P3-R02 correction. |
| [historical_key.json](historical_key.json) | Source-based key, table identities, review status, image hashes and crop coordinates. |
| [Source-key inventory](output/historical_key.md) | Readable version of the key. |
| [R1588_OPERATING_RULES.md](R1588_OPERATING_RULES.md) | Recovered group lengths, initial table and switching instructions. |
| [decode_historical.py](decode_historical.py) | Reproduce the reviewed transcription, key collation and historical-rule probes. |
| [Historical reading](output/historical_reading.md) | Source readings and explicit stops, without editorial words filling gaps. |
| [Replay ledger](output/historical_replay.json) | Exact derived-text coordinates, states, readings and source-file hashes. |
| [Key collation](output/key_collation.json) | Every supplied-key entry compared with the source transcription. |
| [Review queue](output/key_review_queue.md) | Remaining key readings and incompatible supplied code forms. |
| [EVIDENCE.md](EVIDENCE.md) | Findings and their limits. |
| [REMAINING_WORK.md](REMAINING_WORK.md) | Concrete requirements for completion. |

## Current result

The instructions prescribe Prima initially. Prima uses three digits for a leading 0 or even digit and four for an odd digit; Secunda reverses the odd/even rule, with leading 0 still taking three. Indicators change the active table. Physical row breaks alone do not reset it.

The opening frames 69 groups before an unresolved form at P1-R05:43. Robert's review confirms `3337,768`; the replay retains those digits and does not insert a missing prefix. A separate local probe of the corrected P3-R02 reads:

```text
Prima:   1158 (punctum), 412 (switch to Secunda)
Secunda: 929 (Graf), 2215 (switch to Prima)
Prima:   1121, 221 ... [next form unresolved]
```

The local probe assumes Prima at its starting point. It does not bridge the stopped opening scan or establish uninterrupted Secunda use across the later passage.

Of the 277 supplied-key entries, **181 have source transcriptions, seven have provisional readings, 83 need handwriting review, and six have incompatible code lengths**. Having a source transcription does not mean that the old value agrees with it or that every alternative has been expanded. These are not decipherment percentages.

## Reproduce

Python 3.9+, standard library only:

```sh
python3 decode_historical.py
python3 audit.py
python3 -m unittest -v
```

The historical decoder checks frozen input hashes and verifies its nine generated outputs (including the revised bilingual edition). Use `python3 decode_historical.py --build` after a reviewed amendment to regenerate them. Edit `reading_edition.json` to revise editorial wording; source-aligned excerpts require matching code readings, so a changed key flags their translation for review. Software checks establish reproducibility and consistency; they do not authenticate handwriting.

`working_key.csv`, `input/supplied_reading.md`, `decode.py`, `decoding_spans.json` and their associated reports preserve the supplied working key, editorial German/English, and conditional lookup model. They are comparison materials. `audit.py` verifies those supplied-input reports; its success is not a validation of the complete historical reading. The current historical replay is generated separately by `decode_historical.py`.

## Sources and contributions

Prepared by Robert Pitt from the Starhemberg–Kaunitz cipher associated with 1758, the supplied transcription and edition, and DECODE source photographs. The letter's source description identifies folios 87–88 and a `1758 III-IV` filename range; an exact date and full archival citation still need verification. No manuscript images are distributed here.

For corrections, give the table, exact code string, source image and location, literal reading, and uncertainty. Preserve leading zeros and distinguish encoded text from spelling normalization or editorial additions. See the [remaining work](REMAINING_WORK.md).

Code is released under the [MIT License](LICENSE-CODE). Robert Pitt's original research, documentation and data contributions are licensed under [CC BY 4.0](LICENSE-RESEARCH.md). These licenses do not claim rights over third-party material. Cite Robert Pitt, this repository and the exact commit used, and indicate changes.
