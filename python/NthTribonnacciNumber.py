class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        a = 0
        b = 1
        c = 1
        d = 0
        while n - 3 >= 0:
            d = a + b + c
            a = b
            b = c
            c = d
            n -= 1
        return d
