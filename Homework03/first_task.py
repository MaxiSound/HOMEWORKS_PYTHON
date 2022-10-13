# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
import os
from random import *
os.system('cls')

n = randint(5, 13)
list = [randint(1, 21) for i in range(n)]
print(list, '\n')

print('Сумма элементов на нечетных позициях равна:\n',
      sum(list[1::2]))

# Вариант №2
# spisok =[]
# a = int(input('Введите длину списка:\n'))
# for i in range(a):
#     spisok.append(random.randint(1, 10))
# print(f'Создан новый список:\n {spisok}')
# sum = 0
# for i in range(a):
#     if i % 2 > 0: sum += spisok[i]
# print(f'Сумма чисел списка стоящих в нечетных позициях равна:\n {sum}')
