def sum_arr(arr):
    """Сумма всех элементов списка"""
    if not arr:
        return 0
    else:
        return arr[0] + sum_arr(arr[1:])


def arr_count(arr):
    """Подсчет элементов списка"""
    counter = 0
    if not arr:
        return 0
    else:
        return (counter + 1) + arr_count(arr[1:])


def arr_max(arr):
    """Максимальное значение в списке."""
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = arr_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
