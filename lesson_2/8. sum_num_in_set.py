len_num = int(input('Введите количество вводимых чисел: '))
tested_digit = input('Введите цифру, которую необходимо посчитать: ')
count_num = 0
for i in range(len_num):
    num = input(f'Введите {i + 1} число: ')
    for n in num:
        if tested_digit == n:
            count_num += 1
print(f'Цифра {tested_digit} встречается в последовательности {count_num} раз')
