class Solution:

    def remove_parentheses(self, s, p1, p2, reverse):
        stack = []
        result = []
        step = 1
        if reverse:
            step = -1
        for c in s[::step]:
            if c == p1:
                stack.append(c)
                result.append(c)
            elif c == p2:
                if stack:
                    stack.pop()
                    result.append(c)
            else:
                result.append(c)

        return "".join(result[::step])

    def minRemoveToMakeValid(self, s: str) -> str:
        s1 = self.remove_parentheses(s, '(', ')', False)
        return self.remove_parentheses(s1, ')', '(', True)


a = Solution()
print(a.minRemoveToMakeValid("))(("))
