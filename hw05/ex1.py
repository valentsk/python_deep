# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def file(str):
    file_path = os.path.dirname(str)
    file_name, file_ext = os.path.splitext(str)
    file_name = os.path.basename(str)
    return file_path, file_name, file_ext

str = 'C:\temp\python_new\homework\hw05\ex1.py'
print(file(str))

