def even_num_index(first_array):
    first_array = first_array.split(',')
    second_array = []
    for i in first_array:
        if int(i) % 2 == 0:
            second_array.append(first_array.index(i))

    return second_array


print(even_num_index('2, 7, 8, 9, 12, 44, 59, 90, 112'))
