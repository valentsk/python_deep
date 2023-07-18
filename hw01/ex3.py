# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
secret_number = randint(0, 10)
attempt = 10
inc_attempt = 1
print('Я загадал число, у тебя 10 попыток его найти!')
while attempt > 0:
    print(f'Попытка №{inc_attempt}')
    user_number = int(input("Введи число: "))
    if user_number < secret_number:
        print('Больше')
    elif user_number > secret_number:
        print('Меньше')
    else:
        print('Ты угадал!')
        break
    attempt -= 1
    inc_attempt += 1
if attempt == 0:
    print('У тебя закончились попытки! Попробуй еще!')
