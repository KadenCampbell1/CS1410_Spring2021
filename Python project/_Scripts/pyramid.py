import sys
from time import perf_counter

cache = {(0, 0): 0}
cache_hit = [0]
function_calls = [0]


def weight_on(r, c):
    function_calls[0] = int(function_calls[0] + 1)
    print(f"function calls: {function_calls[0]}")
    value = None
    if (r, c) in cache:
        cache_hit[0] = int(cache_hit[0] + 1)
        print(int(cache_hit[0]))
        return cache[(r, c)]
    else:
        if r == 0 and c == 0:
            cache[(r, c)] = 0
            return 0
        if c == 0:
            value = float((weight_on(r - 1, c) + 200) / 2)
            cache[(r, c)] = round(value, 2)
        if c == r:
            value = float((weight_on(r - 1, c - 1) + 200) / 2)
            cache[(r, c)] = round(value, 2)
        if c != 0 and c != r:
            value = float(((weight_on(r - 1, c) + 200) / 2) + ((weight_on(r - 1, c - 1) + 200) / 2))
            cache[(r, c)] = round(value, 2)
        cache[(r, c)] = round(value, 2)
    return round(value, 2)


def main():
    cache.clear()
    print(weight_on(6, 6))
    print(cache)


if __name__ == "__main__":
    main()
