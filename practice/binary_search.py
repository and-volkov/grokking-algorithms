"""Примеры и задача для бинарного поиска"""

"""
В отсортированном массиве каждый раз выбирается число в середине
И исключается половина оставшихся чисел
Сложность алгоритма = O(log n)
"""


def binary_search(list_of_items, item):
    low = 0
    high = len(list_of_items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_of_items[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


example_list = [1, 3, 5, 7, 9, 10]
print(binary_search(example_list, 7))
print(binary_search(example_list, -1))
