# 4. Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

f = open("file.txt")

n = int(f.readline(1))
n = int(input('Введите число: \n'))
list = []

for i in range(n):
    list.append(random.randint(n*-1, n))

print(list)
result = 1

for line in f:
    print (list[int(line)], ' * ' , end='' )
    result = result * list[int(line)]

print('= ', result)