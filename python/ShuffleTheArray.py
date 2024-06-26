from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(0, n):
            result.append(nums[i])
            result.append(nums[n + i])

        nums = result
        return nums
