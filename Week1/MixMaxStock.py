from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r] :
                flag = prices[r] - prices[l]
                profit = max(profit, flag)
            else:
                l = r

            r = r + 1

        return profit
