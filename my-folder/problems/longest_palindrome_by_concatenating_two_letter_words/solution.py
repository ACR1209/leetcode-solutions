class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        ans = 0
        central = False
        for word, count_w in count.items():
            
            if word[0] == word[1]:
                if count_w % 2 == 0:
                    ans += count_w
                    continue
            
                ans += count_w - 1
                if not central:
                    central = True
                    ans += 1
                
                continue
            
            if word[0] < word[1]:
                ans += 2 * min(count[word], count[word[1] + word[0]])
        
        return 2 * ans