class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if i + len(needle) - 1< len(haystack) and haystack[i:i+len(needle) ] == needle:
                return i
        return -1
