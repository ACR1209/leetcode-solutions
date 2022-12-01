class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        seen = set()
        for i in count.values():
            if i not in seen:
                seen.add(i)
            else:
                return False

        return True