from typing import List


class Solution:
    def dfs(self, grid, x, y):
        grid[x][y] = "0"
        for v, h in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= v < len(grid) and 0 <= h < len(grid[0]) and grid[v][h] == "1":
                self.dfs(grid, v, h)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    self.dfs(grid, x, y)
                    ans += 1
        return ans


so = Solution()
so.numIslands([["1", "0", "1", "1", "0", "1", "1"]])
