# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import Func_call_record_func as fc
import Func_sum_polinom as fs
import Func_fill_missing_coeff as fm
import Func_read_file as r


def transform_polinom(user_polynom: str, user_file: str):
    polyn = user_polynom.replace('$', '')
    polyn = polyn.replace('**', '^')
    polyn = polyn.replace(' ', '')
    polyn = polyn[:-2]
    return polyn


file1 = 'file1.txt'  # Файл c записью 1-го многочлена
file2 = 'file2.txt'  # Файл c записью 2-го многочлена

polynom1 = r.read_file(file1)
polynom2 = r.read_file(file2)

p1 = transform_polinom(polynom1, file1)
p2 = transform_polinom(polynom2, file2)
print(type(p1))
tp1 = fm.fill_missing_coeff(p1)
tp2 = fm.fill_missing_coeff(p2)

result = fs.sum_polinom(tp1, tp2)

file_result = 'f_result.txt'
fc.call_record_func(len(result)-1, result, file_result)
