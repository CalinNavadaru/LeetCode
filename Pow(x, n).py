class Solution:
    def __pow_aux__(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        return self.myPow(x * x, (n - 1) // 2) * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0 and x != 0:
            n = n - 2 * n
            x = 1 / x
        return self.__pow_aux__(x, n)
