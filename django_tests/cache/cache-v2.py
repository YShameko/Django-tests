# A bit modified version of this function
def fibonacci(n, cache_mode = False):
    if cache_mode:
        cached_value = r.get(n - 1)
        if cached_value is None:
            numbers_list = fibo_calc(n)
            r.set(n, json.dumps(numbers_list))
        else:
            cached_n = r.get(n)
            if cached_n is None:
                numbers_list = json.loads(cached_value)
                f_n = numbers_list[n - 2] + numbers_list[n - 3]
                numbers_list.append(f_n)
                r.set(n, json.dumps(numbers_list))
            else:
                numbers_list = json.loads(cached_n)
    else:
        numbers_list = fibo_calc(n)

    return numbers_list
