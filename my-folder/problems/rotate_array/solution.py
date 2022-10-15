class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Seems to be slower, but it's O(1) in space and O(k) in time
        # n: int = len(nums)
        # if k >= n:
        #    k %= n
        #
        # for i in range(k):
        #   num: int = nums.pop()
        #   nums.insert(0, num)
        
        n = len(nums)
        res = [0] * n
        if k >= n:
            k %= n
        
        
        for i in range(n):
            new_pos = i + k
            
            if new_pos >= n:
                new_pos %= n
            
            res[new_pos] = nums[i]
        
        for i in range(n):
            nums[i] = res[i]
        
        
        
        
