class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        x_copy = x
        while x_copy:
            y = y * 10 + x_copy % 10
            x_copy //= 10
        return y == x
