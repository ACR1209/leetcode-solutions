class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        from functools import lru_cache
        
        @lru_cache()
        def helper(prices, buy):
            if not len(prices):
                return 0
            
            if buy:
                a = -prices[0]+helper(prices[1:], not buy)
                b = helper(prices[1:], buy)
            else:
                a = prices[0]+helper(prices[2:], not buy)
                b = helper(prices[1:], buy)
                
            return max(a, b)
        
        return helper(tuple(prices), True)