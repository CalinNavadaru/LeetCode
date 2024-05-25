from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        for elem in nums:
            xor_sum ^= elem
        return xor_sum
