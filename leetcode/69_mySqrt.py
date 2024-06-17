class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        ans = -1
        # 二分查找的时候需要考虑是<=还是<
        while i <= j:
            mid = (i + j) // 2
            midSquare = mid * mid
            if midSquare > x:
                j = mid - 1
            else:
                ans = mid
                i = mid + 1
        return ans
