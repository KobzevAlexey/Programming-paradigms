# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

import random


def create_numbers(length, minimum, maximum):
    numbers = []
    for el in range(length):
        numbers.append(random.randint(minimum, maximum))
    return numbers


def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


numbers = create_numbers(10, 1, 10)
print(numbers)
sorted_numbers = sort_list_imperative(numbers)
print(sorted_numbers)
