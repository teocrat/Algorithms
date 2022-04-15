import random


while True:
    d_type = input('Введите тип данных: i (целое число), f (вещественное число), c (буква латинского алфавита): ')
    if d_type != 'i' and d_type != 'f' and d_type != 'c':
        print('Введен неверный тип данных')
    else:
        break
while True:
    start_symbol = input('Введите начальный символ диапазона: ')
    end_symbol = input('Введите конечный символ диапазона: ')
    if end_symbol < start_symbol:
        print('Конечный символ не может стоять раньше стартового')
    else:
        break

if d_type == 'i':
    result = random.randint(int(start_symbol), int(end_symbol))
elif d_type == 'f':
    result = f'{random.uniform(float(start_symbol), float(end_symbol)):.2f}'
elif d_type == 'c':
    result = chr(random.randint(ord(start_symbol), ord(end_symbol)))

print(f'Случайный символ в  диапазоне от {start_symbol} до {end_symbol}: {result}')
