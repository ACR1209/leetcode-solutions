class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Sort the list in decresing order for attack
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        result = 0
        max_def = 0
        
        # Loop through all the properties, but we 
        # are just going to compare defense 
        # because we know that:
        # attack(i) <= attack(i + 1) so the (i + 1)
        # can only be weak if and only if the 
        # previous elements have a bigger defense
        for _attack, defense in properties:
            if defense < max_def:
                result += 1
            else:
                max_def = defense
                
        return result
        

        