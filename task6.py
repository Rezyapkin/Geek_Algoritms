'''
Задание 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква
'''

max_number_letter = 28
number_letter = int(input('Введите номер буквы в алфавите '))

if 0 < number_letter <= max_number_letter:
    letter = chr(ord('A') + number_letter - 1)
    print(letter)
else:
    print('Неверный ввод')