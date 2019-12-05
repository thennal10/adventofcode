
def func():
    og_inp = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,6,23,2,6,23,27,2,27,9,31,1,5,31,35,1,35,10,39,2,39,9,43,1,5,43,47,2,47,10,51,1,51,6,55,1,5,55,59,2,6,59,63,2,63,6,67,1,5,67,71,1,71,9,75,2,75,10,79,1,79,5,83,1,10,83,87,1,5,87,91,2,13,91,95,1,95,10,99,2,99,13,103,1,103,5,107,1,107,13,111,2,111,9,115,1,6,115,119,2,119,6,123,1,123,6,127,1,127,9,131,1,6,131,135,1,135,2,139,1,139,10,0,99,2,0,14,0]
    inp = og_inp.copy()
    for noun in range(99):
        for verb in range(99):

            inp[1] = noun
            inp[2] = verb
            for i in range(0, len(inp), 4):
                oper = inp[i]
                pos1 = inp[i+1]
                pos2 = inp[i+2]
                respos = inp[i+3]

                if oper == 1:
                    res = inp[pos1] + inp[pos2]
                elif oper == 2:
                    res = inp[pos1]*inp[pos2]
                elif oper == 99:
                    break

                try:
                    inp[respos] = res
                except IndexError:
                    break
            print(inp)

            if inp[0] == 19690720:
                print(noun)
                print(verb)
                return noun, verb
            inp = og_inp.copy()

func()