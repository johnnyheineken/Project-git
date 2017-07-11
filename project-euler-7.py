# project euler 7
primes = [2]


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        sqrtnum = int(number ** 0.5) + 1
        primes_subset = [i for i in primes if i < sqrtnum]
        if all([number % i != 0 for i in primes_subset]):
            return True
        else:
            return False


num = 3
while len(primes) < 10002:
    if is_prime(num):
        primes.append(num)
        print(num)
    num = num + 2
