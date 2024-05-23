from typing import List


class Solution:
    def __generate__(self, n, p, opened, closed):
        result = []
        if closed == opened == n:
            return [p]
        p1 = p + "("
        opened += 1
        if opened <= n:
            result.extend(self.__generate__(n, p1, opened, closed))
        opened -= 1
        closed += 1
        p1 = p + ")"
        if closed <= opened:
            result.extend(self.__generate__(n, p1, opened, closed))
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        return self.__generate__(n, "", 0, 0)