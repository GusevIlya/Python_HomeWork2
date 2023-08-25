'''
Задача 14:
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

10 -> 1 2 4 8
'''

n = int(input('Введите число: '))
result = 0
k = 0
res = ""
while result < n:
    result = 2 ** k
    k += 1
    if result < n:
        res = res + str(result) + " "
print(res)
