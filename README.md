# Starhemberg–Kaunitz cipher, 1758

A partial working key and readable edition of a numerical cipher associated with the Starhemberg–Kaunitz correspondence: the ciphertext, two-table key, German reading, English translation, and reproducible lookup results.

The passage is readable from the supplied edition, but **a complete executable description of the cipher remains unresolved**. The key contains 277 entries; the rules for subdividing all long groups, switching tables, and interpreting the four G signs are not yet established.

## Input, key, and output

| File | Purpose |
| --- | --- |
| [ciphertext.txt](ciphertext.txt) | 52 transcribed rows across four manuscript pages, retaining separators, leading zeros, uncertain digits, and G signs. |
| [working_key.csv](working_key.csv) | 277 supplied table-specific mappings, with occurrence annotations and confidence labels. |
| [READING.md](READING.md) | German edition, English translation, and notes on differences from the interlinear German. |
| [audit.py](audit.py) | Applies the supplied key and verifies selected source locations using the Python standard library. |
| [EVIDENCE.md](EVIDENCE.md) | Current supporting examples, unresolved readings, and limits. |
| [output/human_pages_literal_overlay.md](output/human_pages_literal_overlay.md) | Literal main-table lookup on pages 1–2, retaining unknowns and alternatives. |
| [output/all_rows_dual_table_concordance.tsv](output/all_rows_dual_table_concordance.tsv) | Every written run on all 52 rows with both table lookups. |
| [output/selected_checks.json](output/selected_checks.json) | Eight checks with exact code sequences, values, and source positions. |
| [output/supplied_key_inventory.md](output/supplied_key_inventory.md) | Readable inventory of both tables. |
| [output/key_inventory.json](output/key_inventory.json) | Counts, unresolved entries, and qualifications. |

## The readable passage

The letter discusses the conduct of the court at Constantinople, Belle-Isle's military preparations, the anticipated arrival of Soubise's corps in Bohemia, allegations involving Brühl and the Russian former Grand Chancellor, and promised subsidy payments. The opening name and several readings remain uncertain.

The [German text and English translation](READING.md) are an editorial edition. They are not produced by concatenating the key entries. The continuous text and accompanying correction notes remain separate where they differ, including *Vorstellungen/Vorstellung*, *Zahlung/Bezahlung*, and the name *Abbé de Bernis*.

## How the key works

The working key includes letters, syllables, longer expressions, and punctuation in two tables named `main` and `second`. Index entries by **both table and exact code string**: `066` means `sein` in the main table but `vor` in the second, while `777` gives `lich` and `ni` respectively. Leading zeros are significant to the representation.

For example, adjacent written groups on P1-R04 expand under the main table as:

```text
448 | 049 | 1127 | 832 | 405
vor | st  | el   | ung | machen
```

The literal output is `vorstelungmachen`. Conventional spelling and word spacing yield *Vorstellung machen*. The repeated `049 / 1127 / 832` also occurs on P1-R06.

A second example, on P2-R19:

```text
219 | 9931 | 645 | 1146 | 473 | 226
ab  | be   | de  | ber  | ni  | s
```

This gives `abbedebernis`, or *Abbé de Bernis* after spacing, accents, and capitalization. See [EVIDENCE.md](EVIDENCE.md) for the checks and qualifications.

## What remains unresolved

The table contains 229 main entries and 48 second-table entries. Supplied labels classify 97 as high confidence, 96 as medium, and 84 as low; these labels and occurrence annotations have not been independently authenticated by the script.

`main:409` and `main:9919` have explicit `?` values. Other entries retain alternatives. Long written runs may contain several cipher units, and physical row breaks may split them. Neither every subdivision nor the exact table transitions are known. The four G signs remain uninterpreted.

Pages 1–2 are human-transcribed; pages 3–4 remain draft or partly reviewed. Of the 393 written-run occurrences on pages 1–2, 316 have an exact main-table entry, including three occurrences with `?`. This is a lookup count, **not a decipherment percentage**.

## Reproduce

Requires Python 3.9 or later. From the repository directory:

```sh
python3 audit.py
```

This verifies the frozen input hashes, checks the CSV and eight source/code examples, regenerates five reports in memory, and compares them with the checked-in output. Success prints `"status": "PASS"`. No dependencies or network access are required. From another directory, supply the full path to `audit.py`.

To regenerate the files in `output/`:

```sh
python3 audit.py --build
python3 audit.py
```

Both modes verify the input hashes. A deliberate revision of an input requires review and an explicit update of its hash in the script. The audit checks reproducibility and consistency; it does not independently authenticate the manuscript or discover the key.

## Source, attribution, and contributions

Prepared by Robert Pitt from the supplied transcription, working key, and readable edition of the Starhemberg–Kaunitz archival cipher associated with 1758. The working key and edition are inputs to this audit. The exact letter date and a complete archival citation remain to be established; the source description identifies folios 87–88 and a `1758 III-IV` filename range. No manuscript images are distributed here.

Contributions are welcome through issues or pull requests. Cite exact rows such as `P2-R13`, give the table and code strings, distinguish literal expansions from editorial readings, and retain uncertainties. Useful next work includes checking ambiguous digits, identifying switching rules, interpreting G signs, and producing an occurrence-by-occurrence replay of the full passage.

Code is released under the [MIT License](LICENSE-CODE). Robert Pitt's original research, documentation, and data contributions are licensed under [CC BY 4.0](LICENSE-RESEARCH.md). These licenses do not claim rights over third-party material. Please cite Robert Pitt, this repository, and the exact commit used, and indicate any changes.
