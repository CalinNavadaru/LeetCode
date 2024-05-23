import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        s = n * (n + 1) // 2
        x = math.sqrt(s)
        if x.is_integer():
            return int(x)
        return -1