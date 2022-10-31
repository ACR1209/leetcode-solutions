class Solution:
    def isToeplitzMatrix(self, a: List[List[int]]) -> bool:
        return all([ m - 1 < 0 or n - 1 < 0 or a[m][n] == a[m - 1][n - 1] for m in range(len(a)) for n in range(len(a[0]))])