class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        found = set()
        
        for char in sentence:
            if char not in found:
                found.add(char)
                
        return len(found) == 26
        