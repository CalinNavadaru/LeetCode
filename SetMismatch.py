from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = dict.fromkeys(range(1, len(nums) + 1), 0)
        for num in nums:
            d[num] += 1

        result = [0] * 2
        for num in d.keys():
            if d[num] == 2 or d[num] == 0:
                if d[num] == 2:
                    result[0] = num
                else:
                    result[1] = num
        return result