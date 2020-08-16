# write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the 'true' length of the string.

# Note: if implementing in java, please us a character array so that you can perform this operation in-place
# Example: 'Mr John Smith' -> 'Mr%20Jogn%20Smith'

class Solution: 
    def urlify(self, s: str):
        # though requirements ask for in-place solution ...
        # in Python string objects are immutable, so must return copy regardless

        # This is the most pythonic approach to the problem
        return s.replace(' ', '%20')

    def urlify_2(self, s: str):
        # remove trailing whitespaces
        s = s.strip()