class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = miss = 0

        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup = abs(num)
            else:
                nums[abs(num) - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                miss = i + 1
                
        
        return [dup, miss]

        
        
        
        
        