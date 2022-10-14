# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l: int = 1
        r: int = n 
        last_bad: int = 0
        
        while l <= r:
            mid: int = (l + r) // 2
            if isBadVersion(mid):
                last_bad = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return last_bad
    