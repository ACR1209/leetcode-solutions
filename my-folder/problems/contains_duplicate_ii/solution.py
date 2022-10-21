class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index_seen = {}
        
        for i, num in enumerate(nums):
            if num not in last_index_seen:
                last_index_seen[num] = i
                continue
            
            if i - last_index_seen[num] <= k:
                return True
            last_index_seen[num] = i
        
        return False
            
            