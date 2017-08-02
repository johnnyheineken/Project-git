collatz_dict = {1: 1, 2: 2, 3: 7}


def collatz_length(number, coll_dictionary):
    steps = 0
    original = number
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            steps += 1
            if number < original:
                steps += coll_dictionary[number]
                break
        else:
            number = 3 * number + 1
            steps += 1
    return steps


i = 4

while i < 1000000:
    collatz_length = collatz_length(i, collatz_dict)
    collatz_dict[i] = collatz_length
    print(collatz_length)
    i += 1


print(max(collatz_dict, key=lambda k: collatz_dict[k]))
