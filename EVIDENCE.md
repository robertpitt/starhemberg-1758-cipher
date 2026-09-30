# Evidence and remaining work

## Identified source

**DECODE R1588/R1589 is the identified codebook.** R1588 supplies alphabetical tables and instructions; R1589 is its numerical arrangement. R1588 P3 + P6 correspond to Prima, P5 + P4 to Secunda; R1589 P3 is Prima and P4 is Secunda. R1589 P1 is a cover and P2 an overview. Source-image filenames are retained in the key, but images are not distributed.

Correspondences include Prima `204` null, `219` ab, `448` vor, `617` gu and `1158` punctum, and Secunda `336` s and `066` vor. Robert confirmed Prima `025` as a comma: the worked-example switch annotation belongs to the following `477`. The instruction heading reads 16 June 1753; the catalogue’s 15 June remains a discrepancy. The letter is associated with 1758, folios 87–88; its exact date and full archival citation still need verification.

## Reading rules

Begin in Prima. A leading zero takes three digits in either table; otherwise Prima takes three for even initials and four for odd initials, with the rule reversed in Secunda. The instructions restart dispatches, paragraphs and letters in Prima. A switch to Secunda requires an indicator after a punctum or completed construction. Physical row breaks alone do not establish paragraph boundaries or resets.

Switches, punctuation, nulls and cancellation entries are included in `working_key.csv`. Provisional switches do not change replay state. Cancellation scope remains unresolved, so no surrounding text is deleted. The replay stops on uncertain source signs or a four-digit group without a repeated initial; the latter is a numerical-table consistency safeguard, not a separate length rule stated in the instruction. Recognition of an indicator alone does not prove that its sentence position permits a switch.

## Confirmed corrections and current limits

- **P1-R05:** Norbert’s latest worksheet (`decryption!I22:J22`) gives `3333,7768`, superseding the earlier `3337,768` reading under Robert’s instruction to prioritize Norbert. This correction is applied directly to the ciphertext. The opening now frames 90 groups / 307 digits across page 1 and into page 2, stopping at `3540`, P2-R01:5. It does not establish every lexical expansion.
- **P3-R02:** the reviewed transcription replaces `41,24929,22,45112` with `412,929,2215,112` after `1158` (original characters 55–71, excluding the row label). The leading `5` in Robert’s crop is the clipped end of the preceding group. This correction is now included directly in `ciphertext.txt`; the earlier transcription remains in Git history.
- **P1-R03:** Norbert’s follow-up reads `621`, matching Prima `davon`. Characters 21–23 now read `621` instead of `629`, attributed to his human reading, without an independent new image check here. This changes only that occurrence; the separate key entry `629` remains provisional.
- **Local probe:** independently assuming Prima at P3-R02:50 gives `1158` punctum, `412` → Secunda, then Norbert’s `929 / 2215 / 112 / 122 / 153 / 946` = **gra / f / sta / in / vil / l(e)**, supporting **Graf Stainville**. It reaches nine groups, including untranscribed `557`, before stopping at `6388`, P3-R03:16. This is a local alignment under the stated starting assumption, not a continuation of the opening replay.
- **Coverage:** the 322 source entries comprise 261 lexical, 28 punctuation, 20 null, 11 switch and two cancellation entries. The review table additionally retains 62 supplied guesses, clearly labelled and excluded from decoding. It is a letter-focused selection, not the complete codebook.

## Human review

Norbert’s shared workbook, rechecked on 30 September 2026, contains 73 Prima readings marked `IMG`. The follow-up confirms `1115 = te -r/-n ; t` and corrects `400` from our earlier `Sturm` to `sey -e/-n -d`; it also checks `275`, `621`, `811`, `867` and `5540`. His notation is preserved literally. `1118 = r ; …` remains partial and `049` remains illegible. Robert’s `1121 = C - C[r|k]` remains provisional.

Two IMG entries carry explicit uncertainty: `248 = we ; definit -f/-ve` (first entry uncertain, explicitly not **ent**; worksheet B58:E58) and `5512 = k.h. / dein -e/-n` (“very unsure”; B179:E179). Both are provisional, replacing our earlier accepted readings; the phrase **enthaltene** consequently remains an editorial proposal. Norbert confirms **Betrags**, withdrawing **Ertrags** as a word reading; the latest workbook also image-confirms `004 = s ; ss`. `066` and `1107` are now image-checked; the unmarked `042` revision remains unadopted. Robert confirms that all 48 Secunda worksheet entries are Norbert’s manuscript readings despite the absence of IMG markers. They are credited accordingly, retaining 20 high, 27 medium and one low confidence. Human confidence concerns the stated reading, not every expansion or occurrence.

The 30 September update adds 33 IMG readings, including `011 = habe -n`, `028 = p ; pp`, `442 = kei -t -e -n`, `613 = le -t/-n -s`, `3395 = is ; Corsi -ca`, `5584 = falle -t -n`, `7718 = bald` and `7768 = ke -s -n`. Literal alternatives are retained. `005 = e ; ??` is provisional because Norbert allows **e** in Kurrent or **r** in Latin cursive and cannot read the second entry; `3337 = ment -ion (?)` is explicitly uncertain. These are uncertainties in the key even where a contextual word looks plausible. No new source images or ledgers are added to the repository.

Norbert’s Secunda values take priority over the earlier assistant transcriptions: `141 = wor`, `353 = und`, `732 = von`, `777 = ni`, `2215 = f` and `4447 = nach` are among the changes. In particular, `2215` is now lexical **f**, replacing the earlier Robert-confirmed switch interpretation. This conflict with the operational-panel reading remains explicit and needs comparison with the exact source entry; the decoder follows Norbert’s current reading and does not switch on `2215`. The low-confidence `2259 = te nur` remains provisional.

## To complete the decipherment

1. Resolve the low-confidence and untranscribed entries in the [review table](output/key_review_table.md), including `005`, `248`, `5512`, `049`, `1121`, `629` and `3337`; distinguish literal readings from expanded endings.
2. Recheck the unresolved digit forms at P2-R01 and P3-R03, and the conflicting `2215` switch/letter interpretations, the G signs, paragraph boundaries and cancellation rules against the manuscript. Resolve the worked example’s extra `240` in the continuous string versus its annotated breakdown.
3. Produce a continuous, position-by-position replay through all 52 rows, with verified table states and every unknown retained explicitly.
4. Align every German phrase and English translation to that replay, resolve names and editorial additions, and obtain a final manuscript review and complete source citation.

The prose in [READING.md](READING.md), including unbracketed wording, remains an editorial working edition until that alignment is complete.
