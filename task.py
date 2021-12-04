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
        number_is_in_tail = number in numbers[i + 1:]
    return


@time_counter(rep=1)
def second_solution(numbers):
    numbers_list = numbers
    for i, number in enumerate(numbers):
        number_is_in_tail = number in numbers_list
        numbers_list.pop(0)
    return

first_solution(numbers)
second_solution(numbers)

