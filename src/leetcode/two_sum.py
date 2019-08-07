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

            for j in range(i+1, len(nums)):

                if nums[j] == wait_for_find:
                    lst += [i, j]
                    break
        return lst

    def two_sum(self, nums, target):
        pass


if __name__ == "__main__":

    solution = Solution()

    result = solution.twoSum([2, 2, 11, 15], 4)

    print(result)
