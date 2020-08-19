# Arrays and Strings: 1.2
# Given two strings, write a method to decide if one is a permutation of the other

class Solution:
    def checkPermutation(self, s1, s2):
        # by definition permutations have same characters,
        # therefore must also have same length. 
        if len(s1) != len(s2):
            return False

        # since strings s1, s2 must have the same chars to be a valid permutation
        # if sorting both strings we can get an accurate comparison
        return sorted(s1) == sorted(s2)
