'''
Задание 1.
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Взял задачу №1 из 3/4 урока, т.к. я решил с минимальной сложностью.
К сожалению, не присутствовал на уроках. Но в записи и в методички смутило то, что 1Кб = 1000 б вместо положенных 1024.
Насколько помню, что 1Кб = 1000 байт используется лишь производителями жестких дисков. Но если речь идет об
оперативной памяти то это, на мой взгляд, не корректно.
'''

from time import time
import sys

range_values = (2, 999999)
range_divisors = (2, 999)
'''
Каждый кортеж занимаем по 200 байт (64-бит система), плюс 48 байт - 2 значения int. Итого на два кортежа
с параметрами занимают 496 байт.
'''

# Сложность моего алгоритма O(n) или O(8) для параметров заданных в условии
def my_decision(range_values, range_divisors):
    for divisor in range(range_divisors[0], range_divisors[1] + 1):
        # divisor занимает в моей системе занимает 24 байт (тип Int).
        count = (range_values[1] - range_values[0]) // divisor + \
                (1 if range_values[1] % divisor < range_values[0] % divisor else 0)
        # count занимает в моей системе занимает 24 байт (тип Int).
        print(f'{divisor} - {count}')


# Сложность алгоритма, предложенного Вами на разборе O(m) или O(98)
def teacher_decision(range_values, range_divisors):
    for i in range(range_divisors[0], range_divisors[1] + 1):
        # i - 24 байта
        counter = 0
        # counter - 24 байта
        for j in range(i, range_values[1] + 1, i):
        # j - 24 байта
            if j < range_divisors[1]:
                counter += 1
    print(f'{i} - {counter}')

# В моем алгоритме выделяется на 24 байта меньше под переменные. Хотя это мизер!

start_time = time()
# start_time - имеет тип float и занимает 24 байта
my_decision(range_values, range_divisors)
second_time = time()
# second_time - 24 байта
teacher_decision(range_values, range_divisors)
end_time = time()
# end_type - 24 байта

print(f'Мое решение со сложностью O(n): {second_time - start_time}')
print(f'Ваше решение со сложностью O(m): {end_time - second_time}')

'''
Мое решение со сложностью O(998): 0.024059772491455078
Ваше решение со сложностью O(999998): 1.30889892578125
Цикл, увеличивающий на 1 счетчик, явно лишний. Его быстрее посчитать арифметически
'''
