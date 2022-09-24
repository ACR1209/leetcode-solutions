class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        
        s, e = 0, len(x_str) - 1
        
        while s < e:
            if x_str[s] != x_str[e]:
                return False
            s += 1
            e -= 1
        
        return True
        