from typing import List


def two_num(nums: List[int], target: int) -> List[int]:
    lists = len(nums)
    m = {}
    r = []
    for i in range(lists):
        t = target - nums[i]
        if t in m:
            r.append(m[t])
            r.append(i)
            return r
        else:
            m[nums[i]] = i
    return r
