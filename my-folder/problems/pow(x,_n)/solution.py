class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        current = x
        m = abs(n)
        while m > 0:
            if m & 1:
                result *= current
            current *= current
            m >>= 1

        return 1 / result if n < 0 else result
        
        