import sys
from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            if nums[i] < 1:
                nums[i] = l + 1
        for i in range(l):
            if 0 <= abs(nums[i]) - 1 < l:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(l):
            if nums[i] > 0:
                return i + 1
        return l + 1

    def firstMissingPositive_2(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(len(nums)):
            while i < nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i] :
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            if 0 <= nums[i] - 1 <= i:
                nums[nums[i] - 1] = nums[i]
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums)+1


so = Solution()
so.firstMissingPositive([1, 2, 0])
