class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0
        n = len(chars)
        
        while i <= n - 1:
            j = i
            while j <= n - 1 and chars[i] == chars[j]:
                j += 1
            
            size = j - i
            digits = str(size)
            
            
            chars[k] = chars[i]
            k += 1
            if size > 1: 
                for digit in digits:
                    chars[k] = digit
                    k += 1
                                        
            i = j
       
        while k != len(chars):
            del chars[k]
    
                         
        
            
            
            
            
            
            
        