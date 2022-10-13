# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string_input = input("Введите текст: \n")
string_result = string_input.split(' ')
string_result = filter(lambda s: not 'абв' in s, string_result)
print('Получим результат фильтрации: ')
print(' '.join(list(string_result)))

# Вариант №2
# string_result = string_input.split(' ')
# string_result = [s for s in string_result if s.find('абв') == -1]
# print('Результат: ')
# print (' '.join(list(string_result)))
