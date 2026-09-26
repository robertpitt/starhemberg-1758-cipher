# Evidence for the Starhemberg–Kaunitz decipherment

**R1588/R1589 is the identified codebook.** The remaining task is to transcribe its applicable entries accurately and apply its instructions to the letter. Identification does not establish that every supplied plaintext word or proposed table span is correct.

## Source identity and table pairing

The numerical R1589 tables corroborate the R1588 alphabetical tables and operational panels. The supported pairing is **R1588 P3 + P6 = Prima; P5 + P4 = Secunda**. R1589 P3 is Prima and P4 is Secunda; its P1 is a cover and P2 is an overview, not additional keys.

Selected correspondences include Prima `204` null, `219` ab, `226` s, `448` vor, `617` gu and `1158` punctum, alongside Secunda `336` s and `066` vor. Table identity and leading zeros are essential. The instruction heading is read as 16 June 1753; a catalogue date of 15 June remains a metadata discrepancy.

The [source-key ledger](historical_key.json) and [instruction ledger](r1588_source_rules.json) retain source hashes, dimensions and crop coordinates. Images remain outside the repository. Individual readings are visual transcriptions with stated review status, not a claim of independent palaeographic authentication.

## Operating rules and controls

The [instruction interpretation](R1588_OPERATING_RULES.md) establishes the initial Prima state and group lengths. Dispatches, paragraphs and letters begin in Prima; a switch to Secunda follows a punctum or completed construction and an indicator, never the middle of a word/construction. The physical rows do not encode verified paragraph boundaries.

| Operation | Prima | Secunda |
| --- | --- | --- |
| Switch to the other table | 412, 616, 5538, 3347 (provisional), 477, 1122 | 018, 104, 2215, 326, 4457, 6653 |
| Nulls | 065, 1196, 204, 3307, 415, 5534, 632, 7722, 815, 9908 | 017, 179, 2209, 362, 4475, 517, 6655, 727, 8889, 950 |
| Cancellation | 687 | 2268 |

The cancellation entries are transcribed, but their exact scope is not established. No adjacent text is deleted automatically. Punctuation assignments are enumerated in the [key inventory](output/historical_key.md).

Robert confirmed **025 = comma**. In the worked example the switch annotation belongs to the following `477`, consistent with the operational panel. Prima `9999 = ist` and alternative `1114 = ist` are compatible; Secunda `021 = ist` is another reviewed assignment. The [worked-example report](output/r1588_example_check.md) now frames all 23 groups through the switch. Its continuous string appears to repeat `240`, while the annotated breakdown has 22 groups. That discrepancy and provisional readings of `218` and `3372` prevent claiming full independent lexical validation.

## Reviewed letter readings and current replay

Robert's P1-R05 crop reading is `43,3337,768,551`; the outer groups are clipped at the crop edges. The central `3337,768` is retained exactly. Starting in Prima, the continuous diagnostic reaches 69 groups / 233 digits, then would consume `7685` at P1-R05:43. It stops because that four-digit form lacks the repeated initial observed in the numerical table. This is a conservative consistency safeguard, not an additional prohibition transcribed from the instruction. It does not prove that a specific digit is missing.

Robert's P3-R02 reading is `5,1158,412,929,2215,112`. The initial `5` is the clipped end of the preceding group. The reviewed suffix after `1158` replaces `41,24929,22,45112` with `412,929,2215,112` in a derived transcription only. The exact replacement and original coordinates are in [ciphertext_emendations.json](ciphertext_emendations.json).

An independent probe starting in Prima at the `1158` reads a punctum, switches on `412`, reads Secunda `929 = Graf`, then returns to Prima on `2215`. It frames `1121` across the physical row break and then `221`, before stopping at `5394` at P3-R03:6 in the derived text. This does **not** authenticate the former assumption of uninterrupted Secunda through the Stainville passage. Neither probe silently resumes after a stop or inserts editorial German.

## Key coverage and interpretation

The source transcription contains 290 entries: 226 lexical, 20 nulls, 30 punctuation, 12 indicators and two cancellation entries. It is a letter-focused selection, not an edition of all numerical table rows. Provisional entries remain labelled; a provisional indicator cannot change replay state.

Every one of the 277 supplied-key entries is classified: 181 source-transcribed, seven provisional, 83 awaiting handwriting review and six incompatible with the recovered group lengths (`300`, `557`, `777`, `996`, `8831`, `8888` in the supplied main table). These six are representation problems to investigate, not automatic instructions to alter ciphertext.

Some codes have both letter and word uses: Prima `019` includes `a / Condition`, and `1114` includes `e / ist`. Abbreviated alternatives are not yet fully expanded. Comparing a single root against an old guess cannot alone prove that the old reading is impossible. Robert partially reads `210 = Wum[b|g]` and `1121 = C - C[r|k]`; both are retained literally as provisional, without translating them as words. `629` also needs review. Full details appear in the key ledger and [review queue](output/key_review_queue.md).

## Limits of the supplied edition

The revised German and English in [READING.md](READING.md) distinguish source-aligned extracts from the full provisional prose. The extracts are checked against the replay; the prose is not a continuous decipherment. The supplied comparison edition is preserved in [input/supplied_reading.md](input/supplied_reading.md). The earlier conditional lookup reports check selected code combinations and five assumed second-table spans; they cannot establish historical state continuity. In particular, a passing `audit.py` or a fluent sentence is not proof of a complete decipherment.

Completion requires the remaining key readings, verified paragraph/table boundaries, explanation of unresolved digit forms and G signs, and a continuous literal-to-editorial alignment. [REMAINING_WORK.md](REMAINING_WORK.md) defines those requirements. The current generated replay retains `complete_decipherment: false`.
