class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 1
        length = 4
        for i in range(2, n + 1):
            if(i == length):
                length *= 2
            
            ans = (ans * length + i) % 1000000007
        
        return ans