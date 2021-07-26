'''
Задание 9.
Найти максимальный элемент среди минимальных элементов столбцов матрицы
'''

from random import randint

m = 10
n = 5
# Заполним массив случайными числами
array = [[randint(0, 10) for _ in range(m)] for _ in range(n)]

# Выведем матрицу на экран
for i in range(n):
    s = ""
    for j in range(m):
        s += f'{array[i][j]:5} '
    print(s)

# Найдем искомое значение без промежуточного массива
result = None
for j in range(m):
    min_in_col = None
    for i in range(n):
        if min_in_col is None or min_in_col > array[i][j]:
            min_in_col = array[i][j]

    if result is None or min_in_col > result:
        result = min_in_col

print(result)
