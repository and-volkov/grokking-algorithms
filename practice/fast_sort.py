"""Быстрая сортировка."""


def quicksort(arr):
    if len(arr) < 2:
        return arr  # Базовый случай
    else:
        pivot = arr[0]  # Рекурсивный случай (опорный элемент)
        less = [i for i in arr[1:] if i <= pivot]  # элементы меньше опорного
        greater = [i for i in arr[1:] if i > pivot]  # элементы больше опорного

        return quicksort(less) + [pivot] + quicksort(greater)
