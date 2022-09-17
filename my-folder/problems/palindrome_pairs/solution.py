class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        
        def is_palindrome(str, start, end):
            """Check whether the substring is a palindrome string
            """
            part_word = str[start:end+1]
            return part_word == part_word[::-1]

        def find_reversed_word(str, start, end):
            """Find whether the substring is in the hash table
            Return:
                Not in hash table, return -1
                Otherwise, the corresponding index is returned
            """
            part_word = str[start:end+1]
            ret = hash_map.get(part_word, -1)
            return ret
        
        # Build a hash table to store flipped strings of strings in a given list
        # The key is the flipped string, and the value is the index corresponding to the string before flipping
        hash_map = {}
        for i in range(len(words)):
            word = words[i][::-1]
            hash_map[word] = i
        
        res = []
        
        # Traverse the string, split the string and judge
        for i in range(len(words)):
            word = words[i]
            word_len = len(word)
            # First judge the existence of an empty string. If the current string is a palindrome string (not an empty string), combine it with the current string and put it into the result
            if is_palindrome(word, 0, word_len-1) and "" in hash_map and word != "":
                res.append([hash_map.get(""), i])
            for j in range(word_len):
                # First, check whether the right part after division is a palindrome string
                if is_palindrome(word, j, word_len - 1):
                    # Find out whether the flip of the substring on the left is in the hash table
                    left_part_index = find_reversed_word(word, 0, j-1)
                    # When the returned index value is not - 1 and is not the index corresponding to the current string,
                    # Indicates that there are two strings that can form a palindrome string, and the index is added to the result list
                    if left_part_index != -1 and left_part_index != i:
                        res.append([i, left_part_index])
                # The principle is the same as above, but at this time, judge whether the left part is a palindrome string
                if is_palindrome(word, 0, j-1):
                    # Judge whether the right part of the substring flip is in the hash table
                    right_part_index = find_reversed_word(word, j, word_len-1)
                    if right_part_index != -1 and right_part_index != i:
                        res.append([right_part_index, i])

        return res
                
                
                
                        