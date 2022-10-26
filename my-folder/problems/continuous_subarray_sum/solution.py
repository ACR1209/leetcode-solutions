class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = i = 0
        seen = {0: 0} 
        
        while i < len(nums):
            s += nums[i]
            if s % k not in seen:
                seen[s % k] = i + 1
            
            if seen[s % k] < i:
                return True
            
            i += 1
            
        return False
        