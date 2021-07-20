'''
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''

import random


# Не нашел как по другому вызывать функцию по ее имени
def call_my_func(func_name, arg):
    functions = {'int': int, 'float': float, 'str': str}
    return functions[type](arg)


# Решил написать универсальную функцию определения подходящего типа параметров
def get_type_args(*args):
    cur_type = 'int'

    for arg in args:
        while cur_type != 'str':
            try:
                call_my_func(cur_type, arg)
                break

            except ValueError:
                if cur_type == 'int':
                    cur_type = 'float'
                else:
                    cur_type = 'str'

        if cur_type == 'str':
            break

    return cur_type


s1 = input('Введите левую границу диапазона ')
s2 = input('Введите правую границу диапазона ')

# Определим тип введенных значений
our_type = get_type_args(s1, s2)

v1 = call_my_func(our_type, s1)
v2 = call_my_func(our_type, s2)

# Если правая граница меньше левой
if v2 < v1:
    v1, v2 = v2, v1

if our_type == 'int':
    result = random.randint(v1, v2)
elif our_type == 'float':
    result = v1 + (v2 - v1) * random.random()
elif len(v1) == 1 and len(v2) == 1:
    result = chr(random.randint(ord(v1), ord(v2)))
else:
    print("Неверный ввод")
    exit()

print(result)