print('Введите длины сторон треугольника')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не существует')
elif a != b and b != c and c != a:
    print('Треугольник разносторонний')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')
