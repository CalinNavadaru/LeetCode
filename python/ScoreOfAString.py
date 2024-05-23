class Solution:
    def scoreOfString(self, s: str) -> int:
        new_s = [ord(c) for c in s]
        result = 0
        for i in range(1, len(new_s)):
            result += abs(new_s[i] - new_s[i - 1])

        return result
