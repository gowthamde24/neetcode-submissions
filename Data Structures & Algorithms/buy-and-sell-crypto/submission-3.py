class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max_profit = 0
        
        while r < len(prices):
            if prices[l]<prices[r]:
                currp = prices[r]-prices[l]
                max_profit = max(max_profit,currp)
            else:
                l=r


            r+=1
        return max_profit
        