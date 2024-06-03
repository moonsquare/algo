# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
# 你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 首先排序
        nums.sort()
        n = len(nums)
        ans = list()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = -nums[first]
            third = n - 1
            for second in range(first + 1, n):
                if second >= third:
                    break
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while nums[second] + nums[third] > target:
                    if third - 1 > second:
                        third = third - 1
                    else:
                        break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans
