# Time O(n)
# Space O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed: dict = { target - value: i for i, value in enumerate(nums) }

        # could do it in one line with list comprehension
        # return [[i, needed[num]] for i, num in enumerate(nums) if num in needed and needed[num] != i][0]
        for i, num in enumerate(nums):
            if num in needed and needed[num] != i:
                return [i, needed[num]]

        