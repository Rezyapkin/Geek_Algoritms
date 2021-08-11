'''
Задание 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
'''
from random import randint


# В качестве усовершенствования сделал двустороннюю сортировку
def sort_bubble(input_list, desc=False):
    for i in range(len(input_list)):
        for j in range(i, len(input_list)):
            if (input_list[i] > input_list[j]) ^ desc:
                input_list[i], input_list[j] = input_list[j], input_list[i]

    return input_list


a = [randint(-100, 100) for _ in range(20)]
print(a)

print(sort_bubble(a, True))
