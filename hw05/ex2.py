# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

name_list = ['Петр', 'Иван', 'Мария']
index_list = [10, 20, 30]
bonus_list = ['10.25%', '15.3%', '20.9%']
dict_var = {name_key: index * float(bonus[:-1]) / 100 for (name_key, index, bonus) in zip(name_list, index_list, bonus_list)}
print(dict_var)
# dict_var = {item[0]: item[1] * float(item[2][:-1]) / 100 for item in zip(name_list, index_list, bonus_list)}
