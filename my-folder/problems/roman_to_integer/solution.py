class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        values={ 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        total = 0

        for index, char in enumerate(s[:-1]):
            total += values[char] if values[char] >= values[s[index + 1]] else (-values[char])

        return total + values[s[-1]]
        