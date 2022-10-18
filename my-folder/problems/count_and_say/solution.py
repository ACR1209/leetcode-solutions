class Solution:
    def countAndSay(self, n: int) -> str:
        def count_freq(s):
            freq = []
            l = r = 0
            i = 0
            while i < len(s):
                l = i
                while r < len(s) and s[l] == s[r]:
                    r += 1
                freq.append([r - l, s[l]])
                i = r
            
            return freq
        def make_str(l):
            s = ""
            for freq, num in l:
                s += str(freq) + num
            return s
        
        s = "1"
        for i in range(n - 1):
            freq = count_freq(s)
            s = make_str(freq)
        
        return s
