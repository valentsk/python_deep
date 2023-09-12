#DD.MM.YYYY

def check_date(inp_year):
    day, month, year = map(int, inp_year.split('.'))
    if 0 < day < 32 and 0 < month < 13 and 0 < year < 10_000:
        if month != 2:
            if day in __month_dict:
                return month in __month_dict[day]
            else:
                return True
        else:
            if _check_year(year):
                  return day < 29
            else:
                return day < 30


def _check_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        print('Нормальный')
        return  True
    else:
        print('Высокосный')
        return False

__month_dict = {31:[1,3,5,7,8,10,12], 30:[4,6,9,11]}

if __name__ == '__main__':
    print(check_date(input('Введите дату #DD.MM.YYYY: ')))