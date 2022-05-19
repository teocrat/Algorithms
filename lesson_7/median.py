import random


def median(m):
    size = 2 * m + 1
    my_list = [random.randint(0, 50) for n in range(size)]
    middle = len(my_list) // 2
    print(my_list)
    my_list.sort()
    print(my_list)

    return my_list[middle]


if __name__ == '__main__':
    m = int(input('Введите натуральное число: '))

    print(f'Медиана массива: {median(m)}')
