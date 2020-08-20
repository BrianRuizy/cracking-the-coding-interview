# There are three types of edits that can be performed on strings
# Insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit
# (or zero edits) away
# hard


class Solution:
    def one_away(self, first, second):
        if len(first) == len(second):
            return self.__one_replace(first, second)  # replacement to be 1-away
        elif len(first) + 1 == len(second):
            return self.__one_insert(first, second)  # Insertion to be 1-away
        elif len(first) - 1 == len(second):
            return self.__one_insert(second, first)  # Deletion to be 1-away
        
        return False

    def __one_replace(self, s1, s2):
        # there should only be 1 char different
        # therefore if flag encountered twice return false
        difference = False
        # Assuming both strings are of same length
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if difference:
                    return False
                difference = True

        return True

    def __one_insert(self, s1, s2):
        index1 = 0
        index2 = 0

        while index2 < len(s2) and index1 < len(s1):
            if s1[index1] != s2[index2]:
                if index1 != index2:
                    return False
                index2 += 2
            else:
                index1 += 1
                index2 += 1

        return True
