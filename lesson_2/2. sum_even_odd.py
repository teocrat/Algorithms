num = input('Введите целое число: ')
sum_even = 0
sum_odd = 0
for i in num:
    if int(i) % 2 == 0:
        sum_even += 1
    else:
        sum_odd += 1
print(f'Количество четных цифр в числе {sum_even}.\n'
      f'Количество нечетных цифр в числе {sum_odd}.')
