from sortedcontainers import SortedList
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst: SortedList = SortedList(nums1)
        lst.update(nums2)
        n: int = len(lst)
        return (lst[n // 2]  + lst[(n // 2) - 1]) / 2 if n % 2 == 0 else lst[n // 2]