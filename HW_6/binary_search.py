def binary_search(arr, target):
    left = 0                 # Установка начального левого индекса
    right = len(arr) - 1     # Установка начального правого индекса

    while left <= right:     # Пока левый индекс не превышает правый
        mid = left + (right - left) // 2     # Находим средний индекс

        if arr[mid] == target:   # Если средний элемент равен целевому
            return mid           # Возвращаем индекс среднего элемента
        elif arr[mid] < target:  # Если средний элемент меньше целевого
            left = mid + 1       # Сдвигаем левую границу поиска
        else:                    # Если средний элемент больше целевого
            right = mid - 1      # Сдвигаем правую границу поиска

    return -1   # Если элемент не найден, возвращаем -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_number = 8


result = binary_search(array, target_number)

if result != -1:
    print(f"Элемент {target_number} найден на позиции {result}.")
else:
    print(f"Элемент {target_number} не найден в массиве.")