# project euler 12
def get_divisors(number):
    div_number = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            div_number += 1
    return(div_number * 2)


counter = 1
i = 1
while get_divisors(i) < 500:
    print(i)
    counter += 1
    i += counter

print(get_divisors(i))
print(i)
