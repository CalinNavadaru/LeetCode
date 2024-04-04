def cmp(open_parentheses, c):
    return (
            (open_parentheses == '(' and c == ')') or
            (open_parentheses == '{' and c == '}') or
            (open_parentheses == '[' and c == ']')
    )


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                open_parentheses = stack.pop()
                if not cmp(open_parentheses, c):
                    return False
        return not stack

