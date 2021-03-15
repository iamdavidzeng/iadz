# -*- coding: utf-8 -*-


def rorate(nums: list, k: int):
    """
    按照传入的k值将数组中的元素向右移动k个位置
    Args:
        lst: 传入的数组
        k: 元素需要移动的位置
    Return:
        旋转后的数组
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


if __name__ == "__main__":
    lst = [1, 2, 3]
    result = rorate(lst, 10)
    print(f"rorate: {lst}")
