class Solution:
    def permute(self, nums: List[int], path: List[int] =[], res: List[List[int]] = []) -> List[List[int]]:
       
        def backtrack(res=[], arr= nums, path=[]):
            if not arr:
                res.append(path)

            
            for i, n in enumerate(arr):
                arr.pop(i)
                backtrack(res, arr, path + [n])
                arr.insert(i, n)
            return res
        return  backtrack()

        


                             
