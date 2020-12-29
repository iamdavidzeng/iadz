# -*- coding: utf-8 -*-


def merge_sorted(lst_1, lst_2):
    """
    Merge lst_2 into sotred lst_1
    Args:
        lst_1: sorted list
        lst_2: sorted list wait for merge to lst_1
    Return:
        sorted list
    """
    pass

    new = []

    i, j = 0, 0

    for _ in range(len(lst_1) + len(lst_2)):

        if i == len(lst_1) and j < len(lst_2):
            new.append(lst_2[j])
            j += 1
        elif j == len(lst_2) and i < len(lst_1):
            new.append(lst_1[i])
            i += 1
        else:
            if lst_1[i] <= lst_2[j]:
                new.append(lst_1[i])
                i += 1
            else:
                new.append(lst_2[j])
                j += 1

    return new


if __name__ == "__main__":
    print(merge_sorted([1, 2, 3, 4], [1, 1, 3]))
