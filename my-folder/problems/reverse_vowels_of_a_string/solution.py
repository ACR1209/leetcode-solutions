class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels: str = "aeiou"
        res = list(s)
        l: int = 0
        r: int = len(s) - 1

        while l < r:
            if res[l].lower() not in vowels:
                l += 1
                continue
            if res[r].lower() not in vowels:
                r -= 1
                continue

            res[l], res[r] = res[r], res[l]

            l += 1
            r -= 1
            
        return "".join(res)

