'''
Задание 5.
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''

from random import randint

len_array = 20
min_value = -10
max_value = 10
random_array = [randint(min_value, max_value) for _ in range(len_array)]

print(random_array)

max_value = (-1, 0)
for index, value in enumerate(random_array):
    if value < 0 and (max_value[0] < 0 or max_value[1] < value):
        max_value = (index, value)

if max_value[0] < 0:
    print('Отрицательных чисел в массиве нет')
else:
    print(f'Индекс: {max_value[0]}, значение: {max_value[1]}')
