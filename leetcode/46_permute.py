from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        use = []
        ans = []
        self.recur(nums, use, ans)
        return ans

    def recur(self, nums, use, ans):
        if len(nums) == len(use):
            ans.append(use)
            return
        left = list(set(nums).difference(set(use)))
        for num in left:
            use_copy = use.copy()
            use_copy.append(num)
            self.recur(nums, use_copy, ans)
