from functools import reduce

input = open('./input.txt').readlines()[0]
binary = "".join([str(bin(int(c, 16))[2:].zfill(4)) for c in input])

def parse(packet):
    vsum = 0
    vsum += int(packet[:3], 2)
    type = int(packet[3:6],2)
    if type == 4:
        total = ''
        for i, c in enumerate(packet[6::5]):
            total += packet[7+(5*i):11+(5*i)]
            if c == '0':
                break
        return int(total, 2), vsum, (i*5) + 11
    else:
        id = packet[6]
        pointer = 0
        totls = []
        if id == '0':
            length = int(packet[7:22], 2)
            while length - pointer:
                stot, sver, slen = parse(packet[22+pointer:])
                vsum += sver 
                pointer += slen
                totls.append(stot)
            pointer += 22
        else:
            num_sub = int(packet[7:18], 2)
            for i in range(num_sub):
                stot, sver, slen = parse(packet[18+pointer:])
                vsum += sver 
                pointer += slen
                totls.append(stot)
            pointer += 18
        
        match type:
            case 0: total = sum(totls)
            case 1: total = reduce(lambda x, y: x*y, totls, 1)
            case 2: total = min(totls)
            case 3: total = max(totls)
            case 5: total = int(totls[0] > totls[1])
            case 6: total = int(totls[0] < totls[1])
            case 7: total = int(totls[0] == totls[1])
        
        return total, vsum, pointer
            
output = parse(binary)
print(output[1])
print(output[0])