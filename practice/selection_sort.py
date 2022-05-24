"""Сортировка выбором"""

"""
Нужно проверить каждый элемент в списке O(n)
И эту операцию необходимо провести n раз
Сложность О(n**2)
"""


def find_smallest(arr) -> int:
    """Находит наименьшее значение в массиве"""
    smallest = arr[0]  # хранение наименьшего значения
    smallest_index = 0  # хранение индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """Алгоритм сортировки выбором"""
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # находит наименьший элемент
        new_arr.append(arr.pop(smallest))  # добавляет его в новый массив
    return new_arr


test_list = [5, 1, 3, 2, 8, 4]

print(selection_sort(test_list))
