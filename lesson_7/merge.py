import random


def merge(my_list):
    if len(my_list) > 1:
        middle = len(my_list) // 2
        left_list = my_list[:middle]
        right_list = my_list[middle:]
        merge(left_list)
        merge(right_list)
        i = 0
        j = 0
        n = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                my_list[n] = left_list[i]
                i += 1
            else:
                my_list[n] = right_list[j]
                j += 1
            n += 1

        while i < len(left_list):
            my_list[n] = left_list[i]
            i += 1
            n += 1

        while j < len(right_list):
            my_list[n] = right_list[j]
            j += 1
            n += 1
    return my_list


if __name__ == '__main__':
    s = [random.randint(0, 50) for n in range(10)]
    print(s)
    print(*merge(s))
