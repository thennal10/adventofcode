def validity_check(num):
    strnum = str(num)
    isblock, doubloon, flag = False, False, False
    blocks = []
    block = []
    for count, digit in enumerate(strnum):
        try:
            if int(digit) > int(strnum[count+1]):
                flag = True
                break
        except IndexError:
            pass

        if count != 0:
            if int(digit) == int(strnum[count - 1]):
                block.append(digit)
                if not isblock:
                    block.append(strnum[count - 1])
                    isblock = True
            else:
                if isblock:
                    blocks.append(block)
                    block = []
                    isblock = False

    if isblock:
        blocks.append(block)
        block = []
        isblock = False
    print(blocks)
    for bl in blocks:
        if len(bl) == 2:
            doubloon = True
            break

    if not flag and doubloon:
        return True
    else:
        return False

#print(validity_check(2244666))
c = 0
for i in range(147981, 691423):
   if validity_check(i):
        c += 1
print(c)