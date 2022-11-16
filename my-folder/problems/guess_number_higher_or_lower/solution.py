# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l: int = 1
        r: int = n
        while l <= r:
            current: int = ((l + r) // 2) 
            g: int = guess(current)
            if g == 0:
                return current
            
            if g == -1:
                r = current - 1
            else:
                l = current + 1
        
    
