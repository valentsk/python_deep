# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○Для дочерних объектов указывайте родительскую директорию.
# ○Для каждого объекта укажите файл это или директория.
# ○Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.


import csv
import json
import os
import pickle
import sys
from pprint import pprint


def size_of_dir(dir_path: str) -> int:
    total_size = 0
    for path, _, files in os.walk(dir_path):
        for file in files:
            total_size += sys.getsizeof(os.path.join(path, file))
    return total_size

def json_writer(current_path: str, source: dict[str, dict]):
    name = os.path.join(current_path, 'result.json')
    with open(name, 'w', encoding='utf-8') as data:
        json.dump(source, data, indent=4, ensure_ascii=False)

def csv_writer(current_path: str, source: dict[str, dict]):
    name = os.path.join(current_path, 'result.csv')
    file = [['Full_path', 'Name', 'Parent_dir', 'Type', 'Size']]
    for key, item in source.items():
        file.append([key, *item.values()])
    with open(name, 'w', encoding='utf-8') as data:
        write_csv = csv.writer(data, dialect='excel', delimeter=';')
        write_csv.writerows(file)


def pickle_writer(current_path: str, source: dict[str, dict]):
    name = os.path.join(current_path, 'result.bin')
    with open(name, 'wb') as data:
        pickle.dump(source, data)


def dir_walker(full_path: str = os.getcwd()):
    result = {}
    for path, dir_list, file_list in os.walk(full_path):
        for cur_dir in dir_list:
            result[os.path.join(path, cur_dir)] = {'name': cur_dir,
                                                    'path': path,
                                                    'type': 'DIR',
                                                    'size': size_of_dir(os.path.join(path, cur_dir))}

        for cur_file in file_list:
            result[os.path.join(path, cur_file)] = {'name': cur_file,
                                                    'path': path,
                                                    'type': 'FILE',
                                                    'size':sys.getsizeof(os.path.join(path, cur_file))}
    json_writer(full_path, result)
    pickle_writer(full_path, result)
    csv_writer(full_path, result)
    return result

pprint(dir_walker('C:\\temp\python_new\homework'))