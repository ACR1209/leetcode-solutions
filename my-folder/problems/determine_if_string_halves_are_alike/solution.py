class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        vowels_l = vowels_r = 0

        while l < r:
            if s[l] in 'aeiouAEIOU':
                vowels_l += 1
            if s[r] in 'aeiouAEIOU':
                vowels_r += 1
            l += 1
            r -= 1

        return vowels_l == vowels_r


    