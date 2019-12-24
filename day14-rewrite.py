from math import ceil, floor


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


inp = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""

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

ore, leftovers = produce(reactants, {}, 1)
ore2, leftovers = produce(leftovers, {}, -1)
ore3, leftovers = produce(leftovers, {}, -1)
totes = ore - ore2 - ore3
print(totes)

# PART 2
numfuel = floor(1000000000000/totes)
for waste in leftovers:
    leftovers[waste] *= numfuel
ore4, leftovers = produce(leftovers, {}, -1)
ore5, leftovers = produce(leftovers, {}, -1)
ore6, leftovers = produce(leftovers, {}, -1)
print(floor((ore4+ore5+ore6)/totes))

print(numfuel)
