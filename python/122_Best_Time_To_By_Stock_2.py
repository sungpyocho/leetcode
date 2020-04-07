# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
        result = 0

        for profit in profits:
            if profit > 0:
                result += profit
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,2,3,4,5]))