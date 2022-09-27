class Solution:
    def pushDominoes(self, d: str) -> str:
        while True:
            
            new = d.replace('R.L', '|').replace('.L', 'LL').replace('R.', 'RR').replace('|', 'R.L')
            if new == d:
                break
            else:
                d = new
            
        return d