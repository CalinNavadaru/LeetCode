class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        iso_map_s2t = {}
        iso_map_t2s = {}

        for c_s, c_t in zip(s, t):
            if c_s in iso_map_s2t:
                if iso_map_s2t[c_s] != c_t:
                    return False
            else:
                if c_t in iso_map_t2s:
                    return False

                iso_map_s2t[c_s] = c_t
                iso_map_t2s[c_t] = c_s

        return True
