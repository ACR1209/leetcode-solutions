class Solution:
    def findWords(self, words: List[str]) -> List[str]:


                    
        return [s for s in words for row in [ "qwertyuiop", "zxcvbnm", "asdfghjkl"] if all([ch in row for ch in s.lower()])]
    
                
    