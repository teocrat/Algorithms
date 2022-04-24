from random import randint

seq = [randint(-100, 100) for i in range(20)]
print(seq)

max_neg_num = 0

for i in seq:
    if i < max_neg_num:
        max_neg_num = i

print(max_neg_num)
