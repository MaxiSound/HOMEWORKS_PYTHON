# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# 1 Вариант:
n = int(input('Введите число: \n'))
list = [1]

for i in range(1, n):
    list.append((i+1) * list[i-1])

print(list)

# 2 Вариант:
# n = int(input('Введите число: \n'))
# temp_num = 1
# for i in range(n):
#     temp_num *= i+1
#     print(temp_num, end=', ')

# print()
