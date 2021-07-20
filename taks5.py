'''
Задание 5. Пользователь вводит две буквы. Определить, на каких местах алфавита
они стоят и сколько между ними находится букв
'''

a = input('Введите первую букву ')
b = input('Введите вторую букву ')

# Приведем к верхнему регистру
a_upper, b_upper = a.upper(), b.upper()

if len(a) != 1 or len(b) != 1 or not ('A' <= a_upper <= 'Z' and 'A' <= b_upper <= 'Z'):
    print('Неверный ввод')
    exit()

a_position = ord(a_upper) - ord('A') + 1
b_position = ord(b_upper) - ord('A') + 1

print(f'Буква "{a_upper}" {a_position} по счету')
print(f'Буква "{b_upper}" {b_position} по счету')

count_letter = abs(a_position - b_position)
print(f'Между "{a_upper}" и "{b_upper}" {count_letter} букв')