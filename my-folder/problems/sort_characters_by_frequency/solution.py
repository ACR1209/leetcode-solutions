class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([i[1]*i[0] for i in sorted([[j,i] for i,j in Counter(s).items()], reverse = True)])