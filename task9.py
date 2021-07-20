'''
Задание 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''


def cal_sum_digits(value):
    value = str(value)
    sum = 0
    for digit in value:
        sum += int(digit)
    return sum


sum = -1
while True:
    current = input('Введите натулаьное число, или любой символ для выхода. ')
    if current.isdigit():
       current_sum = cal_sum_digits(current)
       if current_sum > sum:
           max, sum = current, current_sum
    else:
        break

if sum >= 0:
    print(f'Число: {max}, сумма: {sum}')