from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = nums[0]
        freq = 0
        for num in nums:
            if freq == 0:
                majority_element = num
            if majority_element == num:
                freq += 1
            else:
                freq -= 1
        return majority_element