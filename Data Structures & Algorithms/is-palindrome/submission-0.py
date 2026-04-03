class Solution:
    def isPalindrome(self, s: str) -> bool:

        s= s.lower()
        s= ''.join(l for l in s if l.isalnum())
        return s == s[::-1]