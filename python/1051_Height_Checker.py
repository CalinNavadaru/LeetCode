class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct_heights = list(sorted(heights))
        return sum(x != y for x, y in zip(correct_heights, heights))
