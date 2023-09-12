from date import check_date
from sys import argv

# print(check_date(input('Введите дату #DD.MM.YYYY: ')))

print(check_date(*argv[1:]))
