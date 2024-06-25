from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for interval in intervals:
            for i in range(len(ans) - 1, -1, -1):
                if interval[0] <= ans[i][1] and interval[1] >= ans[i][0]:
                    interval[0] = min(ans[i][0], interval[0])
                    interval[1] = max(ans[i][1], interval[1])
                    ans.pop(i)
            ans.append(interval)
        return ans

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先对左端点排序，再合并区间比较简单
        intervals.sort(key=lambda x: x[0])
        ans = []
        for interval in intervals:
            if not ans[-1] and interval[0] <= ans[-1][1]:
                interval[1] = max(interval[1],ans[-1][1])
            else:
                ans.append(interval)
        return ans
