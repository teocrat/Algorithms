from timeit import Timer
from find_prime_num_without_sieve import find_prime_numbers
from find_prime_num_with_sieve import find_prime_numbers_sieve

c = 100
y = 7
t = Timer(lambda: find_prime_numbers(c, y))
print('find_prime_numbers ', t.timeit(number=100), 'c')
print('find_prime_numbers ', t.timeit(number=1000), 'c')
print('find_prime_numbers ', t.timeit(number=10000), 'c')
print('find_prime_numbers ', t.timeit(number=100000), 'c')
print('find_prime_numbers ', t.timeit(number=1000000), 'c')

t = Timer(lambda: find_prime_numbers_sieve(c, y))
print('find_prime_numbers_sieve ', t.timeit(number=100), 'c')
print('find_prime_numbers_sieve ', t.timeit(number=1000), 'c')
print('find_prime_numbers_sieve ', t.timeit(number=10000), 'c')
print('find_prime_numbers_sieve ', t.timeit(number=100000), 'c')
print('find_prime_numbers_sieve ', t.timeit(number=1000000), 'c')

# find_prime_numbers  0.0028313398361206055 c
# find_prime_numbers  0.029823569813743234 c
# find_prime_numbers  0.2750282569322735 c
# find_prime_numbers  2.7698231211397797 c
# find_prime_numbers  27.476874897023663 c
# find_prime_numbers_sieve  0.007330981083214283 c
# find_prime_numbers_sieve  0.08973643998615444 c
# find_prime_numbers_sieve  0.7094330589752644 c
# find_prime_numbers_sieve  7.021701948018745 c
# find_prime_numbers_sieve  70.24951625894755 c
# Как видно из результатов замера скоростей выполнения функций find_prime_numbers и find_prime_numbers_sieve,
# время исполнения функции без решета Эратосфена почти в 3 раза меньше, чем время исполнения функции с решетом.
# Сложность обоих функций линейная (присутсвие циклов)

