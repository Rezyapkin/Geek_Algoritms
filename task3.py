'''
Задание 3.
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

from random import randint

len_array = 10
max_value = 100
random_array = [randint(0, max_value) for _ in range(len_array)]
print(random_array)

min_ = (0, random_array[0])
max_ = (0, random_array[0])

for index, value in enumerate(random_array):
    if value < min_[1]:
        min_ = index, value
    if value > max_[1]:
        max_ = index, value

random_array[min_[0]], random_array[max_[0]] = random_array[max_[0]], random_array[min_[0]]

print(random_array)
