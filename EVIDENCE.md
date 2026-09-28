# Evidence and remaining work

## Identified source

**DECODE R1588/R1589 is the identified codebook.** R1588 supplies alphabetical tables and instructions; R1589 is its numerical arrangement. R1588 P3 + P6 correspond to Prima, P5 + P4 to Secunda; R1589 P3 is Prima and P4 is Secunda. R1589 P1 is a cover and P2 an overview. Source-image filenames are retained in the key, but images are not distributed.

Correspondences include Prima `204` null, `219` ab, `448` vor, `617` gu and `1158` punctum, and Secunda `336` s and `066` vor. Robert confirmed Prima `025` as a comma: the worked-example switch annotation belongs to the following `477`. The instruction heading reads 16 June 1753; the catalogue’s 15 June remains a discrepancy. The letter is associated with 1758, folios 87–88; its exact date and full archival citation still need verification.

## Reading rules

Begin in Prima. A leading zero takes three digits in either table; otherwise Prima takes three for even initials and four for odd initials, with the rule reversed in Secunda. The instructions restart dispatches, paragraphs and letters in Prima. A switch to Secunda requires an indicator after a punctum or completed construction. Physical row breaks alone do not establish paragraph boundaries or resets.

Switches, punctuation, nulls and cancellation entries are included in `working_key.csv`. Provisional switches do not change replay state. Cancellation scope remains unresolved, so no surrounding text is deleted. The replay stops on uncertain source signs or a four-digit group without a repeated initial; the latter is a numerical-table consistency safeguard, not a separate length rule stated in the instruction. Recognition of an indicator alone does not prove that its sentence position permits a switch.

## Confirmed corrections and current limits

- **P1-R05:** Robert read `43,3337,768,551`; the outer groups were clipped. The full outer groups remain `643` and `5512`, and the central `3337,768` is unchanged. No digit has been inserted. The opening frames 69 groups / 233 digits before stopping at candidate `7685`, P1-R05:43.
- **P3-R02:** the reviewed transcription replaces `41,24929,22,45112` with `412,929,2215,112` after `1158` (original characters 55–71, excluding the row label). The leading `5` in Robert’s crop is the clipped end of the preceding group. This correction is now included directly in `ciphertext.txt`; the earlier transcription remains in Git history.
- **Local probe:** independently assuming Prima at P3-R02:50 gives `1158` punctum, `412` → Secunda, `929` Graf, `2215` → Prima, then provisional `1121` across the row break and `221` der. It stops at `5394`, P3-R03:6. It does not bridge the stopped opening or establish the proposed Stainville reading.
- **Coverage:** the 296 source entries comprise 232 lexical, 30 punctuation, 20 null, 12 switch and two cancellation entries. The review table additionally retains 86 supplied guesses, clearly labelled and excluded from decoding. It is a letter-focused selection, not the complete codebook.

## Human review

Norbert’s *Starhemberg - Norbert’s worksheet.xlsx* contributes 32 Prima readings explicitly marked `IMG`, including six additions: `096`, `663`, `676`, `694`, `5528`, `7759`. His alternatives and endings are preserved literally, including `210 = würde -n`. `1118 = r ; …` remains only partially transcribed; `049` remains provisional because his note says “IMG: illegible”. Robert’s partial `1121 = C - C[r|k]` also remains provisional.

Worksheet changes to `042`, `066`, `400`, `867`, `1107`, `1115` lack IMG and have not been adopted on that basis. The worksheet’s `621` does not authorize replacing the letter’s `629`. No Secunda entry was marked IMG. The review table records the reviewer and scope of confirmation; high confidence does not validate every expansion or occurrence.

## To complete the decipherment

1. Resolve the low-confidence and untranscribed entries in the [review table](output/key_review_table.md), including `049`, `1121`, `629`/`621`, `400`, `004` and `1115`; distinguish literal readings from expanded endings.
2. Recheck the unresolved digit forms at P1-R05 and P3-R03, the G signs, paragraph boundaries and cancellation rules against the manuscript. Resolve the worked example’s extra `240` in the continuous string versus its annotated breakdown.
3. Produce a continuous, position-by-position replay through all 52 rows, with verified table states and every unknown retained explicitly.
4. Align every German phrase and English translation to that replay, resolve names and editorial additions, and obtain a final manuscript review and complete source citation.

The prose in [READING.md](READING.md), including unbracketed wording, remains an editorial working edition until that alignment is complete.
