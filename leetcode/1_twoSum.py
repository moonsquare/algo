from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = len(nums)
        m = {}
        r = []
        for i in range(L):
            t = target-nums[i]
            if t in m :
                r.append(m[t])
                r.append(i)
                return r
            else :
                m[nums[i]]=i
        return r
l = [1,2,3,4,5]
s = Solution();
print(s.twoSum(l,9))

