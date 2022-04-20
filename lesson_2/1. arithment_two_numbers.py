while True:
    exp = input('Введите математическое выражение(например 10 + 2).\nДля завершения введите 0:  ')
    if exp == '0':
        break
    else:
        n = exp.split()
        if n[1] == '+':
            print(f'{exp} = {int(n[0]) + int(n[2])}')
        elif n[1] == '-':
            print(f'{exp} = {int(n[0]) - int(n[2])}')
        elif n[1] == '*':
            print(f'{exp} = {int(n[0]) * int(n[2])}')
        elif n[1] == '/':
            if n[2] != '0':
                print(f'{exp} = {(int(n[0]) / int(n[2])):.2f}')
            else:
                print('На ноль делить нельзя')
        else:
            print('Введен недопустимый символ')



