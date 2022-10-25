class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = set([s])
        def backtrack(word, l=0):
            nonlocal res
            if l >= len(s):
                return 
            

            if not s[l].isnumeric():
                res.add(word[:l] + word[l].lower() + word[l + 1:])
                res.add(word[:l] + word[l].upper() + word[l + 1:])
                backtrack(word[:l] + word[l].lower() + word[l + 1:], l + 1)
                backtrack(word[:l] + word[l].upper() + word[l + 1:], l + 1)
            else:
                backtrack(word, l + 1)
            
        backtrack(s)
        return res