# R1588 worked-example check

The complete continuous digit string frames under the recovered rules, starting in Prima and changing to Secunda at `477`. This is an assistant transcription, not a fully authenticated plaintext check.

| Table | Code | Key reading / operation |
| --- | --- | --- |
| prima | `5534` | ∅ |
| prima | `009` | es |
| prima | `9999` | ist |
| prima | `9990` | et |
| prima | `5545` | wa |
| prima | `065` | ∅ |
| prima | `240` | drey / dritte |
| prima | `240` | drey / dritte |
| prima | `218` | [provisional: Tag / täglich?] |
| prima | `025` | , |
| prima | `1196` | ∅ |
| prima | `002` | daß |
| prima | `632` | ∅ |
| prima | `020` | der |
| prima | `3372` | [provisional: franz… Ministre?] |
| prima | `477` | → secunda |
| secunda | `8889` | ∅ |
| secunda | `357` | hi / hier |
| secunda | `780` | et / ange |
| secunda | `6655` | ∅ |
| secunda | `573` | lan / lang |
| secunda | `577` | et |
| secunda | `029` | , |

**Stop:** `{"reason": "end_of_stream"}`.

## Continuous string versus annotated breakdown

Differences are preserved, rather than corrected to make the example agree:

```json
[
  {
    "operation": "delete",
    "continuous_group_index_1based": 7,
    "continuous_codes": [
      "240"
    ],
    "annotated_codes": []
  }
]
```

- The continuous first line appears to repeat 240; the interlinear breakdown lists 240 once. Preserve both representations pending independent review.
- The initial characters of annotated 6655 resemble zeros; the continuous line reads 6655 and the source key lists it as a Secunda null. This cross-reading is recorded, not an independent human confirmation.
- The text beside 218 remains uncertain; a previous human review suggested Läger?, whereas the current assistant reads Tage. Do not silently resolve the disagreement.
- The switch annotation is above 477; 025 has a comma. This is a layout interpretation corroborated by the operational panels.
- The example ends with encoded comma 029; do not impose a final full stop.

The explicit annotation readings and source crop coordinates are in `r1588_worked_example.json`. Resolve provisional readings and compare all abbreviated alternatives with the annotations before claiming full independent validation. In particular, numerical `3372` appears to name a French minister, while the example annotation appears to name a French army; this remains an unresolved source reading or discrepancy.
