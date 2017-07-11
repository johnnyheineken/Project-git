def is_pyth(num1, num2, num3):
    return (num1 ** 2 + num2 ** 2) == num3 ** 2

result = []
for i in range(1, 500):
    print(i)
    for j in range(1, 500):
        k = 1000 - i - j
        if is_pyth(i,j,k):
            result.append([i, j, k])

print(result)
print(200 * 375 * 425)