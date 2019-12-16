import math
import numpy as np

input = "123456"*10
offset = int(input[:7])
signal = [[int(d) for d in input]]

pattern = np.empty((len(signal[0]), len(signal[0])))
base = [0, 1, 0, -1]
for j in range(len(signal[0])):
    nbase = [item for sublist in [[x]*(j+1) for x in base] for item in sublist]
    multiplier = math.ceil((len(signal[0]) + 1)/len(nbase))
    applier = (nbase*multiplier)[1:len(signal[0])+1]
    for i, d in enumerate(pattern):
        pattern[i][j] = applier[i]

for k in range(100):
    result = np.matmul(signal, pattern)
    signal = [[int(str(int(x))[-1]) for x in result[0]]]
print(signal)