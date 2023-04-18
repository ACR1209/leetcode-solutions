class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rest = '' if len(word1) == len(word2) else word2[len(word1):] if len(word2) > len(word1) else word1[len(word2):]

        return ''.join([x+y for x,y in zip(word1, word2)] + [rest])