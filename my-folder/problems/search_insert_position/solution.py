class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
        
        
        
        
    