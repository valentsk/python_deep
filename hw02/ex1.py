# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата

BASE_HEX = 16
BASE_BIN = 2
number = int(input('Введите число: '))
result_bin = ''
result_hex = ''
print('Проверка: ', hex(number))

while number > 0:
    match number % BASE_HEX:
        case 10:
            result_avar = 'a'
        case 11:
            result_avar = 'b'
        case 12:
            result_avar = 'c'
        case 13:
            result_avar = 'd'
        case 14:
            result_avar = 'e'
        case 15:
            result_avar = 'f'
        case _:
            result_avar = str(number % BASE_HEX)
    result_hex = result_avar + result_hex
    number //= BASE_HEX
print('Наш ответ: 0x'+result_hex)

