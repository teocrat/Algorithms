from random import randint

M = 5
N = 4
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = randint(1, 300)
        b.append(n)
        print('%4d' % n, ' ', end='')
    a.append(b)
    print()

max_num = 0
for j in range(M):
    min_nam = 300
    for i in range(N):
        if a[i][j] < min_nam:
            min_nam = a[i][j]
    if min_nam > max_num:
        max_num = min_nam
print("Максимальный элемент среди минимальных: ", max_num)
