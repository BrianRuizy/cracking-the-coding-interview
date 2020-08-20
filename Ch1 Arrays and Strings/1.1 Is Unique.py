# Arrays and Strings: 1.1
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

class Solution():
    def is_unique(self, s):
        # Create empty dictionary, hashmap
        string_map = {}

        # s > 256 not possible to since ASCII is finite
        if len(s) > 256: 
            return False

        # Traverse string s, and check if letter for s exists in mapping
        for letter in s:
            if letter in string_map:
                return False
            else:
                string_map[letter] = 0
        
        return True
        
        