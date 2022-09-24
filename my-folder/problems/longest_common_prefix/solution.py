class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        for i,char in enumerate(min(strs)):
            if all(a[i] == char for a in strs):
                prefix += char
            else:
                break
        return prefix