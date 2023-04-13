# Time O(n) 
# Space O(n)
# Where n is the lenght of the pushed and popped list
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack: list = []
    
        #While there is something to push
        while len(pushed) > 0:
            stack.append(pushed.pop(0))
            # While there's a match between popped and stack remove it
            while len(stack) > 0 and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        
        return len(stack) == 0 
            


        