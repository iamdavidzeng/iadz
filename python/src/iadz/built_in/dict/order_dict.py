from collections import OrderedDict


def get_diffs(after: dict, before: dict) -> OrderedDict:
    return OrderedDict(
        (key, [after.get(key), before.get(key)])
        for key in sorted(after)
        if after.get(key) != before.get(key)
    )


if __name__ == "__main__":
    foo = {"name": "david"}
    bar = {"name": "lucy"}
    changed = get_diffs(foo, bar)
    changed_data = {field: foo.get(field) for field in foo if field in changed}
    print(changed_data)
