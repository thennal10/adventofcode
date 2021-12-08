import math

inp = """deal with increment 46
cut 679
deal into new stack
deal with increment 50
cut -9441
deal into new stack
cut 3142
deal with increment 35
cut -5753
deal with increment 33
cut -7554
deal into new stack
deal with increment 29
deal into new stack
cut 9611
deal into new stack
deal with increment 33
cut 9851
deal with increment 48
cut 2187
deal with increment 43
cut 7371
deal with increment 61
cut -7807
deal with increment 43
cut 443
deal into new stack
cut 4405
deal with increment 41
cut 4281
deal with increment 31
cut 1211
deal with increment 62
cut 1970
deal into new stack
deal with increment 60
cut -5057
deal with increment 59
cut -8537
deal with increment 30
deal into new stack
deal with increment 13
cut 9313
deal with increment 17
deal into new stack
deal with increment 2
cut 9199
deal with increment 29
cut 4299
deal with increment 34
cut -1599
deal with increment 53
cut 176
deal into new stack
deal with increment 16
cut -1292
deal with increment 49
cut 6401
deal with increment 32
cut -7177
deal with increment 70
cut -486
deal with increment 16
deal into new stack
cut -39
deal with increment 19
deal into new stack
deal with increment 53
cut 3475
deal with increment 42
cut -4515
deal with increment 27
cut -140
deal with increment 60
deal into new stack
cut -3470
deal with increment 42
cut -3952
deal with increment 20
cut 2394
deal with increment 72
cut 8012
deal with increment 54
cut 3503
deal with increment 60
cut -5474
deal with increment 30
cut 9038
deal with increment 41
cut 5497
deal with increment 27
cut -9002
deal into new stack
deal with increment 30
cut -8369
deal with increment 15
cut 610
deal into new stack
deal with increment 64
cut 2470"""


total = 119315717514047
pos = 2020
convert = {}
for t in range(101741582076661):
    try:
        pos = convert[pos]
        print("hey")
    except KeyError:
        old_pos = pos
        for instr in inp.split('\n'):
            if instr == 'deal into new stack':
                pos = total - 1 - pos
            elif instr[:3] == 'cut':
                cut = int(instr[3:])
                pos = (pos - cut) % total
            elif instr[:19] == 'deal with increment':
                inc = int(instr[19:])
                pos = (pos*inc) % total
        convert[old_pos] = pos
print(pos)
