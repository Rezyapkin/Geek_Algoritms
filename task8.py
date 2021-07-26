'''
Задание 8.
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
'''

m = 5
n = 4
array = []

for i in range(n):
    print(f'Сторка {i+1}')
    current_sum = 0
    array.append([])
    for j in range(m-1):
        value = int(input())
        array[i].append(value)
        current_sum += value

    array[i].append(current_sum)

for i in range(n):
    s = ""
    for j in range(m):
        s += f'{array[i][j]:5} '
    print(s)
