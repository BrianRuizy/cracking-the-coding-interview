# implement a method to perform basic string compression using the
# counts of repeated characters.

# example:
# aabcccccaaa -> a2b1c5a3

# Note:
# if the true "compressed" string would not become smaller than the original,
# your method should return the original SyntaxWarning
# You can assume the string has only upper and lowercase letters (a-z)
from itertools import groupby


class Solution:
    def string_compression(self, s):
        """[summary]
        Naive approach would be to traverse the mutable string s,
        then compare the current char to the next char to
        distinguish when it changes value.

        Then concatenating all groups of that traversal.
        Example: 'aabccca' -> 'aa' + 'b' + 'ccc' + 'a'

        However, string s can be 1 < n < 10^5 long.
        String concatenation requires making a copy, or n copies,
        reaching O(n^2) quadratic time.

        A better approach would be to make a list of said 'groups'
        using ''.join(), which only takes O(N)
        (where N is the total length of the output)
        """
        # 1. compress the string
        compressed_list = []
        groups = groupby(s)  # groupby object

        for letter, group in groups:
            compressed_list.append(f'{letter}{sum([1 for _ in group])}')
        compressed_string = ''.join(compressed_list)

        # 2. compare the lengths.
        # Return original if compressed is longer
        if len(compressed_string) > len(s):
            return s

        return compressed_string
