# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Примеры: 45 -> 101101, 3 -> 11, 2 -> 10

input_num = int(input("Введите число:\n"))

def Convertation (number):
    if int(number) >= 2:
        return str(Convertation(int(number/2))) + str(number % 2)
    if int(number) == 1:
        return '1'

print ('Получим:\n', Convertation(input_num))
