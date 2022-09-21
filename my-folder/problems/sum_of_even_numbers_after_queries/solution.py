class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(x for x in nums if x % 2 == 0)
        res = []
        
        for val, i in queries:
            if nums[i] % 2 == 0:
                s -= nums[i]
                
            nums[i] += val
            
            if nums[i] % 2 == 0:
                s += nums[i]
            
            res.append(s)
            
        return res
        