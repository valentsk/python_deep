# Создайте функцию генератор чисел Фибоначчи

def gen_Fibo(number: int = 10):
    first, second = 0, 1
    while number > 0:
        yield first
        first, second = second, first + second
        number -= 1

for i in gen_Fibo():
    print(i)