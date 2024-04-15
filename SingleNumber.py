from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_sum = 0
        for e in nums:
            xor_sum ^= e
        return xor_sum
