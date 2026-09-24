# Reading validation and unresolved inventory

**Software checks pass; a full readable decipherment is not established.**
These checks compare selected literal outputs with phrases or stems in the supplied German. They are not independent recovery tests and do not align the entire letter.

| Check | Literal result | Supplied German reference | Comparison |
| --- | --- | --- | --- |
| vorstellung | `vorstelungmachen` | Vorstellungen machen | editorial_difference |
| marechal | `Marechal` | Marechal | matches_after_case_spacing_and_accent_normalization |
| military_stem | `milita` | militarischen | stem_only |
| main_bernis | `abbedebernis` | Abbé de Bernis | matches_after_case_spacing_and_accent_normalization |
| grafen_bruehl | `grafenBrühlunddem` | Grafen Brühl und dem | matches_after_case_spacing_and_accent_normalization |
| stainville | `stainvill(e)` | Stainville | qualified_key_value |
| second_bernis | `abbedebernis` | Abbé Bernis | editorial_difference |
| bezahlung | `bezahlung` | Zahlung | editorial_difference |

- **vorstellung:** The supplied correction is Vorstellung machen; literal stelung also lacks the conventional second l.
- **marechal:** Joins the final 5 of P1-R04 to the opening 521 of P1-R05.
- **military_stem:** Only the milita stem is checked; the whole word is not established by these three units.
- **main_bernis:** Case, spacing and accents are editorial.
- **grafen_bruehl:** Literal values match after case and spacing normalization.
- **stainville:** The last entry retains its supplied optional e; table choice is a local hypothesis.
- **second_bernis:** The supplied prose omits de at the noted occurrence; this candidate restores it and crosses the recorded comma inside 533. Its full prose alignment is not independently established.
- **bezahlung:** The correction notes supply Bezahlung. Matching digits alone do not settle which prose occurrence they annotate.

## Accounting

- Candidate units: 441 (conditional, not a coverage score).
- Cross-row units: 12.
- Qualified value occurrences: 50; literal `?` occurrences: 3.
- Unresolved numeric spans: 206; ambiguous spans: 3.
- Uncertain digit groups: 17; G glyphs: 4.
- Every source character is preserved in the JSON ledger.

## Work queue: unresolved or ambiguous spans

A zero dictionary parse may reflect missing entries, a wrong grouping assumption, a transcription issue, or unknown control rules. It does not establish which explanation is correct.

| ID | Location | Source | Status |
| --- | --- | --- | --- |
| S0001 | P1-R01:1–P1-R01:24 | `204867554711188810201108` | unresolved |
| S0028 | P1-R02:15–P1-R02:18 | `7759` | unresolved |
| S0040 | P1-R02:42–P1-R02:44 | `066` | ambiguous |
| S0052 | P1-R02:66–P1-R03:2 | `0 ↵ 09` | unresolved |
| S0054 | P1-R03:4–P1-R03:6 | `694` | unresolved |
| S0058 | P1-R03:12–P1-R03:14 | `210` | unresolved |
| S0060 | P1-R03:16–P1-R03:19 | `3323` | unresolved |
| S0062 | P1-R03:21–P1-R03:23 | `629` | unresolved |
| S0105 | P1-R04:49–P1-R04:52 | `1158` | unresolved |
| S0125 | P1-R05:30–P1-R05:32 | `663` | unresolved |
| S0127 | P1-R05:34–P1-R05:36 | `643` | unresolved |
| S0129 | P1-R05:38–P1-R05:41 | `3337` | unresolved |
| S0131 | P1-R05:43–P1-R05:45 | `768` | unresolved |
| S0151 | P1-R06:22–P1-R06:25 | `7718` | unresolved |
| S0169 | P1-R06:62–P2-R01:15 | `111 ↵ 301335400041163` | unresolved |
| S0177 | P2-R01:30–P2-R01:33 | `3315` | unresolved |
| S0215 | P2-R02:51–P2-R02:53 | `775` | unresolved |
| S0235 | P2-R03:36–P2-R03:39 | `2203` | unresolved |
| S0250 | P2-R04:9–P2-R04:12 | `3363` | unresolved |
| S0254 | P2-R04:19–P2-R04:22 | `2230` | unresolved |
| S0256 | P2-R04:24–P2-R04:24 | `0` | unresolved |
| S0272 | P2-R04:56–P2-R04:59 | `1158` | unresolved |
| S0308 | P2-R06:7–P2-R06:9 | `021` | unresolved |
| S0312 | P2-R06:15–P2-R06:18 | `7752` | unresolved |
| S0314 | P2-R06:20–P2-R06:22 | `899` | unresolved |
| S0320 | P2-R06:33–P2-R06:35 | `420` | unresolved |
| S0322 | P2-R06:37–P2-R06:39 | `805` | unresolved |
| S0324 | P2-R06:41–P2-R06:43 | `216` | unresolved |
| S0341 | P2-R07:14–P2-R07:16 | `872` | unresolved |
| S0449 | P2-R10:60–P2-R10:62 | `647` | unresolved |
| S0451 | P2-R10:64–P2-R10:66 | `837` | unresolved |
| S0478 | P2-R11:48–P2-R11:50 | `881` | unresolved |
| S0496 | P2-R12:20–P2-R12:22 | `043` | unresolved |
| S0527 | P2-R13:18–P2-R13:21 | `1116` | unresolved |
| S0541 | P2-R13:49–P2-R13:51 | `267` | unresolved |
| S0545 | P2-R13:58–P2-R13:60 | `021` | unresolved |
| S0557 | P2-R14:21–P2-R14:26 | `667664` | unresolved |
| S0606 | P2-R16:5–P2-R16:11 | `2699911` | unresolved |
| S0610 | P2-R16:18–P2-R16:20 | `026` | unresolved |
| S0618 | P2-R16:36–P2-R16:38 | `657` | unresolved |
| S0622 | P2-R16:44–P2-R16:46 | `708` | unresolved |
| S0624 | P2-R16:48–P2-R16:50 | `079` | unresolved |
| S0630 | P2-R16:60–P2-R17:1 | `02 ↵ 9` | unresolved |
| S0636 | P2-R17:11–P2-R17:14 | `1176` | unresolved |
| S0640 | P2-R17:21–P2-R17:37 | `11021165005025020` | unresolved |
| S0652 | P2-R17:59–P2-R17:61 | `111` | unresolved |
| S0655 | P2-R18:1–P2-R18:4 | `9262` | unresolved |
| S0681 | P2-R19:3–P2-R19:5 | `061` | unresolved |
| S0709 | P2-R19:62–P2-R20:1 | `03 ↵ 8` | unresolved |
| S0725 | P2-R20:34–P2-R20:36 | `706` | unresolved |
| S0768 | P2-R21:64–P3-R01:1 | `2 ↵ 6` | unresolved |
| S0769 | P3-R01:2–P3-R01:6 | `[2\|7]` | uncertain_digits |
| S0777 | P3-R01:21–P3-R01:24 | `6678` | unresolved |
| S0779 | P3-R01:26–P3-R01:28 | `685` | unresolved |
| S0785 | P3-R01:39–P3-R01:41 | `066` | ambiguous |
| S0797 | P3-R01:70–P3-R01:72 | `110` | unresolved |
| S0798 | P3-R01:73–P3-R01:77 | `[2\|7]` | uncertain_digits |
| S0805 | P3-R02:5–P3-R02:7 | `113` | unresolved |
| S0809 | P3-R02:16–P3-R02:18 | `026` | unresolved |
| S0811 | P3-R02:20–P3-R02:22 | `055` | unresolved |
| S0823 | P3-R02:50–P3-R02:53 | `1158` | unresolved |
| S0825 | P3-R02:55–P3-R02:56 | `41` | unresolved |
| S0827 | P3-R02:58–P3-R02:62 | `24929` | unresolved |
| S0829 | P3-R02:64–P3-R02:65 | `22` | unresolved |
| S0831 | P3-R02:67–P3-R02:68 | `45` | unresolved |
| S0836 | P3-R03:16–P3-R03:20 | `63885` | unresolved |
| S0840 | P3-R03:26–P3-R03:37 | `550988244528` | unresolved |
| S0842 | P3-R03:39–P3-R03:45 | `1002202` | unresolved |
| S0844 | P3-R03:47–P3-R03:51 | `33775` | unresolved |
| S0846 | P3-R03:53–P3-R03:54 | `16` | unresolved |
| S0849 | P3-R04:13–P3-R04:17 | `33914` | unresolved |
| S0851 | P3-R04:19–P3-R04:23 | `12273` | unresolved |
| S0853 | P3-R04:25–P3-R04:27 | `770` | unresolved |
| S0855 | P3-R04:29–P3-R04:34 | `113095` | unresolved |
| S0857 | P3-R04:36–P3-R04:38 | `199` | unresolved |
| S0859 | P3-R04:43–P3-R04:51 | `550319394` | unresolved |
| S0861 | P3-R04:53–P3-R04:55 | `024` | unresolved |
| S0863 | P3-R04:57–P3-R05:4 | `223902 ↵ 9357` | unresolved |
| S0865 | P3-R05:6–P3-R05:8 | `566` | unresolved |
| S0867 | P3-R05:10–P3-R05:12 | `550` | unresolved |
| S0869 | P3-R05:14–P3-R05:17 | `8835` | unresolved |
| S0871 | P3-R05:19–P3-R05:22 | `5911` | unresolved |
| S0873 | P3-R05:24–P3-R05:27 | `4002` | unresolved |
| S0875 | P3-R05:29–P3-R05:33 | `31502` | unresolved |
| S0877 | P3-R05:35–P3-R05:39 | `[8\|9]` | uncertain_digits |
| S0878 | P3-R05:40–P3-R05:44 | `79971` | unresolved |
| S0880 | P3-R05:46–P3-R05:54 | `304010755` | unresolved |
| S0882 | P3-R05:56–P3-R05:61 | `057776` | unresolved |
| S0885 | P3-R06:1–P3-R06:3 | `114` | unresolved |
| S0887 | P3-R06:5–P3-R06:10 | `050558` | unresolved |
| S0889 | P3-R06:12–P3-R06:16 | `19205` | unresolved |
| S0891 | P3-R06:18–P3-R06:28 | `61461406084` | unresolved |
| S0893 | P3-R06:30–P3-R06:35 | `344331` | unresolved |
| S0895 | P3-R06:37–P3-R06:39 | `335` | unresolved |
| S0897 | P3-R06:41–P3-R06:44 | `4467` | unresolved |
| S0899 | P3-R06:46–P3-R06:48 | `534` | unresolved |
| S0901 | P3-R06:50–P3-R07:7 | `224453 ↵ 3734888` | unresolved |
| S0903 | P3-R07:9–P3-R07:12 | `2770` | unresolved |
| S0905 | P3-R07:14–P3-R07:17 | `3355` | unresolved |
| S0907 | P3-R07:19–P3-R07:21 | `998` | unresolved |
| S0909 | P3-R07:23–P3-R07:24 | `22` | unresolved |
| S0911 | P3-R07:26–P3-R07:28 | `114` | unresolved |
| S0913 | P3-R07:30–P3-R07:39 | `0565194447` | unresolved |
| S0915 | P3-R07:41–P3-R07:44 | `6661` | unresolved |
| S0917 | P3-R07:46–P3-R07:50 | `12457` | unresolved |
| S0919 | P3-R08:17–P3-R08:21 | `48877` | unresolved |
| S0921 | P3-R08:23–P3-R08:31 | `535000975` | unresolved |
| S0923 | P3-R08:33–P3-R08:37 | `02128` | unresolved |
| S0925 | P3-R08:39–P3-R08:40 | `16` | unresolved |
| S0926 | P3-R08:41–P3-R08:45 | `[0\|6]` | uncertain_digits |
| S0928 | P3-R08:47–P3-R08:50 | `2249` | unresolved |
| S0932 | P3-R08:56–P3-R09:2 | `669622 ↵ 51` | unresolved |
| S0934 | P3-R09:4–P3-R09:7 | `5337` | unresolved |
| S0936 | P3-R09:9–P3-R09:19 | `83010775030` | unresolved |
| S0938 | P3-R09:21–P3-R09:23 | `188` | unresolved |
| S0939 | P3-R09:24–P3-R09:31 | `[22\|222]` | uncertain_digits |
| S0940 | P3-R09:32–P3-R09:35 | `7222` | unresolved |
| S0941 | P3-R09:36–P3-R09:40 | `[6\|9]` | uncertain_digits |
| S0942 | P3-R09:41–P3-R09:53 | `2225977105738` | unresolved |
| S0944 | P3-R09:55–P3-R09:60 | `707155` | unresolved |
| S0947 | P3-R10:1–P3-R10:3 | `748` | unresolved |
| S0949 | P3-R10:5–P3-R10:7 | `948` | unresolved |
| S0953 | P3-R10:13–P3-R10:15 | `556` | unresolved |
| S0955 | P3-R10:17–P3-R10:19 | `621` | unresolved |
| S0957 | P3-R10:21–P3-R10:25 | `09444` | unresolved |
| S0959 | P3-R10:27–P3-R10:33 | `3331953` | unresolved |
| S0961 | P3-R10:35–P3-R10:37 | `966` | unresolved |
| S0963 | P3-R10:39–P3-R10:40 | `08` | unresolved |
| S0965 | P3-R10:42–P3-R10:44 | `355` | unresolved |
| S0966 | P3-R10:45–P3-R10:49 | `[2\|9]` | uncertain_digits |
| S0967 | P3-R10:50–P3-R11:2 | `47244010909 ↵ 96` | unresolved |
| S0968 | P3-R11:3–P3-R11:7 | `[6\|8]` | uncertain_digits |
| S0973 | P3-R11:17–P3-R11:19 | `443` | unresolved |
| S0975 | P3-R11:21–P3-R11:28 | `58507778` | unresolved |
| S0977 | P3-R11:30–P3-R11:32 | `199` | unresolved |
| S0981 | P3-R11:59–P3-R12:7 | `8802 ↵ 7731503` | unresolved |
| S0983 | P3-R12:12–P3-R12:13 | `88` | unresolved |
| S0985 | P3-R12:18–P3-R12:22 | `49888` | unresolved |
| S0987 | P3-R12:24–P3-R12:27 | `2069` | unresolved |
| S0989 | P3-R12:29–P3-R12:34 | `066024` | unresolved |
| S0993 | P3-R12:40–P3-R12:42 | `785` | unresolved |
| S0995 | P3-R12:44–P3-R12:49 | `302776` | unresolved |
| S0997 | P3-R12:51–P3-R12:56 | `083357` | unresolved |
| S0999 | P3-R12:58–P3-R12:61 | `2295` | unresolved |
| S1001 | P3-R12:63–P3-R13:4 | `905557 ↵ 6604` | unresolved |
| S1005 | P3-R13:10–P3-R13:16 | `6642199` | unresolved |
| S1007 | P3-R13:18–P3-R13:25 | `11033530` | unresolved |
| S1008 | P3-R13:26–P3-R13:30 | `[0\|6]` | uncertain_digits |
| S1010 | P3-R13:32–P3-R13:34 | `166` | unresolved |
| S1014 | P3-R13:40–P3-R13:43 | `4336` | unresolved |
| S1018 | P3-R13:52–P3-R14:5 | `1558675437425 ↵ 51985` | unresolved |
| S1020 | P3-R14:7–P3-R14:8 | `77` | unresolved |
| S1022 | P3-R14:10–P3-R14:12 | `906` | unresolved |
| S1024 | P3-R14:14–P3-R14:18 | `57344` | unresolved |
| S1026 | P3-R14:20–P3-R14:24 | `30955` | unresolved |
| S1027 | P3-R14:25–P3-R14:29 | `[0\|6]` | uncertain_digits |
| S1028 | P3-R14:30–P3-R14:32 | `822` | unresolved |
| S1030 | P3-R14:37–P3-R14:42 | `129709` | unresolved |
| S1032 | P3-R14:44–P3-R14:49 | `014386` | unresolved |
| S1034 | P3-R14:51–P3-R14:55 | `44444` | unresolved |
| S1036 | P3-R14:57–P3-R15:24 | `30043002 ↵ 014226230079408775070994` | unresolved |
| S1038 | P3-R15:26–P3-R15:31 | `069386` | unresolved |
| S1040 | P3-R15:33–P3-R15:36 | `3886` | unresolved |
| S1042 | P3-R15:38–P3-R15:43 | `609888` | unresolved |
| S1044 | P3-R15:45–P3-R15:47 | `048` | unresolved |
| S1046 | P3-R15:49–P3-R15:51 | `084` | unresolved |
| S1048 | P3-R15:53–P3-R15:58 | `301918` | unresolved |
| S1051 | P3-R16:1–P3-R16:5 | `[0\|6]` | uncertain_digits |
| S1052 | P3-R16:6–P3-R16:7 | `66` | unresolved |
| S1054 | P3-R16:9–P3-R16:14 | `918040` | unresolved |
| S1056 | P3-R16:16–P3-R16:21 | `396887` | unresolved |
| S1058 | P3-R16:23–P3-R16:28 | `059122` | unresolved |
| S1064 | P3-R16:38–P3-R16:46 | `348865119` | unresolved |
| S1066 | P3-R16:48–P3-R16:62 | `050329114337353` | unresolved |
| S1069 | P3-R17:1–P3-R17:2 | `50` | unresolved |
| S1070 | P3-R17:3–P3-R17:7 | `[0\|6]` | uncertain_digits |
| S1074 | P3-R17:14–P3-R17:18 | `[6\|0]` | uncertain_digits |
| S1075 | P3-R17:19–P3-R17:20 | `39` | unresolved |
| S1077 | P3-R17:22–P3-R17:25 | `6680` | unresolved |
| S1079 | P3-R17:27–P3-R17:29 | `335` | unresolved |
| S1081 | P3-R17:31–P3-R17:32 | `68` | unresolved |
| S1082 | P3-R17:33–P3-R17:37 | `[3\|8]` | uncertain_digits |
| S1087 | P3-R17:47–P3-R17:50 | `1129` | unresolved |
| S1091 | P3-R17:57–P3-R17:60 | `4946` | unresolved |
| S1093 | P3-R17:62–P3-R17:70 | `553332247` | unresolved |
| S1095 | P3-R17:72–P3-R18:4 | `660 ↵ 6775` | unresolved |
| S1097 | P3-R18:6–P3-R18:8 | `928` | unresolved |
| S1099 | P3-R18:10–P3-R18:12 | `121` | unresolved |
| S1101 | P3-R18:14–P3-R18:22 | `227438669` | unresolved |
| S1103 | P3-R18:24–P3-R18:24 | `1` | unresolved |
| S1105 | P3-R18:39–P3-R18:41 | `507` | unresolved |
| S1107 | P3-R18:43–P3-R18:50 | `65019211` | unresolved |
| S1109 | P3-R18:52–P3-R18:53 | `61` | unresolved |
| S1110 | P3-R18:54–P3-R18:58 | `[0\|6]` | uncertain_digits |
| S1111 | P3-R18:59–P3-R18:66 | `80323447` | unresolved |
| S1114 | P3-R19:1–P3-R19:5 | `83768` | unresolved |
| S1116 | P3-R19:7–P3-R19:10 | `3555` | unresolved |
| S1120 | P3-R19:16–P3-R19:24 | `505133074` | unresolved |
| S1122 | P3-R19:26–P3-R19:28 | `055` | unresolved |
| S1124 | P3-R19:30–P3-R19:33 | `1467` | unresolved |
| S1126 | P3-R19:35–P3-R19:36 | `69` | unresolved |
| S1127 | P3-R19:37–P3-R19:48 | `[4444\|44444]` | uncertain_digits |
| S1129 | P3-R19:50–P3-R19:55 | `122466` | unresolved |
| S1131 | P3-R19:57–P3-R19:61 | `91894` | unresolved |
| S1133 | P3-R19:63–P3-R19:70 | `92234974` | unresolved |
| S1136 | P3-R20:1–P3-R20:6 | `856903` | unresolved |
| S1140 | P3-R20:12–P3-R20:14 | `991` | unresolved |
| S1142 | P3-R20:16–P3-R20:18 | `043` | unresolved |
| S1144 | P3-R20:20–P3-R20:22 | `962` | unresolved |
| S1146 | P3-R20:24–P3-R20:26 | `618` | unresolved |
| S1148 | P3-R20:28–P3-R20:36 | `669013039` | unresolved |
| S1150 | P3-R20:38–P3-R20:41 | `3329` | unresolved |
| S1152 | P3-R20:43–P3-R20:48 | `625333` | unresolved |
| S1154 | P3-R20:50–P3-R20:53 | `8437` | unresolved |
| S1161 | P3-R21:1–P3-R21:15 | `779811638297757` | unresolved |
| S1166 | P3-R21:25–P3-R21:29 | `[6\|0]` | uncertain_digits |
| S1167 | P3-R21:30–P3-R21:33 | `7752` | unresolved |
| S1169 | P3-R21:35–P3-R21:38 | `3488` | unresolved |
| S1171 | P3-R21:40–P3-R21:42 | `016` | unresolved |
| S1173 | P3-R21:44–P3-R21:46 | `006` | unresolved |
| S1178 | P4-R01:1–P4-R01:7 | `5512881` | unresolved |
| S1188 | P4-R01:26–P4-R01:28 | `725` | unresolved |
| S1246 | P4-R03:28–P4-R03:30 | `066` | ambiguous |
| S1260 | P4-R03:58–P4-R03:59 | `04` | unresolved |
| S1261 | P4-R03:60–P4-R03:63 | `<G1>` | glyph |
| S1263 | P4-R03:65–P4-R03:68 | `<G2>` | glyph |
| S1264 | P4-R03:69–P4-R03:72 | `<G3>` | glyph |
| S1265 | P4-R03:73–P4-R03:76 | `<G4>` | glyph |
| S1269 | P4-R04:4–P4-R04:6 | `293` | unresolved |
| S1273 | P4-R04:13–P4-R04:16 | `1158` | unresolved |
