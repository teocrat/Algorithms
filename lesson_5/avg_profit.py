import collections

while True:
    try:
        ent_num = int(input('Введите количество предприятий: '))
    except ValueError:
        print('Введено недопустимое значение')
        continue
    break

enterprises = collections.defaultdict()
all_profit = 0

for i in range(ent_num):
    ent_name = input(f'Введите наименование {i + 1} предприятия: ')
    profit = 0
    n = 1
    while n <= 4:
        try:
            profit += float(input(f'Введите доход предприятия за {n} квартал: '))
        except ValueError:
            print('Введено недопустимое значение')
            continue
        n += 1
        enterprises[ent_name] = profit
    all_profit += profit

mid_profit = all_profit / ent_num

above_avg = []
below_avg = []

for key, value in enterprises.items():
    if value >= mid_profit:
        above_avg.append(key)
    else:
        below_avg.append(key)

print(f'Средняя прибыль для всех предприятий за год: {mid_profit:.2f}')
print('Предприятия с доходом выше среднего: ')
for n in above_avg:
    print(n)
print('Предприятия с доходом ниже среднего: ')
for i in below_avg:
    print(i)
