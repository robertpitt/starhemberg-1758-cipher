# Comparison of the newly supplied DECODE images

Checked 26 September 2026. **DECODE 1588 is strongly supported as the matching key, or a very close version of it. Its complete operation on the letter is not yet established. DECODE 1591 does not presently supply a matching key.**

This updates the earlier search result, not the negative finding about the different 1752 codebook (DECODE 1695/1698). No ciphertext, working-key entries, table-span hypotheses or decoder outputs were altered.

## Sources and method

The new folder contains ten PNGs, approximately 144 MB in total: R1588 P2–P6 and R1591 P1–P5. Small previews established the layout, followed by original-resolution crops of selected entries and instruction passages. No automated OCR text was used as evidence. The [observation ledger](supplied_codebook_observations.json) records source hashes, dimensions, crop coordinates, normalized root readings and their comparisons with the frozen working key. These visual readings remain open to independent palaeographic review; they are not a complete diplomatic transcription.

Original images and temporary crops remain outside the repository. The ledger contains text and provenance only.

[R1588's catalogue](https://de-crypt.org/decrypt-web/RecordsView/1588) identifies **HHStA, Staatskanzlei Interiora, Chiffrenschlüssel, Kt. 15, Fasc. 21, ff. 54–57**. This is the early lead requested after the literature search. The catalogue gives **15 June 1753**, whereas the survey previously consulted gives **16 June 1753** for instructions ff. 54–55. The one-day discrepancy is unresolved; the missing opening page may help settle it. Neither date should be silently substituted for the other.

## R1588: exact roots and corrected continuation pairing

**Correction:** the previous comparison paired unheaded continuation sheets by consecutive filenames. That was not a sound basis for table assignment. The entries and numerical families instead strongly support **P3 + P6 = Prima**, and **P5 + P4 = Secunda**. P3 and P5 have explicit headings; assignment of the two continuations remains an inference to confirm against the instructions and R1589.

P6 has `226=s`, `448=vor`, `832=ung`, `811=um` and `001=von`, agreeing with the same modern main table supported by headed P3. P4 has `066=vor`, agreeing with second; its S heading includes `336`, whereas P6's includes `226`. These are consistent with the different numerical families on the headed sheets. P6's indicators name Clavis 2 and P4's name Clavis 1, consistent with signals to the other table; that last interpretation still requires the operating instructions.

The following selected root readings agree with entries in our supplied key. Abbreviated endings and all alternative values have not been fully transcribed. Continuation assignments use the inference above.

| Code | Root read in R1588 | Photographed table | Existing working table |
| --- | --- | --- | --- |
| 219 | ab | Prima | main |
| 9931 | be | Prima | main |
| 645 | de | Prima | main |
| 1146 | ber | Prima | main |
| 473 | ni | Prima | main |
| 405 | machen, with abbreviated forms | Prima | main |
| 246 | Constantinopel | Prima | main |
| 226 | s | Prima (P6) | main |
| 448 | vor | Prima (P6) | main |
| 832 | ung, with a variant | Prima (P6) | main |
| 811 | um | Prima (P6) | main |
| 001 | von | Prima (P6) | main |
| 066 | vor | Secunda (P4) | second |
| 946 | l | Secunda | second: l(e) |

The six consecutive units `219 / 9931 / 645 / 1146 / 473 / 226` in the proposed *Abbé de Bernis* span now have lexical support within **one table**, under this pairing. The previously reported mid-word table conflict is withdrawn. This is a stronger match than isolated syllables and supports modern `main` corresponding to Prima and `second` to Secunda in the inspected entries. It does not authenticate every modern entry.

There are still readings which challenge or refine the reconstruction:

- P6 lists `867 = wo`, differing from main `ge / o`, and `204` among *Errantes* (nulls). The opening `204867…` can therefore begin **null + wo** in inferred Prima. The full opening and starting-table rule remain unproved.
- P4's `066 = vor` agrees with second and no longer presents a Prima/main mismatch. It does not establish Prima's value for 066.
- The Secunda L heading supports `946 = l`, without independently authenticating the optional `e` in `l(e)`.

The worked example on R1588 P2 also gives `020 = der` and `002 = das`, agreeing with existing main-table roots. Those observations are recorded as **worked-example evidence**, separately from the photographed tables. Its complete relationship to the tables and the letter has not been demonstrated. A full positive-control replay of the example is still needed.

The tables contain explicit null lists, punctuation categories and entries headed *Indicantes Clavim*. These establish that controls exist in this material; they do not yet establish their operation in our letter. No control or null was imported into the decoder.

### Human-reviewed indicators and source searches

Robert Pitt reviewed three targeted crops. The [reviewed transcription](supplied_indicator_review.json) records:

- Worked example: `025`, annotated `indic: Clav. 2ᵈᵘᵐ:`; `477` is beneath it. The neighboring `218` annotation remains uncertain (`Läger?`) and is not used in a decoding claim.
- `Indicantes Clavim 1ᵃᵐ`: **018, 104, 2215, 326, 4457, 6653**.
- `Indicantes Clavim 2ᵈᵃᵐ`: **412, 616, 5538, ?347, 477, 1122**. On the wider crop, Robert tentatively reads the uncertain entry as **3347** ("appears to read"). The conservative wildcard search remains in place; it finds no occurrence for any first digit.

These supersede provisional assistant readings of `320`, `618`, `5338` and a confident `3347`. In particular, **the letter's `618` at P3-R20 is not a match to the reviewed `616` indicator**. No ciphertext correction from 618 to 616 is justified.

[check_supplied_indicators.py](check_supplied_indicators.py) searches the unchanged transcription with source coordinates. Uncertain digit groups and G signs are barriers; separators and physical row boundaries can be crossed. It distinguishes full written groups from substrings. The [result](output/supplied_indicator_search.json) is a search inventory, not a parse:

| Reviewed candidate | Certain-digit substring hits | Entire written-group hits |
| --- | ---: | ---: |
| Example `025` | 6 | 3: P1-R02, P2-R02, P2-R07 |
| Table `018` | 1 | 0 |
| Table `104` | 4 | 0 |
| Table `2215` | 2 | 1: P3-R17, characters 52–55 |
| Table `412` | 2 | 0 |
| Table `477` | 6 | 0 |
| 326, 4457, 6653, 616, 5538, 1122 | 0 each | 0 |
| Unresolved pattern `?347` | 0 | 0 |

All six `477` hits cross observed commas; the second `2215` hit crosses the proposed Stainville segmentation (`122 / 153…`). These are not independent evidence of controls. Conversely, the absence of an entire written-group hit cannot exclude a control when historical separators may be misleading. Uncertain transcription areas are not exhausted by the search.

`2215` is currently assigned `f` in our second working table. Its confirmed appearance in the historical indicator list makes that assignment worth testing, but does not authorize replacing it before a coherent, source-supported replay succeeds.

Robert also confirmed the lower heading as **Com̄ata** (expanded **Commata**) and its first code as **025** on P6, now assigned to Prima by the continuation evidence. We therefore have two human-reviewed facts: the example annotates `025` as a Clavis 2 indicator, while the sheet lists it under punctuation. **This is a difference in the recorded roles, not yet proof of an operational contradiction.** The corrected pairing places the comma on inferred Prima, so a different-active-table explanation cannot simply be assumed. The example’s active state and any additional conventions must be established from the instructions. Likewise, an indicator can produce no plaintext, so the dash beneath `477` in the example must not automatically be interpreted as proof that it is a null rather than a control.

The supplied working key already records `main:025` as a comma. Robert explicitly rechecked and confirmed the table's punctuation assignment. This supports that role in the historical material; it does not establish the letter's active table at any occurrence. No global `025` switching rule is justified.

### Human-reviewed lexical comparison

Robert's next review confirms the first word **ist** with the following codes:

| Source | Confirmed code | Confirmed first word | Qualification |
| --- | --- | --- | --- |
| Worked example, P2 | 9999 | ist | No active table inferred from this observation. |
| Prima sheet, P3 | 1114 | ist | The additional word is tentatively read `ißt?`; not relied on. |
| Secunda sheet, P5 | 021 | ist | The additional word is tentatively read `ißt?`; not relied on. |

This establishes three source-attested assignments, not the absence of other homophones or alternative entries. In particular, it does **not** prove that `9999` cannot encode *ist* elsewhere in the photographed tables.

The reproducible source search now includes these lexical codes. Neither `9999` nor `1114` occurs in the certain-digit stream, including across physical boundaries. `021` has six substring occurrences, of which two are entire written groups: **P2-R06:7–9** and **P2-R13:58–60**. Both are currently unresolved in the conservative decoder. These are locations for a future historical-key replay, not two newly deciphered words: active table, adjoining units and manuscript readings still need validation.

An additional original-resolution visual check reads **Prima `246 = Constantinopel`**, directly agreeing with the existing main-table entry and its occurrence at **P1-R02:33–35**. The crop and source coordinates are recorded in the observation ledger; this last reading is an assistant visual observation, not part of Robert's reviewed E–G entries. It strengthens the lexical overlap without resolving the operating rules.

Run `python3 check_supplied_indicators.py` to check reproducibility; `--build` writes the report after a reviewed change. The frozen input hashes are checked in either mode. No decoder behavior changes.

## Satoshi's additional readings and R1589

Satoshi identifies R1589 as a numerically sorted copy of the same key and notes that the duplicated initial digits were added afterward. The [R1589 catalogue](https://de-crypt.org/decrypt-web/RecordsView/1589) identifies **Kt. 15, Fasc. 21, ff. 58–59**, dated 1753, with two pages of a numerical variable-length nomenclator. The catalogue was inspected; the images were not. There are no R1589 files in the supplied folder, and the online image control redirected to login. The same-key relationship and later addition of digits are therefore currently attributed to Satoshi, not independently verified here.

The [comparison ledger](satoshi_codebook_review.json) separates his proposals from our crop readings:

| Code | Satoshi's proposal | Original-resolution check |
| --- | --- | --- |
| 881 | n(e) | 881 visible at a short n entry with variants; exact expansion remains to check. |
| 210 | wurck | **Discrepancy:** the entry appears to be *würde…*. Nearby *würck…* has 1107, agreeing with our working key. Human review requested. |
| 1158 | punctum | Supported: 1158 is under **Puncta**. Treat as punctuation, not the plaintext word *punctum*. |
| 9973 | tri | Number occurs at a **tr** entry with abbreviated variants. Exact expansion *tri* remains to verify. |
| 617 | gu | Supported; the working key's low-confidence **igu** should be reconsidered. |
| 889 | aus | Supported; agrees with working key. |
| 019 | Condition | Supported, with abbreviated ending(s); agrees with working key. |
| 629 | davon, questioned | The entry is in the **auf…** sequence, tentatively *aufdaß*. A separate *davon* entry appears to have **621**. These need human review. |
| 681 | sprech, questioned | Appears to give the shorter root **spr**, agreeing with the working key; full *sprech* is not established. |

All nine codes are now included in the reproducible search inventory. This is a search, not a parse. Exact written-group occurrences are: 881 (1), 210 (1), 1158 (4), 9973 (1), 617 (1), 889 (2), 019 (0), 629 (1), 681 (1). The absence of a separate written group does not exclude a code inside a longer group; 019 has three substring hits.

Two particularly useful tests emerge:

- **P1-R04:49–52:** `1158` follows `405 / 1101` (working *machen / kön(te)*) and precedes `020` (*der*). A sentence stop fits this position. Three further full written occurrences are P2-R04, P3-R02 and P4-R04. These are distributed punctuation checks, not yet a complete punctuation replay.
- **P2-R15:45–60:** `880 / 9973 / 617 / 022`. Combining existing *in / … / … / en* with Satoshi's proposed *tri* and source-supported *gu* produces **in-tri-gu-en**, consistent with *Intriguen*. This is conditional on the expansion at 9973 and the active table, not an independent proof of the entire sentence.

The repeated-first-digit observation is a useful historical lead, but it is not a universal instruction to consume four digits whenever the first two agree. Our key also contains ordinary triplets such as 448. No stripping or segmentation rule has been imported without the missing instructions.

## R1591: different numerical conventions

[R1591's catalogue](https://de-crypt.org/decrypt-web/RecordsView/1591) covers **Kt. 15, Fasc. 21, ff. 66–70**. It therefore spans both ff. 66–67 and the requested ff. 68–69; the broad catalogue date is not a precise date for every photographed component.

The first instruction page is headed for ciphers **No. 12 and No. 13**. It describes No. 12 using three-digit odd numbers from 101 to 999, with even numbers and `861` treated as nulls; the following paragraph describes No. 13 using even numbers from 200 to 948 and contrary-parity/out-of-range nulls. The continuation permits continuous writing but requires three-digit units, including nulls, in that mode. These are targeted operational readings, not a full edition of the instructions.

The supplied numeric sheet, headed *Littera B*, is an odd-numbered table. A clear diagnostic entry is `867 = an`, differing from R1588's `867 = wo` and from the supplied working value. Its connection to every instruction page must be checked rather than assumed solely from the shared DECODE record number.

This material offers an overlap in general practice—parity, nulls and concealed boundaries—but no demonstrated multi-unit plaintext match to our letter. It is a lower-priority candidate. The current comparison does **not** claim an exhaustive rejection of every system or unseen table in R1591.

## What remains to establish an exact match

1. **Obtain R1588 P1 and the two R1589 images.** The supplied sequence starts at P2, mid-instruction. The online image list redirected to a login form, so the missing page could not be inspected. The missing instruction page is needed to establish the starting table, segmentation and switching conventions; its contents must not be guessed. R1589 should independently check the continuation pairing and disputed number-to-word assignments.
2. Transcribe and independently check enough of both historical tables, including controls and alternatives, to replay the complete worked example. Keep the example and tables separately identified until that comparison succeeds.
3. Test the letter's opening and distributed anchors with a fixed, source-supported table policy. Use the now-consistent *Bernis* span as an anchor; independently confirm the continuation pairing and check genuine mapping discrepancies, including 617 and 867. Never silently repair digits or substitute a more convenient table.
4. Extend to a full source-accounted replay. Report gaps, nulls, table changes, doubtful readings and G signs rather than replacing them with the editorial German.

**Assessment:** the multi-unit matches, corrected continuation pairing and new lexical/punctuation checks strongly support R1588 as the relevant key or a closely related version. Exact version identity and a complete executable decipherment remain to be demonstrated. The earlier apparent mixed-table conflict was our sheet-assignment error, not evidence against this key.
