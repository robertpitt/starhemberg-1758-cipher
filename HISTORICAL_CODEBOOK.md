# Does the 1752 codebook apply to this letter?

**Finding: direct application of the photographed DECODE 1695/1698 codebook is rejected for the unchanged transcription of this 1758 letter.** The opening has a plaintext mismatch, and an independent, deliberately permissive syntax test fails within the first three cipher rows. This does not establish a complete decipherment or exclude a historical relationship between the systems.

## Sources and transcription

The input is Robert Pitt's supplied transcription in `ciphertext.txt`, confirmed as the intended input on 25 September 2026. It is not a fresh OCR replacement. Its SHA-256 remains `66e550b75db3d7e7dc1b41cb724c5628885ce4cb66535f49acb49c09e96bcedc`. No ciphertext digits, working-key entries, or existing decoder rules were changed.

The supplied photographs correspond to [DECODE 1695](https://de-crypt.org/decrypt-web/RecordsView/1695?showdetail=), [1698](https://de-crypt.org/decrypt-web/RecordsView/1698?showdetail=), and instructions [1696](https://de-crypt.org/decrypt-web/RecordsView/1696?showdetail=) and [1697](https://de-crypt.org/decrypt-web/RecordsView/1697?showdetail=). [Source filenames and hashes](historical_codebook_sources.json) identify the files; images are not distributed here.

Small previews were followed by original-resolution crops of diagnostic entries, column starts/ends and instruction passages. R1698 provides the clearest numeric sheets; R1695 shows the same code structure. This is a targeted comparison, not a transcription or proof of equality of every entry in the two copies.

The first cipher line, its interlinear opening, and the third-row `3323` run were checked against a crop from the original first letter PDF. The visual readings remain reviewable evidence, not infallible OCR. The supplied transcription is retained throughout.

## Rules supported by the manuscript

These are operational paraphrases, not a diplomatic edition or reliance on the modern DOCX translation.

| Rule | Source | Consequence |
| --- | --- | --- |
| Two classes/tables, with multiple number lengths in both. | R1696 I7480 P1 and R1697 I7482 P1, item 1 | Prima/Secunda are not simply different digit lengths. |
| `8` is an *errans*; standalone `3` indicates four following digits. | Same pages, items 2–3 | A long code consumes five digits including the initial `3`. |
| Nulls can be mixed among ordinary two-digit numbers, but cannot interrupt the four significant digits after `3`. | Same pages, item 4 | Do not globally delete `8`; it can be significant inside a long code. |
| A `3` belonging to the preceding pair is not an indicator. | Item 5, continuing onto R1697 I7483 P2 | For example, `23` can precede a separate `31126`. |
| Three-digit quantities/dates require distinguishing marks associated with the first digit. | R1697 I7483 P2, item 6 | The negative test admits all `8xx` codes without requiring their marks. |
| Written divisions can occur at different intervals. | Same page, item 7 | Commas and physical rows are not assumed to delimit codes. |
| Some entries have alternative meanings, particularly names and word forms. | Same page, item 8 | Lookup need not give one unique modern word. |
| Letters start with Prima; indicated switches can occur frequently, even within a word. | R1696 I7481 P2, item 10; R1697 I7483 P2, item 9 | Table choice should follow controls, not desired plaintext. |

The numeric sheets confirm `876 → Clavis Secunda` in Prima and `899 → Clavis Prima` in Secunda. These are **not the only switch-labelled entries**. The exclusion test allows every `8xx` entry and unrestricted table choice, so it does not require a complete transcription of the switch list.

The five-digit columns run from `31000` through `31500`, with a separate `30000` entry. Both tables show this structure. The negative test deliberately enlarges the permitted set to **all `31xxx` plus `30000`**, including numbers beyond those photographed.

## Two independent failures

### Forced opening code

The letter begins `204867…`. Its first historical code must be `20`: no null or long-code indicator precedes it.

| Interpretation | Value | Source |
| --- | --- | --- |
| Prima, the prescribed starting table | `Seine Excell[enz]`, a title | R1698 I7484 P1, first numeric column; cross-checked in R1695 I7477 P8 |
| Secunda, tested as an alternative | `aus` | R1698 I7486 P3, first numeric column |
| Letter's interlinear opening | `woferne` | First cipher line of the letter |

The title abbreviation is expanded here. Neither table supplies the interlinear opening. This check is independent of our reconstructed working key. An erroneous interlinear reading alone would not settle the matter; the syntax test provides a second line of evidence.

### Exhaustive, permissive syntax test

[check_historical_codebook.py](check_historical_codebook.py) projects the certain P1/P2 transcription to **1,341 digits**, retaining source locations. It ignores commas, dots, spaces and physical row boundaries. No digit is discarded or repaired; uncertain pages 3–4 are not used.

The test admits more possibilities than the historical inventory:

- Any ordinary pair beginning with a digit other than `3` or `8`, including unlisted pairs.
- Any `31xxx` long code, plus `30000`.
- Any `8xx` special code and `900`, without testing meaning or typography.
- Standalone `8` as a null.
- In a second variant, arbitrary null `8`s between the digits of an ordinary pair.
- Unrestricted table choice; both historical tables share these code shapes.

All paths are explored by reachability over digit positions. Neither variant has a complete path. The furthest reachable boundary is after **117 digits**, immediately before **P1-R03, source character 17**. There the next required long code is `32362`, absent even from the enlarged code set.

The more permissive variant has four terminal failures:

| Next-unit source position | Required long code |
| --- | --- |
| P1-R01:31 | `37248` |
| P1-R01:57 | `34998` |
| P1-R03:16 | `33236` |
| P1-R03:17 | `32362` |

The final two starts lie inside the transcribed `3323` run, checked in the manuscript crop. Changing tables, disregarding separators, or adding more `31xxx` meanings cannot resolve these failures. A digit repair or recoding would be a new hypothesis needing evidence.

## Positive control and reproduction

The first cipher row of the historical worked example, R1697 I7483 P2, was manually read as:

```text
8 / 31126 / 8 / 31397 / 31338 / 8 / 31281 / 8 / 832 / 8 / 31405
```

The test accepts this exact path, including its significant three-digit entry among nulls. Prima `31126 = in` and `31281 = von` were separately checked against the numeric table and the interlinear example. This is a **tokenization positive control**, not a claim to have transcribed and verified every word of the complete example.

```sh
python3 check_historical_codebook.py
python3 -m unittest -v
python3 audit.py
```

The [machine-readable result](output/historical_codebook_check.json) records both variants, every terminal failure and a witness path to the furthest boundary. Regenerate it with `python3 check_historical_codebook.py --build` after a reviewed change. The original nine-report audit remains separate.

## Interpretation and limits

The photographed codebook **does not directly explain this letter under its documented system**. Its `876`/`899` entries must not be imported as controls into this letter merely because those digit strings occur here.

An undocumented recoding, a related key with different assignments, transcription corrections or another manuscript convention remain possible; none is established. This comparison also does not authenticate all 277 existing working-key entries.

A transcription of every historical plaintext entry is unnecessary for this negative result: it cannot supply the absent `32xxx`, `33xxx`, `34xxx` and `37xxx` long-code families. That larger transcription and a complete edition of the worked example have not been claimed as completed.

The supplied workbook is a separate annotated occurrence list with repairs and different source coordinates. It cannot be merged into this letter without establishing its source and reviewing its evidence. It does not repair the demonstrated failures.

The next productive step is to seek a key or instructions tied specifically to this 1758 letter, while continuing source-based tests of our current segmentation and transition hypotheses. Independent evidence of a recoding would justify reopening this comparison.
