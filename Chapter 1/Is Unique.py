# Arrays and Strings: 1.1
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

class Solution():
    def isUnique(self, s):
        unique = None
        string_map = {}

        for letter in s:
            if letter in string_map:
                unique = False
                break
            else:
                string_map[letter] = 0
                unique = True
        
        return unique