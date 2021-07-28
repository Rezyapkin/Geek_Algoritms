'''
Задание 2.
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
'''

import math, time

# Два цикла, сложность похожа на O(n^2)
def find_simple_without_eratosthenes(i):
    values = [2]
    current_value = 1
    while len(values) < i:
        current_value += 1
        is_simple = True
        for value in values:
            if current_value % value == 0:
                is_simple = False
                break

        if is_simple:
            values.append(current_value)

    return values[-1]


# Проблема в том как выбрать границы массива для решета я подобрал как n * log2 n.
def find_simple_with_eratosthenes(i):
    sieve_eratosthenes = [value for value in range(2, math.ceil(i * math.log2(i)))]
    index = 0
    value = 2
    cur_index = 0
    while index < i and cur_index < len(sieve_eratosthenes):
        if sieve_eratosthenes[cur_index] > 0:
            index += 1
            value = sieve_eratosthenes[cur_index]

            for j in range(value + cur_index, len(sieve_eratosthenes), value):
                sieve_eratosthenes[j] = 0

        cur_index += 1

    return value if index == i else None

start_time = time.time()
print(find_simple_without_eratosthenes(10000))
second_time = time.time()
print(find_simple_with_eratosthenes(10000))
end_time = time.time()

print(f'Без Решета Эратосфена со сложностью O(n^2): {second_time - start_time}')
print(f'C Решетом Эратосфена со сложностью O(n log n): {end_time - second_time}')

'''
С решетом Эратосфена быстрее, но требуется много памяти.
Для n = 10000:
Без Решета Эратосфена со сложностью O(n^2): 9.121320247650146
C Решетом Эратосфена со сложностью O(n log n): 0.07995772361755371
'''
