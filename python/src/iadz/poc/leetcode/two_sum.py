# -*- coding: utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        for i in range(len(nums)):
            wait_for_find = target - nums[i]

            for j in range(i + 1, len(nums)):

                if nums[j] == wait_for_find:
                    lst += [i, j]
                    break
        return lst

    def two_sum(self, nums, target):
        map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in map:
                return [map[another_num], index]
            map[num] = index
        return None


if __name__ == "__main__":

    solution = Solution()

    result = solution.two_sum([2, 2, 11, 15], 4)

    print(result)
