class Solution:
    def maximum69Number (self, num: int) -> int:

        def get_digit(n: int)->int:
            if num // 10**n % 10 < 0:
                return False
            return num // 10**n % 10

        max: int = num
        i: int = 0

        while digit := get_digit(i): 
            current: int = num - (6 * (10**i)) + (9 * (10**i))
            if digit == 6 and max < current:
                max = current

            i += 1

        return max

        
