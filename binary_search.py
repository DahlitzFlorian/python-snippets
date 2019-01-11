import random


def binary_search(lst, integer):

    lower_bound = 0
    upper_bound = len(lst) - 1
    number_guesses = 0

    while True:
        index = (lower_bound + upper_bound) // 2

        guess = lst[index]
        number_guesses += 1

        if guess == integer:
            break

        if guess > integer:
            upper_bound = index - 1
        else:
            lower_bound = index + 1

    return number_guesses


print("Number Guesses")

for _ in range(30):
    integers = random.sample(range(50000), 10000)

    integer_to_find = random.choice(integers)

    sorted_integers = sorted(integers)

    guesses = binary_search(sorted_integers, integer_to_find)

    print("{:6} {:7}".format(integer_to_find, guesses))
