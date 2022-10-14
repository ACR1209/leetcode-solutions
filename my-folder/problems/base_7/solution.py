class Solution:
    def convertToBase7(self, num: int) -> str:
        
        res = ""
        sign = "" if num > 0 else "-"
        num = abs(num)
        
        while num != 0:
            res = str(num % 7) + res
            num //= 7 
        
        return sign + res if len(res) > 0 else "0"
        