'''
Задание 1.
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

range_values = (2, 99)
range_divisors = (2, 9)

# Зачем тут массивы?) Когда можно решить математически
for divisor in range(range_divisors[0], range_divisors[1] + 1):
    count = (range_values[1] - range_values[0]) // divisor + \
            (1 if range_values[1] % divisor < range_values[0] % divisor else 0)
    print(f'{divisor} - {count}')
