class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m_len = 0
        n = len(s)
        i, j = 0,0 
        seen = []
        while i < n and j < n:
            if s[j] not in seen:
                seen.append(s[j])
                j += 1
                m_len = max(m_len, j - i)
            else:
                seen.remove(s[i])
                i += 1
        
        return m_len
                
                
        