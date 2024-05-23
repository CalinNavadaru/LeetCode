from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if middle == 0 and nums[middle] > nums[middle + 1]:
                return 0
            if middle == len(nums) - 1 and nums[middle] > nums[middle - 1]:
                return len(nums) - 1
            if nums[middle - 1] < nums[middle] > nums[middle + 1]:
                return middle
            if nums[middle - 1] >= nums[middle] >= nums[middle + 1]:
                right = middle - 1
            elif nums[middle] <= nums[middle + 1] or \
                    nums[middle] <= nums[middle + 1]:
                left = middle + 1

        return 0


a = Solution()
print(a.findPeakElement([1, 2, 3, 1]))
print(a.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
