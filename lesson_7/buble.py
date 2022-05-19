import random


def bubble(my_list):
    flag = False
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] < my_list[j + 1]:
                my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]
                flag = True
        if flag:
            flag = False
        else:
            break

    return my_list


if __name__ == '__main__':
    s = [random.randint(-100, 100) for n in range(20)]
    print(s)
    print(*bubble(s))
