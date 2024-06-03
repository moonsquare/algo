# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
import sys
from typing import List


# 解题思路，遍历记录当前最低价格与最大利润，遍历完成即是最大利润
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_profit = 0
        for curPrice in prices:
            if curPrice < min_price:
                min_price = curPrice
            else:
                max_profit = max(max_profit, curPrice - min_price)
        return max_profit
