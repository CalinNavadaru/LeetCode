class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            d[c] = d.get(c, 0) - 1

        return all(d[c] == 0 for c in d)