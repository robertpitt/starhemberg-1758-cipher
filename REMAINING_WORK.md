# Remaining work toward a complete decipherment

The decoder now produces a reproducible **conditional partial reading**. It joins supported row fragments, subdivides a numeric run only when the supplied dictionaries admit a unique complete candidate, and applies five explicitly located second-table hypotheses. It does not know the historical switching instruction. A passing software audit is not a claim that the whole letter reads correctly.

## Current result

The [reading validation report](output/reading_validation.md) compares eight selected literal results with the supplied German. Three match after case, spacing and accent normalization; one verifies only a stem; one retains a qualified key value; three expose editorial differences. All eight literal regression checks pass.

The replay accounts for every source character. Under its conservative rules it contains 441 candidate units, 206 unresolved numeric spans, three table-ambiguous spans, 17 uncertain digit groups, and four G glyphs. Fifty candidate-unit occurrences retain qualified values, including three `?` occurrences. These are distinct bookkeeping measures, with overlaps; they are not a count of missing key entries or a decipherment percentage. Changes to segmentation will change the span counts.

Twelve candidate units cross physical rows. Three recorded definite separators fall inside the explicit second-table candidate units. Those operations are visible in the source ledger, rather than silently applied to the transcription.

## Work in priority order

| Priority | Work | Where to start | Completion condition |
| --- | --- | --- | --- |
| 1 | Collate the source at the transition and separator-sensitive locations. | P3-R02 characters 49–68; P3-R11 around character 41; P3-R08 `9527,83`; P3-R18–R21. Then the 17 uncertain digit groups in the work queue. | Record defensible readings of digits and marks against the scans, with alternatives where the source does not decide. Any correction is justified independently of whether it makes a decoding fit. |
| 2 | Establish the entry and return switching mechanism. | Entry is conditionally between the main-table passage ending P3-R02:48 and the Stainville candidate beginning P3-R02:69. Return is conditionally after the Bezahlung candidate ending P3-R18:38 and before the main-table candidate beginning P3-R21:48. | Identify an observable trigger/state rule, verify it at other occurrences, and explain entry and return without choosing tables from desired plaintext. Locate any additional changes rather than assuming exactly two. |
| 3 | Establish segmentation beyond the local examples. | The opening `204867554711188810201108`; the P1-R06/P2-R01 join; `11021165005025020` on P2-R17; long page-three spans. | Account for digit boundaries, cross-row units, separators inside units, and the six main-table shape exceptions with explicit reproducible rules. Preserve competing parses until evidence selects one. |
| 4 | Complete and validate the working key. | Missing entries such as `7759`, `1158`, and `1116`; `main:409` and `main:9919`; alternative-valued entries; the three unresolved `066` table choices. | Support each assignment across its applicable occurrences. Separate missing units from wrongly grouped runs. Resolve or bound counterexamples and qualify genuinely ambiguous values. |
| 5 | Explain controls and the ending. | G1–G4 on P4-R03; remaining short fragments and any proposed null/cancellation/switch signs. | Specify the action of each control with evidence. No digit or glyph is discarded merely because it blocks a plausible reading. |
| 6 | Reconcile the entire literal output with the editorial German. | Use the row output and the supplied edition, including Vorstellung/Vorstellungen, Bezahlung/Zahlung, Abbé de Bernis/Abbé Bernis, Betrags, solle, [einer], and the uncertain opening. | Produce an occurrence-level alignment that identifies encoded content, spelling normalization, supplied expansions, actual discrepancies, and genuinely unreadable gaps. Then review the English translation against the settled German. |
| 7 | Obtain independent reproduction and a meaningful external test. | A second reviewer and, if available, another passage or letter using the same system that was not used to construct the rules. | A reviewer can reproduce the reading from source and explicit rules, inspect residual uncertainties, and test the rules without being handed a desired plaintext to fit. |

Priorities 1–3 are the immediate focus. Existing source-location anchors narrow the investigation; they do not identify the control instruction by themselves.

## Specific unresolved interpretation choices

- The first transition interval is `,1158,41,24929,22,45`. `1158` has no supplied key entry. The final `45` is the beginning of the written run `45112`, not a separately transcribed group. None of these numbers is currently designated a switch.
- The second-table `533` in the P3-R11 name crosses a recorded comma. Determine whether the source mark is genuinely non-boundary punctuation, another kind of sign, or a transcription error before generalizing that behavior.
- A unique second-table match outside an explicit hypothesis is only a candidate. For example, `005` on P1-R05 matches the second-table value `de`, but that does not establish a local switch or validate the surrounding name.
- The main-table code shape has exceptions `300`, `557`, `777`, `996`, `8831`, and `8888`. Do not “repair” these entries to force the predominant parity pattern.
- The `?` values and unlisted runs are not nulls. “No code identified for solle” is not proof that solle was not enciphered.

## What we can call complete

A **substantially deciphered** result needs a reproducible, continuous reading using justified grouping and table rules, with only localized, clearly described uncertainties. It may retain genuinely unreadable source marks.

A **complete decipherment** needs every legible cipher element explained, including operational signs and table changes; remaining gaps must be attributable to the source rather than an unexplained cipher mechanism. A fluent supplied edition, many successful local mappings, or a passing unit test does not meet this threshold alone.

## Reproduce and inspect

```sh
python3 audit.py
python3 -m unittest -v
```

The integrated audit verifies nine generated reports and retains `complete_decipherment: false`. To regenerate all reports after a reviewed change, run `python3 audit.py --build`, then repeat both commands above.

- [Conditional row-by-row reading](output/decoded_reading.md)
- [Selected reading comparisons and full unresolved-span queue](output/reading_validation.md)
- [Exact source ledger and candidate values](output/decoding.json)
- [Explicit local table/segmentation hypotheses](decoding_spans.json)
- [Supporting evidence and source-review qualifications](EVIDENCE.md)
