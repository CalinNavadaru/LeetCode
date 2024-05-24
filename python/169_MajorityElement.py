from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_number = 0
        freq = 0
        for elem in nums:
            if freq == 0:
                majority_number = elem
            if majority_number == elem:
                freq += 1
            else:
                freq -= 1

        return majority_number
