import math

class Reaction:
    def __init__(self, reactants, products):
        self.r = reactants
        self.p = products


def decompose(products, reactions):
    leftovers = {}
    reactants = products
    while True:
        n_reactants = []
        for reactant in reactants:

            if reactant[0] == "ORE":
                n_reactants.append(reactant)
                continue

            creation = [x for x in reactions if x.p[0] == reactant[0]][0]

            ratio = math.ceil(reactant[1] / creation.p[1])
            if ratio == 0:
                multiplier = 1
            else:
                multiplier = ratio

            leftover = (creation.p[1] * multiplier) - reactant[1]
            if leftover > 0:
                try:
                    leftovers[reactant[0]] += leftover
                except KeyError:
                    leftovers[reactant[0]] = leftover

            raws = creation.r
            for raw in raws:
                nraw = raw.copy()
                nraw[1] = nraw[1] * multiplier
                n_reactants.append(nraw)
        reactants = n_reactants

        for r in n_reactants:
            if r[0] != 'ORE':
                break
        else:
            break

    print(reactants)
    ores = sum([r[1] for r in reactants])
    return ores, leftovers


def utilize(products, reactions):
    leftovers = {}
    reactants = products
    while True:
        n_reactants = {}
        for reactant in reactants.copy():

            if reactant == "ORE":
                n_reactants[reactant] = reactants[reactant]
                continue

            creation = [x for x in reactions if x.p[0] == reactant][0]

            if creation.p[1] > reactants[reactant]:
                n_reactants[reactant] = reactants[reactant]
                continue
            ratio = math.floor(reactants[reactant] / creation.p[1])
            if ratio == 0:
                multiplier = 1
            else:
                multiplier = ratio

            leftover = reactants[reactant] - (creation.p[1] * multiplier)
            if leftover > 0:
                try:
                    leftovers[reactant] += leftover
                except KeyError:
                    leftovers[reactant] = leftover

            raws = creation.r
            for raw in raws:
                nraw = raw.copy()
                nraw[1] = nraw[1] * multiplier
                try:
                    n_reactants[nraw[0]] += nraw[1]
                except KeyError:
                    n_reactants[nraw[0]] = nraw[1]
        reactants = n_reactants

        for r in n_reactants:
            if r == 'ORE':
                continue
            creation = [x for x in reactions if x.p[0] == r][0]
            if creation.p[1] < reactants[r]:
                break
        else:
            break

    for k in reactants:
        if k == 'ORE':
            continue
        else:
            try:
                leftovers[k] += reactants[k]
            except KeyError:
                leftovers[k] = reactants[k]
    return reactants['ORE'], leftovers


input = """164 ORE => 2 TLJL
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
for line in input.split('\n'):
    left, right = line.split(' => ')
    reactants = []
    for mat in left.split(', '):
        split = mat.split(' ')
        quantity, symbol = int(split[0]), split[1]
        reactants.append([symbol, quantity])

    split = right.split(' ')
    quantity, symbol = int(split[0]), split[1]
    products = [symbol, quantity]
    reactions.append(Reaction(reactants, products))


daddy = [x for x in reactions if x.p[0] == 'FUEL'][0]
products = daddy.r
ores, leftovers = decompose(products, reactions)
print(ores)
#leftovers = [[k, leftovers[k]] for k in leftovers]
print(leftovers)
minus = 0
while True:
    try:
        nores, leftovers = utilize(leftovers, reactions)
        print(leftovers)
    except KeyError:
        break
    minus += nores
print(ores - minus)

