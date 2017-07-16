# project euler 10
# in this code i tried to implement miller rabin primality test
# and in the end, i succeeded!
# but i found out that this test is not the best solution
# to find primes under 2M:/
# nevermind.


from random import randint
primes = [2]


def is_prime_vocal(n, loops):
    '''implementation of miller rabin primality test'''
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d = int(d / 2)
    i = 0
    print('s = ' + str(s))
    print('d = ' + str(d))
    while i < loops:
        a = randint(a=2, b=n - 2)
        print('a = ' + str(a))
        x = a ** d % n
        print('x = ' + str(x))
        if x == 1 or x == n - 1:
            i += 1
        else:
            for r in range(s):
                x = x ** 2 % n
                print('x' + str(r) + ' = ' + str(x))
                if x == 1:
                    return False
                    break
                elif x == n - 1:
                    i += 1
                    break
                elif r == s - 1:
                    return False
    return True


print(is_prime_vocal(17, 1))


def is_prime(n, loops):
    '''implementation of miller rabin primality test.
    this is silent version of the previous function,
    as it is testing quite a lot of numbers afterwards.
    I was actaully lazy to silent it another way'''
    if n % 5 == 0 or n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d = int(d / 2)
    i = 0
    # print('s = ' + str(s))
    # print('d = ' + str(d))
    while i < loops:
        a = randint(a=2, b=n - 2)
        # print('a = ' + str(a))
        x = a ** d % n
        # print('x = ' + str(x))
        if x == 1 or x == n - 1:
            i += 1
        else:
            for r in range(s):
                x = x ** 2 % n
                # print('x' + str(r) + ' = ' + str(x))
                if x == 1:
                    return False
                    break
                elif x == n - 1:
                    i += 1
                    break
                elif r == s - 1:
                    return False
    return True


primes = [2, 3, 5]
testnum = 7
while testnum < 20000:
    if is_prime(testnum, 10):
        print(testnum)
        primes.append(testnum)
    testnum += 2

print(sum(primes))

# and this is the moment where i found:
# well, this is just too slow.
