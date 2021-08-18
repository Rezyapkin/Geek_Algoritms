'''
Задание 1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
'''


import hashlib


s = 'helloworldhello'
n = len(s)
result = {}
for i in range(n):
    for j in range (1, n - i + 1):
        subs = s[i:(j+i)]
        h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
        if h_subs not in result:
            result[h_subs] = subs

print(len(result))
