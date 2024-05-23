class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            elif c == ')':
                max_depth = max(depth, max_depth)
                depth -= 1

        return max_depth
