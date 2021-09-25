class Solution:
    def isPalindrome(self, x: str) -> bool:
        x = str(x)
        return x == x[::-1]