import pytest


def merge_sort(lst):
    def merge(l1, l2):
        new = []
        while l1 and l2:
            if l1[0] < l2[0]:
                new.append(l1.pop(0))
            else:
                new.append(l2.pop(0))
        while l1:
            new.append(l1.pop(0))
        while l2:
            new.append(l2.pop(0))
        return new

    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


@pytest.mark.parametrize(
    ("params", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([2, 3, 4, 5, 1], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ],
)
def test_merge_sort(params, expected):
    assert merge_sort(params) == expected
