print('Введите три числа')

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if b < a < c or c < a < b:
    print(f'Среднее число {a}')
elif c < b < a or a < b < c:
    print(f'Среднее число {b}')
elif a < c < b or b < c < a:
    print(f'Среднее число {c}')
else:
    print('Невозможно выявить среднее число')

