import numpy as np

class Intcode:

    # initialization
    def __init__(self, intcode):
        # add additional memory
        n = 500
        self.intcode = intcode + [0]*n
        self.rel = 0
        self.i = 0
        self.input = 0

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
        i = self.i
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
                    var = self.input
                    self.modify(param1, i+1, var)
                elif opcode == 4:
                    # print output
                    c = 2
                    yield self.fetch(param1, i+1)
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

def rotate(d, r):
    if r == 1:
        if d == [0, 1]:
            return [1, 0]
        elif d == [1, 0]:
            return [0, -1]
        elif d == [0, -1]:
            return [-1, 0]
        elif d == [-1, 0]:
            return [0, 1]
    elif r == 0:
        if d == [0, 1]:
            return [-1, 0]
        elif d == [-1, 0]:
            return [0, -1]
        elif d == [0, -1]:
            return [1, 0]
        elif d == [1, 0]:
            return [0, 1]

code = [3,8,1005,8,311,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,28,1,1104,0,10,1006,0,71,2,1002,5,10,2,1008,5,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,66,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,87,1006,0,97,2,1002,6,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,116,1006,0,95,1,1009,10,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,145,1,1002,19,10,2,1109,7,10,1006,0,18,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,179,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,200,1,1105,14,10,1,1109,14,10,2,1109,11,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,235,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,257,2,101,9,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,282,2,1109,19,10,1,105,0,10,101,1,9,9,1007,9,1033,10,1005,10,15,99,109,633,104,0,104,1,21102,937268368140,1,1,21102,328,1,0,1106,0,432,21102,1,932700599052,1,21101,0,339,0,1105,1,432,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,209421601831,1,21102,1,386,0,1106,0,432,21102,235173604443,1,1,21102,1,397,0,1106,0,432,3,10,104,0,104,0,3,10,104,0,104,0,21101,825439855372,0,1,21102,1,420,0,1106,0,432,21101,0,988220907880,1,21102,431,1,0,1106,0,432,99,109,2,22101,0,-1,1,21101,40,0,2,21102,1,463,3,21102,453,1,0,1106,0,496,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,458,459,474,4,0,1001,458,1,458,108,4,458,10,1006,10,490,1102,1,0,458,109,-2,2106,0,0,0,109,4,2102,1,-1,495,1207,-3,0,10,1006,10,513,21102,0,1,-3,22102,1,-3,1,21202,-2,1,2,21102,1,1,3,21101,532,0,0,1105,1,537,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,560,2207,-4,-2,10,1006,10,560,21201,-4,0,-4,1106,0,628,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,579,0,1106,0,537,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,598,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,620,21201,-1,0,1,21102,1,620,0,105,1,495,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
robot = Intcode(code)

grid = np.zeros((2, 200, 200))
pos = [100, 100]
grid[0][pos[1]][pos[0]] = 1
direction = [1, 0]
program = robot.run()
while True:
    robot.input = grid[0][pos[1]][pos[0]]
    try:
        paint = next(program)
        rotation = next(program)
    except StopIteration:
        print(np.count_nonzero(grid[1]))
        break

    grid[0][pos[1]][pos[0]] = paint
    grid[1][pos[1]][pos[0]] = 1
    direction = rotate(direction, rotation)
    pos[0] += direction[0]
    pos[1] += direction[1]
