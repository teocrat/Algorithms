def find_prime_numbers(c, y):
    pr_num = [2]
    for i in range(3, c + 1, 2):
        if i > 10 and i % 10 == 5:
            continue
        for j in pr_num:
            if j * j - 1 > i:
                pr_num.append(i)
                break
            if i % j == 0:
                break
        else:
            pr_num.append(i)

    if y - 1 > len(pr_num):
        print('Порядковый номер числа выходит за пределы списка')
    else:
        for n in pr_num:
            if pr_num[y - 1] == n:
                return n


if __name__ == '__main__':
    c = int(input(('Введите число, являющееся пределом списка простых чисел: ')))
    y = int(input('Порядковый номер числа, которое вы хотите найти?: '))
    print(find_prime_numbers(c, y))
