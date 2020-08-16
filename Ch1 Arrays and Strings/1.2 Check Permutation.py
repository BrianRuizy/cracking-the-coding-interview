# Arrays and Strings: 1.2
# Given two strings, write a method to decide if one is a permutation of the other

class Solution:
    def checkPermutation(self, s1, s2):
        s1_map = {}
        
        for index,letter in enumerate(s1):
            s1_map[letter] = index
