# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def invers_try(**kwargs):
    new_dict = {}
    for key, val in kwargs.items():
        try:
            new_dict[val] = key
        except:
            new_dict[str(val)] = key
    return new_dict

print(invers_try(one=1, two = ['2'], three = (3,)))