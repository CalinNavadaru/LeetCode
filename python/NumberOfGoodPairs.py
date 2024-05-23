from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                a += 1 * (nums[i] == nums[j])

        return a