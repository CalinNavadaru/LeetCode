class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        transport = 0
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        while i1 >= 0 or i2 >= 0:
            x1 = int(num1[i1]) if i1 >= 0 else 0
            x2 = int(num2[i2]) if i2 >= 0 else 0
            value = x1 + x2 + transport
            transport = value // 10
            value %= 10
            result.insert(0, str(value))
            i1 -= 1
            i2 -= 1
        if transport:
            result.insert(0, str(transport))

        return "".join(result)


a = Solution()
print(a.addStrings("11", "123"))
