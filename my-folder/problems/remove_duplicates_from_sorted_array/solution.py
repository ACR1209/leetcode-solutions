class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size: int = len(nums)
        insertIndex: int = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1                   
        return insertIndex
            
            