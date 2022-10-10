class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        i = 0
        while palindrome[i] == "a" and i < n // 2:
            i += 1
            
        return palindrome[:i] + "a" + palindrome[i + 1:] if i < n - 1 and i != n//2 else palindrome[:-1] + "b" 
        
        
        