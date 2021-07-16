from decimal import Decimal
foo = [
    {
        "minimum_price": "1234.00"
    },
    {
        "minimum_price": "160.00"
    },
    {
        "minimum_price": "159.00"
    },
]

bar = sorted(foo, key=lambda f: Decimal(f["minimum_price"]), reverse=False)
print(f"sorted: {bar}")
