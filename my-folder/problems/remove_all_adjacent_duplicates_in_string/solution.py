class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if len(stack) != 0 and stack[-1] == char:
                stack.pop()
                continue
            
            stack.append(char)
        
        return "".join(stack)