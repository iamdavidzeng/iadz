xs = {"a": 4, "b": 3, "c": 2, "d": 1}

xs_1 = sorted(xs.items(), key=lambda x: x[1])


print(dict(zip([i[0] for i in xs_1], [i[1] for i in xs_1])))
