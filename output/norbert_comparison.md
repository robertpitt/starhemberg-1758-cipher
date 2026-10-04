# Norbert worksheet comparison

Source: Norbert’s completed worksheet, retrieved 2026-10-04. Workbook SHA-256: `7bd0eb469e2ccb47ef7d247c5df01387eeb8991fd8c449424d94a40813bb9941`. Text-only snapshots are in [sources](../sources).

Imported **445 key readings** (267 Prima, 178 Secunda) and **779 cipher groups** in 52 worksheet blocks. **0 key differences** from the imported source; **15 provisional key readings** retain explicit uncertainty.

Worksheet groups are replayed from Prima using the repository’s length and switch rules. All 779 groups and 2 table transitions agree with the worksheet’s stated tables.

**This is a replay of Norbert’s grouped transcription.** The reviewed manuscript transcription in [ciphertext.txt](../ciphertext.txt) still differs. The conservative manuscript replay and its stopping points remain in [historical_reading.md](historical_reading.md). Group framing does not verify handwriting, expand word endings or authenticate the interlinear prose.

Codes retain leading zeros. `-`, `Comma`, `punctum`, `media nota` and the two `indic. clav.` entries map to existing null, punctuation and switch operations. Other values retain their literal alternatives. Cached workbook results are recorded as cached values, not newly evaluated formulas.

Worksheet block labels follow manuscript page order. A block may include the end of a code printed on the next physical row. Email interlinear line breaks are independent of these block labels.

## Worksheet annotations

| Cell | Norbert’s note |
| --- | --- |
| P7 | 028 is an enciphering error |
| P8 | 038 = “solle” |
| P22 | marked green: ciphertext has four 3‘s in a row; should be five |
| P27 | fin p1 |
| E116 | ? |
| R157 | 8835: should be 8833 (Comma) |
| J176 | 771? |

The `028` and `8835` notes describe proposed corrections to enciphering. Both actual groups remain in the imported stream. The green `3333,7768` correction is already present in the repository. `771?` and the isolated `?` remain source notes.

## Differences in the digit streams

The table aligns the projected manuscript stream with the workbook stream using character sequence matching. It lists candidate changes, including unresolved source signs (`#`), without changing the manuscript transcription. Coordinates are one-based characters after the row label, or one-based digits within a worksheet code cell. Insertions are shown before the given manuscript coordinate. Repeated digits can make an edit boundary ambiguous.

154 candidate edit spans. Manuscript projection: 2553 characters; worksheet: 2574 digits.

| Operation | Manuscript start | Manuscript digits/signs | Worksheet start | Worksheet digits |
| --- | --- | --- | --- | --- |
| replace | P2-R01:5 | `3` | B32:1 | `5` |
| replace | P2-R01:22 | `7` | F32:2 | `2` |
| replace | P2-R01:32 | `1` | H32:3 | `7` |
| replace | P2-R02:9 | `0` | C37:2 | `6` |
| replace | P2-R02:45 | `0` | K37:3 | `6` |
| insert | P2-R02:51 | `∅` | M37:1 | `7` |
| insert | P2-R03:1 | `∅` | O37:3 | `136` |
| replace | P2-R03:38 | `03` | I42:3 | `6` |
| replace | P2-R04:12 | `3` | C47:4 | `5` |
| insert | P2-R04:24 | `∅` | F47:2 | `7` |
| replace | P2-R05:25 | `2` | F52:3 | `0` |
| replace | P2-R06:51 | `7` | L57:3 | `2` |
| replace | P2-R08:61 | `6` | N67:4 | `4` |
| replace | P2-R09:50 | `0` | J72:3 | `6` |
| delete | P2-R10:18 | `676` | E77:1 | `∅` |
| replace | P2-R10:23 | `7` | E77:2 | `2` |
| replace | P2-R10:31 | `77` | G77:2 | `22` |
| replace | P2-R10:62 | `7` | N77:3 | `1` |
| replace | P2-R10:66 | `7` | O77:3 | `2` |
| replace | P2-R12:8 | `8` | B87:2 | `9` |
| replace | P2-R12:20 | `0` | E87:1 | `6` |
| replace | P2-R13:2 | `0` | A92:2 | `6` |
| replace | P2-R13:20 | `1` | E92:3 | `4` |
| replace | P2-R14:24 | `6` | F97:1 | `0` |
| replace | P2-R16:11 | `1` | C107:4 | `7` |
| replace | P2-R16:22 | `6` | F107:1 | `0` |
| replace | P2-R16:44 | `7` | K107:1 | `2` |
| replace | P2-R16:61 | `2` | A112:2 | `3` |
| replace | P2-R17:5 | `7` | B112:3 | `2` |
| replace | P2-R17:19 | `5` | E112:4 | `3` |
| replace | P2-R18:20 | `2` | E117:1 | `0` |
| replace | P2-R18:29 | `33` | G117:1 | `55` |
| replace | P2-R18:36 | `17` | H117:3 | `42` |
| replace | P2-R20:4 | `0` | A127:2 | `6` |
| replace | P2-R20:13 | `7` | C127:3 | `2` |
| replace | P2-R20:34 | `7` | H127:1 | `2` |
| replace | P2-R21:36 | `55` | I132:1 | `66` |
| replace | P3-R01:2 | `#` | O132:3 | `2` |
| replace | P3-R01:73 | `#` | N137:4 | `2` |
| insert | P3-R02:5 | `∅` | B142:1 | `1` |
| replace | P3-R02:65 | `1` | O142:3 | `7` |
| insert | P3-R03:12 | `∅` | D147:1 | `1` |
| replace | P3-R03:16 | `6` | E147:2 | `0` |
| insert | P3-R03:22 | `∅` | F147:4 | `3` |
| replace | P3-R03:32 | `2` | J147:1 | `3` |
| replace | P3-R03:35 | `5` | K147:1 | `3` |
| insert | P3-R03:49 | `∅` | N147:3 | `1` |
| replace | P3-R03:54 | `6` | P147:2 | `01` |
| replace | P3-R04:15 | `9` | D152:3 | `6` |
| replace | P3-R04:46 | `3` | L152:1 | `5` |
| replace | P3-R05:20 | `9` | E157:2 | `00` |
| replace | P3-R05:24 | `4` | F157:3 | `1` |
| insert | P3-R05:31 | `∅` | H157:3 | `6` |
| replace | P3-R05:35 | `#` | J157:1 | `3` |
| replace | P3-R05:41 | `99` | J157:3 | `05` |
| replace | P3-R05:48 | `4` | L157:3 | `1` |
| replace | P3-R05:51 | `0` | M157:3 | `6` |
| replace | P3-R05:59 | `7` | P157:1 | `1` |
| replace | P3-R06:18 | `6` | E162:3 | `0` |
| replace | P3-R06:22 | `1` | G162:1 | `4` |
| replace | P3-R06:43 | `6` | L162:3 | `9` |
| replace | P3-R07:4 | `4` | A167:3 | `2` |
| replace | P3-R07:21 | `8` | F167:1 | `9` |
| replace | P3-R07:32 | `6` | H167:3 | `0` |
| replace | P3-R07:43 | `6` | K167:3 | `0` |
| replace | P3-R07:48 | `4` | L167:3 | `2` |
| insert | P3-R07:50 | `∅` | M167:2 | `7` |
| replace | P3-R08:7 | `5` | B172:2 | `3` |
| delete | P3-R08:17 | `4` | E172:1 | `∅` |
| insert | P3-R08:23 | `∅` | F172:1 | `3` |
| replace | P3-R08:41 | `#` | K172:3 | `0` |
| replace | P3-R08:50 | `9` | L172:4 | `6` |
| replace | P3-R08:58 | `96` | N172:3 | `00` |
| replace | P3-R09:24 | `#` | G177:1 | `22` |
| replace | P3-R09:36 | `#` | H177:3 | `9` |
| replace | P3-R09:45 | `9` | I177:4 | `0` |
| replace | P3-R09:48 | `1` | J177:3 | `7` |
| insert | P3-R09:52 | `∅` | L177:1 | `5` |
| replace | P3-R10:9 | `0` | C182:1 | `3` |
| replace | P3-R10:15 | `66` | D182:3 | `030` |
| insert | P3-R10:23 | `∅` | G182:1 | `0` |
| replace | P3-R10:25 | `43` | H182:1 | `5` |
| replace | P3-R10:37 | `6` | K182:1 | `0` |
| insert | P3-R10:43 | `∅` | L182:2 | `3` |
| replace | P3-R10:44 | `5#` | M182:1 | `9` |
| delete | P3-R10:52 | `2` | N182:1 | `∅` |
| replace | P3-R11:3 | `#` | A187:1 | `0` |
| replace | P3-R11:19 | `3` | D187:1 | `5` |
| replace | P3-R11:24 | `0` | E187:2 | `6` |
| delete | P3-R12:2 | `7` | A192:2 | `∅` |
| insert | P3-R12:5 | `∅` | B192:1 | `0` |
| replace | P3-R12:18 | `4` | D192:1 | `99` |
| replace | P3-R12:30 | `6` | G192:2 | `1` |
| replace | P3-R12:38 | `4` | I192:3 | `1` |
| insert | P3-R12:48 | `∅` | L192:2 | `1` |
| delete | P3-R12:49 | `6` | M192:1 | `∅` |
| replace | P3-R12:54 | `3` | N192:1 | `5` |
| replace | P3-R12:63 | `9` | P192:1 | `5` |
| replace | P3-R13:26 | `#` | G197:3 | `0` |
| replace | P3-R13:34 | `6` | H197:3 | `0` |
| replace | P3-R13:40 | `4` | I197:4 | `6` |
| replace | P3-R13:55 | `86` | N197:1 | `05` |
| replace | P3-R14:2 | `1` | Q197:3 | `6` |
| insert | P3-R14:7 | `∅` | B202:1 | `5` |
| replace | P3-R14:8 | `7` | B202:3 | `1` |
| insert | P3-R14:11 | `∅` | C202:2 | `6` |
| delete | P3-R14:12 | `6` | D202:1 | `∅` |
| insert | P3-R14:15 | `∅` | D202:2 | `3` |
| insert | P3-R14:23 | `∅` | G202:1 | `3` |
| replace | P3-R14:24 | `5#8` | G202:3 | `00` |
| replace | P3-R14:38 | `2` | I202:2 | `1` |
| replace | P3-R14:41 | `0` | J202:2 | `6` |
| replace | P3-R14:46 | `4` | K202:3 | `6` |
| replace | P3-R14:55 | `4` | N202:1 | `7` |
| insert | P3-R15:15 | `∅` | E207:2 | `0` |
| replace | P3-R15:36 | `66` | L207:1 | `50` |
| delete | P3-R15:41 | `8` | M207:2 | `∅` |
| replace | P3-R15:53 | `3` | P207:1 | `5` |
| replace | P3-R16:1 | `#` | A212:1 | `0` |
| replace | P3-R16:12 | `0` | C212:1 | `9` |
| replace | P3-R16:14 | `0` | C212:3 | `6` |
| insert | P3-R16:21 | `∅` | E212:3 | `8` |
| replace | P3-R16:25 | `9` | F212:3 | `0` |
| replace | P3-R17:3 | `#` | A217:3 | `0` |
| replace | P3-R17:14 | `#` | C217:1 | `0` |
| insert | P3-R17:25 | `∅` | D217:4 | `6555` |
| insert | P3-R17:27 | `∅` | F217:2 | `8` |
| delete | P3-R17:28 | `3568#` | G217:1 | `∅` |
| replace | P3-R17:50 | `9` | J217:1 | `1` |
| replace | P3-R17:57 | `4` | K217:3 | `3` |
| insert | P3-R17:62 | `∅` | M217:1 | `1` |
| replace | P3-R18:1 | `6` | P217:4 | `0` |
| replace | P3-R18:21 | `6` | F222:1 | `9` |
| insert | P3-R18:40 | `∅` | J222:2 | `67` |
| delete | P3-R18:41 | `76` | K222:2 | `∅` |
| replace | P3-R18:54 | `#` | N222:2 | `6` |
| replace | P3-R19:3 | `7` | A227:1 | `1` |
| delete | P3-R19:12 | `6` | C227:2 | `∅` |
| replace | P3-R19:37 | `#` | J227:1 | `4444` |
| replace | P3-R19:53 | `4` | L227:1 | `0` |
| replace | P3-R19:63 | `9` | N227:3 | `6` |
| replace | P3-R20:1 | `8` | A232:1 | `5` |
| replace | P3-R20:20 | `9` | F232:1 | `3` |
| replace | P3-R20:24 | `6` | G232:1 | `0` |
| replace | P3-R20:30 | `9` | H232:3 | `6` |
| replace | P3-R20:43 | `6` | L232:1 | `0` |
| replace | P3-R21:7 | `6` | B237:3 | `0` |
| replace | P3-R21:11 | `9` | C237:3 | `0` |
| replace | P3-R21:25 | `#` | G237:1 | `7` |
| replace | P3-R21:40 | `0` | I237:3 | `61` |
| insert | P3-R21:44 | `∅` | J237:4 | `1` |
| replace | P3-R21:46 | `6` | K237:3 | `5` |
| insert | P4-R01:26 | `∅` | G242:1 | `7` |
| replace | P4-R03:60 | `####` | N252:3 | `2222` |

## Literal group comparison

“Agrees” compares the imported key with the literal lookup. “Provisional” preserves uncertainty in a source reading. Missing or different cached values are called out separately. These labels are not a prose accuracy score.

| Block | Code cell | Table | Code | Worksheet cached reading | Repository reading / operation | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P1-R01 | A2 | prima | `204` | - | ∅ | Agrees |
| P1-R01 | B2 | prima | `867` | wo | wo | Agrees |
| P1-R01 | C2 | prima | `5547` | fe -r/-n ; r | fe -r/-n ; r | Agrees |
| P1-R01 | D2 | prima | `1118` | r ; rr ; Böhm -en -ische | r ; rr ; Böhm -en -ische | Agrees |
| P1-R01 | E2 | prima | `881` | ne -r/-n ; 9 | ne -r/-n ; 9 | Agrees |
| P1-R01 | F2 | prima | `020` | der -en | der -en | Agrees |
| P1-R01 | G2 | prima | `1108` | dar | dar | Agrees |
| P1-R01 | H2 | prima | `880` | in | in | Agrees |
| P1-R01 | I2 | prima | `437` | er -s  | er -s | Agrees |
| P1-R01 | J2 | prima | `248` | we ; definit -f/-ve | [provisional: we ; definit -f/-ve] | Provisional |
| P1-R01 | K2 | prima | `5512` | h ;  h / dein -e/-n | [provisional: h ;  h / dein -e/-n] | Provisional |
| P1-R01 | L2 | prima | `212` | n ; nn | n ; nn | Agrees |
| P1-R01 | M2 | prima | `1115` | te -r/-n ; t | te -r/-n ; t | Agrees |
| P1-R01 | N2 | prima | `811` | um | um | Agrees |
| P1-R01 | O2 | prima | `234` | stand -en | stand -en | Agrees |
| P1-R01 | P2 | prima | `9989` | weg -en | weg -en | Agrees |
| P1-R02 | A7 | prima | `5528` | deß -sen | deß -sen | Agrees |
| P1-R02 | B7 | prima | `275` | hiesig -e/-r -n -s | hiesig -e/-r -n -s | Agrees |
| P1-R02 | C7 | prima | `5540` | be | be | Agrees |
| P1-R02 | D7 | prima | `7759` | tra | tra | Agrees |
| P1-R02 | E7 | prima | `1102` | g ; gg  | g ; gg | Agrees |
| P1-R02 | F7 | prima | `004` | s ; ss  | s ; ss | Agrees |
| P1-R02 | G7 | prima | `880` | in | in | Agrees |
| P1-R02 | H7 | prima | `246` | Constantinopel | Constantinopel | Agrees |
| P1-R02 | I7 | prima | `1107` | würck -lich | würck -lich | Agrees |
| P1-R02 | J7 | prima | `066` | sein -e/-r -n -s | sein -e/-r -n -s | Agrees |
| P1-R02 | K7 | prima | `068` | richt -e/-n -t -ig | richt -e/-n -t -ig | Agrees |
| P1-R02 | L7 | prima | `442` | kei -t -e -n | kei -t -e -n | Agrees |
| P1-R02 | M7 | prima | `011` | habe -n | habe -n | Agrees |
| P1-R02 | N7 | prima | `028` | p ; pp | p ; pp | Agrees |
| P1-R02 | O7 | prima | `025` | Comma | , | Agrees |
| P1-R03 | A12 | prima | `009` | es | es | Agrees |
| P1-R03 | B12 | prima | `694` | nöthig nothwendig | nöthig nothwendig | Agrees |
| P1-R03 | C12 | prima | `400` | sey -e/-n -d | sey -e/-n -d | Agrees |
| P1-R03 | D12 | prima | `210` | würde -n | würde -n | Agrees |
| P1-R03 | E12 | prima | `3323` | mich | mich | Agrees |
| P1-R03 | F12 | prima | `621` | davon | davon | Agrees |
| P1-R03 | G12 | prima | `446` | zu ; zuzu  | zu ; zuzu | Agrees |
| P1-R03 | H12 | prima | `7750` | unter | unter | Agrees |
| P1-R03 | I12 | prima | `068` | richt -e/-n -t -ig | richt -e/-n -t -ig | Agrees |
| P1-R03 | J12 | prima | `262` | Comma | , | Agrees |
| P1-R03 | K12 | prima | `423` | damit | damit | Agrees |
| P1-R03 | L12 | prima | `666` | ich -e/ -n | ich -e/ -n | Agrees |
| P1-R03 | M12 | prima | `3340` | diß | diß | Agrees |
| P1-R03 | N12 | prima | `5584` | falle -t -n | falle -t -n | Agrees |
| P1-R03 | O12 | prima | `004` | s ; ss  | s ; ss | Agrees |
| P1-R04 | A17 | prima | `5549` | al ; all | al ; all | Agrees |
| P1-R04 | B17 | prima | `7760` | hie -r | hie -r | Agrees |
| P1-R04 | C17 | prima | `007` | die | die | Agrees |
| P1-R04 | D17 | prima | `428` | dien\|st -en | dien\|st -en | Agrees |
| P1-R04 | E17 | prima | `222` | lich -e/-r -n -s | lich -e/-r -n -s | Agrees |
| P1-R04 | F17 | prima | `448` | vor | vor | Agrees |
| P1-R04 | G17 | prima | `049` | [ste] | [provisional: [ste]] | Provisional |
| P1-R04 | H17 | prima | `1127` | l ; ll | l ; ll | Agrees |
| P1-R04 | I17 | prima | `832` | ung -en | ung -en | Agrees |
| P1-R04 | J17 | prima | `405` | mach -e -n | mach -e -n | Agrees |
| P1-R04 | K17 | prima | `1101` | könte -n | könte -n | Agrees |
| P1-R04 | L17 | prima | `1158` | punctum | . | Agrees |
| P1-R04 | M17 | prima | `020` | der -en | der -en | Agrees |
| P1-R04 | N17 | prima | `9961` | herr -n -s | herr -n -s | Agrees |
| P1-R05 | A22 | prima | `5521` | Marsch\|all | Marsch\|all | Agrees |
| P1-R05 | B22 | prima | `5540` | be | be | Agrees |
| P1-R05 | C22 | prima | `1127` | l ; ll | l ; ll | Agrees |
| P1-R05 | D22 | prima | `005` | e ; meld -en/-ung | e ; meld -en/-ung | Agrees |
| P1-R05 | E22 | prima | `3395` | is ; Corsi -ca | is ; Corsi -ca | Agrees |
| P1-R05 | F22 | prima | `613` | le -t/-n -s | le -t/-n -s | Agrees |
| P1-R05 | G22 | prima | `663` | ist | ist | Agrees |
| P1-R05 | H22 | prima | `643` | mit | mit | Agrees |
| P1-R05 | I22 | prima | `3333` | vor | vor | Agrees |
| P1-R05 | J22 | prima | `7768` | ke -t -n | ke -t -n | Agrees |
| P1-R05 | K22 | prima | `5512` | h ;  h / dein -e/-n | [provisional: h ;  h / dein -e/-n] | Provisional |
| P1-R05 | L22 | prima | `1195` | sach -e/ -n | sach -e/ -n | Agrees |
| P1-R05 | M22 | prima | `1157` | ng -e/ -n -t | ng -e/ -n -t | Agrees |
| P1-R05 | N22 | prima | `460` | all -e/-r -n -s | all -e/-r -n -s | Agrees |
| P1-R06 | A27 | prima | `3365` | an | an | Agrees |
| P1-R06 | B27 | prima | `042` | st ; Mähr -e -ische | st ; Mähr -e -ische | Agrees |
| P1-R06 | C27 | prima | `5549` | al ; all | al ; all | Agrees |
| P1-R06 | D27 | prima | `662` | te -r/-n -t -s | te -r/-n -t -s | Agrees |
| P1-R06 | E27 | prima | `446` | zu ; zuzu  | zu ; zuzu | Agrees |
| P1-R06 | F27 | prima | `7718` | bald | bald | Agrees |
| P1-R06 | G27 | prima | `7773` | ige -r/n -d -s | ige -r/n -d -s | Agrees |
| P1-R06 | H27 | prima | `3375` | 90 ; he -t/ -n | 90 ; he -t/ -n | Agrees |
| P1-R06 | I27 | prima | `661` | r ; rr | r ; rr | Agrees |
| P1-R06 | J27 | prima | `049` | [ste] | [provisional: [ste]] | Provisional |
| P1-R06 | K27 | prima | `1127` | l ; ll | l ; ll | Agrees |
| P1-R06 | L27 | prima | `832` | ung -en | ung -en | Agrees |
| P1-R06 | M27 | prima | `020` | der -en | der -en | Agrees |
| P1-R06 | N27 | prima | `847` | Arm -ée -ir | Arm -ée -ir | Agrees |
| P1-R06 | O27 | prima | `1113` | und | und | Agrees |
| P2-R01 | A32 | prima | `013` | ver | ver | Agrees |
| P2-R01 | B32 | prima | `5540` | be | be | Agrees |
| P2-R01 | C32 | prima | `004` | s ; ss  | s ; ss | Agrees |
| P2-R01 | D32 | prima | `1163` | ser | ser | Agrees |
| P2-R01 | E32 | prima | `832` | ung -en | ung -en | Agrees |
| P2-R01 | F32 | prima | `020` | der -en | der -en | Agrees |
| P2-R01 | G32 | prima | `5564` | bis | bis | Agrees |
| P2-R01 | H32 | prima | `3375` | 90 ; he -t/ -n | 90 ; he -t/ -n | Agrees |
| P2-R01 | I32 | prima | `655` | ri | ri | Agrees |
| P2-R01 | J32 | prima | `7775` | ge -t -n | ge -t -n | Agrees |
| P2-R01 | K32 | prima | `217` | mi | mi | Agrees |
| P2-R01 | L32 | prima | `1165` | li -gs ; Firmian | li -gs ; Firmian | Agrees |
| P2-R01 | M32 | prima | `1104` | ta | ta | Agrees |
| P2-R01 | N32 | prima | `5567` | ri | ri | Agrees |
| P2-R02 | A37 | prima | `085` | sche -r/-n -s | sche -r/-n -s | Agrees |
| P2-R02 | B37 | prima | `070` | ein -e/ -n/-m -s | ein -e/ -n/-m -s | Agrees |
| P2-R02 | C37 | prima | `068` | richt -e/-n -t -ig | richt -e/-n -t -ig | Agrees |
| P2-R02 | D37 | prima | `832` | ung -en | ung -en | Agrees |
| P2-R02 | E37 | prima | `232` | ei | ei | Agrees |
| P2-R02 | F37 | prima | `5547` | fe -r/-n ; r | fe -r/-n ; r | Agrees |
| P2-R02 | G37 | prima | `655` | ri | ri | Agrees |
| P2-R02 | H37 | prima | `1102` | g ; gg  | g ; gg | Agrees |
| P2-R02 | I37 | prima | `042` | st ; Mähr -e -ische | st ; Mähr -e -ische | Agrees |
| P2-R02 | J37 | prima | `5540` | be | be | Agrees |
| P2-R02 | K37 | prima | `096` | schaff -e -n | schaff -e -n | Agrees |
| P2-R02 | L37 | prima | `010` | ti -on | ti -on | Agrees |
| P2-R02 | M37 | prima | `7775` | ge -t -n | ge -t -n | Agrees |
| P2-R02 | N37 | prima | `025` | Comma | , | Agrees |
| P2-R02 | O37 | prima | `1113` | und | und | Agrees |
| P2-R03 | A42 | prima | `663` | ist | ist | Agrees |
| P2-R03 | B42 | prima | `7799` | sich | sich | Agrees |
| P2-R03 | C42 | prima | `001` | von | von | Agrees |
| P2-R03 | D42 | prima | `099` | sein -e -m -r -s | sein -e -m -r -s | Agrees |
| P2-R03 | E42 | prima | `5592` | sich | sich | Agrees |
| P2-R03 | F42 | prima | `7760` | hie -r | hie -r | Agrees |
| P2-R03 | G42 | prima | `880` | in | in | Agrees |
| P2-R03 | H42 | prima | `5584` | falle -t -n | falle -t -n | Agrees |
| P2-R03 | I42 | prima | `226` | s; ss | s; ss | Agrees |
| P2-R03 | J42 | prima | `3362` | geb -e/-n -t | geb -e/-n -t | Agrees |
| P2-R03 | K42 | prima | `667` | den -en | den -en | Agrees |
| P2-R03 | L42 | prima | `9931` | be | be | Agrees |
| P2-R03 | M42 | prima | `5582` | mü | mü | Agrees |
| P2-R03 | N42 | prima | `7723` | hu ; gering | hu ; gering | Agrees |
| P2-R04 | A47 | prima | `1157` | ng -e/ -n -t | ng -e/ -n -t | Agrees |
| P2-R04 | B47 | prima | `460` | all -e/-r -n -s | all -e/-r -n -s | Agrees |
| P2-R04 | C47 | prima | `3365` | an | an | Agrees |
| P2-R04 | D47 | prima | `3331` | t ; tt ; seh -e/-n -t  | t ; tt ; seh -e/-n -t | Agrees |
| P2-R04 | E47 | prima | `223` | nach -t -er | nach -t -er | Agrees |
| P2-R04 | F47 | prima | `070` | ein -e/ -n/-m -s | ein -e/ -n/-m -s | Agrees |
| P2-R04 | G47 | prima | `3368` | gut -e/-r -n -s | gut -e/-r -n -s | Agrees |
| P2-R04 | H47 | prima | `1107` | würck -lich | würck -lich | Agrees |
| P2-R04 | I47 | prima | `832` | ung -en | ung -en | Agrees |
| P2-R04 | J47 | prima | `446` | zu ; zuzu  | zu ; zuzu | Agrees |
| P2-R04 | K47 | prima | `013` | ver | ver | Agrees |
| P2-R04 | L47 | prima | `681` | spr | spr | Agrees |
| P2-R04 | M47 | prima | `017` | ech -e/-r -t | ech -e/-r -t | Agrees |
| P2-R04 | N47 | prima | `1158` | punctum | . | Agrees |
| P2-R04 | O47 | prima | `437` | er -s  | er -s | Agrees |
| P2-R05 | A52 | prima | `040` | wie | wie | Agrees |
| P2-R05 | B52 | prima | `020` | der -en | der -en | Agrees |
| P2-R05 | C52 | prima | `9919` | ho | ho | Agrees |
| P2-R05 | D52 | prima | `5512` | h ;  h / dein -e/-n | [provisional: h ;  h / dein -e/-n] | Provisional |
| P2-R05 | E52 | prima | `613` | le -t/-n -s | le -t/-n -s | Agrees |
| P2-R05 | F52 | prima | `830` | mir | mir | Agrees |
| P2-R05 | G52 | prima | `042` | st ; Mähr -e -ische | st ; Mähr -e -ische | Agrees |
| P2-R05 | H52 | prima | `676` | a ; ä | a ; ä | Agrees |
| P2-R05 | I52 | prima | `226` | s; ss | s; ss | Agrees |
| P2-R05 | J52 | prima | `007` | die | die | Agrees |
| P2-R05 | K52 | prima | `013` | ver | ver | Agrees |
| P2-R05 | L52 | prima | `897` | tro | tro | Agrees |
| P2-R05 | M52 | prima | `042` | st ; Mähr -e -ische | st ; Mähr -e -ische | Agrees |
| P2-R05 | N52 | prima | `832` | ung -en | ung -en | Agrees |
| P2-R05 | O52 | prima | `494` | Comma | , | Agrees |
| P2-R05 | P52 | prima | `002` | daß | daß | Agrees |
| P2-R06 | A57 | prima | `220` | das | das | Agrees |
| P2-R06 | B57 | prima | `021` | so | so | Agrees |
| P2-R06 | C57 | prima | `409` | u ; Churfürst -in/-en | u ; Churfürst -in/-en | Agrees |
| P2-R06 | D57 | prima | `7752` | bi | bi | Agrees |
| P2-R06 | E57 | prima | `899` | si | si | Agrees |
| P2-R06 | F57 | prima | `085` | sche -r/-n -s | sche -r/-n -s | Agrees |
| P2-R06 | G57 | prima | `7784` | Corp -o/-s | Corp -o/-s | Agrees |
| P2-R06 | H57 | prima | `420` | ohn -e | ohn -e | Agrees |
| P2-R06 | I57 | prima | `805` | fehl -t/-e -r/-n | fehl -t/-e -r/-n | Agrees |
| P2-R06 | J57 | prima | `216` | bar | bar | Agrees |
| P2-R06 | K57 | prima | `880` | in | in | Agrees |
| P2-R06 | L57 | prima | `7720` | dem | dem | Agrees |
| P2-R06 | M57 | prima | `1162` | Monat -lich | Monat -lich | Agrees |
| P2-R06 | N57 | prima | `7749` | Julius | Julius | Agrees |
| P2-R07 | A62 | prima | `880` | in | in | Agrees |
| P2-R07 | B62 | prima | `1118` | r ; rr ; Böhm -en -ische | r ; rr ; Böhm -en -ische | Agrees |
| P2-R07 | C62 | prima | `070` | ein -e/ -n/-m -s | ein -e/ -n/-m -s | Agrees |
| P2-R07 | D62 | prima | `872` | tre | tre | Agrees |
| P2-R07 | E62 | prima | `5547` | fe -r/-n ; r | fe -r/-n ; r | Agrees |
| P2-R07 | F62 | prima | `7770` | werde -n -t | werde -n -t | Agrees |
| P2-R07 | G62 | prima | `025` | Comma | , | Agrees |
| P2-R07 | H62 | prima | `460` | all -e/-r -n -s | all -e/-r -n -s | Agrees |
| P2-R07 | I62 | prima | `090` | ein -e/ -n/-m -s | ein -e/ -n/-m -s | Agrees |
| P2-R07 | J62 | prima | `666` | ich -e/ -n | ich -e/ -n | Agrees |
| P2-R07 | K62 | prima | `7777` | ge -gen | ge -gen | Agrees |
| P2-R07 | L62 | prima | `9903` | trau -e/-n -t -lich | trau -e/-n -t -lich | Agrees |
| P2-R07 | M62 | prima | `830` | mir | mir | Agrees |
| P2-R07 | N62 | prima | `873` | noch | noch | Agrees |
| P2-R07 | O62 | prima | `886` | nicht -s | nicht -s | Agrees |
| P2-R08 | A67 | prima | `7760` | hie -r | hie -r | Agrees |
| P2-R08 | B67 | prima | `482` | auf | auf | Agrees |
| P2-R08 | C67 | prima | `1166` | voll -macht -ig | voll -macht -ig | Agrees |
| P2-R08 | D67 | prima | `9963` | komme -t/ -n | komme -t/ -n | Agrees |
| P2-R08 | E67 | prima | `008` | zu ; zuzu  | zu ; zuzu | Agrees |
| P2-R08 | F67 | prima | `831` | ze -t/ -n | ze -t/ -n | Agrees |
| P2-R08 | G67 | prima | `5512` | h ;  h / dein -e/-n | [provisional: h ;  h / dein -e/-n] | Provisional |
| P2-R08 | H67 | prima | `613` | le -t/-n -s | le -t/-n -s | Agrees |
| P2-R08 | I67 | prima | `3391` | Comma | , | Agrees |
| P2-R08 | J67 | prima | `244` | da | da | Agrees |
| P2-R08 | K67 | prima | `830` | mir | mir | Agrees |
| P2-R08 | L67 | prima | `889` | aus | aus | Agrees |
| P2-R08 | M67 | prima | `020` | der -en | der -en | Agrees |
| P2-R08 | N67 | prima | `5564` | bis | bis | Agrees |
| P2-R08 | O67 | prima | `3375` | 90 ; he -t/ -n | 90 ; he -t/ -n | Agrees |
| P2-R09 | A72 | prima | `655` | ri | ri | Agrees |
| P2-R09 | B72 | prima | `7775` | ge -t -n | ge -t -n | Agrees |
| P2-R09 | C72 | prima | `1144` | er -s  | er -s | Agrees |
| P2-R09 | D72 | prima | `7762` | fa | fa | Agrees |
| P2-R09 | E72 | prima | `5512` | h ;  h / dein -e/-n | [provisional: h ;  h / dein -e/-n] | Provisional |
| P2-R09 | F72 | prima | `1118` | r ; rr ; Böhm -en -ische | r ; rr ; Böhm -en -ische | Agrees |
| P2-R09 | G72 | prima | `832` | ung -en | ung -en | Agrees |
| P2-R09 | H72 | prima | `7700` | nur | nur | Agrees |
| P2-R09 | I72 | prima | `1140` | gar | gar | Agrees |
| P2-R09 | J72 | prima | `446` | zu ; zuzu  | zu ; zuzu | Agrees |
| P2-R09 | K72 | prima | `698` | wohl | wohl | Agrees |
| P2-R09 | L72 | prima | `5540` | be | be | Agrees |
| P2-R09 | M72 | prima | `1109` | kan | kan | Agrees |
| P2-R10 | A77 | prima | `7766` | nt -e/-r -n/-s -t | nt -e/-r -n/-s -t | Agrees |
| P2-R10 | B77 | prima | `040` | wie | wie | Agrees |
| P2-R10 | C77 | prima | `231` | wen -ig/ -er -s | wen -ig/ -er -s | Agrees |
| P2-R10 | D77 | prima | `482` | auf | auf | Agrees |
| P2-R10 | E77 | prima | `020` | der -en | der -en | Agrees |
| P2-R10 | F77 | prima | `623` | gleich | gleich | Agrees |
| P2-R10 | G77 | prima | `022` | en | en | Agrees |
| P2-R10 | H77 | prima | `217` | mi | mi | Agrees |
| P2-R10 | I77 | prima | `1165` | li -gs ; Firmian | li -gs ; Firmian | Agrees |
| P2-R10 | J77 | prima | `1104` | ta | ta | Agrees |
| P2-R10 | K77 | prima | `655` | ri | ri | Agrees |
| P2-R10 | L77 | prima | `085` | sche -r/-n -s | sche -r/-n -s | Agrees |
| P2-R10 | M77 | prima | `670` | ma -s | ma -s | Agrees |
| P2-R10 | N77 | prima | `641` | nehm -e/-n -t | nehm -e/-n -t | Agrees |
| P2-R10 | O77 | prima | `832` | ung -en | ung -en | Agrees |
| P2-R10 | P77 | prima | `446` | zu ; zuzu  | zu ; zuzu | Agrees |
| P2-R11 | A82 | prima | `414` | mahl -e/ -n -s | mahl -e/ -n -s | Agrees |
| P2-R11 | B82 | prima | `640` | wan | wan | Agrees |
| P2-R11 | C82 | prima | `211` | sie | sie | Agrees |
| P2-R11 | D82 | prima | `482` | auf | auf | Agrees |
| P2-R11 | E82 | prima | `070` | ein -e/ -n/-m -s | ein -e/ -n/-m -s | Agrees |
| P2-R11 | F82 | prima | `1119` | et | et | Agrees |
| P2-R11 | G82 | prima | `054` | was | was | Agrees |
| P2-R11 | H82 | prima | `022` | en | en | Agrees |
| P2-R11 | I82 | prima | `445` | t ; tt   | t ; tt | Agrees |
| P2-R11 | J82 | prima | `5547` | fe -r/-n ; r | fe -r/-n ; r | Agrees |
| P2-R11 | K82 | prima | `1118` | r ; rr ; Böhm -en -ische | r ; rr ; Böhm -en -ische | Agrees |
| P2-R11 | L82 | prima | `881` | ne -r/-n ; 9 | ne -r/-n ; 9 | Agrees |
| P2-R11 | M82 | prima | `1115` | te -r/-n ; t | te -r/-n ; t | Agrees |
| P2-R11 | N82 | prima | `646` | zeit -en/ -lich | zeit -en/ -lich | Agrees |
| P2-R11 | O82 | prima | `1189` | punct -en | punct -en | Agrees |
| P2-R11 | P82 | prima | `7775` | ge -t -n | ge -t -n | Agrees |
| P2-R12 | A87 | prima | `068` | richt -e/-n -t -ig | richt -e/-n -t -ig | Agrees |
| P2-R12 | B87 | prima | `899` | si | si | Agrees |
| P2-R12 | C87 | prima | `206` | nd | nd | Agrees |
| P2-R12 | D87 | prima | `7799` | sich | sich | Agrees |
| P2-R12 | E87 | prima | `643` | mit | mit | Agrees |
| P2-R12 | F87 | prima | `667` | den -en | den -en | Agrees |
| P2-R12 | G87 | prima | `275` | hiesig -e/-r -n -s | hiesig -e/-r -n -s | Agrees |
| P2-R12 | H87 | prima | `613` | le -t/-n -s | le -t/-n -s | Agrees |
| P2-R12 | I87 | prima | `409` | u ; Churfürst -in/-en | u ; Churfürst -in/-en | Agrees |
| P2-R12 | J87 | prima | `662` | te -r/-n -t -s | te -r/-n -t -s | Agrees |
| P2-R12 | K87 | prima | `446` | zu ; zuzu  | zu ; zuzu | Agrees |
| P2-R12 | L87 | prima | `013` | ver | ver | Agrees |
| P2-R12 | M87 | prima | `7727` | laß -e/-n -t -lich | laß -e/-n -t -lich | Agrees |
| P2-R12 | N87 | prima | `400` | sey -e/-n -d | sey -e/-n -d | Agrees |
| P2-R12 | O87 | prima | `297` | punctum | . | Agrees |
| P2-R13 | A92 | prima | `065` | - | ∅ | Agrees |
| P2-R13 | B92 | prima | `219` | ab | ab | Agrees |
| P2-R13 | C92 | prima | `9931` | be | be | Agrees |
| P2-R13 | D92 | prima | `645` | de | de | Agrees |
| P2-R13 | E92 | prima | `1146` | ber -g | ber -g | Agrees |
| P2-R13 | F92 | prima | `3370` | ni -e | ni -e | Agrees |
| P2-R13 | G92 | prima | `226` | s; ss | s; ss | Agrees |
| P2-R13 | H92 | prima | `211` | sie | sie | Agrees |
| P2-R13 | I92 | prima | `3375` | 90 ; he -t/ -n | 90 ; he -t/ -n | Agrees |
| P2-R13 | J92 | prima | `460` | all -e/-r -n -s | all -e/-r -n -s | Agrees |
| P2-R13 | K92 | prima | `220` | das | das | Agrees |
| P2-R13 | L92 | prima | `267` | jen -e/-r -n -s | jen -e/-r -n -s | Agrees |
| P2-R13 | M92 | prima | `7773` | ige -r/n -d -s | ige -r/n -d -s | Agrees |
| P2-R13 | N92 | prima | `021` | so | so | Agrees |
| P2-R13 | O92 | prima | `058` | Monsieur | Monsieur | Agrees |
| P2-R14 | A97 | prima | `7740` | du | du | Agrees |
| P2-R14 | B97 | prima | `3348` | ra | ra | Agrees |
| P2-R14 | C97 | prima | `206` | nd | nd | Agrees |
| P2-R14 | D97 | prima | `001` | von | von | Agrees |
| P2-R14 | E97 | prima | `667` | den -en | den -en | Agrees |
| P2-R14 | F97 | prima | `064` | zwischen | zwischen | Agrees |
| P2-R14 | G97 | prima | `7720` | dem | dem | Agrees |
| P2-R14 | H97 | prima | `868` | Graf -in/-en | Graf -in/-en | Agrees |
| P2-R14 | I97 | prima | `5537` | Brühl | Brühl | Agrees |
| P2-R14 | J97 | prima | `1113` | und | und | Agrees |
| P2-R14 | K97 | prima | `5519` | dem | dem | Agrees |
| P2-R14 | L97 | prima | `836` | abge | abge | Agrees |
| P2-R14 | M97 | prima | `1100` | se -t -n | se -t -n | Agrees |
| P2-R14 | N97 | prima | `654` | z ; unzu | z ; unzu | Agrees |
| P2-R15 | A102 | prima | `1115` | te -r/-n ; t | te -r/-n ; t | Agrees |
| P2-R15 | B102 | prima | `3392` | Rußland -ische | Rußland -ische | Agrees |
| P2-R15 | C102 | prima | `266` | groß -te/-r -n -s | groß -te/-r -n -s | Agrees |
| P2-R15 | D102 | prima | `230` | Canzl -e/-r -ey | Canzl -e/-r -ey | Agrees |
| P2-R15 | E102 | prima | `5553` | ge ; gege | ge ; gege | Agrees |
| P2-R15 | F102 | prima | `7701` | st | st | Agrees |
| P2-R15 | G102 | prima | `5575` | in? | [provisional: in?] | Provisional |
| P2-R15 | H102 | prima | `1127` | l ; ll | l ; ll | Agrees |
| P2-R15 | I102 | prima | `662` | te -r/-n -t -s | te -r/-n -t -s | Agrees |
| P2-R15 | J102 | prima | `880` | in | in | Agrees |
| P2-R15 | K102 | prima | `9973` | tri | tri | Agrees |
| P2-R15 | L102 | prima | `617` | gu | gu | Agrees |
| P2-R15 | M102 | prima | `022` | en | en | Agrees |
| P2-R15 | N102 | prima | `070` | ein -e/ -n/-m -s | ein -e/ -n/-m -s | Agrees |
| P2-R16 | A107 | prima | `250` | [bericht -et] | [provisional: [bericht -et]] | Provisional |
| P2-R16 | B107 | prima | `269` | als -o | als -o | Agrees |
| P2-R16 | C107 | prima | `9917` | gewiß -lich -e | gewiß -lich -e | Agrees |
| P2-R16 | D107 | prima | `5557` | und | und | Agrees |
| P2-R16 | E107 | prima | `026` | ganz -lich | ganz -lich | Agrees |
| P2-R16 | F107 | prima | `013` | ver | ver | Agrees |
| P2-R16 | G107 | prima | `7727` | laß -e/-n -t -lich | laß -e/-n -t -lich | Agrees |
| P2-R16 | H107 | prima | `7773` | ige -r/n -d -s | ige -r/n -d -s | Agrees |
| P2-R16 | I107 | prima | `657` | wahr -heit | wahr -heit | Agrees |
| P2-R16 | J107 | prima | `022` | en | en | Agrees |
| P2-R16 | K107 | prima | `208` | an -?n | [provisional: an -?n] | Provisional |
| P2-R16 | L107 | prima | `079` | media nota | ; | Agrees |
| P2-R16 | M107 | prima | `666` | ich -e/ -n | ich -e/ -n | Agrees |
| P2-R16 | N107 | prima | `013` | ver | ver | Agrees |
| P2-R17 | A112 | prima | `039` | muth -e/-n -lich | muth -e/-n -lich | Agrees |
| P2-R17 | B112 | prima | `002` | daß | daß | Agrees |
| P2-R17 | C112 | prima | `868` | Graf -in/-en | Graf -in/-en | Agrees |
| P2-R17 | D112 | prima | `1176` | br ; Manheim | br ; Manheim | Agrees |
| P2-R17 | E112 | prima | `1103` | o / lig -e/-r -n -t -s | o / lig -e/-r -n -t -s | Agrees |
| P2-R17 | F112 | prima | `1102` | g ; gg  | g ; gg | Agrees |
| P2-R17 | G112 | prima | `1165` | li -gs ; Firmian | li -gs ; Firmian | Agrees |
| P2-R17 | H112 | prima | `005` | e ; meld -en/-ung | e ; meld -en/-ung | Agrees |
| P2-R17 | I112 | prima | `025` | Comma | , | Agrees |
| P2-R17 | J112 | prima | `020` | der -en | der -en | Agrees |
| P2-R17 | K112 | prima | `040` | wie | wie | Agrees |
| P2-R17 | L112 | prima | `030` | es | es | Agrees |
| P2-R17 | M112 | prima | `830` | mir | mir | Agrees |
| P2-R17 | N112 | prima | `085` | sche -r/-n -s | sche -r/-n -s | Agrees |
| P2-R17 | O112 | prima | `880` | in | in | Agrees |
| P2-R17 | P112 | prima | `1119` | et | et | Agrees |
| P2-R18 | A117 | prima | `262` | Comma | , | Agrees |
| P2-R18 | B117 | prima | `7725` | me -r/-n -t -s  | me -r/-n -t -s | Agrees |
| P2-R18 | C117 | prima | `5512` | h ;  h / dein -e/-n | [provisional: h ;  h / dein -e/-n] | Provisional |
| P2-R18 | D117 | prima | `015` | re -s/-n -t -r | re -s/-n -t -r | Agrees |
| P2-R18 | E117 | prima | `024` | es -en | es -en | Agrees |
| P2-R18 | F117 | prima | `7775` | ge -t -n | ge -t -n | Agrees |
| P2-R18 | G117 | prima | `5512` | h ;  h / dein -e/-n | [provisional: h ;  h / dein -e/-n] | Provisional |
| P2-R18 | H117 | prima | `7742` | sto ; oe ; ö | sto ; oe ; ö | Agrees |
| P2-R18 | I117 | prima | `1118` | r ; rr ; Böhm -en -ische | r ; rr ; Böhm -en -ische | Agrees |
| P2-R18 | J117 | prima | `7772` | bey | bey | Agrees |
| P2-R18 | K117 | prima | `9995` | ge -t/ -n | ge -t/ -n | Agrees |
| P2-R18 | L117 | prima | `244` | da | da | Agrees |
| P2-R18 | M117 | prima | `5568` | che -r/-n -s | che -r/-n -s | Agrees |
| P2-R19 | A122 | prima | `061` | te -r/-n -t -s | te -r/-n -t -s | Agrees |
| P2-R19 | B122 | prima | `219` | ab | ab | Agrees |
| P2-R19 | C122 | prima | `9931` | be | be | Agrees |
| P2-R19 | D122 | prima | `645` | de | de | Agrees |
| P2-R19 | E122 | prima | `1146` | ber -g | ber -g | Agrees |
| P2-R19 | F122 | prima | `473` | ni -e | ni -e | Agrees |
| P2-R19 | G122 | prima | `226` | s; ss | s; ss | Agrees |
| P2-R19 | H122 | prima | `819` | finde -t -n | finde -t -n | Agrees |
| P2-R19 | I122 | prima | `269` | als -o | als -o | Agrees |
| P2-R19 | J122 | prima | `014` | man -n | man -n | Agrees |
| P2-R19 | K122 | prima | `030` | es | es | Agrees |
| P2-R19 | L122 | prima | `698` | wohl | wohl | Agrees |
| P2-R19 | M122 | prima | `7755` | hätte -n | hätte -n | Agrees |
| P2-R19 | N122 | prima | `835` | glaub -e/-n -t -lich | glaub -e/-n -t -lich | Agrees |
| P2-R19 | O122 | prima | `038` | solle -t/ -n | solle -t/ -n | Agrees |
| P2-R20 | A127 | prima | `262` | Comma | , | Agrees |
| P2-R20 | B127 | prima | `220` | das | das | Agrees |
| P2-R20 | C127 | prima | `862` | vorge | vorge | Agrees |
| P2-R20 | D127 | prima | `3349` | ben | ben | Agrees |
| P2-R20 | E127 | prima | `5528` | deß -sen | deß -sen | Agrees |
| P2-R20 | F127 | prima | `7740` | du | du | Agrees |
| P2-R20 | G127 | prima | `622` | ra | ra | Agrees |
| P2-R20 | H127 | prima | `206` | nd | nd | Agrees |
| P2-R20 | I127 | prima | `072` | krä -fft | krä -fft | Agrees |
| P2-R20 | J127 | prima | `7773` | ige -r/n -d -s | ige -r/n -d -s | Agrees |
| P2-R20 | K127 | prima | `042` | st ; Mähr -e -ische | st ; Mähr -e -ische | Agrees |
| P2-R20 | L127 | prima | `087` | unter | unter | Agrees |
| P2-R20 | M127 | prima | `233` | stü -ck | stü -ck | Agrees |
| P2-R20 | N127 | prima | `831` | ze -t/ -n | ze -t/ -n | Agrees |
| P2-R21 | A132 | prima | `1113` | und | und | Agrees |
| P2-R21 | B132 | prima | `099` | sein -e -m -r -s | sein -e -m -r -s | Agrees |
| P2-R21 | C132 | prima | `1155` | mög-lich -e/-n -r -s | mög-lich -e/-n -r -s | Agrees |
| P2-R21 | D132 | prima | `049` | [ste] | [provisional: [ste]] | Provisional |
| P2-R21 | E132 | prima | `888` | s ; ss  | s ; ss | Agrees |
| P2-R21 | F132 | prima | `603` | thu -en/n – lich | thu -en/n – lich | Agrees |
| P2-R21 | G132 | prima | `7770` | werde -n -t | werde -n -t | Agrees |
| P2-R21 | H132 | prima | `811` | um | um | Agrees |
| P2-R21 | I132 | prima | `667` | den -en | den -en | Agrees |
| P2-R21 | J132 | prima | `7796` | hiesige -r/-n hof-es | hiesige -r/-n hof-es | Agrees |
| P2-R21 | K132 | prima | `5522` | dahin | dahin | Agrees |
| P2-R21 | L132 | prima | `008` | zu ; zuzu  | zu ; zuzu | Agrees |
| P2-R21 | M132 | prima | `5540` | be | be | Agrees |
| P2-R21 | N132 | prima | `9989` | weg -en | weg -en | Agrees |
| P2-R21 | O132 | prima | `262` | Comma | , | Agrees |
| P3-R01 | A137 | prima | `002` | daß | daß | Agrees |
| P3-R01 | B137 | prima | `020` | der -en | der -en | Agrees |
| P3-R01 | C137 | prima | `5500` | selb -e/-ige -r/-n -m -s  | selb -e/-ige -r/-n -m -s | Agrees |
| P3-R01 | D137 | prima | `667` | den -en | den -en | Agrees |
| P3-R01 | E137 | prima | `868` | Graf -in/-en | Graf -in/-en | Agrees |
| P3-R01 | F137 | prima | `5537` | Brühl | Brühl | Agrees |
| P3-R01 | G137 | prima | `7772` | bey | bey | Agrees |
| P3-R01 | H137 | prima | `066` | sein -e/-r -n -s | sein -e/-r -n -s | Agrees |
| P3-R01 | I137 | prima | `5588` | König -in -s | König -in -s | Agrees |
| P3-R01 | J137 | prima | `013` | ver | ver | Agrees |
| P3-R01 | K137 | prima | `244` | da | da | Agrees |
| P3-R01 | L137 | prima | `450` | [cht] | [provisional: [cht]] | Provisional |
| P3-R01 | M137 | prima | `010` | ti -on | ti -on | Agrees |
| P3-R01 | N137 | prima | `1102` | g ; gg  | g ; gg | Agrees |
| P3-R01 | O137 | prima | `446` | zu ; zuzu  | zu ; zuzu | Agrees |
| P3-R02 | A142 | prima | `405` | mach -e -n | mach -e -n | Agrees |
| P3-R02 | B142 | prima | `1113` | und | und | Agrees |
| P3-R02 | C142 | prima | `489` | ihn -en | ihn -en | Agrees |
| P3-R02 | D142 | prima | `026` | ganz -lich | ganz -lich | Agrees |
| P3-R02 | E142 | prima | `055` | zu ; zuzu  | zu ; zuzu | Agrees |
| P3-R02 | F142 | prima | `233` | stü -ck | stü -ck | Agrees |
| P3-R02 | G142 | prima | `1118` | r ; rr ; Böhm -en -ische | r ; rr ; Böhm -en -ische | Agrees |
| P3-R02 | H142 | prima | `831` | ze -t/ -n | ze -t/ -n | Agrees |
| P3-R02 | I142 | prima | `802` | su | su | Agrees |
| P3-R02 | J142 | prima | `5568` | che -r/-n -s | che -r/-n -s | Agrees |
| P3-R02 | K142 | prima | `1155` | mög-lich -e/-n -r -s | mög-lich -e/-n -r -s | Agrees |
| P3-R02 | L142 | prima | `1158` | punctum | . | Agrees |
| P3-R02 | M142 | prima | `412` | indic. clav. 2dam | → secunda | Agrees |
| P3-R02 | N142 | secunda | `929` | graf -en/ -in -s | graf -en/ -in -s | Agrees |
| P3-R02 | O142 | secunda | `2275` | st ; würde -n | st ; würde -n | Agrees |
| P3-R02 | P142 | secunda | `112` | a ; Prinz Carl | a ; Prinz Carl | Agrees |
| P3-R03 | A147 | secunda | `122` | in | in | Agrees |
| P3-R03 | B147 | secunda | `153` | vi | vi | Agrees |
| P3-R03 | C147 | secunda | `946` | l ; ll | l ; ll | Agrees |
| P3-R03 | D147 | secunda | `155` | e ; Mr NN | e ; Mr NN | Agrees |
| P3-R03 | E147 | secunda | `703` | rath -e/ -n -t -s | rath -e/ -n -t -s | Agrees |
| P3-R03 | F147 | secunda | `8853` | selbst -en | selbst -en | Agrees |
| P3-R03 | G147 | secunda | `122` | in | in | Agrees |
| P3-R03 | H147 | secunda | `550` | [ein -e/-n -m -s] | [provisional: [ein -e/-n -m -s]] | Provisional |
| P3-R03 | I147 | secunda | `988` | ei | ei | Agrees |
| P3-R03 | J147 | secunda | `344` | ge -t/ -n | ge -t/ -n | Agrees |
| P3-R03 | K147 | secunda | `328` | hand -len/-lung -en | hand -len/-lung -en | Agrees |
| P3-R03 | L147 | secunda | `100` | ich -e/-r -n -s | ich -e/-r -n -s | Agrees |
| P3-R03 | M147 | secunda | `2202` | schreib -e/ -n -t | schreib -e/ -n -t | Agrees |
| P3-R03 | N147 | secunda | `331` | an | an | Agrees |
| P3-R03 | O147 | secunda | `775` | den -en | den -en | Agrees |
| P3-R03 | P147 | secunda | `101` | ab ; Mme Pompadour(?) | [provisional: ab ; Mme Pompadour(?)] | Provisional |
| P3-R03 | Q147 | secunda | `533` | be | be | Agrees |
| P3-R04 | A152 | secunda | `005` | de | de | Agrees |
| P3-R04 | B152 | secunda | `714` | ber -g | ber -g | Agrees |
| P3-R04 | C152 | secunda | `771` | ni -e | ni -e | Agrees |
| P3-R04 | D152 | secunda | `336` | s ; ss ; Vortrag | s ; ss ; Vortrag | Agrees |
| P3-R04 | E152 | secunda | `141` | Comma | , | Agrees |
| P3-R04 | F152 | secunda | `2273` | c ; wor | c ; wor | Agrees |
| P3-R04 | G152 | secunda | `770` | von | von | Agrees |
| P3-R04 | H152 | secunda | `113` | dies -e/-r -n -s | dies -e/-r -n -s | Agrees |
| P3-R04 | I152 | secunda | `095` | Minis -tre/teri -o -s -um | Minis -tre/teri -o -s -um | Agrees |
| P3-R04 | J152 | secunda | `199` | mir | mir | Agrees |
| P3-R04 | K152 | secunda | `550` | [ein -e/-n -m -s] | [provisional: [ein -e/-n -m -s]] | Provisional |
| P3-R04 | L152 | secunda | `519` | theil -e/ -n -s | theil -e/ -n -s | Agrees |
| P3-R04 | M152 | secunda | `394` | vorge | vorge | Agrees |
| P3-R04 | N152 | secunda | `024` | le -t -n -s | le -t -n -s | Agrees |
| P3-R04 | O152 | secunda | `2239` | sen | sen | Agrees |
| P3-R04 | P152 | secunda | `029` | Comma | , | Agrees |
| P3-R05 | A157 | secunda | `357` | hie -r | hie -r | Agrees |
| P3-R05 | B157 | secunda | `566` | zu ; zuzu | zu ; zuzu | Agrees |
| P3-R05 | C157 | secunda | `550` | [ein -e/-n -m -s] | [provisional: [ein -e/-n -m -s]] | Provisional |
| P3-R05 | D157 | secunda | `8835` | Erz -haus | Erz -haus | Agrees |
| P3-R05 | E157 | secunda | `500` | und | und | Agrees |
| P3-R05 | F157 | secunda | `111` | bin | bin | Agrees |
| P3-R05 | G157 | secunda | `002` | ich -e -n | ich -e -n | Agrees |
| P3-R05 | H157 | secunda | `316` | dar | dar | Agrees |
| P3-R05 | I157 | secunda | `502` | über -ig/ -e -n -s | über -ig/ -e -n -s | Agrees |
| P3-R05 | J157 | secunda | `370` | um | um | Agrees |
| P3-R05 | K157 | secunda | `571` | so | so | Agrees |
| P3-R05 | L157 | secunda | `301` | q ; me | q ; me | Agrees |
| P3-R05 | M157 | secunda | `016` | h ; Holdernes | h ; Holdernes | Agrees |
| P3-R05 | N157 | secunda | `755` | r ; rr | r ; rr | Agrees |
| P3-R05 | O157 | secunda | `057` | ver | ver | Agrees |
| P3-R05 | P157 | secunda | `176` | wu | wu | Agrees |
| P3-R06 | A162 | secunda | `114` | nd ; Graf Puebla | nd ; Graf Puebla | Agrees |
| P3-R06 | B162 | secunda | `050` | [er] | [provisional: [er]] | Provisional |
| P3-R06 | C162 | secunda | `558` | t ; tt | t ; tt | Agrees |
| P3-R06 | D162 | secunda | `192` | za ; als -o | za ; als -o | Agrees |
| P3-R06 | E162 | secunda | `050` | [er] | [provisional: [er]] | Provisional |
| P3-R06 | F162 | secunda | `146` | im | im | Agrees |
| P3-R06 | G162 | secunda | `4406` | üb ; franck -en | üb ; franck -en | Agrees |
| P3-R06 | H162 | secunda | `084` | ri | ri | Agrees |
| P3-R06 | I162 | secunda | `344` | ge -t/ -n | ge -t/ -n | Agrees |
| P3-R06 | J162 | secunda | `331` | an | an | Agrees |
| P3-R06 | K162 | secunda | `335` | dem | dem | Agrees |
| P3-R06 | L162 | secunda | `4497` | voll -ig/ -macht | voll -ig/ -macht | Agrees |
| P3-R06 | M162 | secunda | `534` | komme -t -n | komme -t -n | Agrees |
| P3-R06 | N162 | secunda | `2244` | en  | en | Agrees |
| P3-R06 | O162 | secunda | `533` | be | be | Agrees |
| P3-R07 | A167 | secunda | `732` | stand/ständ -en | stand/ständ -en | Agrees |
| P3-R07 | B167 | secunda | `8882` | der -en | der -en | Agrees |
| P3-R07 | C167 | secunda | `770` | von | von | Agrees |
| P3-R07 | D167 | secunda | `335` | dem | dem | Agrees |
| P3-R07 | E167 | secunda | `599` | du | du | Agrees |
| P3-R07 | F167 | secunda | `922` | ra | ra | Agrees |
| P3-R07 | G167 | secunda | `114` | nd ; Graf Puebla | nd ; Graf Puebla | Agrees |
| P3-R07 | H167 | secunda | `050` | [er] | [provisional: [er]] | Provisional |
| P3-R07 | I167 | secunda | `519` | theil -e/ -n -s | theil -e/ -n -s | Agrees |
| P3-R07 | J167 | secunda | `4447` | te -r/-n -t -s | te -r/-n -t -s | Agrees |
| P3-R07 | K167 | secunda | `6601` | Nachricht -en | Nachricht -en | Agrees |
| P3-R07 | L167 | secunda | `122` | in | in | Agrees |
| P3-R07 | M167 | secunda | `577` | et | et | Agrees |
| P3-R07 | N167 | secunda | `923` | was | was | Agrees |
| P3-R08 | A172 | secunda | `2233` | zu ; zuzu | zu ; zuzu | Agrees |
| P3-R08 | B172 | secunda | `932` | zweifel -e/-n -t | zweifel -e/-n -t | Agrees |
| P3-R08 | C172 | secunda | `783` | sche -r/-n -t | sche -r/-n -t | Agrees |
| P3-R08 | D172 | secunda | `122` | in | in | Agrees |
| P3-R08 | E172 | secunda | `8877` | et | et | Agrees |
| P3-R08 | F172 | secunda | `353` | Comma | , | Agrees |
| P3-R08 | G172 | secunda | `500` | und | und | Agrees |
| P3-R08 | H172 | secunda | `097` | sich | sich | Agrees |
| P3-R08 | I172 | secunda | `502` | über -ig/ -e -n -s | über -ig/ -e -n -s | Agrees |
| P3-R08 | J172 | secunda | `128` | hau -b/ -t s | hau -b/ -t s | Agrees |
| P3-R08 | K172 | secunda | `160` | dis | dis | Agrees |
| P3-R08 | L172 | secunda | `2246` | fall -e/-n -t | fall -e/-n -t | Agrees |
| P3-R08 | M172 | secunda | `144` | s ; ss ; Rosenberg | s ; ss ; Rosenberg | Agrees |
| P3-R08 | N172 | secunda | `6600` | mit | mit | Agrees |
| P3-R08 | O172 | secunda | `2251` | viel -e/-r -n/-s -leicht | viel -e/-r -n/-s -leicht | Agrees |
| P3-R09 | A177 | secunda | `533` | be | be | Agrees |
| P3-R09 | B177 | secunda | `783` | sche -r/-n -t | sche -r/-n -t | Agrees |
| P3-R09 | C177 | secunda | `010` | i ; Höpken | i ; Höpken | Agrees |
| P3-R09 | D177 | secunda | `775` | den -en | den -en | Agrees |
| P3-R09 | E177 | secunda | `030` | heit | heit | Agrees |
| P3-R09 | F177 | secunda | `188` | aus | aus | Agrees |
| P3-R09 | G177 | secunda | `2272` | ser | ser | Agrees |
| P3-R09 | H177 | secunda | `2292` | et | et | Agrees |
| P3-R09 | I177 | secunda | `2250` | punctum | . | Agrees |
| P3-R09 | J177 | secunda | `777` | das | das | Agrees |
| P3-R09 | K177 | secunda | `057` | ver | ver | Agrees |
| P3-R09 | L177 | secunda | `538` | spr | spr | Agrees |
| P3-R09 | M177 | secunda | `707` | ech -e/-n -t -n | ech -e/-n -t -n | Agrees |
| P3-R09 | N177 | secunda | `155` | e ; Mr NN | e ; Mr NN | Agrees |
| P3-R10 | A182 | secunda | `748` | hi | hi | Agrees |
| P3-R10 | B182 | secunda | `948` | gew | gew | Agrees |
| P3-R10 | C182 | secunda | `303` | tagen -lich (?) | [provisional: tagen -lich (?)] | Provisional |
| P3-R10 | D182 | secunda | `550` | [ein -e/-n -m -s] | [provisional: [ein -e/-n -m -s]] | Provisional |
| P3-R10 | E182 | secunda | `302` | aber | aber | Agrees |
| P3-R10 | F182 | secunda | `109` | mahl -s -en | mahl -s -en | Agrees |
| P3-R10 | G182 | secunda | `044` | ig -e/ -r -n/ -s | ig -e/ -r -n/ -s | Agrees |
| P3-R10 | H182 | secunda | `533` | be | be | Agrees |
| P3-R10 | I182 | secunda | `195` | zahl -e/ -n -t | zahl -e/ -n -t | Agrees |
| P3-R10 | J182 | secunda | `396` | ung -en | ung -en | Agrees |
| P3-R10 | K182 | secunda | `008` | an | an | Agrees |
| P3-R10 | L182 | secunda | `335` | dem | dem | Agrees |
| P3-R10 | M182 | secunda | `947` | su | su | Agrees |
| P3-R10 | N182 | secunda | `4401` | b ; dein -e/-n -s | b ; dein -e/-n -s | Agrees |
| P3-R10 | O182 | secunda | `090` | si | si | Agrees |
| P3-R10 | P182 | secunda | `996` | di | di | Agrees |
| P3-R11 | A187 | secunda | `042` | o ; Kaunitz gr. | o ; Kaunitz gr. | Agrees |
| P3-R11 | B187 | secunda | `355` | zu ; zuzu | zu ; zuzu | Agrees |
| P3-R11 | C187 | secunda | `2244` | en  | en | Agrees |
| P3-R11 | D187 | secunda | `558` | t ; tt | t ; tt | Agrees |
| P3-R11 | E187 | secunda | `567` | richt -e/-n -t -ig | richt -e/-n -t -ig | Agrees |
| P3-R11 | F187 | secunda | `778` | hat | hat | Agrees |
| P3-R11 | G187 | secunda | `199` | mir | mir | Agrees |
| P3-R11 | H187 | secunda | `101` | ab ; Mme Pompadour(?) | [provisional: ab ; Mme Pompadour(?)] | Provisional |
| P3-R11 | I187 | secunda | `533` | be | be | Agrees |
| P3-R11 | J187 | secunda | `005` | de | de | Agrees |
| P3-R11 | K187 | secunda | `714` | ber -g | ber -g | Agrees |
| P3-R11 | L187 | secunda | `771` | ni -e | ni -e | Agrees |
| P3-R11 | M187 | secunda | `336` | s ; ss ; Vortrag | s ; ss ; Vortrag | Agrees |
| P3-R11 | N187 | secunda | `8802` | gänz -lich | gänz -lich | Agrees |
| P3-R12 | A192 | secunda | `731` | neu -lich | neu -lich | Agrees |
| P3-R12 | B192 | secunda | `050` | [er] | [provisional: [er]] | Provisional |
| P3-R12 | C192 | secunda | `388` | lich -e/-r -g -s | lich -e/-r -g -s | Agrees |
| P3-R12 | D192 | secunda | `999` | wie | wie | Agrees |
| P3-R12 | E192 | secunda | `8882` | der -en | der -en | Agrees |
| P3-R12 | F192 | secunda | `069` | ho ; Migazzi gr. | ho ; Migazzi gr. | Agrees |
| P3-R12 | G192 | secunda | `016` | h ; Holdernes | h ; Holdernes | Agrees |
| P3-R12 | H192 | secunda | `024` | le -t -n -s | le -t -n -s | Agrees |
| P3-R12 | I192 | secunda | `141` | Comma | , | Agrees |
| P3-R12 | J192 | secunda | `785` | ob | ob | Agrees |
| P3-R12 | K192 | secunda | `302` | aber | aber | Agrees |
| P3-R12 | L192 | secunda | `717` | damit | damit | Agrees |
| P3-R12 | M192 | secunda | `083` | auch | auch | Agrees |
| P3-R12 | N192 | secunda | `557` | werde -n | werde -n | Agrees |
| P3-R12 | O192 | secunda | `2295` | zuge | zuge | Agrees |
| P3-R12 | P192 | secunda | `505` | halt -e/ -n -t | halt -e/ -n -t | Agrees |
| P3-R12 | Q192 | secunda | `557` | werde -n | werde -n | Agrees |
| P3-R13 | A197 | secunda | `6604` | solch -e/-r -n -s | solch -e/-r -n -s | Agrees |
| P3-R13 | B197 | secunda | `344` | ge -t/ -n | ge -t/ -n | Agrees |
| P3-R13 | C197 | secunda | `6642` | trau -e/-n -t -lich | trau -e/-n -t -lich | Agrees |
| P3-R13 | D197 | secunda | `199` | mir | mir | Agrees |
| P3-R13 | E197 | secunda | `110` | nach -t -er | nach -t -er | Agrees |
| P3-R13 | F197 | secunda | `335` | dem | dem | Agrees |
| P3-R13 | G197 | secunda | `300` | mein -e/-r -n/-m -s | mein -e/-r -n/-m -s | Agrees |
| P3-R13 | H197 | secunda | `160` | dis | dis | Agrees |
| P3-R13 | I197 | secunda | `2246` | fall -e/-n -t | fall -e/-n -t | Agrees |
| P3-R13 | J197 | secunda | `336` | s ; ss ; Vortrag | s ; ss ; Vortrag | Agrees |
| P3-R13 | K197 | secunda | `344` | ge -t/ -n | ge -t/ -n | Agrees |
| P3-R13 | L197 | secunda | `901` | geb -e/ -n -t | geb -e/ -n -t | Agrees |
| P3-R13 | M197 | secunda | `155` | e ; Mr NN | e ; Mr NN | Agrees |
| P3-R13 | N197 | secunda | `057` | ver | ver | Agrees |
| P3-R13 | O197 | secunda | `543` | tro | tro | Agrees |
| P3-R13 | P197 | secunda | `742` | stu -ck | stu -ck | Agrees |
| P3-R13 | Q197 | secunda | `556` | ng -e/-n -t -e/-n -t | ng -e/-n -t -e/-n -t | Agrees |
| P3-R14 | A202 | secunda | `985` | scho -n/-e -t -n | scho -n/-e -t -n | Agrees |
| P3-R14 | B202 | secunda | `571` | so | so | Agrees |
| P3-R14 | C202 | secunda | `960` | oft -e/-r -n -s | oft -e/-r -n -s | Agrees |
| P3-R14 | D202 | secunda | `537` | fehl -e/-r -n -t | fehl -e/-r -n -t | Agrees |
| P3-R14 | E202 | secunda | `344` | ge -t/ -n | ge -t/ -n | Agrees |
| P3-R14 | F202 | secunda | `309` | ch ; schl | ch ; schl | Agrees |
| P3-R14 | G202 | secunda | `350` | ag -e/ -n -t | ag -e/ -n -t | Agrees |
| P3-R14 | H202 | secunda | `022` | habe -n | habe -n | Agrees |
| P3-R14 | I202 | secunda | `119` | nicht -s | nicht -s | Agrees |
| P3-R14 | J202 | secunda | `769` | me -r/-n -t -s | me -r/-n -t -s | Agrees |
| P3-R14 | K202 | secunda | `016` | h ; Holdernes | h ; Holdernes | Agrees |
| P3-R14 | L202 | secunda | `386` | r ; rr ; pro memoria(?) | [provisional: r ; rr ; pro memoria(?)] | Provisional |
| P3-R14 | M202 | secunda | `4444` | zu ; zuzu | zu ; zuzu | Agrees |
| P3-R14 | N202 | secunda | `730` | versicher -en/-t -ung | versicher -en/-t -ung | Agrees |
| P3-R14 | O202 | secunda | `043` | punctum | . | Agrees |
| P3-R14 | P202 | secunda | `002` | ich -e -n | ich -e -n | Agrees |
| P3-R15 | A207 | secunda | `014` | lass -e/-n -t -lich | lass -e/-n -t -lich | Agrees |
| P3-R15 | B207 | secunda | `2262` | es | es | Agrees |
| P3-R15 | C207 | secunda | `300` | mein -e/-r -n/-m -s | mein -e/-r -n/-m -s | Agrees |
| P3-R15 | D207 | secunda | `794` | orth -s | orth -s | Agrees |
| P3-R15 | E207 | secunda | `008` | an | an | Agrees |
| P3-R15 | F207 | secunda | `775` | den -en | den -en | Agrees |
| P3-R15 | G207 | secunda | `070` | un | un | Agrees |
| P3-R15 | H207 | secunda | `994` | auf | auf | Agrees |
| P3-R15 | I207 | secunda | `069` | ho ; Migazzi gr. | ho ; Migazzi gr. | Agrees |
| P3-R15 | J207 | secunda | `386` | r ; rr ; pro memoria(?) | [provisional: r ; rr ; pro memoria(?)] | Provisional |
| P3-R15 | K207 | secunda | `388` | lich -e/-r -g -s | lich -e/-r -g -s | Agrees |
| P3-R15 | L207 | secunda | `500` | und | und | Agrees |
| P3-R15 | M207 | secunda | `988` | ei | ei | Agrees |
| P3-R15 | N207 | secunda | `048` | fe -r/-t -n -r | fe -r/-t -n -r | Agrees |
| P3-R15 | O207 | secunda | `084` | ri | ri | Agrees |
| P3-R15 | P207 | secunda | `501` | g ; gg ; dein -e/-n -t -m | g ; gg ; dein -e/-n -t -m | Agrees |
| P3-R15 | Q207 | secunda | `918` | ste -r/-n -t -s | ste -r/-n -t -s | Agrees |
| P3-R16 | A212 | secunda | `066` | vor | vor | Agrees |
| P3-R16 | B212 | secunda | `918` | ste -r/-n -t -s | ste -r/-n -t -s | Agrees |
| P3-R16 | C212 | secunda | `946` | l ; ll | l ; ll | Agrees |
| P3-R16 | D212 | secunda | `396` | ung -en | ung -en | Agrees |
| P3-R16 | E212 | secunda | `8887` | und | und | Agrees |
| P3-R16 | F212 | secunda | `050` | [er] | [provisional: [er]] | Provisional |
| P3-R16 | G212 | secunda | `122` | in | in | Agrees |
| P3-R16 | H212 | secunda | `8881` | er -s | er -s | Agrees |
| P3-R16 | I212 | secunda | `2234` | a(?) ; ung -en | [provisional: a(?) ; ung -en] | Provisional |
| P3-R16 | J212 | secunda | `8865` | gewiß -lich/ -e | gewiß -lich/ -e | Agrees |
| P3-R16 | K212 | secunda | `119` | nicht -s | nicht -s | Agrees |
| P3-R16 | L212 | secunda | `050` | [er] | [provisional: [er]] | Provisional |
| P3-R16 | M212 | secunda | `329` | wi | wi | Agrees |
| P3-R16 | N212 | secunda | `114` | nd ; Graf Puebla | nd ; Graf Puebla | Agrees |
| P3-R16 | O212 | secunda | `337` | en | en | Agrees |
| P3-R16 | P212 | secunda | `353` | Comma | , | Agrees |
| P3-R17 | A217 | secunda | `500` | und | und | Agrees |
| P3-R17 | B217 | secunda | `2259` | ul ; wolte -t/ -n | ul ; wolte -t/ -n | Agrees |
| P3-R17 | C217 | secunda | `039` | nur | nur | Agrees |
| P3-R17 | D217 | secunda | `6686` | wünsch -e/ -n | wünsch -e/ -n | Agrees |
| P3-R17 | E217 | secunda | `555` | dass | dass | Agrees |
| P3-R17 | F217 | secunda | `083` | auch | auch | Agrees |
| P3-R17 | G217 | secunda | `929` | graf -en/ -in -s | graf -en/ -in -s | Agrees |
| P3-R17 | H217 | secunda | `2275` | st ; würde -n | st ; würde -n | Agrees |
| P3-R17 | I217 | secunda | `112` | a ; Prinz Carl | a ; Prinz Carl | Agrees |
| P3-R17 | J217 | secunda | `122` | in | in | Agrees |
| P3-R17 | K217 | secunda | `153` | vi | vi | Agrees |
| P3-R17 | L217 | secunda | `946` | l ; ll | l ; ll | Agrees |
| P3-R17 | M217 | secunda | `155` | e ; Mr NN | e ; Mr NN | Agrees |
| P3-R17 | N217 | secunda | `333` | die | die | Agrees |
| P3-R17 | O217 | secunda | `2247` | noth -ig/ -wendigkeit | noth -ig/ -wendigkeit | Agrees |
| P3-R17 | P217 | secunda | `6600` | mit | mit | Agrees |
| P3-R18 | A222 | secunda | `775` | den -en | den -en | Agrees |
| P3-R18 | B222 | secunda | `928` | sti -mm | sti -mm | Agrees |
| P3-R18 | C222 | secunda | `121` | pu | pu | Agrees |
| P3-R18 | D222 | secunda | `2274` | li ; würck -e/-n -t -lich | li ; würck -e/-n -t -lich | Agrees |
| P3-R18 | E222 | secunda | `386` | r ; rr ; pro memoria(?) | [provisional: r ; rr ; pro memoria(?)] | Provisional |
| P3-R18 | F222 | secunda | `991` | te -r/-n -t -s | te -r/-n -t -s | Agrees |
| P3-R18 | G222 | secunda | `533` | be | be | Agrees |
| P3-R18 | H222 | secunda | `195` | zahl -e/ -n -t | zahl -e/ -n -t | Agrees |
| P3-R18 | I222 | secunda | `396` | ung -en | ung -en | Agrees |
| P3-R18 | J222 | secunda | `567` | richt -e/-n -t -ig | richt -e/-n -t -ig | Agrees |
| P3-R18 | K222 | secunda | `050` | [er] | [provisional: [er]] | Provisional |
| P3-R18 | L222 | secunda | `192` | za ; als -o | za ; als -o | Agrees |
| P3-R18 | M222 | secunda | `116` | bis | bis | Agrees |
| P3-R18 | N222 | secunda | `168` | he -t/ -n | he -t/ -n | Agrees |
| P3-R18 | O222 | secunda | `032` | ro | ro | Agrees |
| P3-R18 | P222 | secunda | `344` | ge -t/ -n | ge -t/ -n | Agrees |
| P3-R18 | Q222 | secunda | `783` | sche -r/-n -t | sche -r/-n -t | Agrees |
| P3-R19 | A227 | secunda | `168` | he -t/ -n | he -t/ -n | Agrees |
| P3-R19 | B227 | secunda | `355` | zu ; zuzu | zu ; zuzu | Agrees |
| P3-R19 | C227 | secunda | `566` | zu ; zuzu | zu ; zuzu | Agrees |
| P3-R19 | D227 | secunda | `505` | halt -e/ -n -t | halt -e/ -n -t | Agrees |
| P3-R19 | E227 | secunda | `133` | bey | bey | Agrees |
| P3-R19 | F227 | secunda | `074` | sein -e/-r -n/-s -m | sein -e/-r -n/-s -m | Agrees |
| P3-R19 | G227 | secunda | `055` | hof -fe -t/ -n | hof -fe -t/ -n | Agrees |
| P3-R19 | H227 | secunda | `146` | im | im | Agrees |
| P3-R19 | I227 | secunda | `769` | me -r/-n -t -s | me -r/-n -t -s | Agrees |
| P3-R19 | J227 | secunda | `4444` | zu ; zuzu | zu ; zuzu | Agrees |
| P3-R19 | K227 | secunda | `122` | in | in | Agrees |
| P3-R19 | L227 | secunda | `066` | vor | vor | Agrees |
| P3-R19 | M227 | secunda | `918` | ste -r/-n -t -s | ste -r/-n -t -s | Agrees |
| P3-R19 | N227 | secunda | `946` | l ; ll | l ; ll | Agrees |
| P3-R19 | O227 | secunda | `2234` | a(?) ; ung -en | [provisional: a(?) ; ung -en] | Provisional |
| P3-R19 | P227 | secunda | `974` | bri | bri | Agrees |
| P3-R20 | A232 | secunda | `556` | ng -e/-n -t -e/-n -t | ng -e/-n -t -e/-n -t | Agrees |
| P3-R20 | B232 | secunda | `903` | mo | mo | Agrees |
| P3-R20 | C232 | secunda | `004` | ch | ch | Agrees |
| P3-R20 | D232 | secunda | `991` | te -r/-n -t -s | te -r/-n -t -s | Agrees |
| P3-R20 | E232 | secunda | `043` | punctum | . | Agrees |
| P3-R20 | F232 | secunda | `362` | - | ∅ | Agrees |
| P3-R20 | G232 | secunda | `018` | indic. clav. 1Mam | → prima | Agrees |
| P3-R20 | H232 | prima | `666` | ich -e/ -n | ich -e/ -n | Agrees |
| P3-R20 | I232 | prima | `013` | ver | ver | Agrees |
| P3-R20 | J232 | prima | `039` | muth -e/-n -lich | muth -e/-n -lich | Agrees |
| P3-R20 | K232 | prima | `3329` | aber | aber | Agrees |
| P3-R20 | L232 | prima | `025` | Comma | , | Agrees |
| P3-R20 | M232 | prima | `3338` | daß | daß | Agrees |
| P3-R20 | N232 | prima | `437` | er -s  | er -s | Agrees |
| P3-R20 | O232 | prima | `001` | von | von | Agrees |
| P3-R20 | P232 | prima | `007` | die | die | Agrees |
| P3-R21 | A237 | prima | `7798` | sem | sem | Agrees |
| P3-R21 | B237 | prima | `1103` | o / lig -e/-r -n -t -s | o / lig -e/-r -n -t -s | Agrees |
| P3-R21 | C237 | prima | `820` | di | di | Agrees |
| P3-R21 | D237 | prima | `7757` | os -se -gen/-n | os -se -gen/-n | Agrees |
| P3-R21 | E237 | prima | `022` | en | en | Agrees |
| P3-R21 | F237 | prima | `7777` | ge -gen | ge -gen | Agrees |
| P3-R21 | G237 | prima | `7775` | ge -t -n | ge -t -n | Agrees |
| P3-R21 | H237 | prima | `234` | stand -en | stand -en | Agrees |
| P3-R21 | I237 | prima | `886` | nicht -s | nicht -s | Agrees |
| P3-R21 | J237 | prima | `1161` | ger -n | ger -n | Agrees |
| P3-R21 | K237 | prima | `005` | e ; meld -en/-ung | e ; meld -en/-ung | Agrees |
| P3-R21 | L237 | prima | `7779` | et | et | Agrees |
| P3-R21 | M237 | prima | `054` | was | was | Agrees |
| P3-R21 | N237 | prima | `437` | er -s  | er -s | Agrees |
| P3-R21 | O237 | prima | `248` | we ; definit -f/-ve | [provisional: we ; definit -f/-ve] | Provisional |
| P4-R01 | A242 | prima | `5512` | h ;  h / dein -e/-n | [provisional: h ;  h / dein -e/-n] | Provisional |
| P4-R01 | B242 | prima | `881` | ne -r/-n ; 9 | ne -r/-n ; 9 | Agrees |
| P4-R01 | C242 | prima | `262` | Comma | , | Agrees |
| P4-R01 | D242 | prima | `407` | sondern | sondern | Agrees |
| P4-R01 | E242 | prima | `7700` | nur | nur | Agrees |
| P4-R01 | F242 | prima | `488` | im | im | Agrees |
| P4-R01 | G242 | prima | `7725` | me -r/-n -t -s  | me -r/-n -t -s | Agrees |
| P4-R01 | H242 | prima | `7778` | durch | durch | Agrees |
| P4-R01 | I242 | prima | `889` | aus | aus | Agrees |
| P4-R01 | J242 | prima | `1107` | würck -lich | würck -lich | Agrees |
| P4-R01 | K242 | prima | `832` | ung -en | ung -en | Agrees |
| P4-R01 | L242 | prima | `3333` | vor | vor | Agrees |
| P4-R01 | M242 | prima | `673` | theil -e/-n -s | theil -e/-n -s | Agrees |
| P4-R01 | N242 | prima | `3321` | ha | ha | Agrees |
| P4-R01 | O242 | prima | `9967` | ft (fft?) | [provisional: ft (fft?)] | Provisional |
| P4-R02 | A247 | prima | `437` | er -s  | er -s | Agrees |
| P4-R02 | B247 | prima | `019` | a ; Condition -s | a ; Condition -s | Agrees |
| P4-R02 | C247 | prima | `022` | en | en | Agrees |
| P4-R02 | D247 | prima | `1113` | und | und | Agrees |
| P4-R02 | E247 | prima | `1144` | er -s  | er -s | Agrees |
| P4-R02 | F247 | prima | `5536` | halt -e/-n -s | halt -e/-n -s | Agrees |
| P4-R02 | G247 | prima | `022` | en | en | Agrees |
| P4-R02 | H247 | prima | `223` | nach -t -er | nach -t -er | Agrees |
| P4-R02 | I247 | prima | `7727` | laß -e/-n -t -lich | laß -e/-n -t -lich | Agrees |
| P4-R02 | J247 | prima | `221` | von | von | Agrees |
| P4-R02 | K247 | prima | `667` | den -en | den -en | Agrees |
| P4-R02 | L247 | prima | `263` | sti -mm | sti -mm | Agrees |
| P4-R02 | M247 | prima | `7781` | pu | pu | Agrees |
| P4-R02 | N247 | prima | `5524` | la | la | Agrees |
| P4-R02 | O247 | prima | `010` | ti -on | ti -on | Agrees |
| P4-R02 | P247 | prima | `022` | en | en | Agrees |
| P4-R03 | A252 | prima | `5528` | deß -sen | deß -sen | Agrees |
| P4-R03 | B252 | prima | `481` | geheim -e/-r -n -s ; uns | geheim -e/-r -n -s ; uns | Agrees |
| P4-R03 | C252 | prima | `809` | tract -at/-en -iren | tract -at/-en -iren | Agrees |
| P4-R03 | D252 | prima | `226` | s; ss | s; ss | Agrees |
| P4-R03 | E252 | prima | `5592` | sich | sich | Agrees |
| P4-R03 | F252 | prima | `7772` | bey | bey | Agrees |
| P4-R03 | G252 | prima | `066` | sein -e/-r -n -s | sein -e/-r -n -s | Agrees |
| P4-R03 | H252 | prima | `003` | hof -fe -t/ -n | hof -fe -t/ -n | Agrees |
| P4-R03 | I252 | prima | `3374` | ange | ange | Agrees |
| P4-R03 | J252 | prima | `641` | nehm -e/-n -t | nehm -e/-n -t | Agrees |
| P4-R03 | K252 | prima | `5557` | und | und | Agrees |
| P4-R03 | L252 | prima | `013` | ver | ver | Agrees |
| P4-R03 | M252 | prima | `428` | dien\|st -en | dien\|st -en | Agrees |
| P4-R03 | N252 | prima | `042` | st ; Mähr -e -ische | st ; Mähr -e -ische | Agrees |
| P4-R03 | O252 | prima | `222` | lich -e/-r -n -s | lich -e/-r -n -s | Agrees |
| P4-R03 | P252 | prima | `405` | mach -e -n | mach -e -n | Agrees |
| P4-R04 | A257 | prima | `293` | wi ; extract | wi ; extract | Agrees |
| P4-R04 | B257 | prima | `1127` | l ; ll | l ; ll | Agrees |
| P4-R04 | C257 | prima | `1158` | punctum | . | Agrees |
| P4-R04 | D257 | prima | `3391` | Comma | , | Agrees |

## Interlinear reading

Norbert’s supplied email text, including page breaks, uncertainty and `[ciphertext: …]` annotations, is preserved in [norbert_interlinear.txt](../sources/norbert_interlinear.txt). [READING.md](../READING.md) uses the new reading and identified ciphertext corrections in the editorial edition. It still requires phrase-by-phrase alignment.
