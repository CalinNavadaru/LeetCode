class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        p1 = 1
        p2 = 1
        a = range(0, len(nums) - 1)
        b = range(len(nums) - 1, 0, -1)
        result = [1] * len(nums)
        for i_p1, i_p2 in zip(a, b):
            p1 *= nums[i_p1]
            p2 *= nums[i_p2]
            result[i_p1 + 1] *= p1
            result[i_p2 - 1] *= p2

        return result