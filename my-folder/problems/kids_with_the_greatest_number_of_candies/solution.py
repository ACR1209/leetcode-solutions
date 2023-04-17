class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies: int = max(candies)
        return [candie + extraCandies >= maxCandies for candie in candies]