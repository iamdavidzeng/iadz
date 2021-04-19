import multiprocessing


def func_a(a=1, b=1):
    print(a)
    return func_a(b, a + b)


if __name__ == "__main__":
    p = multiprocessing.Pool(1000)
    with p as _p:
        _p.map(func_a, [])
