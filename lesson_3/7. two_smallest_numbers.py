from random import randint

num_array = [randint(1, 100) for n in range(20)]
print(num_array)
min_number = min(num_array)
num_array.remove(min_number)
sec_min_number = min(num_array)

print(f'Первое минимальное число {min_number}\nВторое минимальное число {sec_min_number}')
