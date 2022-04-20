len_set = int(input('Введите количесво вводимых чисел: '))
max_count_digit = 0

for i in range(len_set):
    num = int(input(f'Введите {i + 1} число: '))
    sum_num = 0
    for n in str(num):
        n = int(n)
        sum_num += n % 10
        n // 10
    if max_count_digit == sum_num:
        max_num = num
    elif max_count_digit < sum_num:
        max_count_digit = sum_num
        max_num = num


print(f'Наибольшее число по сумме цифр {max_num}, сумма цифр этого числа {max_count_digit}')
