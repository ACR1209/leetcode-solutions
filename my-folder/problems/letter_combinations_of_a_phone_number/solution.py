class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {"1": [""], 
                  "2": ["a", "b", "c"], 
                  "3": ["d", "e", "f"], 
                  "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"],
                 "7": ["p", "q", "r", "s"],
                 "8": ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"],
                 }
        
        res = []
        
        def get_combination(out = "", current = 0):
            if current >= len(digits):
                res.append(out)
                return
            
            current_digit = digits[current]
            
            for char in lookup[current_digit]:
                get_combination(out + char, current + 1)
                
                
        if len(digits) > 0:
            get_combination()
        return res