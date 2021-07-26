'''
Задание 2.
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
'''

from random import randint

len_array = 10
max_value = 100
random_array = [randint(0, max_value) for _ in range(len_array)]
print(random_array)

output_array = [index for index in range(len(random_array)) if random_array[index] & 1 == 0]
print(output_array)