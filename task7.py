'''
Задание 7.
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''

from random import randint


len_array = 10
max_value = 100
random_array = [randint(0, max_value) for _ in range(len_array)]
print(random_array)

count_min = 2
array_min = []  # Отсортированный по возрастанию массив найденных минимумов

for value in random_array:
    if count_min > len(array_min) or array_min[-1] > value:
        # Ищем в какое место массива array_min вставить значение
        index = 0
        while index < len(array_min):
            if array_min[index] > value:
                break
            index += 1

        # Вставляем значение в нужную позицию
        array_min.insert(index, value)

        # Отсекаем лишнее
        if len(array_min) > count_min:
            array_min.pop()

print(array_min)
