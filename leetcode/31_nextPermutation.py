from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        j = len(nums) - 1
        while j > 0:
            if nums[j - 1] < nums[j]:
                # 此时已找出要替换的nums[j-1]，用j到end里比nums[j-1]大的最小的。并且j到end目前是降序
                break
            j -= 1
        if j > 0:
            i = len(nums) - 1
            while i > j - 1:
                if nums[i] > nums[j - 1]:
                    nums[i], nums[j - 1] = nums[j - 1], nums[i]
                    break
                i -= 1
        #
        k, t = j, len(nums) - 1
        while k < t:
            nums[k], nums[t] = nums[t], nums[k]
            k += 1
            t -= 1

