import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums and k <= len(nums):
            left_nums, right_nums, mid_nums = list[int](), list[int](), list[int]()
            # 随机取一个元素做分割
            pivot_v = random.choice(nums)
            for i in nums:
                if i < pivot_v:
                    left_nums.append(i)
                elif i == pivot_v:
                    mid_nums.append(i)
                else:
                    right_nums.append(i)
            len_right = len(right_nums)
            len_mid_right = len_right + len(mid_nums)
            if len_right < k <= len_mid_right:
                return pivot_v
            elif k <= len_right:
                return self.findKthLargest(right_nums, k)
            else:
                return self.findKthLargest(left_nums, k - len_mid_right)
        else:
            return 0


nums1 = [-1, -1]
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
solution = Solution()
print(solution.findKthLargest(nums1, 2), end=" ")
print(solution.findKthLargest(nums2, 4), end=" ")
