class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add_one(current):
            
            if digits[current] == 9:
                digits[current] = 0
                add_one(current - 1)
            elif current < 0:
                digits.insert(0, 1)    
            else:
                digits[current] += 1
        add_one(len(digits) - 1)
        return digits