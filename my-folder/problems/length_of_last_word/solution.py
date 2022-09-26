class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        en = len(s) - 1
        
        while s[en] == " ":
            en -= 1
        
        st = en - 1 if en - 1 >= 0 and s[en - 1] != " " else en      
       
        while st > 0 and s[st - 1] != " ":
            st -= 1
       
            
        return (en - st) + 1
        