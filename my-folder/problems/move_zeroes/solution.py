class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        
        if any(nums): 
            
            i = 0
            add = 0
            while i < len(nums):
                if nums[i] == 0:
                    nums.pop(i)
                    add += 1
                else:
                    i += 1
            
            for i in range(add):
                nums.append(0)
            
                
        