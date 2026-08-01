class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # diff lengths, not anagram

        s_set = set(s) # convert to set - only unique chars
        for char in s_set: # compare counts of each unique char
            if s.count(char) != t.count(char):
                return False

        return True