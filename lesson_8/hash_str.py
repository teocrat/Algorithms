import hashlib


def count_sbstr(s):
    s = str(s).lower()
    n = len(s)
    h_s = set()

    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            h = hashlib.md5(s[i:j].encode('utf-8')).hexdigest()
            h_s.add(h)

    return len(h_s)


inp_s = input('Введите строку: ')

print(f'Количество различных подстрок в строке {inp_s}: {count_sbstr(inp_s)}')