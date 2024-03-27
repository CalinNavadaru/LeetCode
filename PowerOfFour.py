class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        import math
        exponent = math.log(n, 4)
        return exponent == int(exponent)