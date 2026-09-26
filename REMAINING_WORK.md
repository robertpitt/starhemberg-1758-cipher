# Remaining work

**Codebook identification is settled: R1588/R1589.** Its basic group-length and switching rules are recovered. Completion now depends on source transcription and a continuous, reproducible application to the letter.

| Priority | Work | Completion condition |
| --- | --- | --- |
| 1 | Complete the letter-specific key against both numerical and alphabetical tables. | Resolve the 83 pending and seven provisional supplied-key comparisons, investigate six incompatible code forms, and transcribe additional entries encountered in the letter. Expand abbreviated alternatives where needed. Every accepted reading has a source location and review status. |
| 2 | Resolve the two current framing stops. | Explain the human-confirmed `768` at P1-R05 and the state after `1158,412,929,2215,112` at P3-R02 without silently adding digits or suppressing the return-to-Prima indicator. Any amendment needs independent source evidence. |
| 3 | Finish lexical validation of the worked example. | The complete example now frames through its table switch. Independently review the duplicated `240` in the continuous string and the readings of `218` and `3372`; verify all abbreviated alternatives against the annotated plaintext. |
| 4 | Establish continuous state through all 52 letter rows. | Verify actual paragraph boundaries, each switch and return, uncertain digits, and crossed-row groups. Locate any source damage; do not choose tables from expected German. Explain the four G signs and the scope of cancellation codes. |
| 5 | Produce the final literal reading and editorial alignment. | Account for every legible cipher element; distinguish roots, alternative readings, normalized spelling, editorial expansions and genuine gaps. Reconcile the supplied German and then review the English translation. |
| 6 | Independent reproduction and citation check. | A second reviewer reproduces the reading from explicit rules and key without needing the desired plaintext. Verify the letter's date and full archival citation. |

## Immediate review

The current opening trace needs these untranscribed entries among others: `1115`, `5528`, `7759`, `004`, `011`, `028`, `694`, `3395`, `613`, `663`, `3337`. Prima `1121` now has Robert’s partial reading `C - C[r|k]`, retained as provisional. Reading those entries will improve the literal result, but cannot by itself repair a digit-boundary or table-state conflict.

Robert could only partially read `1121 = C - C[r|k]` and `210 = Wum[b|g]`; both remain provisional. `004`, `011` and `1115` still await a reading. The complete [key review queue](output/key_review_queue.md) lists all pending supplied-key comparisons and missing entries encountered in the current traces. The queue is not a complete inventory of all entries needed later in the letter because the continuous replay stops early.

## What is already deliverable

- Source-based key with 290 entries, source hashes and crop coordinates; provisional readings remain explicit.
- Operational panels covering nulls, punctuation, indicators and cancellation entries, with scope limitations recorded.
- Original transcription preserved, with the human-reviewed P3-R02 change applied only to a derived copy.
- Reproducible historical-rule probes and a comparison accounting for all 277 supplied-key entries.

The revised [German and English edition](READING.md) includes source-aligned extracts and marks the limits of the full editorial text. It does not fill the historical replay’s gaps.

## Completion standard

A substantially deciphered result needs a continuous, reproducible reading with only localized source uncertainties. A complete result explains every legible cipher element and control; remaining gaps must be attributable to the source, rather than an unexplained mechanism. The current output meets neither threshold yet.

Run `python3 decode_historical.py`, `python3 audit.py` and `python3 -m unittest -v` to verify the current outputs and behavioral checks. These validate software and consistency, not handwriting or the full plaintext.
