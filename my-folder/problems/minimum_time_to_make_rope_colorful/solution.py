class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        l, r = 0, 0
        
        while l < len(colors) and r < len(colors):
            c_total, c_max = 0, 0
            
            while r < len(colors) and colors[l] == colors[r]:
                c_total += neededTime[r]
                c_max = max(c_max, neededTime[r])
                r += 1
                
            time += c_total - c_max
            l = r
                
            
            
        return time
            