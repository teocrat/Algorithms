n = int(input('Введите целое число: '))
sum_set = 0
for i in range(1, n + 1):
    sum_set += i
if sum_set == n * (n + 1) / 2:
    print('Доказано')
else:
    print('Не доказано')

