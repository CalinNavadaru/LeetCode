def prop(c1, c2):
    return (c1.lower() == c2.lower() and
            (c1.isupper() and c2.islower() or
             c1.islower() and c2.isupper()))


class Solution:
    def makeGood(self, s: str) -> str:
        i = 1
        s = [c for c in s]
        while i <= len(s) - 1:
            if i > 0 and prop(s[i - 1], s[i]):
                s.pop(i - 1)
                s.pop(i - 1)
                i -= 2
            i += 1

        if len(s) == 2 and prop(*s):
            return ""
        return "".join(s)