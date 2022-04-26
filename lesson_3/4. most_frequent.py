from collections import Counter
from random import randint

seq = [randint(1, 100) for i in range(20)]

c = Counter(seq)
print(seq)
max_num = 2
mxn = 0
for v in c:
    if c[v] >= max_num:
        max_num = c[v]
        mxn = max_num
        print(f'Число {v} встречается {max_num} раза')
if mxn == 0:
    print('Все числа встречаются один раз')