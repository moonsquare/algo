from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans
        while True:
            i = j = 0
            while j < len(matrix[i]):
                ans.append(matrix[i][j])
                j += 1
            matrix.pop(i)
            if not matrix or not matrix[0]:
                return ans
            i = 0
            j = len(matrix[i]) - 1
            while i < len(matrix):
                ans.append(matrix[i][j])
                matrix[i].pop(j)
                i += 1
            if not matrix or not matrix[0]:
                return ans
            i = len(matrix) - 1
            j = len(matrix[i]) - 1
            while j >= 0:
                ans.append(matrix[i][j])
                j -= 1
            matrix.pop(i)
            if not matrix or not matrix[0]:
                return ans
            i = len(matrix) - 1
            j = 0
            while i >= 0:
                ans.append(matrix[i][j])
                matrix[i].pop(j)
                i -= 1
            if not matrix or not matrix[0]:
                return ans


so = Solution()
matrix = [[], [], []]
so.spiralOrder(matrix)
