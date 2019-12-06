from anytree import Node, RenderTree, find, PreOrderIter

class body:
    def __init__(self, name, orbiter):
        self.name = name
        self.orbiter_list = [orbiter]

    def add(self, orbiter):
        self.orbiter_list.append(orbiter)


inp = """N66)QHW
JLG)GBP
12Q)F84
JMQ)QDZ
1FF)45G
T82)NHZ
Z1C)BP4
JMB)XQ1
51X)FTR
7TD)YTD
S65)TZ2
N56)F1B
31N)Z26
GPP)RHP
XK5)SSH
LDG)7C3
LLS)96H
ZN6)SFY
QDF)C2B
4T8)Z15
6MC)VTY
JZ9)QYF
7KK)W4Q
8KL)FC2
F2Z)2YC
YTZ)866
127)QFZ
XWZ)BXH
TXC)H1R
C14)C4J
C9K)BHP
3V4)81F
9H4)127
QSK)DD6
MNL)MGQ
G2J)9VS
HZV)DPP
BZ6)W5J
QVQ)QQH
G16)6NM
8ZC)5JQ
R54)D2K
6ZP)8B2
QJW)Z94
FF2)VK3
3NR)XQ9
2SQ)154
KSB)6T3
HNT)GB4
H1R)NMR
NCT)JNJ
KPT)4R5
ZGW)53N
JDY)4C6
42W)QSK
QWH)JXS
Z8K)99G
8X8)JLQ
WM3)6ZP
5XQ)KNQ
TXD)7C5
MV1)76W
79T)RDK
D4F)LL8
9K5)65L
SRF)JDB
2JT)FCC
JGQ)F4W
1V3)ZC2
P69)B72
974)9JR
Z4W)MVY
3SP)9KP
ZWV)FXX
6SN)QW4
33J)4Z7
6SN)974
FJR)LTK
FJR)B7Y
N1G)ZFD
ZY1)1NZ
7RL)7T8
FXX)424
CFD)TW7
7H1)V6P
KQD)KL1
KZ4)5ZD
73V)QPL
KRX)KM3
S2N)F6S
25L)LQM
CQL)PJW
LSY)ZY1
JK7)R1N
N56)YQV
255)66S
W5J)VHS
7DZ)7RG
H8N)ZHR
Z4J)VJ4
X9K)CJ8
ZLR)PR9
QBW)X37
Q43)56Y
78Z)W2Q
GB4)QDF
TYM)L8G
PB6)ZKH
Z6Y)4HD
17T)H1F
NB1)D72
NC6)ZTH
T9V)G1C
6QP)1LV
Y8Y)42N
B3G)P55
ZW9)JXZ
TBN)6RV
Q83)T53
58F)FJR
TGN)S8R
1H9)M9P
F6K)ZGW
VJH)W1L
ZGF)W44
4T3)QW9
JSY)FF5
QBD)BF8
MKQ)4MM
6MM)TYW
H1Q)SGJ
8RF)7RL
Z7C)GYM
7VM)YZK
CTD)Z4J
NP5)98J
X25)D88
7SR)LY2
2YN)7DZ
PD1)KL3
QLQ)Q83
1LV)H5C
1QK)Y3R
X6C)3HP
WMC)LGM
412)QSD
ND2)M6Y
GX9)35L
P35)XZP
FC3)3HF
Q95)22V
CS6)CF8
HQR)JZ9
RJF)V6F
FZC)3ZN
631)1H9
6T4)WL1
LKG)LSY
2RW)J8F
BZ3)Y8Y
MH9)1WD
8TQ)QXT
9KP)RP4
ZFF)QSZ
P77)RDB
2NH)NKW
R3H)QK9
W6C)CMY
6T3)ZSZ
HWM)56V
YC1)ZVB
1G4)YYW
MTV)LXV
XR7)1FF
95M)T2J
C79)8ZC
RXT)H4Z
Q2F)8D8
V8S)97R
1H9)7SR
JR9)GY2
V6P)NZ1
L4L)KZ4
PWC)MXY
34D)YC1
TW7)D11
C6F)KWY
N5N)3V4
TZV)FDY
J71)MK7
BCC)JLS
4SM)GKL
649)BFN
RK4)319
P81)HMG
474)VHJ
1GS)356
SHG)92Y
HNB)WMC
YYP)68F
M3L)FBG
LNG)MT2
QW4)6DB
1RK)YZG
NN5)NSQ
X1S)ZGZ
9BQ)R3H
4HD)39W
N44)SJN
NTZ)3CQ
3TK)985
39J)5J4
VBC)X25
DJ4)7XW
SVJ)BGV
VVQ)7DD
85J)8RF
MPX)58F
K9X)876
ZY4)B9W
FJF)BVR
C45)SYW
11V)5HR
FXW)9P9
XKY)94X
Z6L)K5Q
PTT)7HP
95M)85N
5RX)6NR
6NW)5GX
RY2)88X
382)TQ5
QYF)M8Z
VTY)Z63
4ZB)63M
LY2)969
NTV)LCL
SB2)CFD
PR9)8L9
VHJ)PJ6
516)KMC
51B)516
Q43)DDK
JLS)ZY4
JQX)VZ9
7D5)S2Q
NXT)SHM
B5B)WPG
P77)4T3
RDL)SBZ
G9T)ZDN
RLM)75B
BVR)LHY
Z15)9XQ
LN5)5VS
LQM)YLK
XR1)D9X
Q7K)KSB
PP9)N5X
2LT)6T4
3C8)1XC
6NR)5JH
8QM)TGN
36Z)4R2
8YM)NB3
4N6)6L7
SGK)8Z4
1BK)VQX
P55)PBZ
Y5T)D4C
GJV)3RC
KCB)81Z
63Q)NBM
GYV)MNL
C37)9H4
23V)3WR
MLK)B2G
N72)YCF
46P)CTD
HNC)SQ1
5GV)GV3
7WJ)49H
6VV)JB8
H13)8GT
FJQ)6YW
7Z4)7VF
MK3)GPY
H4K)65D
4W3)1LQ
974)TLZ
T6W)5T5
6DD)LKG
4C6)78H
D7K)TYM
TZ2)W8B
DHF)LH8
BK5)BHM
ZDN)9CV
6NM)MKQ
1QK)5S7
18W)YOU
RKS)C57
MH4)TFY
SWR)8HD
JGQ)631
T6B)Z3Q
XV1)9GM
3N7)WPL
VFT)DYB
223)THD
SR5)G9S
YZG)GYS
NHZ)VCP
3JG)PHJ
FNG)NJL
WPL)6Z3
6M7)JMB
KW9)KLR
FZR)3BY
463)YSB
VX8)K3M
QSZ)YRH
ZSZ)QS3
HR7)FL3
14W)K45
11M)48B
T6W)B1W
8LC)1JJ
LHY)WX1
BWZ)2P8
H6N)6M7
PJW)XTF
N3Z)4ZZ
RCR)F2Z
5V7)N3S
CYM)NL5
Z3Q)3D7
319)FBR
C3K)C93
3BY)ZZW
D11)8QM
KQK)GPM
MH5)FL4
2W2)MV1
QDC)MK3
ZY4)2WT
XCN)523
VJD)7Q9
TYW)MKT
323)ZCK
6V5)HQR
ZQN)284
ZZL)N72
VHR)YMB
L7J)9YR
D5P)QVQ
F71)FZC
6FZ)9PN
CN5)Z1C
K45)DSL
QB5)T16
7B4)C3K
M5L)XK5
4R2)4FL
JMQ)QJW
969)WYB
88F)NK7
ZKH)76D
YYY)VGM
DD6)RK4
356)6P4
VF5)DDM
48Z)XWR
6RQ)H2K
FQX)RTZ
96H)M77
8L9)CN5
GL2)754
4ZB)11V
83S)S59
MYZ)253
YRS)2VM
N23)7GC
85N)87L
78H)MR9
8H1)7B1
TNR)6P7
BND)624
XCW)Z7C
RFV)4SM
X1S)ZTW
TTL)5Z3
SB4)57B
CS7)ZD1
9FR)TDD
LNG)T73
KV4)KWV
C57)4R7
F1B)96Q
ZRR)5XH
RDK)3CS
KF7)4W3
TDD)SGG
4FT)BQV
BWZ)WWS
NHJ)SVJ
S8R)TDS
XLX)BZ5
HK9)D73
S3C)G9Z
6P7)3W4
HPQ)P9R
7P7)LVN
XDL)CQV
65L)182
1NZ)C91
W9T)JXV
TCB)2TV
LVN)MH5
1WR)VHF
KMC)FFW
KGW)JK9
G8J)8XV
NW8)C34
QSD)GMK
253)Y1N
RKT)1XV
ZLS)CXN
Z7R)ZFF
5T5)7N8
TT4)HPH
523)6DD
GYM)9K5
FFK)XRN
FVZ)42W
HQG)7HH
9CV)PCJ
WSP)QZM
67K)C14
NT8)QD4
VNZ)XT4
QW9)LLW
92Y)N66
QXT)GYV
JDB)9QQ
PCJ)YDN
5WM)C55
M8Z)97X
H7J)R2M
NB9)2BS
K9X)GPP
CMY)GZP
QR7)46Q
FTR)JDY
985)W3N
T73)CP7
GZP)VX8
V1P)CSP
B3W)ZGF
14C)3KK
9XQ)183
ZD1)6YN
D4K)KPT
GV3)BS8
38S)XLX
X3C)Q1V
QX7)1MP
VK6)CCV
DDK)46P
GYS)H74
XQ9)HNT
G54)5KV
ZZ5)JXQ
X37)LLS
L8G)D6D
BZ3)N6T
SS9)475
D3R)3NC
JWX)YZC
WP5)CB6
QS4)D68
PY2)745
XWR)9YP
6L7)8NG
S2Q)11M
VNR)MBD
5M4)6MM
VF7)CXK
XR7)Q76
3CS)SRF
Y7J)VSY
NPX)8KQ
7MX)LML
7F6)X3C
YDN)LZ9
33J)8HY
GZZ)2PH
7Q9)PYK
D1K)5V7
NBM)P7W
XKD)QBD
5T3)YMV
MT2)PQY
N6T)7Z3
2RZ)63B
5QK)KRX
M4R)FQV
RKT)LYW
SBZ)47J
D81)XR1
54Q)6BL
JKV)CTR
ML1)K9Y
4Q2)63Y
PWH)BZ3
XQD)LBF
3KZ)63Z
3N1)3XT
WQ2)VDZ
QK9)V6Y
6BL)N41
79V)LBR
C91)WQM
F6S)79V
4JQ)DH2
35L)RKS
NN2)6R1
RNP)VV6
53N)9XG
V6C)865
5ZD)23V
F85)YHM
F4W)JWX
WTS)N7Y
8Z4)WP5
78L)21N
XGZ)G8J
DB2)322
BS8)JKV
3DX)BY1
D2R)YBN
W8B)J48
LLF)R7V
B7T)XZQ
QSD)B3G
81F)K9T
3HS)GHS
RN2)NST
PJ6)ZBX
TRY)D4M
3Y6)MD7
B6R)NC6
LXS)FXJ
191)RKT
N5X)CGW
761)46M
3NC)5Y4
BYN)XV7
3P1)HJB
W3N)XGZ
LBW)FVS
4W8)DWX
8PX)M2B
PB6)LVZ
73K)6SN
ZYT)2DZ
SVM)W6C
PLV)K8N
8B2)Q43
PDS)3PM
RD8)RY2
7WN)XDL
CZD)51F
KND)P3M
3ZN)V6C
LCL)SGK
Y1W)3XQ
3N4)YYP
8X3)BYQ
7ZF)F85
WL1)P5D
MR9)VH4
J8N)31M
GHS)3SP
12H)DD4
WLN)NPX
8Z9)M25
6HZ)T4B
7MZ)26W
7QW)M5L
C4J)RPS
KNQ)T3Z
9FV)NPH
LGF)KZ2
P7D)7S8
866)F9X
CTB)SB2
SL9)C1C
17J)5WM
13Q)PF5
HPV)1QK
BF8)PY6
FBG)TXD
R2Z)PWQ
TN5)6QP
WPG)TH6
X3C)6VV
FRV)8VK
V6B)2SQ
Z79)ZN4
V3S)WLR
LL8)7G5
ST6)SL2
56V)25L
4ZZ)WM8
2XJ)ZLR
C93)D81
X4Q)KGW
BFG)ML1
88X)LQY
5W7)JGG
CP7)59H
7S8)9VC
NZH)Y3D
ZXJ)VYD
R1N)BZ6
Q2N)12H
NKW)NTV
2DZ)8KF
FK6)B6R
LSY)LFG
NPH)2JT
1MP)FQX
5GX)N3Z
LL8)F71
29B)ZQN
KLR)K7L
1WD)3TK
PWQ)PJ5
PX5)MPX
HWD)G9T
QTQ)Y5T
1HC)X9K
P9H)WK8
VQK)V1P
66R)RJF
1L6)RQ1
68M)15L
CGW)HWM
7QP)BND
YMB)1GS
HCR)6K5
NH6)VWM
XSW)3DX
SGJ)W6T
3W6)34D
3SH)BK5
BW1)1JQ
CF8)PWC
3D7)S6N
BF6)4SC
8VK)8Q2
KZ2)HWD
LYW)P35
ZH9)RXT
WD2)JMQ
8B4)4SH
SJ8)Y4X
YZC)NN2
JV2)M4R
PSQ)3ZF
8PD)7KK
98J)XSW
1G5)FYT
L39)X4Q
5VS)889
P7W)N84
VN3)38S
BGY)R5C
284)Y6Z
6Z3)MH9
7C3)DL8
7KM)G1W
3N4)4DF
LML)HQG
LFG)8LC
4ZZ)ZH9
8XV)1SC
YLK)3C8
BMY)XZF
9JV)ZZL
7GC)ND2
LG7)N23
15D)HZV
M2F)31N
NN2)7B4
42N)VYN
PQY)BXS
Z7F)BH1
QS3)RVQ
QD8)N1G
DL8)9B7
9Y4)T6Y
3CQ)VZ8
B9N)C37
BJ9)C4H
JHJ)5DG
C2B)MLW
JNJ)8KZ
NH5)TD8
BND)191
D88)3BV
W2Q)8X3
Q89)7WJ
624)2XN
5Y4)CTQ
3DX)48X
PJ5)9FV
C45)63Q
GMK)91X
3KK)QX5
9GM)8PD
D68)Q95
BY1)29B
63Y)SKH
LTK)MLK
ZKH)WLN
485)7QP
CCH)223
BHP)CYM
W5S)HG2
876)Q9P
KZ1)7KC
RZ2)BF6
MRY)1WR
CMC)C6F
XJJ)PHX
FVS)53K
Y7H)RFV
LLW)J3B
7HP)JNN
XG1)NG9
9W2)8SB
CWB)2RZ
99G)5QK
13L)LPT
L5Y)L7J
G4G)S61
6Y8)GGC
3QG)52W
T4B)H4K
TGD)3QG
BQX)C27
2P5)PSP
V6Y)Q89
NM8)G4G
ZTH)SL9
JJB)1FX
48X)48Z
TJW)8F6
QQH)NH5
59H)TNR
72F)GV2
S6N)WQW
SKD)P58
6YN)Z7R
3PM)C79
6MR)ZLS
SJ1)MH4
W95)LNG
8HY)HCR
2P5)SPS
3GB)7P7
L4B)5HM
5XH)39J
QCB)474
BQX)382
VJ4)ZS1
65T)VN3
GYS)H56
7QB)X7N
322)7BM
3HP)9WZ
5LB)JHJ
49G)NCT
SYW)CQL
R7V)C9K
CMJ)RWD
XTF)W9T
KZ1)Y2Y
K1H)RN2
F6G)KB6
NF9)N9Z
53K)KKZ
6RV)P81
CJ8)N5N
2VM)MTX
5S7)VJ5
81Z)T87
CTD)P9H
VJ5)F6G
GX9)Y7J
3WR)KRP
SH7)48W
HG2)347
HJB)65T
29M)ZK8
1BB)5ZY
WXF)3HS
8RH)13Q
KY8)VJD
P35)761
KM3)SKM
2DZ)YTZ
16Z)Y4L
XKY)F6K
8KZ)NHJ
8HD)FZR
CB6)JTD
LZW)17T
LN1)RYF
RSS)XR7
JGG)36Z
MTX)PLV
WK7)RZF
NL5)ZWF
68F)SVM
YTF)STL
J8F)6TD
MYW)73K
51F)JRV
NBN)8PX
GTQ)BJ9
RDM)H7J
4FL)QB5
5J4)5T3
75B)RCR
YHM)QT4
GPY)P32
KL1)12Q
VHS)RKD
M77)X1V
JGW)BFF
TJ5)K93
TT6)L4B
Y6Z)DNJ
88V)FYZ
2XN)WK7
G36)TCB
3G9)YD9
9JB)P77
PD1)VF5
B72)16Z
QNR)SV4
SGG)W5S
WWS)FCN
Y4X)3N1
9JR)8Z9
FDY)HB2
J3B)TT6
WSS)LVH
YD3)VNR
HRK)VF7
H5C)18W
K8N)Z6L
VZ8)33J
26W)64S
Z93)PD1
6RS)615
JX3)VQJ
D6D)BVY
LQY)YYY
B89)RLM
7N8)V3S
8Q2)GJV
SKH)XJB
RP4)PSQ
GBP)B5V
P9R)4Q8
G9S)HZC
5JQ)GLZ
VHF)TD4
JXV)VRL
745)49G
RYF)D3X
889)PWH
SH7)TTL
4ZN)X6C
BX1)6FH
RP6)1L6
66R)7QB
5JW)ZQK
31M)ZWV
SY9)G36
SSH)7VM
7GS)M29
96V)2C3
424)J8T
B1W)2YN
BRM)KYF
5JH)146
62Z)RT8
WTK)FYM
YQ6)P79
Q4K)9W2
ZFF)9BQ
Z94)4JQ
37C)2W2
R5C)PB6
H4Z)M4Z
B7L)LN1
H1R)JXC
18J)649
8F6)KCB
THD)B5B
HK9)G45
D8V)KQK
WQM)CS7
CXN)1HW
VV6)2LT
2XN)W95
WLR)K91
6KN)V6B
3XT)L4L
XXW)K9X
1S1)NXT
ZC2)6V5
P3M)Q9R
WM3)G2J
19M)N96
NN2)5XQ
H1F)J71
VYN)SS9
XSW)XXW
Y82)4ZN
ZZW)95M
RMB)3GB
475)WTK
JXC)FFK
NJL)YVB
G45)8TQ
PSP)SJ8
X9K)5RX
4X6)KZ1
QZM)2WF
GFK)SKD
CSP)66R
ZTW)9JV
B7Y)4W8
7KC)TS7
T53)LGF
7GS)M67
146)J8M
T3Z)YHV
PM9)5GV
Y1N)B7T
RLJ)3N4
91X)LXT
RKD)NCM
1V2)TK8
RPS)VXJ
5Z3)XVS
M7B)JFN
DR8)SAN
YMV)VJH
WX1)13L
52W)R3G
64S)WXF
VK3)QD8
YTD)XKD
BFF)XG1
21N)4ZJ
SHY)JJG
6TD)LN5
Y82)G54
J8T)7FL
VVR)5RG
J8M)Q2F
XMK)8YX
VYD)RNP
ZHR)DF5
K93)3SH
WYT)L92
C14)86C
MVY)FJF
MKT)V58
G4M)1V3
8Q7)RZ2
8D8)YGG
C1C)7H1
LZ9)N56
SPS)MYZ
C4H)7JC
XZP)6Y8
Q9R)HK2
97R)8VZ
MD7)7F6
LYS)MMK
7DD)HGK
D2K)T6W
RDB)5DD
9XG)HR7
6VV)ZYF
HHK)62Z
TBN)6RQ
MHC)XJJ
N84)5VR
XQ1)J8N
XT4)XMK
GGC)MVX
DF5)2XJ
57B)HB3
J53)9JB
FJF)NM8
XZF)B9N
GY2)HD1
ZK8)J5V
L5Q)B4V
YSB)2SM
QD4)ZCX
YRH)Q2N
KWY)Y21
HB2)RP6
N3S)XCW
VBV)K2H
6QP)NT8
5HJ)GX9
BP4)MRY
63Q)QKT
8GT)4N6
W9T)JR9
9YR)BWZ
ZN4)NB9
QPL)L39
LLS)BMY
BDM)FVN
HB3)BRM
87L)XLV
3KZ)NB1
MVX)LK8
H56)79T
Y4L)HHK
XZ9)VFT
D3X)1RK
N19)7QW
51X)S65
LTN)DJ4
Q9J)KQD
XVS)P7D
5TC)NH6
Z6C)JSY
RZF)G16
C34)KW9
T2J)D7K
TFD)RSS
BCC)FM4
YHV)VK6
H74)D1K
F9X)VNZ
YQV)1HB
3BV)BZD
DSL)TJW
D27)1G4
K92)BDM
49H)2NH
5KV)MYW
WGK)54L
2SM)SVT
5VR)GVD
N41)CMJ
VQX)K1H
JRV)XGW
BGV)QNR
KYF)855
LPT)VBV
P58)H13
D4M)H6N
FVN)HNC
5DG)PTT
2C3)DTW
MBD)S2N
22V)VVR
Z63)PP9
48B)TN5
PY6)P7R
46M)NKX
8NG)BX1
CK7)NP5
L92)Q9J
QTQ)D31
K9T)KQH
QWH)TGD
MK7)C2Q
RCR)DHF
YSF)LLF
6RQ)1S1
DTW)HPV
N3Z)72Z
HGK)CTB
G16)7MX
B9W)KF7
QFZ)NW8
JFN)15D
5ZY)2YT
39W)T9V
J3B)54Q
2C2)B4K
NCM)DR8
HZH)WYT
M29)YRS
7BM)KND
M4Z)SH7
ML1)G4M
9VC)JV2
J53)R54
4DF)HPQ
7VF)WQ2
YG6)GZZ
H7L)D27
QBZ)61N
1JJ)L5Y
J2Q)WDL
NWZ)9RK
CQV)NZH
YSF)R68
PHX)LZW
G1W)QX7
RD8)8X8
H7D)WSP
6K5)ZZ5
PWC)RMB
STL)6MC
9P9)Q7K
Y2Y)TFD
N7Y)H1Q
1RB)7TD
JXS)SDY
P32)LTN
D4C)Z8K
FM4)R8H
JXQ)818
ZY1)H7D
C27)8YM
TXD)GTQ
D72)HRK
4KJ)D8V
615)PY1
WDL)HRB
SVT)HK9
G19)88Q
DH2)QBZ
TFY)2P5
LGM)QTT
SL2)3JG
Y3R)JGW
R2M)5J1
DNJ)Z79
64S)BQX
5RG)TBN
9B7)DB2
TD4)96V
HD1)88V
3QM)N3R
4Z7)K92
7B1)KSF
NMR)SJ1
JXC)WD2
YN1)4ZB
PYK)SR5
S59)J2Q
RQ1)485
Y6Z)19M
YTD)3P1
ZFD)XCN
LBF)7T6
63M)G5R
D9X)GFK
NPM)D4K
FC2)4X6
J6B)TXC
GLZ)YQ6
7T6)QLQ
XJB)7Z4
PY1)Z4W
KSS)J53
TK8)RLJ
JNN)68M
N9Z)T82
LBR)DM2
YYW)FJQ
LYS)N19
G5R)M3L
6FH)NTZ
D31)VJT
SB4)7GS
8KF)2C2
8Q7)H7L
TDS)NPM
VZ9)VQK
9VS)7WN
M6Y)LXS
HMG)7D5
JB8)GL2
F84)XQD
QKT)323
PF5)MTV
VCP)NN5
PFL)GPX
KL3)83S
YVB)W6D
W6T)37C
8QY)1B5
F7W)CWB
TD8)1BB
D73)3G9
ZYF)6MR
YD9)QS4
X7N)WH3
PF2)1QP
Q76)CS6
PBZ)CMC
FXJ)J6B
P5B)QBW
FYM)R2Z
B4V)7MZ
ZWF)1V2
LVZ)1BK
VZ8)95W
7HH)C4B
YBN)DDV
WXF)QBM
ZCX)7ZF
CW3)ZYT
T2S)H3Q
COM)4FT
MMK)8QY
8VZ)SWR
5DG)S3Y
146)HSZ
HSZ)F7W
L1C)H8N
7RG)FK6
1HB)ST6
Z93)1HC
7G5)4KJ
JK9)63X
5F3)5TC
NST)KV7
VYN)CZD
HHD)JK7
NKX)VBC
CTB)BCC
745)FXW
CXK)SS6
3HF)S3C
54L)5M4
N23)3Y6
NB3)PY2
SFY)FRV
Q9P)4BQ
SDY)PX5
NZ1)MHC
HRB)3TT
CZK)8RH
66S)73V
6X8)B3W
M9P)QDC
1LQ)V6Q
HK2)BYN
754)5F3
7T8)1G5
4Q8)ZW9
LXT)Z7G
45G)4Q2
S49)B89
9PN)72F
CMN)T5Z
WQW)PDS
1B5)Z6Y
7C5)QR7
J82)2W8
KB6)5JW
W4Q)Y5B
2YT)18J
TS7)K7K
R68)LYS
T6Y)J82
855)29M
8SB)HYM
FCC)XWZ
8PD)7KM
WL1)67K
GV2)1RB
FCN)SY9
L7J)C45
NG9)4T8
KSF)78L
6V5)FNG
LH8)CW3
97X)78Z
BFN)WTS
ZCK)DY7
T16)VHR
2WF)FS5
QT4)JJB
K7L)85J
9QQ)LNV
M25)PFL
QPL)BW1
RHP)NF9
1ZH)HGT
1XV)TT4
N9Z)SHY
VGM)WSS
WH3)51X
D82)X1S
BQV)P69
TQ5)6HZ
Q1V)V7B
154)SB4
XLV)M2F
FC2)PF2
3RC)D4F
JLQ)XKY
1XC)6RS
GD6)WGK
5RG)HH4
FBR)QWH
G4G)PM9
182)412
LNV)KSS
ZVB)5W7
7DD)RD8
B2G)6NW
GJV)YTF
J5V)ZN6
XDC)JGQ
2TV)NBN
XRN)JLG
319)KY8
GPM)BM5
C2Q)YG6
4FT)TZV
6DB)3NR
JXZ)ZXJ
63Z)8Q7
Y21)G19
K45)14C
94X)BFG
KWV)2RW
NK7)XDC
DM2)TRY
7B1)HNB
6RS)P5B
VXJ)V8S
XV7)L1C
1QP)768
H3Q)LBW
8QY)9FR
KW9)KVM
DDM)9Y4
9YP)HHD
4SH)W79
GVD)6X8
BZ5)XV1
R3G)NYC
LK8)JNB
TLZ)M7B
R8H)255
8KQ)3QM
P5D)QCB
WP5)T6B
7JC)Y82
2WT)S49
QDZ)YN1
183)88F
VDZ)T2S
M67)Y7H
382)D3R
SKM)NMZ
4SC)1ZH
YGG)NWZ
5S7)3KZ
P7R)RDL
S61)JQX
98D)KV4
RT8)14W
ZBX)8RX
FF5)SHG
96Q)QTQ
7FL)VVQ
B4K)Z6C
4ZJ)TJ5
6P4)FVZ
95W)CMN
2YC)51B
CTQ)8B4
K9Y)VH6
C55)JYQ
NYC)HZH
TTL)8KL
3XT)WM3
H2K)X16
TD8)D2R
9K5)DR3
VSY)CZK
TH6)B7L
Z26)CCH
56Y)CK7
L5J)GD6
FFW)463
CMC)ZRR
T5Z)8H1
PHJ)6KN
ZS1)D82
818)3N7
K7K)Y1W
V6F)LG7
Y5B)3W6
K5Q)TY7
DDV)YSF
VJT)N44
86C)L5Q
2PH)FF2
CTR)XZ9
X16)Z93
87L)98D
5BK)17J
W79)PXJ
QX5)BGY
SHM)FC3
1SC)6FZ
5DD)JX3
6R1)D5P
761)5HJ
HH4)RDM
D11)T54
JTD)YD3
4MM)LDG
VQJ)5BK
B5V)5LB
4KJ)L5J
N3R)Z7F
72Z)Q4K"""

#inp = """COM)B
#B)C
# #C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN"""

inp = inp.split('\n')
print(inp)
starters = []
for instr in inp:
    flag = False
    bod, orb = instr.split(')')
    for starter in starters:
        if orb == starter.name:
            starters.remove(starter)
            for starter2 in starters:
                node = find(starter2, lambda node: node.name == bod)
                if node != None:
                    starter.parent = node
                    break
            else:
                node = Node(bod)
                starters.append(node)
                starter.parent = node
            flag = True
            break
    for starter in starters:
        node = find(starter, lambda node: node.name == bod)
        if node != None:
            break
    else:
        node = Node(bod)
        starters.append(node)

    if flag:
        continue
    new = Node(orb, parent=node)

#print(total_steps)

for starter in starters:
    for pre, fill, node in RenderTree(starter):
        print("%s%s" % (pre, node.name))
total = 0
#for node in PreOrderIter(starters[0]):
#    print(node.depth)
#    total += node.depth
#print(total)

you = find(starters[0], lambda node: node.name == 'YOU')
node = you
transfers = 0
while True:
    parent = node.parent
    santa = find(parent, lambda node: node.name == 'SAN')
    if santa == None:
        node = parent
        transfers += 1
    else:
        transfers += santa.depth - parent.depth - 1
        print(transfers)
        break
#print(starter.children)
