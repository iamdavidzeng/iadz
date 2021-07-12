foo = [
    {
        "minimum_price": 100,
    },
    {
        "minimum_price": 200,
    },
    {
        "minimum_price": 50,
    },
]

bar = sorted(foo, key=lambda f: f["minimum_price"], reverse=False)
print(f"sorted: {bar}")
