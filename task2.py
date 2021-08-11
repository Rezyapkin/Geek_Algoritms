'''
Задание 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
from random import randint


# Реализовал без заведения новых массивов каждый раз. Все происходит внутри массива
def merge_sort(input_list, start=0, stop=-1):
    if stop == - 1:
        stop = len(input_list) - 1

    if start >= stop:
        return input_list

    middle = (stop - start) // 2
    merge_sort(input_list, start, start + middle)
    merge_sort(input_list, start + middle + 1, stop)

    i = start
    j = start + middle + 1

    while i <= start + middle and i <= stop and j <= stop:
        if input_list[i] > input_list[j]:
            input_list.insert(i, input_list.pop(j))
            middle += 1
            j += 1
        i += 1

    return input_list


a = [randint(0, 50) for _ in range(20)]
print(a)

print(merge_sort(a))
