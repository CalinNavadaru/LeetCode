class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x - 1
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


def test():
    a = Solution()
    print(a.mySqrt(8))

test()