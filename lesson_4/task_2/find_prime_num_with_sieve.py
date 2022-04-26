def find_prime_numbers_sieve(c, y):
    sieve = set(range(2, c + 1))
    prime_set = []

    while sieve:
        prime = min(sieve)
        prime_set.append(prime)
        b = set(range(prime, c + 1, prime))
        sieve -= b
    if y - 1 > len(prime_set):
        print('Порядковый номер числа выходит за пределы списка')
    else:
        for n in prime_set:
            if prime_set[y - 1] == n:
                return n


if __name__ == '__main__':
    c = int(input(('Введите число, являющееся пределом списка простых чисел: ')))
    y = int(input('Порядковый номер числа, которое вы хотите найти?: '))
    print(find_prime_numbers_sieve(c, y))
