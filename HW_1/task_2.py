# Задача №2
# Дан список целых чисел numbers. Необходимо написать в декларативном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

import random


def create_numbers(length, minimum, maximum):
    numbers = []
    for el in range(length):
        numbers.append(random.randint(minimum, maximum))
    return numbers

def sort_list_declarative(numbers):
    numbers = sorted(numbers, reverse=True)
    return numbers

numbers = create_numbers(10, 1, 10)
print(numbers)
sorted_numbers = sort_list_declarative(numbers)
print(sorted_numbers)