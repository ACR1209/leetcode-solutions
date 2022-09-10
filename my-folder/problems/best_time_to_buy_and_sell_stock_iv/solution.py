class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or len(prices) < 2:
            return 0
        
        l = [0] * (k + 1)
        g = [0] * (k + 1)
        
        for i, day in enumerate(prices[:-1]):
            profit = prices[i + 1] - day
            for j in range(k, 0, -1):
                l[j] = max(g[j - 1] + max(profit, 0), l[j] + profit)
                g[j] = max(l[j], g[j])
        
        return g[k]
            