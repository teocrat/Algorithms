from random import randint

num = randint(0, 101)
i = 10
while i > 0:
    n = int(input("Угадай число от 0 до 100. Твоё число?: "))
    if n == num:
        print(f'Угадал.Число {num}')
        break
    elif n < num:
        print('Твоё число меньше загаданного')
    else:
        print('Твоё число больше загаданного')
    i -= 1
    if i == 0:
        print(f'Ты не угадал. Загаданное число {num}')

