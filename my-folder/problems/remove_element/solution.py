class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return len(nums)
        
        insert = nums.index(val)
        
        
        for i in range(insert + 1, len(nums)):
            if nums[i] != val:
                nums[insert] = nums[i]
                insert += 1
        
        return insert