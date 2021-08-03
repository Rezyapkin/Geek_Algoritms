'''
Задание 1.
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
'''

# В комментарии к задаче сказано использовать что-то из Collection. Возьмем OrderedDict

from collections import OrderedDict, namedtuple

data = OrderedDict()
Profit = namedtuple('Profit', ['values', 'avg'])

n = int(input('Введите количество преприятий '))

for i in range(1, n + 1):
    while True:
        name = input(f'Введите наименование предприятия №{i} ')
        if data.get(name):
            print('Сведения об этом предприятии уже есть в нашей базе данных. Повторите ввод. ')
        else:
            break


    total = 0
    values = []

    for j in range(1, 5):
        value = float(input(f'Введите значение прибыли в квартале №{j} '))
        values.append(value)
        total += value

    data[name] = Profit(values=values, avg=(total / len(values)))
    print('-' * 50)

avg = sum(map(lambda x: x.avg, data.values())) / len(data)
print(f'Средняя прибыль: {avg:10.2}')

print('Предприятия чья прибыль больше средней:')
for company in filter(lambda x: data[x].avg > avg, data):
    print(f'{company}, средняя прибыль: {data[company].avg}')

print('-' * 50)

print('Предприятия чья прибыль меньше средней:')
for company in filter(lambda x : data[x].avg < avg, data):
    print(f'{company}, средняя прибыль: {data[company].avg}')
