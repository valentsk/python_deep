# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

# from fractions import gcd
import math

number_a_b = input('Введите дробь: ')
number_a = number_a_b.split('/')[0]
number_b = number_a_b.split('/')[1]
nok = math.gcd(int(number_a), int(number_b))
print('НОК через gcd: ', nok)
print('Проверка сокращенной дроби через gcd: ', int(int(number_a) / nok), '/', int(int(number_b) / nok))

max_nok = 1
for i in range(2, int(number_a)):
    if int(number_a) % i == 0 and int(number_b) % i == 0:
        max_nok = i


print('Вычисленный нок: ', max_nok)
print(number_a, number_b)
print('Наше сокращенная дробь: ', int(int(number_a) / max_nok), '/', int(int(number_b) / max_nok))

print('Сумма числителя и знаменателя =', int(number_a) / max_nok + int(number_b) / max_nok)
print('Произведение числителя и знаменятеля =', int(number_a) / max_nok * int(number_b) / max_nok)

# def summarize_and_multiply(a, b):
#     result_sum = a + b
#     result_mul = a * b
#     return result_sum, result_mul
# print('Результат у'summarize_and_multiply(int(number_a), int(number_b)))
