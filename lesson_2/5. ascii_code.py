for n in range(32, 128):
    print(f'{n} - {chr(n)}')
    if n % 10 == 0:
        print()
print()
print("_" * 3 + "  вариант 2")
print()

from tabulate import tabulate

ar = {}
for n in range(32, 128):
    ar[n] = chr(n)

    if len(ar) == 10:
        print(tabulate(ar.items(), headers=['Код', 'Символ'], tablefmt="grid"))
        print()
        ar.clear()
print(tabulate(ar.items(), headers=['Код', 'Символ'], tablefmt="grid"))
