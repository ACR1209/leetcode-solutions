class Solution:
    def reverseWords(self, s: str) -> str:        
       return ' '.join ( [ a for a in s.strip().split(' ')[::-1] if  len(a.strip()) > 0 ])


