class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:      
        return [index for index, _val in sorted([(i, sum(row)) for i, row in enumerate(mat)], key=lambda x: (x[1], x[0]))[:k]]