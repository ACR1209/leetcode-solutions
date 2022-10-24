class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        
        for i, s in enumerate(arr):
            if len(s) != len(set(s)):
                del arr[i]
        
        unique = [''] 
        len_unique = 0
        
        for s in arr:
            for u in unique:
                current = s + u
                if len(current) == len(set(current)):
                    unique.append(current)
                    len_unique = max(len_unique, len(current))
        return len_unique
        
            
            