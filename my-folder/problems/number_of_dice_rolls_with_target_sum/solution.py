class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        modulo = 10**9 + 7
        #don't use row 0 and all column 0 
        dp = [[0] * (target + 1) for j in range(n+1)]
      
        for dd in range(1, n+1):
            
            for tt in range(dd, min(k * dd, target) + 1 ):
                if dd == 1:
                    dp[dd][tt] = 1
                else:
                    end   = tt - 1
                    start = max(1, tt - k)
                    dp[dd][tt] = sum(dp[dd-1][start:end+1])
    
        return dp[n][target] % modulo           