class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum()) # lowercase, no space, alphanumeric
        left = 0 
        right = len(s) - 1

        while left < right: # until pointers pass over
            if s[left] != s[right]:
                return False # don't match
            left += 1
            right -= 1

        return True   