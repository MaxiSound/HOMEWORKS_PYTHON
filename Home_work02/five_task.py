# 5. Реализуйте алгоритм перемешивания списка.

import random

lenght = 20
list = [i for i in range(lenght)]

print('Список: \n', list)

for i in range(len(list)):
    r = random.randint(i, lenght-1)
    m = list[i]
    list[i] = list[r]
    list[r] = m

print('Перемешиваем список: \n', list)
