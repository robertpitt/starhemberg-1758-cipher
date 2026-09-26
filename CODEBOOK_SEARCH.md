# Codebook search: findings and next comparisons

Research checked 26 September 2026. **R1588 is now strongly supported as the relevant historical key, or a closely related version; full operational application remains unverified.** The comparison letter remains separate. No input digits or working-key assignments were changed.

**Update, 26 September:** supplied images identify the early leads as DECODE 1588 and 1591. R1588 supplies substantial exact root overlaps. Entry and numerical-family evidence corrects the continuation pairing to P3+P6 (Prima) and P5+P4 (Secunda), removing the previously reported Bernis table conflict. R1588’s opening instruction page and all R1589 images are now supplied; selected numerical entries independently corroborate the pairing. See [operating rules and framing checks](R1588_OPERATING_RULES.md). See the [source comparison](SUPPLIED_CODEBOOK_COMPARISON.md) and [observation ledger](supplied_codebook_observations.json). An exact whole-letter match is still unverified.

## The comparison letter is identified

[Andy Aymeloglu's edition](https://aaymeloglu.github.io/unsolved-ciphers/starhemberg-reading.html) concerns Starhemberg's letter of 23 May 1758 about Wall, Farinelli and Minorca. It uses DECODE 1695/1698 and instructions 1696/1697. The author explicitly distinguishes a complete proposed reading from exact decipherment and records conjectural repairs.

Our letter has 52 cipher rows and different contents, including Constantinople, Belle-Isle, Soubise and subsidies. Its precise date remains unestablished. These are different letters.

All 32 records in the supplied spreadsheet that lie wholly within lines V3 or V9 match the corresponding digit positions in the linked edition: 13 on V3 and 19 on V9. This strongly identifies the spreadsheet's source letter. It does **not** validate all 216 spreadsheet records or their plaintext. The [comparison snapshot](output/codebook_search_checks.json) records the two lines, offsets, results and our input hashes. Spreadsheet numeric cells were zero-padded to their stated span widths for this comparison only.

The [negative direct-application test](HISTORICAL_CODEBOOK.md) remains applicable to our unchanged transcription. Success on another letter does not supply the missing code families here.

## Distinctive evidence from our working key

Every one of the **115 four-digit entries** repeats its first digit. This makes systems that add a repeated initial digit worth investigating. However, **34 three-digit entries** also repeat their first digit: 28 main and six second. For example, main `448` and second `112` are triplets. Therefore, a blanket rule that consumes four digits whenever the first two agree conflicts with the current working key.

These are properties of a supplied, partially reconstructed key, not proof of a historical algorithm. Candidate instructions must explain the exceptions and table-dependent behavior without choosing rules solely to fit the desired German.

## Specific leads

| Lead | Reason to inspect | Limitation |
| --- | --- | --- |
| HHStA, Staatskanzlei Interiora, Chiffrenschlüssel, **Kt. 15, Fasc. 21, ff. 54–55** and **ff. 68–69** | The published survey lists German multi-table instructions dated 16 June 1753 and approximately 1745–1755. These are chronologically appropriate leads. | Now identified as R1588 and R1591. Supplied pages, now including R1588 P1 and the R1589 numerical counterpart, inspected selectively. See the current source comparison. |
| **DECODE [2191](https://de-crypt.org/decrypt-web/RecordsView/2191)/[2192](https://de-crypt.org/decrypt-web/RecordsView/2192)**, instructions **[2190](https://de-crypt.org/decrypt-web/RecordsView/2190)** | Tomokiyo describes a repeated-initial, false-thousands-digit system. R2191 is catalogued at Kt. 20, Fasc. 27, ff. 102–104; instructions at ff. 98–101. | His vocabulary-based dating suggests around 1780, later than our letter. A method analogue, not an authenticated matching key. |
| **DECODE [2210](https://de-crypt.org/decrypt-web/RecordsView/2210)/[2211](https://de-crypt.org/decrypt-web/RecordsView/2211)**, instructions **[2212](https://de-crypt.org/decrypt-web/RecordsView/2212)** | Related repeated-digit mechanism: remove the added digit before looking up a three-digit value. R2210: Kt. 20, Fasc. 27, ff. 152–153; instructions ff. 156–159. | Also estimated around 1780; the simple repeated-first-two parsing rule conflicts with our triplet entries. |
| **DECODE [1699](https://de-crypt.org/decrypt-web/RecordsView/1699)** | Catalogue identifies a circular cipher dated 26 March 1759, Kt. 16, Fasc. 23 IV, ff. 19–21. | Later than 1758 and catalogued as fixed-length. An adjacent archival lead only; no numerical match established. |

The early instruction dates come from Appendix E of [Antal, Mírka and Kováč, *Development of obfuscation techniques in Vienna during the early modern era*](https://doi.org/10.1080/01611194.2025.2457096). That study documents repeated digits, parity-dependent nulls and multiple-table conventions in the broader collection. Its Esterházy–Kaunitz example uses the already-tested 1752 system; it is not evidence that that system fits our letter.

The repeated-digit mechanisms and approximate 1780 dates above are reported in [Satoshi Tomokiyo's *Variable-Length Numerical Code in Austrian Archives*](https://cryptiana.web.fc2.com/code/variable2.htm). The R2191, R2210 and R1699 catalogue pages were inspected, but their images could not be retrieved because the image viewer entered a login redirect loop. Their key assignments have therefore **not** been independently checked. Broad catalogue ranges such as 1686–1877 must not be treated as dates of composition.

## What would establish a match

1. Obtain the early German instructions and their associated numeric key sheets; inspect only small previews and decisive original-resolution crops initially.
2. Test multiple distributed anchors, including main `448/049/1127/832/405` and `219/9931/645/1146/473/226`, plus second-table spans. Allow only transformations actually supported by instructions.
3. Establish segmentation, table switches, nulls and the G signs independently of the proposed plaintext; explain apparently conflicting triplets and four-digit entries.
4. Replay the unchanged transcription with explicit source accounting, recording any proposed manuscript corrections separately. A few matching words alone would not authenticate the key or complete the decipherment.

The immediate work is now **source review at the framing stops, complete key collation, and replay with the recovered rules**; the requested R1588/R1589 images have arrived. The later examples can help recognize the mechanism while searching; their dates prevent treating them as the answer without further evidence.
