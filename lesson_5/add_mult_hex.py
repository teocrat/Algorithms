from collections import defaultdict
from collections import deque

hex_num_1 = input('Введите первое число в шестнадцатиричном формате: ')
hex_num_2 = input('Введите второе число в шестнадцатиричном формате: ')

hex_num_1 = hex_num_1.upper()
hex_num_2 = hex_num_2.upper()

hex_str = '0123456789ABCDEF'
int_dict = defaultdict(int)

i = 0
for key in hex_str:
    int_dict[key] += i
    i += 1


def int_func(num_hex):
    int_num = 0
    hnum = deque(num_hex)
    hnum.reverse()
    for n in range(len(hnum)):
        c = int_dict[hnum[n]] * 16 ** n
        int_num += c
    return int_num


def hex_func(num_int):
    inum = deque()
    while num_int > 0:
        a = num_int % 16
        for j in int_dict:
            if int_dict[j] == a:
                inum.append(j)
        num_int //= 16
    inum.reverse()
    return ''.join(list(inum))


num_1 = int_func(hex_num_1)
num_2 = int_func(hex_num_2)

sum_num = hex_func(num_1 + num_2)
mult_num = hex_func(num_1 * num_2)

print(f'Сумма чисел: {sum_num}')
print(f'Произведение чисел: {mult_num}')
