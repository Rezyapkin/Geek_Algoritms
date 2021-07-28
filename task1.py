'''
Задание 1.
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Взял задачу №1 из 3-ого урока, т.к. я решил с минимальной сложностью.
Пусть n - количество делителей, m - количество проверямых чисел на деление (n = 8, m = 98 по условиям)
'''

from time import time

range_values = (2, 999999)
range_divisors = (2, 999)

# Сложность моего алгоритма O(n) или O(8) для параметров заданных в условии
def my_decision(range_values, range_divisors):
    for divisor in range(range_divisors[0], range_divisors[1] + 1):
        count = (range_values[1] - range_values[0]) // divisor + \
                (1 if range_values[1] % divisor < range_values[0] % divisor else 0)
        print(f'{divisor} - {count}')


# Сложность алгоритма, предложенного Вами на разборе O(m) или O(98)
def teacher_decision(range_values, range_divisors):
    for i in range(range_divisors[0], range_divisors[1] + 1):
        counter = 0
        for j in range(i, range_values[1] + 1, i):
            if j < range_divisors[1]:
                counter += 1
    print(f'{i} - {counter}')


start_time = time()
my_decision(range_values, range_divisors)
second_time = time()
teacher_decision(range_values, range_divisors)
end_time = time()

print(f'Мое решение со сложностью O(n): {second_time - start_time}')
print(f'Ваше решение со сложностью O(m): {end_time - second_time}')

'''
Мое решение со сложностью O(998): 0.024059772491455078
Ваше решение со сложностью O(999998): 1.30889892578125
Цикл, увеличивающий на 1 счетчик, явно лишний. Его быстрее посчитать арифметически
'''
