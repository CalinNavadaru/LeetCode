from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        result = [[1]]
        for iteration in range(2, num_rows + 1):
            new_row = []
            for i in range(len(result[-1]) - 1):
                new_row.append(result[-1][i] + result[-1][i + 1])
            row = [1] + new_row + [1]
            result.append(row)
        return result
