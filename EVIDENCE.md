# Starhemberg–Kaunitz cipher: current evidence

This document records the supporting examples and open questions for the supplied two-table working key. The checks establish literal lookups and source locations, not a complete decipherment procedure or independent historical authentication.

## Key inventory

| Property | Result |
| --- | ---: |
| Table-specific entries | 277 |
| Main / second entries | 229 / 48 |
| Distinct decimal strings | 275 |
| Duplicate table/group rows | 0 |
| Supplied high / medium / low labels | 97 / 96 / 84 |
| Explicit unknown entries | 2 |

The explicit unknowns are `main:409` and `main:9919`. Alternatives such as `070 = ein (also der?)`, `613 = o / mit`, and `7784 = Corps?` remain verbatim. Occurrence counts are supplied annotations, not a recount of this transcription.

Table identity matters: `066` maps to `sein` / `vor` and `777` to `lich` / `ni` in main / second respectively. Code groups remain strings with leading zeros.

## Reproducible examples

The first six checks use adjacent, exact written runs in the human-transcribed pages. The final two search literal digits in the draft page-three transcription under an explicitly proposed subdivision and table choice.

| Check | Source | Table and codes | Literal expansion |
| --- | --- | --- | --- |
| K23-01 | P1-R04 | main: `448 / 049 / 1127 / 832 / 405` | `vor / st / el / ung / machen` |
| K23-02 | P1-R04, P1-R06 | main: `049 / 1127 / 832` | `st / el / ung` |
| K23-03 | P2-R01, P2-R10 | main: `217 / 1165 / 1104` | `mi / li / ta` |
| K23-04 | P2-R13, P2-R19 | main: `219 / 9931 / 645` | `ab / be / de` |
| K23-05 | P2-R19 | main: `219 / 9931 / 645 / 1146 / 473 / 226` | `ab / be / de / ber / ni / s` |
| K23-06 | P2-R14 | main: `868 / 5537 / 1113 / 5519` | `grafen / Brühl / und / dem` |
| K23-07 | Across P3-R03/R04 and within P3-R11 | second: `533 / 005 / 714 / 771` | `be / de / ber / ni` |
| K23-08 | P3-R18, across written-run divisions | second: `533 / 195 / 396` | `be / zahl / ung` |

Exact character positions, confidence annotations, and conditions are in [output/selected_checks.json](output/selected_checks.json).

`vorstelungmachen` requires conventional spelling to become *Vorstellung machen*. The literal key supplies no intervening `en` between `ung` and `machen`. `abbedebernis` requires spacing, accents, and capitals to become *Abbé de Bernis*. These editorial operations are separate from lookup.

On P2-R13, the repeated `219 / 9931 / 645` prefix is followed by `1116`, which has no main-table entry. The context does not authorize inserting an otherwise unsupported value.

The K23-07 second-table expansion does not automatically supply the following `s`. The raw continuations differ and need separate collation. K23-08 verifies the code combination for *Bezahlung* and finds its digits in P3-R18; it does not independently authenticate the editorial location of the correction described in the readable edition.

## Written marks and editorial text

`main:025` expands to a comma. This encoded punctuation is distinct from comma- or tick-like separators between written numerals. The transcription retains both representations.

The German edition and its correction notes are preserved separately in [READING.md](READING.md). The prose retains *Vorstellungen*, *Zahlung*, and two instances of *Abbé Bernis* without `de`, while the notes describe different cipher readings.

Other unresolved readings include:

- **Betrags:** supplied as a corrected reading. `5540 = b / be` is present, but intervening `7759` is absent from the key; the complete word is not independently decoded by that entry alone.
- **solle:** no code has yet been identified. This does not prove the word absent or rule out smaller-unit encoding.
- **[einer]:** remains bracketed; no unsupported code is inserted.
- **Subsidio:** retained without adopting the suggested alternative.
- **Opening name and Einsicht[ung]:** remain uncertain.
- **Soubisische and feyerlich:** supplied readings, not independently authenticated by the software checks.

## Extent and limits

The transcription has 52 rows. Pages 1–2 contain 393 written-run occurrences: 313 have a non-`?` main-table value, three have an explicit `?`, and 77 have no exact main-table entry. Unknowns are not nulls. A long unlisted run can contain several genuine cipher units; a listed run can still carry alternatives. These counts do not measure decipherment completeness.

The [dual-table concordance](output/all_rows_dual_table_concordance.tsv) shows both tables for every written run. It infers no table assignment from the page number. The [literal overlay](output/human_pages_literal_overlay.md) uses only exact main-table lookups for pages 1–2, without splitting long runs or joining physical rows.

A full replay still needs explicit per-occurrence segmentation, table transitions, treatment of roots/endings and punctuation, interpretation of G1–G4, and resolution of remaining unknowns. Pages 3–4 need further transcription review. Manuscript images are not included, so visual authentication cannot be reproduced from this repository alone.

Run `python3 audit.py` to verify the inputs and all five generated reports. Check identifiers are stable references, not a chronology of research work.
