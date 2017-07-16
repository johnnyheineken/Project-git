# project euler 10 - sieve of erasthothenes


def primes(n):
    '''this function takes in the number up to which we would like to output
    primes. it also uses some best practices,
    where there is prespecified list of True values'''
    primes = [True] * n
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i ** 2::i] = [False] * len(primes[i ** 2::i])
    return [j for j in range(2, n) if primes[j]]


print(sum(primes(2000000)))
