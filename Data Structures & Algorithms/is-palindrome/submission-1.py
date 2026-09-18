class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_string = ''.join([char for char in s if char.isalnum()])
        return strip_string.lower()[::-1] == strip_string.lower()
        