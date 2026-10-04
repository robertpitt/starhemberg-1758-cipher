# Evidence and remaining work

## Identified source

**DECODE R1588/R1589 is the identified codebook.** R1588 supplies alphabetical tables and instructions; R1589 is its numerical arrangement. R1588 P3 + P6 correspond to Prima, P5 + P4 to Secunda; R1589 P3 is Prima and P4 is Secunda. R1589 P1 is a cover and P2 an overview. Source-image filenames are retained in the key, but images are not distributed.

Correspondences include Prima `204` null, `219` ab, `448` vor, `617` gu and `1158` punctum, and Secunda `336` s and `066` vor. Robert confirmed Prima `025` as a comma: the worked-example switch annotation belongs to the following `477`. The instruction heading reads 16 June 1753; the catalogue’s 15 June remains a discrepancy. The letter is associated with 1758, folios 87–88; its exact date and full archival citation still need verification.

## Reading rules

Begin in Prima. A leading zero takes three digits in either table; otherwise Prima takes three for even initials and four for odd initials, with the rule reversed in Secunda. The instructions restart dispatches, paragraphs and letters in Prima. A switch to Secunda requires an indicator after a punctum or completed construction. Physical row breaks alone do not establish paragraph boundaries or resets.

Switches, punctuation, nulls and cancellation entries are included in `working_key.csv`. Provisional switches do not change replay state. Cancellation scope remains unresolved, so no surrounding text is deleted. The replay stops on uncertain source signs or a four-digit group without a repeated initial; the latter is a numerical-table consistency safeguard, not a separate length rule stated in the instruction. Recognition of an indicator alone does not prove that its sentence position permits a switch.

## Confirmed corrections and current limits

- **P1-R05:** Norbert’s latest worksheet (`decryption!I22:J22`) gives `3333,7768`, superseding the earlier `3337,768` reading under Robert’s instruction to prioritize Norbert. This correction is applied directly to the ciphertext. The opening now frames 90 groups / 307 digits across page 1 and into page 2, stopping at `3540`, P2-R01:5. It does not establish every lexical expansion.
- **P3-R02:** the earlier reviewed transcription replaced `41,24929,22,45112` with `412,929,2215,112` after `1158` (original characters 55–71, excluding the row label). The leading `5` in Robert’s crop was the clipped end of the preceding group. The completed worksheet instead supplies `412,929,2275,112` at `decryption!M142:P142`. The existing manuscript transcript is preserved for comparison; its `2215` needs review against Norbert’s new `2275`.
- **P1-R03:** Norbert’s follow-up reads `621`, matching Prima `davon`. Characters 21–23 now read `621` instead of `629`, attributed to his human reading, without an independent new image check here. This changes only that occurrence; the separate key entry `629` remains provisional.
- **Local probe:** independently assuming Prima at P3-R02:50 still frames nine groups before stopping at `6388`, P3-R03:16. Under the completed key, its old `2215 / 112` sequence no longer supports Stainville. Norbert’s worksheet gives `929 / 2275 / 112 / 122 / 153 / 946 / 155`, with contextual choices **graf / st / a / in / vi / l / e**, supporting **Graf Stainville** in his grouped transcription. The old `2215 = f` key entry is absent from the completed worksheet and is retained only with its earlier provenance; it is not used in the worksheet replay.
- **Coverage:** the 530 source entries comprise 467 lexical, 30 punctuation, 20 null, 11 switch and two cancellation entries. The review table additionally retains six supplied guesses, clearly labelled and excluded from decoding. The completed worksheet contributes 445 entries; 85 other source entries retain their earlier provenance. This remains a letter-focused selection, not the complete codebook.

## Completed worksheet, 4 October 2026

Norbert announced completion of his decryption worksheet. The downloaded workbook contains `clavis prima` (267 readings), `clavis 2da` (178 readings), and `decryption` (779 groups in 52 blocks). The retrieval date, source filename and workbook SHA-256 are recorded in [sources/norbert_workbook.json](sources/norbert_workbook.json). Embedded images are excluded from the repository. The standard-library importer [norbert.py](norbert.py) saves text-only key and decryption CSVs, including cell locations, literal notes, formula text and cached lookup results.

The completed values take priority over the earlier partial import. This adds 152 previously absent key identities and replaces 56 supplied guesses with source readings. Among existing identities, 161 normalized literal values change. Examples include Prima `437 = er -s`, `440 = hab -e -n`, `7768 = ke -t -n`, and Secunda `112 = a ; Prinz Carl`, `141 = Comma`, `153 = vi`, `353 = Comma`, `500 = und`, `732 = stand/ständ -en`, `777 = das`, `2275 = st ; würde -n`, and `4447 = te -r/-n -t -s`. These changes supersede the corresponding earlier values, rather than accumulating as competing active readings.

Prima `005 = e ; meld -en/-ung` and `1118 = r ; rr ; Böhm -en -ische` resolve the earlier incomplete values. `049 = [ste]` remains illegible because of torn paper. `248` still explicitly excludes **ent** as a literal reading. `5512 = h ;  h / dein -e/-n` remains uncertain. Fifteen worksheet entries are provisional because their values or notes express uncertainty; partial notes about unreadable alternatives at Prima `5537` and Secunda `155` are also preserved. New readings without stated confidence are Moderate. Existing confidence and Robert’s confirmations are retained for unchanged, confirmed values. No IMG marker is required to import Norbert’s completed readings.

The [comparison output](output/norbert_comparison.md) replays all 779 groups continuously from Prima, matching the worksheet’s stated tables and both switches (`decryption!M142`, Prima → Secunda; `G232`, Secunda → Prima). Its cached lookups agree with the imported key. This establishes consistency between the supplied transcription and decoder rules; it does not independently authenticate the handwriting or expand every alternative.

The worksheet stream has 2574 digits. The manuscript projection has 2553 characters, including unresolved signs. Sequence alignment identifies 154 candidate edit spans, beginning with the manuscript’s `3540` versus worksheet `5540` at P2-R01:5 / `decryption!B32`. Repeated digits can make edit boundaries ambiguous. These spans are exposed for review; the importer does not silently overwrite `ciphertext.txt` or infer paragraph resets from physical row boundaries.

Norbert’s notes identify `028` as an enciphering error for `038 = solle`, and Secunda `8835` as an error for comma `8833`. The worksheet replay retains actual `028` and `8835`; the proposed corrections remain annotations. His green `3333,7768` note corresponds to the correction already adopted at P1-R05. The notes `?` and `771?` are preserved without forcing changes to adjoining groups.

The supplied [email transcription](sources/norbert_interlinear.txt) preserves its four page sections, historical spelling, uncertainty and explicit ciphertext differences: **Herr**, **Belle-Isle**, **soubisische**, restored **de Bernis**, **worvon dieser Ministre mir**, and **damit**. [READING.md](READING.md) adopts these readings, **zehlen**, **an dem**, and **ganz neuerlich**, and replaces the unsupported `[einer]` phrase with uncertain `[ehestens?] eine abermahlige Zahlung`. Its English translation is revised accordingly. Interlinear line breaks are independent of the 52 cipher blocks.

## Earlier human review, superseded where noted above

The 30 September 2026 import incorporated 73 Prima readings marked `IMG`, including 33 new readings, and all 48 Secunda readings. Robert confirmed that the absence of Secunda IMG markers did not mean those entries were unreviewed. Those source versions and confidence labels remain in Git history. Unchanged confirmations, including `1115 = te -r/-n ; t`, `400 = sey -e/-n -d` and `004 = s ; ss`, are retained in the current key.

That earlier version left `005` and `1118` incomplete, used `7768 = ke -s -n`, and deferred the unmarked `042` revision. The completed worksheet supersedes those values, including `042 = st ; Mähr -e -ische`. Its new `5512` notation also supersedes `k.h. / dein -e/-n`, while preserving uncertainty. Norbert’s word reading **Betrags**, withdrawing **Ertrags**, remains adopted. Robert’s `1121 = C - C[r|k]` remains provisional and is absent from the completed worksheet.

Earlier Secunda imports used `141 = wor`, `353 = und`, `732 = von`, `777 = ni`, `4447 = nach` and provisional `2259 = te nur`. All are replaced by the completed readings above or in the source CSV. The earlier `2215 = f` had replaced a Robert-confirmed switch interpretation; that old source conflict still requires an exact manuscript check. Its retained lexical entry does not drive a switch and is absent from the completed worksheet’s Stainville sequence.

## To complete the decipherment

1. Resolve the low-confidence readings in the [review table](output/key_review_table.md), including `248`, `5512`, `049`, `1121`, `629` and `3337`; distinguish literal readings from expanded endings and uncertain alternate entries.
2. Review the 154 candidate edit spans in the [worksheet comparison](output/norbert_comparison.md), particularly P2-R01 and the new `2275` at P3-R02. Recheck G signs, paragraph boundaries, cancellation rules and the `028`/`038` and `8835`/`8833` enciphering notes against the manuscript. Resolve the worked example’s extra `240` in the continuous string versus its annotated breakdown.
3. Extend the manuscript replay through all 52 rows using reviewed source corrections. The completed worksheet already replays continuously; its agreement with the decoder does not settle the manuscript differences.
4. Align every German phrase and English translation to that replay, including `[ehestens?]`, resolve editorial additions, and obtain a final manuscript review and complete source citation.

The prose in [READING.md](READING.md), including unbracketed wording, remains an editorial working edition until that alignment is complete.
