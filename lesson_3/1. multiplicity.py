nat_num = [n for n in range(2, 100)]
div_num = [n for n in range(2, 10)]
mult_dict = {}

for i in nat_num:
    for j in div_num:
        if i % j == 0:
            mult_dict.setdefault(j, 0)
            mult_dict[j] += 1

for n in mult_dict:
    print(f'{n} кратны {mult_dict[n]} чисел/а')
