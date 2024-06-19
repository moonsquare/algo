from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            ano = target - nums[i]
            if ano in temp:
                return [i, temp.get(ano)]
            else:
                temp[nums[i]] = i


so = Solution()
so.twoSum([2, 7, 11, 15], 9)
