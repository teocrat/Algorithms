n = int(input('Введите количество элементов последовательности: '))
sum_subseq = 0
for i in range(n):
    sum_subseq += 1 / (-2) ** i
print(f'Сумма последовательности равна {sum_subseq}')

