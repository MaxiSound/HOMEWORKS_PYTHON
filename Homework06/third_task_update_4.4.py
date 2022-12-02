# изменение на строке 17

from os import path
from random import randint


def string_gen(list_factor):
    k = len(list_factor)-1
    string_write = str(list_factor[0])
    for i, val in enumerate(list_factor):
        if i != 0:
            string_write = str(val) + 'x^' + str(i) + ' + ' + string_write

    return string_write


def polynomial_gen(file_name="file.txt"):
    k = int(input("Введите число (натуральная степень):\n"))
    file = open(file_name, 'w')
    list_factor = [randint(0, 100) for i in range(k+1)]

    string_write = string_gen(list_factor)

    file.write(string_write)
    file.close()

    print(f"в файл '{path.abspath(file_name)}' записано - {string_write}")


if __name__ == '__main__':
    polynomial_gen()
