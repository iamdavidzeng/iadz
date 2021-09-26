# -*- coding: utf-8 -*-


# insert_sort
def insert_sort(lst):
    for i in range(1, len(lst)):
        pivot = lst[i]
        for j in range(i, -1, -1):
            if pivot < lst[j - 1]:
                lst[j] = lst[j - 1]
            else:
                break
        lst[j] = pivot

    # tool_lst = []
    # for i in lst:
    #     if not tool_lst:
    #         tool_lst.append(i)
    #     else:
    #         for j in range(len(tool_lst)):
    #             if i < tool_lst[j]:
    #                 tool_lst.insert(j, i)
    #                 break
    return lst


# select_sort
def select_sort(lst):
    for i in range(len(lst)):
        tmp = lst[i]
        target = i
        for j in range(i + 1, len(lst)):
            if tmp > lst[j]:
                target, tmp = j, lst[j]
        lst[i], lst[target] = tmp, lst[i]
    return lst


# bubble_sort
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# quick_sort
def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        left = [item for item in lst[1:] if item <= pivot]
        right = [item for item in lst[1:] if item > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


# merge_sort
def merge_sort(lst):
    def merge(left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result

    if len(lst) < 2:
        return lst
    else:
        pivot = len(lst) // 2
        left = merge_sort(lst[:pivot])
        right = merge_sort(lst[pivot:])
        return merge(left, right)


if __name__ == "__main__":
    unsorted_lst = [10, 2, 3, 4, 5, 1]
    print(insert_sort(unsorted_lst.copy()))
    print(select_sort(unsorted_lst.copy()))
    print(bubble_sort(unsorted_lst.copy()))
    print(quick_sort(unsorted_lst.copy()))
    print(merge_sort(unsorted_lst.copy()))
