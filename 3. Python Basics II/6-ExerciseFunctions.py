# Exercise Functions
# Highest Even: Write a function to find the highest even number from the list.


def highest_even_num(nums=[]):
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)

    return max(evens)


print(highest_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def highest_even_num_faster(nums=[]):
    currentMax = 0
    for n in nums:
        if n % 2 == 0 and n > currentMax:
            currentMax = n

    return currentMax


print(highest_even_num_faster([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
