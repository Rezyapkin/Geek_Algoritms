'''
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

from collections import deque


class MyHex:

    def __init__(self, digits=[]):
        self.digits = deque(map(lambda x: str(x).upper(), digits))
        if not self.__check_digits():
            raise ValueError("Массив с цифрами содержит недопустимые символы")
        self.__clear_digits()

    def __check_digits(self):
        result = True
        for digit in self.digits:
            if not ('0' <= digit <= '9' or 'A' <= digit <= 'F'):
                result = False
                break
        return result

    def __clear_digits(self):
        while len(self.digits) > 0 and self.digits[0] == '0':
            self.digits.popleft()

        if len(self.digits) == 0:
            self.digits.append('0')

    def __str__(self):
        return "".join(self.digits)

    @staticmethod
    def __chr_to_int(digit):
        return ord(digit) - (ord('0') if '0' <= digit <='9' else ord('A') - 10)

    @staticmethod
    def __int_to_chr(value):
        digit = value % 16
        return chr((ord('0') if 0 <= digit <=9 else ord('A') - 10) + digit)

    def __add__(self, other):
        # Создадим очередь с цифрами из цифр исходного объекта
        result_digits = self.digits.copy()
        result_digits.reverse()

        # Создадим очередь с цифрами из второго слагаемого
        other_digits = other.digits.copy()
        other_digits.reverse()

        i = 0
        add_one = 0

        for i in range(max(len(result_digits), len(other_digits))):
            value = (__class__.__chr_to_int(result_digits[i]) if len(result_digits) > i else 0) + \
                    (__class__.__chr_to_int(other_digits[i]) if len(other_digits) > i else 0) + \
                    add_one
            add_one = 0 if value < 16 else 1
            new_digit = __class__.__int_to_chr(value % 16)
            if len(result_digits) > i:
                result_digits[i] = new_digit
            else:
                result_digits.append(new_digit)

        if add_one > 0:
            result_digits.append('1')

        result_digits.reverse()

        return __class__(result_digits)


    def __mul__(self, other):
        tmp_dict = dict()
        max_digit = max(map(lambda x: __class__.__chr_to_int(x), set(other.digits)))
        current = __class__([])
        for i in range(max_digit + 1):
            tmp_dict[__class__.__int_to_chr(i)] = current
            current += self

        other_digits = other.digits.copy()
        result = __class__([])
        for i in range(len(other.digits)):
            value = other_digits.pop()
            current = tmp_dict[value].digits.copy()
            for j in range (i):
                current.append('0')

            result += __class__(current)

        return result


a = MyHex(['f', 'f', 'e'])
# Для b специально сделал кривой ввод, чтобы показать, что класс корректно с ним работает!)
b = MyHex([0, 1, 'f'])

print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')
