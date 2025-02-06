import json
import redis

r = redis.Redis(host='localhost', port=6379)

def fibonacci(n, cache_mode = False):
    if cache_mode:
        cached_value = r.get(n - 1)
        if cached_value is None:
            numbers_list = fibo_calc(n)
            r.set(n, json.dumps(numbers_list), ex=30)
        else:
            numbers_list = json.loads(cached_value)
            f_n = numbers_list[n - 2] + numbers_list[n - 3]
            numbers_list.append(f_n)
    else:
        numbers_list = fibo_calc(n)

    return numbers_list

def fibo_calc(n):
    global calculations_counter
    calculations_counter += 1
    numbers_list = [1, 1]
    while len(numbers_list) < n:
        index = len(numbers_list)
        next_number = numbers_list[index - 1] + numbers_list[index - 2]
        numbers_list.append(next_number)
    return numbers_list

#--------------------------------------------------------------------------
calculations_counter = 1
for i in range(1, 50):
    sequence = fibonacci(i)
    print(sequence)
print('Full calculations of the sequence were made',calculations_counter,'times.')
print('----------------------------------------')

calculations_counter = 1
for i in range(1, 50):
    sequence = fibonacci(i, True)
    print(sequence)
print('Now using cache calculations of the sequence were made',calculations_counter,'times.')