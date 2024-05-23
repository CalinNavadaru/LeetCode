class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for index, c in enumerate(s):
            if c == "(":
                stack.append(index)
            elif c == ")":
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(index)

        while stack and star:
            if stack[-1] > star[-1]:
                return False
            stack.pop()
            star.pop()
        return len(stack) == 0
