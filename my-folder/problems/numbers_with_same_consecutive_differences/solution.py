class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()
        
        def dfs(current, left):
            if left == 0:
                res.add(current)
                return
            
            last = current % 10
            if last + k <= 9:
                dfs(current * 10 + last + k, left - 1)
            
            if last - k >= 0:
                dfs(current * 10 + last - k, left - 1)
        
        for i in range(1, 10):
            dfs(i, n - 1)
            
        return list(res)
            