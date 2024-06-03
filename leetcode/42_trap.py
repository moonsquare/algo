from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftPoint, rightPoint = 0, n - 1
        leftMax, rightMax = height[0], height[n-1]
        ans = 0
        while leftPoint < rightPoint:
            if height[leftPoint] < height[rightPoint]:
                if height[leftPoint] > leftMax:
                    leftMax = height[leftPoint]
                ans = ans + leftMax - height[leftPoint]
                leftPoint += 1
            else:
                if height[rightPoint] > rightMax:
                    rightMax = height[rightPoint]
                ans = ans + rightMax - height[rightPoint]
                rightPoint -= 1
        return ans
