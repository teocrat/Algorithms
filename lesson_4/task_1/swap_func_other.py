from random import randint


def swap_numbers_other(num_array):
    max_number = 0
    min_number = 100

    for i in num_array:
        if i > max_number:
            max_number = i
        if i < min_number:
            min_number = i

    for i, j in enumerate(num_array):
        if j == max_number:
            i_max = i

    for i, j in enumerate(num_array):
        if j == min_number:
            i_min = i

    num_array[i_min] = max_number
    num_array[i_max] = min_number
    return num_array


if __name__ == '__main__':
    num_array = [randint(1, 100) for i in range(20)]
    print(num_array)
    print(swap_numbers_other(num_array))
