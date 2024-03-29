from math import ceil, floor
import copy

class Reaction():

    def __init__(self, reactants, product):
        self.reactants = reactants
        self.product = product


def produce(r, lefts, mode):
    reactants = r
    leftovers = lefts
    while True:
        for reactant in [x for x in reactants if x != 'ORE']:
            reaction = [x for x in reactions if reactant in x.product][0]

            produced_q = reaction.product[reactant]
            required_q = reactants[reactant]

            if mode == 1:
                multiplier = ceil(required_q/produced_q)
            elif mode == -1:
                multiplier = floor(required_q/produced_q)

            try:
                leftovers[reactant] += ((produced_q * multiplier) - required_q) * mode
            except KeyError:
                leftovers[reactant] = ((produced_q * multiplier) - required_q) * mode

            for r2 in reaction.reactants:
                try:
                    reactants[r2] += reaction.reactants[r2] * multiplier
                except KeyError:
                    reactants[r2] = reaction.reactants[r2] * multiplier
            del reactants[reactant]
        if len(reactants) == 1:
            return reactants['ORE'], leftovers


inp = """164 ORE => 2 TLJL
2 VKMKW => 4 DTCB
2 VKMKW, 16 ZKMXZ, 2 TSVN => 3 TSVQX
2 NFJKN, 2 LMVCD, 5 DSQLK => 1 RNRPB
3 NFJKN, 3 TSVQX, 6 VKMKW => 7 FBFQZ
7 ZKMXZ, 1 PVQLR => 4 MBWVZ
3 SHMGH => 4 ZKMXZ
2 MSZWL => 4 QSDC
3 DGFK => 9 TSVN
21 DTCB, 1 DSQLK => 8 DGDGS
1 DGFK, 1 SXNZP, 1 GCHL => 9 JZWH
1 DSQLK, 4 WFDK, 1 BVSL, 1 TZND, 15 HVPMK, 1 NSKX => 3 DSFDZ
1 ZDVCH, 2 PVQLR, 7 VLNX, 4 JTZM, 1 MVLHV, 1 RDBR, 11 MBWVZ => 7 ZTXQ
9 JZWH, 4 BVSL, 2 NFJKN, 26 LMVCD, 3 MKFDR, 2 TGMNG, 1 NTMRX, 12 DGDGS => 4 PBRZF
25 RNRPB => 6 MKFDR
27 ZKMXZ, 4 NFJKN, 1 DTCB => 5 RDBR
2 ZXTQ, 13 KHRFD => 7 JQJGR
3 WFDVM, 18 QSLKV => 5 NSBN
2 ZXTQ, 6 NTMRX => 4 WFDK
1 VKMKW, 14 TSVQX, 10 ZKMXZ => 6 NFJKN
1 NVDL, 1 ZKMXZ, 9 NSKX => 5 ZDVCH
7 QSDC, 1 BVSL => 4 GCHL
1 QSLKV, 13 XRBKF => 5 NTMRX
11 GDPLN => 8 KHRFD
15 VCJSD => 7 LSLP
4 PCHC, 1 SXNZP, 1 JQJGR => 9 KPBPL
18 TGMNG => 4 HVPMK
1 XRBKF, 26 LVLV => 6 WFDVM
9 VCJSD, 14 SXNZP => 4 TGMNG
22 WFDK, 20 FBFQZ => 6 LHJBH
195 ORE => 7 SHMGH
2 VCJSD, 1 XRBKF => 8 QSLKV
8 ZTXNJ, 4 TLJL => 2 MSZWL
2 LMVCD, 9 PVQLR => 4 NSKX
2 TLJL, 1 GJDPC, 8 ZXTQ => 8 PCHC
6 NSBN, 4 JVJV => 9 ZCDZ
155 ORE => 1 GDPLN
1 GDPLN => 4 VKMKW
1 KPBPL => 8 LVLV
30 NSBN, 20 MVLHV => 1 JVJV
1 LVLV => 1 DGFK
7 TSVQX => 6 LMVCD
7 TLJL, 16 MSZWL, 5 KHRFD => 2 ZXTQ
55 MBWVZ, 61 KHRFD, 16 DSFDZ, 40 LHJBH, 6 ZTXQ, 28 JZWH, 1 PBRZF => 1 FUEL
5 JQJGR, 20 VCJSD => 5 MVLHV
1 SHMGH, 1 ZTXNJ => 4 GJDPC
3 XRBKF, 9 QSLKV, 2 WFDK => 5 JTZM
5 GJDPC => 6 VCJSD
1 GJDPC, 7 XRBKF => 4 PVQLR
11 BVSL => 6 SXNZP
104 ORE => 3 ZTXNJ
3 JZWH, 9 HVPMK, 2 GCHL => 6 VLNX
1 LSLP => 6 XRBKF
1 TLJL => 5 BVSL
5 HVPMK => 9 DSQLK
6 FBFQZ, 22 PVQLR, 4 ZCDZ => 1 NVDL
3 JZWH => 1 TZND"""

reactions = []
for line in inp.split('\n'):
    left, right = line.split(' => ')
    reactants = {}
    for mat in left.split(', '):
        split = mat.split(' ')
        quantity, symbol = int(split[0]), split[1]
        reactants[symbol] = quantity

    split = right.split(' ')
    quantity, symbol = int(split[0]), split[1]
    product = {symbol: quantity}
    reactions.append(Reaction(reactants, product))

daddy = [x for x in reactions if 'FUEL' in x.product][0]
reactants = daddy.reactants
og_reactants = copy.deepcopy(reactants)

ore, leftovers = produce(reactants, {}, 1)
ore2, leftovers = produce(leftovers, {}, -1)
ore3, leftovers = produce(leftovers, {}, -1)
totes = ore - ore2 - ore3
print(totes)
print(leftovers)

# PART 2
#2249610
m = 2371651
while True:
    nreactants = {k: og_reactants[k]*m for k in og_reactants}

    ore, leftovers = produce(nreactants, {}, 1)
    ore2, leftovers = produce(leftovers, {}, -1)
    ore3, leftovers = produce(leftovers, {}, -1)
    totes = ore - ore2 - ore3
    print(totes)
    print(m)
    m += 1


old_m = floor(1000000000000/totes)
m = 2*old_m
min = old_m
max = m
while True:
    nreactants = {k: og_reactants[k]*m for k in og_reactants}

    ore, leftovers = produce(nreactants, {}, 1)
    ore2, leftovers = produce(leftovers, {}, -1)
    ore3, leftovers = produce(leftovers, {}, -1)
    totes = ore - ore2 - ore3
    print(totes)
    print(m)
    if totes > 1000000000000:
        max = m
        old_m = m
        m = floor((max + min)/2)
    else:
        max = old_m
        min = m
        old_m = m
        m = floor((max + min)/2)

