class Intcode:

    # initialization
    def __init__(self, intcode):
        # add additional memory
        n = 500
        self.intcode = intcode + [0]*n
        self.rel = 0

    # fetches a value based on the given parameter mode and index
    def fetch(self, mode, idx):
        if mode == 0:
            return self.intcode[self.intcode[idx]]
        elif mode == 1:
            return self.intcode[idx]
        elif mode == 2:
            return self.intcode[self.intcode[idx]+self.rel]

    # modifies the value at a certain position to equal output
    def modify(self, mode, idx, output):
        if mode == 0:
            self.intcode[self.intcode[idx]] = output
        elif mode == 2:
            self.intcode[self.intcode[idx]+self.rel] = output

    # main intcode program
    def run(self):
        i = 0
        c = 0
        inp = self.intcode
        # until the end of the program
        while i < len(inp):
            # the operation to be done
            oper = inp[i]

            # break immediately if it's 99
            if oper == 99:
                break
            else:
                # figure out the parameter modes
                str_oper = str(oper)
                for j in range(5 - len(str_oper)):
                    str_oper = '0' + str_oper

                opcode = int(str_oper[-2:])
                param1, param2, param3 = int(str_oper[-3]), int(str_oper[-4]), int(str_oper[-5])

                # actual functions
                if opcode == 1:
                    # add
                    c = 4
                    val1 = self.fetch(param1, i+1)
                    val2 = self.fetch(param2, i+2)
                    self.modify(param3, i+3, val1+val2)
                elif opcode == 2:
                    # multiply
                    c = 4
                    val1 = self.fetch(param1, i+1)
                    val2 = self.fetch(param2, i+2)
                    self.modify(param3, i+3, val1*val2)
                elif opcode == 3:
                    # take input
                    c = 2
                    var = int(input())
                    self.modify(param1, i+1, var)
                elif opcode == 4:
                    # print output
                    c = 2
                    print(self.fetch(param1, i+1))
                elif opcode in [5, 6]:
                    # clubbed together because they're similar
                    # sets instruction pointer to a value based on another value
                    c = 0
                    val1 = self.fetch(param1, i+1)
                    val2 = self.fetch(param2, i+2)

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
                    # compares values
                    c = 4
                    val1 = self.fetch(param1, i+1)
                    val2 = self.fetch(param2, i+2)
                    if opcode == 7:
                        if val1 < val2:
                            self.modify(param3, i+3, 1)
                        else:
                            self.modify(param3, i+3, 0)
                    if opcode == 8:
                        if val1 == val2:
                            self.modify(param3, i+3, 1)
                        else:
                            self.modify(param3, i+3, 0)
                elif opcode == 9:
                    # sets rel
                    c = 2
                    val1 = self.fetch(param1, i+1)
                    self.rel += val1

            i += c
        print(inp)
