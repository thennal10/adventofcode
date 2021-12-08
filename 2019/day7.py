from itertools import permutations

def param_modes(mode, list, idx):
    if mode == 0:
        return list[list[idx]]
    elif mode == 1:
        return list[idx]

class Amplifier():
    def __init__(self, intcode):
        self.intcode = intcode
        self.i = 0

    def func(self, ls):
        i = self.i
        inp = self.intcode
        c = 0
        in_ls = ls
        while i < len(inp):
            oper = inp[i]

            if oper == 99:
                return "HALT!"
                break
            else:
                str_oper = str(oper)
                for j in range(5 - len(str_oper)):
                    str_oper = '0' + str_oper

                opcode = int(str_oper[-2:])

                if opcode == 1:
                    c = 4
                    val1 = param_modes(int(str_oper[-3]), inp, i+1)
                    val2 = param_modes(int(str_oper[-4]), inp, i+2)
                    inp[inp[i + 3]] = val1 + val2
                elif opcode == 2:
                    c = 4
                    val1 = param_modes(int(str_oper[-3]), inp, i+1)
                    val2 = param_modes(int(str_oper[-4]), inp, i+2)
                    inp[inp[i + 3]] = val1*val2
                elif opcode == 3:
                    c = 2
                    inp[inp[i+1]] = int(in_ls[0])
                    try:
                        in_ls = [in_ls[1]]
                    except Exception:
                        pass
                elif opcode == 4:
                    c = 2
                    self.i = i+2
                    return param_modes(int(str_oper[-3]), inp, i+1)
                elif opcode in [5, 6]:
                    c = 0
                    val1 = param_modes(int(str_oper[-3]), inp, i + 1)
                    val2 = param_modes(int(str_oper[-4]), inp, i + 2)

                    if opcode == 5:
                        if val1 != 0:
                            i = val2
                        else:
                            c = 3
                    elif opcode == 6:
                        if val1 == 0:
                            i = val2
                        else:
                            c = 3
                elif opcode in [7, 8]:
                    c = 4
                    val1 = param_modes(int(str_oper[-3]), inp, i + 1)
                    val2 = param_modes(int(str_oper[-4]), inp, i + 2)
                    if opcode == 7:
                        if val1 < val2:
                            inp[inp[i + 3]] = 1
                        else:
                            inp[inp[i + 3]] = 0
                    if opcode == 8:
                        if val1 == val2:
                            inp[inp[i + 3]] = 1
                        else:
                            inp[inp[i + 3]] = 0
            i += c
        print(inp)

inp = [3,8,1001,8,10,8,105,1,0,0,21,38,55,80,97,118,199,280,361,442,99999,3,9,101,2,9,9,1002,9,5,9,1001,9,4,9,4,9,99,3,9,101,5,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,1001,9,4,9,102,5,9,9,101,4,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,3,9,9,4,9,99,3,9,101,5,9,9,1002,9,2,9,101,3,9,9,1002,9,5,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
#inp = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
#27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# Get all permutations of [1, 2, 3]
perms = permutations([5, 6, 7, 8, 9])
# Print the obtained permutations
maxim = 0
for perm in perms:
    amplifiers = [Amplifier(inp.copy()) for amp in range(5)]

    #first loop
    res = 0
    for c, amplifier in enumerate(amplifiers):
        res = amplifier.func([perm[c], res])
    i = 0
    while True:
        if i > 4:
            i = 0
        res = amplifiers[i].func([res])
        if res == "HALT!":
            break
        elif res > maxim:
            maxim = res
        i += 1

print(maxim)
