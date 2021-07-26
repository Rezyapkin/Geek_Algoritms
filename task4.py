'''
Задание 4.
4. Определить, какое число в массиве встречается чаще всего.
'''

from random import randint

len_array = 100
max_value = 10
random_array = [randint(0, max_value) for _ in range(len_array)]

print(random_array)
count_values = {}

for value in random_array:
    if value in count_values.keys():
        count_values[value] += 1
    else:
        count_values[value] = 1

max_value = (0, 0)
for key, value in count_values.items():
    if value > max_value[1]:
        max_value = key, value

print(f'Число {max_value[0]} встретилось чаще всего ({max_value[1]})')
