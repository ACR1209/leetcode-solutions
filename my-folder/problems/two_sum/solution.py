class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        res = []
        for i, num in enumerate(nums):
            if num not in complement:
                complement[target - num] = i
            else:
                return [i, complement[num]]
            