import sys
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(len(dp)):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS_2(self, nums: List[int]) -> int:
        sublist = []
        for num in nums:
            if not sublist or num > sublist[-1]:
                sublist.append(num)
            else:
                # 在sublist中找到位置
                i = 0
                j = rep = len(sublist) - 1
                while i <= j:
                    mid = (j + i) // 2
                    if num > sublist[mid]:
                        i = mid + 1
                    else:
                        rep = mid
                        j = mid - 1
                sublist[rep] = num
        return len(sublist)
