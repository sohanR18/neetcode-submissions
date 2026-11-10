class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l , r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                
                maxp = max(maxp, profit)
            else:
                l = r
            r += 1
        return maxp