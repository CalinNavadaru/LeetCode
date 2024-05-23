from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        index = 0
        num = 0
        for index, num in enumerate(nums):
            if d.get(num, 0) == 0:
                d[target - num] = (num, index)
            else:
                return [index, d[num][1]]

        return [index, d[target - num][1]]
