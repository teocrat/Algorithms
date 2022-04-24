from random import randint

num_array = [randint(1, 100) for n in range(10)]
print(num_array)
max_number = max(num_array)
min_number = min(num_array)

for i, n in enumerate(num_array):
    if n == max_number:
        i_max = i

for i, n in enumerate(num_array):
    if n == min_number:
        i_min = i

if i_max < i_min:
    i_max, i_min = i_min, i_max


print(sum(num_array[i_min + 1: i_max]))
