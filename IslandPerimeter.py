from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return self.compute_perimeter(grid)

    def compute_perimeter(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self.__compute(i, j, grid)

    def __compute(self, i, j, grid):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return 0
        grid[i][j] = -1
        s = 0
        if 0 <= i + 1 < len(grid) and grid[i + 1][j] == 1:
            s += self.__compute(i + 1, j, grid)
        if 0 <= i + 1 < len(grid) and grid[i - 1][j] == 1:
            s += self.__compute(i - 1, j, grid)
        if 0 <= j < len(grid[0]) and grid[i][j + 1] == 1:
            s += self.__compute(i, j + 1, grid)
        if 0 <= j < len(grid[0]) and grid[i][j - 1] == 1:
            s += self.__compute(i, j - 1, grid)

        return s + 1


a = Solution()
print(a.compute_perimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
