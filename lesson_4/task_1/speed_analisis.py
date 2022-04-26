from random import randint
from timeit import Timer
from swap_func import swap_numbers
from swap_func_other import swap_numbers_other

num_array = [randint(1, 100) for n in range(20)]
t = Timer(lambda: swap_numbers(num_array))
print('swap_numbers ', t.timeit(number=100), 'c')
print('swap_numbers ', t.timeit(number=1000), 'c')
print('swap_numbers ', t.timeit(number=10000), 'c')
print('swap_numbers ', t.timeit(number=100000), 'c')
print('swap_numbers ', t.timeit(number=1000000), 'c')

t = Timer(lambda: swap_numbers_other(num_array))

print('swap_numbers_other ', t.timeit(number=100), 'c')
print('swap_numbers_other ', t.timeit(number=1000), 'c')
print('swap_numbers_other ', t.timeit(number=10000), 'c')
print('swap_numbers_other ', t.timeit(number=100000), 'c')
print('swap_numbers_other ', t.timeit(number=1000000), 'c')

# swap_numbers  0.0005230399547144771 c
# swap_numbers  0.00554104195907712 c
# swap_numbers  0.05060388194397092 c
# swap_numbers  0.5040037350263447 c
# swap_numbers  4.984209620044567 c
# swap_numbers_other  0.0005520450649783015 c
# swap_numbers_other  0.005436246981844306 c
# swap_numbers_other  0.0539498400175944 c
# swap_numbers_other  0.5405089299893007 c
# swap_numbers_other  5.54760879999958 c

# Как видно из результатов замера скоростей выполнения функций swap_numbers и swap_numbers_other,
# скорость на маленьких n практически неизменна, при n = 1000000 время различается почти на секунду.
# Из этого можно сделать вывод, что встроенные функции max() и min() работают несколько быстрее, чем циклы for in.
# Сложность обоих алгоритмов линейная (присутсвие циклов)
