class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # if the number is odd it means 
        # it can't be a 
        # doubled array because the number of 
        # elements must be even
        if len(changed) % 2:
            return []
        
        count = Counter(changed)
        ans = []
        changed.sort()
        
        
        for num in changed:
            
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                ans.append(num)
            elif num > 0 and count[num] and count[2 * num]:
                count[num] -= 1
                count[2*num] -= 1
                
                ans.append(num)
        
        
        return ans if len(ans) == len(changed) // 2 else []