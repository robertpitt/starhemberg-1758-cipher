# R1588 instructions and R1589 numerical cross-check

Checked 26 September 2026. **The supplied instruction page establishes a usable group-length rule and an initial table. R1589 independently corroborates selected assignments and the corrected Prima/Secunda sheet pairing. A full decipherment is still incomplete.**

The new folder contains five images: R1588 P1, R1589 P1 (cover), P2 (both tables), P3 (Prima detail), and P4 (Secunda detail). The four R1589 photographs do not represent four different key tables. Original images and temporary crops remain outside the repository. [Source hashes, dimensions, crop coordinates and readings](r1588_source_rules.json) make the checks traceable.

## Instructions recovered

The heading is read as **16 June 1753**. This supports the published survey's date; the previously observed catalogue date of 15 June remains a metadata discrepancy. The following is a normalized interpretation, not a complete diplomatic transcription independently checked by a palaeographer.

| Leading digit | Prima group length | Secunda group length |
| --- | ---: | ---: |
| 0 | 3 | 3 |
| 2, 4, 6, 8 | 3 | 4 |
| 1, 3, 5, 7, 9 | 4 | 3 |

The first clause, read together with the numerical tables, establishes these lengths. Ordinary triplets such as Prima `448` therefore present no exception: equality of the first two digits is not the length rule.

The second clause says to begin dispatches, paragraphs and letters in **Prima**. It permits a switch to Secunda after a *punctum* or completed construction, with an indicator placed before the new table's material; never in the middle of a word or construction. The paragraph wording expands the manuscript's section-symbol abbreviation. An initial indicator is unnecessary because the starting table is prescribed. Physical line and page breaks must not be treated as paragraph resets without checking the letter.

The continuation on R1588 P2 advises avoiding frequent paragraph breaks, using nulls often, not inserting clear text between cipher groups, writing concisely, and omitting the cipher for the final punctum. These are operating instructions for the historical cipher, not instructions to change our supplied transcription. The reviewed indicators naming Prima provide evidence for return signals; their occurrence-by-occurrence use still needs validation.

## Numerical checks

R1589's explicitly headed tables agree with these selected readings from R1588:

| Table | Codes and readings |
| --- | --- |
| Prima | `204` null (blacked-out cell), `219` ab, `226` s, `448` vor, `617` gu, `681` spr, `867` wo, `1158` punctum |
| Secunda | `336` s, `066` vor |

These independently support **R1588 P3 + P6 = Prima**, and **P5 + P4 = Secunda**, resolving the earlier filename-based pairing error. They authenticate these selected correspondences, not every entry in either table.

The numerical copy also supports two refinements: `210` appears to read **würde…**, and `629` an **auf…** expression, tentatively *aufdaß*. A separate `621` entry reads *davon*. Robert’s subsequent partial reading of `210` is **Wum[b|g]**; it supersedes the displayed key value but does not settle its word meaning. `629` remains provisional. `681` supports the shorter root *spr*, rather than requiring the entire word *sprech*.

**Two apparent inconsistencies are now explained:**

- Numerical Prima `9999` reads **ist**, agreeing with the worked example. Prima `1114 = ist` is an alternative assignment already human-reviewed. Different codes for the same word are not a contradiction.
- Reinspection of the worked-example crop shows a comma immediately below `025`; the *indic: Clav. 2dum* annotation sits above the following `477`. Together with the instructions and human-reviewed control list, this supports **025 = comma, followed by 477 = switch to Secunda**. The earlier attribution of the switch annotation to 025 should not drive a decoding rule. Robert's literal transcription is retained separately; this is the revised layout interpretation.

The numerical copy visibly has extra leading digits beside three-digit table numbers, consistent with Satoshi's account of added duplicate initials. The images alone do not date those alterations. Full collation of every entry remains outstanding.

## Tests on the unchanged letter

[check_r1588_framing.py](check_r1588_framing.py) applies the source-read lengths and reviewed indicators to a digit stream with original row/character coordinates. It does not substitute words or repair digits. The [diagnostic output](output/r1588_framing_check.json) is reproducible with `python3 check_r1588_framing.py` (`--build` regenerates it).

From the beginning in Prima, it segments:

`204 / 867 / 5547 / 1118 / 881 / 020 / 1108 …`

The first two units have historical support as **null + wo**. The remaining opening words require exact root/ending collation; the script does not insert the editorial *woferne*.

The scan reaches **69 groups / 233 digits** before its first consistency stop at **P1-R05:43**. The source there contains `768,5512`; the Prima length rule would consume `7685`, which lacks the repeated initial seen in the four-digit numerical entries. The scanner conservatively stops before accepting it. This safeguard is not a separately transcribed prohibition in clause 1, nor proof that a particular digit is wrong. Review the original letter and surrounding alignment before proposing a repair.

A separate, explicitly conditional probe begins at **P3-R02:50**, assuming Prima. It reads **1158 / 412**: a punctum followed by a reviewed indicator for Secunda. This gives a concrete candidate transition near the earlier second-table anchors. The next group by the Secunda rule would be `4929` at **P3-R02:59**, another unverified four-digit form. The probe stops there; it does not validate the rest of the passage or bridge the earlier failed scan.

Neither 69 framed groups nor any lookup count is a decipherment percentage. Unknown paragraph boundaries, doubtful digits, G signs, table-state continuity and lexical alternatives remain material limitations.

## Reviewed transcription and current replay

The earlier diagnostic above deliberately uses the unchanged input. Robert has since confirmed the central P1-R05 `3337,768` sequence and corrected the P3-R02 suffix after `1158` to `412,929,2215,112`. The outer `43` / `551` in the first crop and initial `5` in the second crop are clipped parts of neighbouring groups, not replacement whole groups.

[decode_historical.py](decode_historical.py) applies the recorded [human amendment](ciphertext_emendations.json) to a derived transcription. Its independent P3 probe reads `1158` punctum, `412` switch to Secunda, `929` Graf, `2215` return to Prima, then Prima `1121` across the row break and `221`. It stops at `5394` at P3-R03:6 in the derived text. The old `4929` diagnostic is superseded for this reviewed passage. The P1 stop remains unchanged; no missing prefix has been inserted into `768`.

The [historical key](historical_key.json) now records 290 source entries, including operational panels. Its lexical alternatives and provisional readings still need review. The [remaining-work list](REMAINING_WORK.md) defines the outstanding key transcription, worked-example control, continuous replay and editorial alignment. Identification and access to the numerical tables are settled.
