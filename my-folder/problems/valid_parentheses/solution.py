class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        lookup = {")": "(", "}": "{", "]": "["}
        
        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                q.append(char)
            if char == ")" or char == "}" or char == "]":
                if len(q) == 0:
                    return False
                
                last = q.pop()
                if last != lookup[char]:
                    return False
        return len(q) == 0