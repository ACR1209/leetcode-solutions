class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        l: int = 0
        r: int = n - 1
        res: List[int] = [0] * n
        i: int = r
        
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                res[i] = nums[l]**2
                l += 1
            else:
                res[i] = nums[r]**2
                r -= 1
            
            i -= 1
        
        return res
        