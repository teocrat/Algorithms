print('Введите координаты первой точки: ')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
print('Введите координаты второй точки: ')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
k = (y1 + y2) / (x1 + x2)
b = (y2 + x2) / y1
print(f'y = {k:.2f}x + {b:.2f}')
