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

Run `python3 audit.py` to verify the inputs and all nine generated reports, including the conditional replay. Check identifiers are stable references, not a chronology of research work.

## Segmentation: measured properties and conditional boundaries

The results below are reproduced by `python3 analyze_boundaries.py` in [output/boundary_analysis.json](output/boundary_analysis.json). They distinguish facts about the supplied files from interpretations of the historical cipher. No uncertain digit is selected, no unknown is deleted, and plaintext is not used to score a parse.

### What the supplied key establishes

Every listed code has three or four digits. The main table contains 127 three-digit and 102 four-digit entries; the second contains 35 and 13 respectively. Every four-digit entry in both tables starts with a repeated digit.

All 48 second-table entries follow this shape:

- Three digits: initial digit `0`, `1`, `3`, `5`, `7`, or `9`.
- Four digits: initial pair `22`, `44`, `66`, or `88`.

The predominant main-table shape reverses that parity: three digits beginning `0`, `2`, `4`, `6`, or `8`, or four digits beginning `11`, `33`, `55`, `77`, or `99`. However, six supplied entries violate this simple rule: `300`, `557`, `777`, `996`, `8831`, and `8888`. They are retained as exceptions, not corrected or treated as switching commands. These patterns describe this incomplete CSV; they do not license assigning values to every number of the same shape.

The supplied second table is **prefix-free**: no listed code is the beginning of another listed code. Thus, from a fixed starting digit, a complete parse consisting entirely of listed second-table entries is unique if it exists. This does not identify the starting digit, fill gaps in the key, or prove that the historical table was prefix-free.

The main table has 11 shorter/longer prefix conflicts involving `557`, `777`, `888`, and `996`. For example, both `777` and `7775` are entries. Consequently a parser must consider alternatives rather than decide greedily by shortest or longest entry. Prefix conflicts alone do not prove that any particular complete passage has multiple parses.

### Row breaks and uninterrupted runs

The transcription has 28 row boundaries without a definite separator at the end of the earlier row. Of these, 25 have wholly literal digits in the two adjoining runs. Joining those runs gives a unique complete main-table parse in 12 cases; in 11 of those, a code crosses the physical row break. The remaining 13 literal cases have no complete parse using the supplied entries. Three cases contain uncertain digits and are not resolved by choosing an alternative.

Examples of conditional cross-row units:

| Row boundary | Transcribed fragments | Listed main-table code | Supplied value |
| --- | --- | --- | --- |
| P1-R04/R05 | `5` / `521` | `5521` | Marechal |
| P1-R05/R06 | `3` / `365` | `3365` | an |
| P2-R02/R03 | `11` / `63` | `1163` | er |
| P2-R11/R12 | `777` / `5` | `7775` | ge / gen |
| P2-R18/R19 | `556` / `8` | `5568` | ch |
| P4-R03/R04 | `4` / `05` | `405` | machen |

These are exact matches with no digit changes. Conversely, P2-R04/R05 joins `437` and `040` but parses as **two** entries, `437 / 040`. An unmarked row break is therefore not by itself evidence that the surrounding digits form one code.

There are 79 wholly numeric written runs longer than four digits. Seven have a complete main-table parse and two have a complete second-table parse; each of these nine parses is unique within its supplied table. Examples are `1157460 → 1157 / 460` (P2-R04), `460090 → 460 / 090` (P2-R07), and `153946 → 153 / 946` (P3-R03, second table). The other 70 lack a complete known-entry parse in either table. This is a limitation of these dictionary-only tests, not proof of wrong digits, nulls, or further table changes.

### Separators can conflict with the proposed readings

On P3-R11, the transcription contains:

```text
1015,33005714,771,336
```

The supplied second table gives the unique complete parse of this digit span:

```text
101 / 533 / 005 / 714 / 771 / 336
ab  / be  / de  / ber / ni  / s
```

The recorded comma in `1015,33…` lies **inside** the proposed `533` unit. There is no recorded separator between `101` and `533`. Therefore this name reading, if accepted, requires both ignoring one recorded separator as a unit boundary and inserting an unwritten boundary. The precise spot for manuscript verification is P3-R11 character 41 in `ciphertext.txt`.

A second example is P3-R08's `9527,83`: the supplied reading `952 / 783 → feln / sche` puts the comma inside `783`. P3-R18's `19539,6…` likewise puts a comma inside `396` in the proposed `533 / 195 / 396 → be / zahl / ung`.

These are verifiable conflicts between the transcription's marks and particular key-based readings. They do not establish whether the original marks are non-boundary signs, misleading separators, or transcription errors. The original mark must be checked before choosing among those explanations.

## Table use: located anchors, unresolved switching instruction

Searching every possible starting digit for runs of at least four consecutive known second-table entries gives four maximal spans. The search ignores punctuation only as a diagnostic and records every crossed mark and row break. Numeric uncertainties and G signs remain barriers. No expected German is supplied to the search.

| Source span | Second-table segmentation | Supplied literal values |
| --- | --- | --- |
| P3-R02 character 69 to P3-R03 character 10 | `112 / 122 / 153 / 946` | sta / in / vil / l(e) |
| P3-R03 character 55 to P3-R04 character 11 | `533 / 005 / 714 / 771` | be / de / ber / ni |
| P3-R07 character 51 to P3-R08 character 16 | `923 / 2233 / 952 / 783 / 122` | zu / zwei / feln / sche / in |
| P3-R11 characters 37–57 | `101 / 533 / 005 / 714 / 771 / 336` | ab / be / de / ber / ni / s |

Positions count characters after the row identifier and tab, including punctuation and uncertainty notation. Each exact digit span has no complete parse using the supplied main table, even allowing different code lengths. The main table is incomplete, so this is not proof that an expanded main table could never explain it. The four-entry cutoff is a search definition, not a statistical significance threshold; short incidental matches are possible.

The first span starts in the final three digits of P3-R02's written run `45112`. Together with `122,153946` on the next row, it yields the supplied spelling components of *Stainville*. This supports placing second-table use before the end of P3-R02, **conditional on that reading**, rather than assigning a table to an entire page.

### Conditional bounds on transitions

On P3-R02, the main table supplies `233 / 1118 / 831 / 802 / 5568 / 1155` at characters 24–48, giving `stü / r / tzen / su / ch / möglich (or en)`. The second-table Stainville span begins at character 69. If both are genuine applications of their indicated tables and one table is active at a time, at least one transition lies between them. The intervening transcription is:

```text
,1158,41,24929,22,45
```

Those are characters 49–68 of P3-R02. No particular digit, mark, or group in this interval is established as a switch. In particular, `1158` is not present in the supplied CSV, and the final `45` is the leading part of the written run `45112`, not a separately recorded group.

For the return, the supplied second table yields `533 / 195 / 396` (*Bezahlung*) at P3-R18 characters 25–38. The unbroken run `7779054437248` at P3-R21 characters 48–60 has the unique supplied main-table parse `7779 / 054 / 437 / 248`. Later, P4-R02 characters 8–38 contain the main-table sequence `022 / 1113 / 1144 / 5536 / 022 / 223 / 7727` with every recorded separator respected. Accepting the earlier second-table and P3-R21 main-table applications bounds at least one return transition between those anchors. It does not locate the exact return or establish that there were only two changes overall.

### What would settle the next facts

The most focused source checks are P3-R02 characters 49–68 (the first transition interval), P3-R11 around `1015,33…` (a comma inside proposed `533`), P3-R08 around `9527,83`, and P3-R18–R21 (the return interval). These need careful collation of the original manuscript marks and their surrounding text. The original spread was inspected locally, including enlarged entry/return regions and the P3-R11 name. That inspection did not establish an unambiguous switching instruction or justify changing the frozen transcription. Overlapping interlinear strokes remain a limitation. The scans and rendered excerpts are kept outside this repository.

A switching rule must explain the same observable feature at entry and exit, and survive checks at its other occurrences. These located readings do not yet identify that feature. The measured code shapes provide a useful constraint for the next tests, while their exceptions prevent promoting a simple parity rule to a complete decoding instruction.

The inspected source is `AT-OeStAHHStA StAbt Frankreich Diplomatische Korrespondenz 103 Stahremberg an Kaunitz 1758 III-IV fol. 87-88 2.pdf`, its single PDF page showing manuscript pages 2–3. Its SHA-256 is `92e5f6b0bc092ebd6525817d87fe97c101820a9a070dd51b7817af7d0365b290`. The numerical results above are reproducible from the repository alone; the visual review requires this external source.

## Executable application and current validation

[decode.py](decode.py) applies complete known-entry parses to unseparated numeric runs, including across physical row breaks. It retains ambiguity when more than one segmentation/table choice is available and leaves unmatched material visible. Five source-located second-table hypotheses in [decoding_spans.json](decoding_spans.json) permit the specifically documented separator crossings; they do not constitute a switching algorithm. The replay does not use the German edition to choose any parse.

The [literal row output](output/decoded_reading.md) and [source ledger](output/decoding.json) preserve gaps, symbols, alternatives, and every source character. The [validation report](output/reading_validation.md) checks eight local outputs against the supplied readings and distinguishes normalized matches from a partial stem, qualified values, and editorial discrepancies. Passing these checks does not authenticate the complete passage. [REMAINING_WORK.md](REMAINING_WORK.md) lists the outstanding research and completion criteria.
