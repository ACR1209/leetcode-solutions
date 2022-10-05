class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:        
        seen = set(nums1)
        res = set()
        
        def add_seen(l):
            nonlocal seen, res
            
            for n in set(l):
                if n in seen:
                    res.add(n)
                    seen.remove(n)
                else:
                    seen.add(n)
            
        add_seen(nums2)
        add_seen(nums3)
        return [*res]
        
        
        