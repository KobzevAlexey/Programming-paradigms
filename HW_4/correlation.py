import math
from functools import reduce

def calculate_mean(arr):
    # Рассчитываем среднее значение
    return sum(arr) / len(arr)

def calculate_standard_deviation(arr, mean):
    # Рассчитываем среднеквадратическое отклонение
    deviation = map(lambda x: (x - mean) ** 2, arr) # Вычисляем квадрат разности каждого элемента среднего значения
    variance = reduce(lambda a, b: a + b, deviation) / len(arr) # Суммируем квадраты разностей и делим на количество элементов
    return math.sqrt(variance) # Вычисляем квадратный корень из дисперсии

def calculate_covariance(arr1, arr2):
    mean1 = calculate_mean(arr1)
    mean2 = calculate_mean(arr2)

    # Рассчитываем ковариацию
    deviation_product = map(lambda x, y: (x - mean1) * (y - mean2), arr1, arr2) # Вычисляем произведение разностей элементов массивов
    covariance = reduce(lambda a, b: a + b, deviation_product) / len(arr1) # Суммируем произведения разностей и делим на количество элементов
    return covariance

def calculate_pearson_correlation(arr1, arr2):
    # Рассчитываем корреляцию Пирсона
    covariance = calculate_covariance(arr1, arr2)
    std_deviation1 = calculate_standard_deviation(arr1, calculate_mean(arr1))
    std_deviation2 = calculate_standard_deviation(arr2, calculate_mean(arr2))
    return covariance / (std_deviation1 * std_deviation2)

x = [1, 2, 3, 4, 5]
y = [2, 3, 6, 8, 10]

correlation = calculate_pearson_correlation(x, y)
print("Корреляция Пирсона: ", correlation)