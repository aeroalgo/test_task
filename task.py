import numpy as np
import time

numbers = list(np.random.randint(low=1, high=10, size=100000))


def time_counter(*, rep=1):
    def time_counter_inner1(func):
        def time_counter_inner2(*args, **kwargs):
            start = time.perf_counter()
            for i in range(rep):
                result = func(*args, **kwargs)
            print(f'{func.__name__} time: '
                  f'{time.perf_counter() - start}sec with repetition {rep}')
            return result

        return time_counter_inner2

    return time_counter_inner1


@time_counter(rep=1)
def first_solution(numbers):
    for i, number in enumerate(numbers):
        # Операция среза это очень дорогая операция
        number_is_in_tail = number in numbers[i + 1:]
    return


@time_counter(rep=1)
def second_solution(numbers):
    numbers_list = numbers
    for i, number in enumerate(numbers):
        number_is_in_tail = number in numbers_list
        # Удаление каждого элемента по которому мы проитерировались
        numbers_list.pop(0)
    return


@time_counter(rep=1)
def third_solution(numbers):
    numbers_count = {i: 0 for i in range(min(numbers), max(numbers)+1)}
    print(numbers_count)
    for i in range(len(numbers)):
        numbers_count[numbers[i]] += 1

    for i in range(len(numbers)):
        if numbers_count[numbers[i]] > 1:
            numbers_count[numbers[i]] -= 1
            number_is_in_tail = True
        else:
            number_is_in_tail = False
    return


first_solution(numbers)
second_solution(numbers)
third_solution(numbers)
