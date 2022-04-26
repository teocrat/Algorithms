M = 5
N = 4
matrix = [[] for n in range(N)]
for a in matrix:
    for j in range(M):
        num = int(input('Введите число: '))
        a.append(num)

for i in matrix:
    for j in i:
        print('%4d' % j, ' ', end='')

    print(' |', '%4d' % sum(i))

for i in range(M):
    print('----  ', end='')
print()
for i in range(M):
    s = 0
    for j in range(N):
        s += matrix[j][i]
    print('%4d' % s, ' ', end='')
