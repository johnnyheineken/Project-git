

def binomial(prev_bin):
    pyramide = [0] + prev_bin + [0]
    result = []
    for i in range(len(pyramide) - 1):
        result += [sum(pyramide[i:i + 2])]
    return result



res = [1]
i = 1
while i < 41:
    res = binomial(res)
    i += 1

print(max(res))