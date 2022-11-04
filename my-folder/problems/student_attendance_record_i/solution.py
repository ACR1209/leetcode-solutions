class Solution:
    def checkRecord(self, s: str) -> bool:
        absent: int = 0
        late: int = 0
        i: int = 0

        while i < len(s):  
            if absent >= 2 or late >= 3:
                return False

            if s[i] == "L":
                late += 1
            else:
                late = 0

            if s[i] == "A":
                absent += 1

            i += 1
        
        return absent < 2 and late < 3
                

