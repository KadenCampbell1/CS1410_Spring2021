import sys
from time import perf_counter

cache = {(0, 0): 0}
cache_hit = 0
function_calls = 0


def weight_on(r, c):
    value = None
    global function_calls
    function_calls += 1
    if (r, c) in cache:
        global cache_hit
        cache_hit += 1
        return cache[(r, c)]
    else:
        if r == 0 and c == 0:
            cache[(r, c)] = 0
            return 0
        if c == 0:
            value = float((weight_on(r - 1, c) + 200) / 2)
            cache[(r, c)] = value
        if c == r:
            value = float((weight_on(r - 1, c - 1) + 200) / 2)
            cache[(r, c)] = value
        if c != 0 and c != r:
            value = float(((weight_on(r - 1, c) + 200) / 2) + ((weight_on(r - 1, c - 1) + 200) / 2))
            cache[(r, c)] = value
        cache[(r, c)] = value
    return value


def main():
    cache.clear()
    value = sys.argv[1]  # _Scripts\pyramid.py <number> "this is how to use value"
    start = perf_counter()
    lyst = []
    for i in range(int(value)):
        lyst.clear()
        for x in range(0, i + 1):
            lyst.append("{:.2f}".format(weight_on(i, x)))
        print(f"{str(lyst)[1:-1]}".replace("'", "").replace(",", ""))

    end = perf_counter()
    time = end - start
    print(f"\nElapsed time: {time} seconds\n"
          f"Number of function calls: {function_calls}\n"
          f"Number of cache calls: {cache_hit}")


if __name__ == "__main__":
    main()
