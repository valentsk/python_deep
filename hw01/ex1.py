a = int(input('Введите сторону a: '))
b = int(input('Введите сторону b: '))
c = int(input('Введите сторону c: '))
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Такого треугольника не существует')
else:
    if (a == b and b == c):
        print('Треугольник равносторонний')
    elif (a == b or a == c or b == c):
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')



