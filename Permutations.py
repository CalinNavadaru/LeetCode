from typing import List


class Solution:
    sol = []
    result = []
    visited = []

    def __init__(self):
        self.sol = []
        self.result = []
        self.visited = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.sol = [0 for _ in range(len(nums))]
        self.visited = [False for _ in range(len(nums))]
        self.__perm(nums, 0)
        return self.result

    def __perm(self, nums, index):
        if index == len(nums):
            self.result.append(self.sol.copy())
            return

        for i in range(len(nums)):
            if not self.visited[i]:
                self.visited[i] = True
                self.sol[index] = nums[i]
                self.__perm(nums, index + 1)
                self.sol[index] = 0
                self.visited[i] = False
