import sys
from random import randint

print('1 программа:')
print()

nat_num = [n for n in range(2, 100)]  # 920 байт
div_num = [n for n in range(2, 10)]  # 120 байт
mult_dict = {}  # 360 байт

for i in nat_num:
    for j in div_num:
        if i % j == 0:
            mult_dict.setdefault(j, 0)
            mult_dict[j] += 1

for n in mult_dict:
    print(f'{n} кратны {mult_dict[n]} чисел/а')

# оценка количества памяти, выделенной под переменные:
print()
print(f'Объем памяти, выделенной под переменные в 1 программе: '
      f'{sys.getsizeof(nat_num) + sys.getsizeof(div_num) + sys.getsizeof(mult_dict)} байт')
print()
print('-' * 70)
print()
print('2 программа:')
print()

seq = [randint(-100, 100) for i in range(20)]  # 248 байт
print(seq)

max_neg_num = 0  # 28 байт

for i in seq:
    if i < max_neg_num:
        max_neg_num = i

print(f'Наименьшее число: {max_neg_num}')

# оценка количества памяти, выделенной под переменные:

print()
print(f'Объем памяти, выделенной под переменные в 2 программе: '
      f'{sys.getsizeof(seq) + sys.getsizeof(max_neg_num)} байт')
print()
print('-' * 70)
print()
print('3 программа:')
print()

num_array = [randint(1, 100) for n in range(10)]  # 184 байта
print(num_array)
max_number = max(num_array)  # 28 байт
min_number = min(num_array)  # 28 байт

for i, n in enumerate(num_array):
    if n == max_number:
        i_max = i

for i, n in enumerate(num_array):
    if n == min_number:
        i_min = i

if i_max < i_min:
    i_max, i_min = i_min, i_max

print(f'Сумма чисел в интервале от минимального до максимального: {sum(num_array[i_min + 1: i_max])}')

# оценка количества памяти, выделенной под переменные:

print()
print(f'Объем памяти, выделенной под переменные в 3 программе: '
      f'{sys.getsizeof(num_array) + sys.getsizeof(max_number) + sys.getsizeof(min_number)} байт')

# Как видно из вышепредставленных программ оптимальное использование памяти показала 3 программа.
# В 3 программе для переменных max_number и min_number выделено всего по 28 байт,
# хотя они вычисляются при помощи встроенных функций. Таким образом видно, что применение встроенных
# функций определяет переменные как числа, что более оптимально, чем вычисление этих переменных при помощи
# циклов. В 1 программе большой объем памяти выделено под словарь. Большая разница между переменными nat_num
# и div_num объясняется количеством генерируемых чмсел.
# Версия Python 3.10.4, разрядность Windows 64
