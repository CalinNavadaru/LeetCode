from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        sum_val = 0
        d = {}
        for index, num in enumerate(nums):
            sum_val += 1 if num == 1 else -1
            if sum_val == 0:
                max_len = index + 1
            elif sum_val in d:
                max_len = max(max_len, index - d[sum_val])
            else:
                d[sum_val] = index

        return max_len
