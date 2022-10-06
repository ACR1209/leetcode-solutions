class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_copy = [*set(arr)]
        arr_copy.sort()
        ranks = {}
        res = []
        
        for i, num in enumerate(arr_copy):
            ranks[num] = i + 1
        
        for num in arr:
            res.append(ranks[num])
            
        return res
         
        
        