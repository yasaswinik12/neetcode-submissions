class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1
        for r in t:
            if r in hm:
                hm[r] -= 1
                if hm[r] == 0:
                    del hm[r]
            else:
                return False
        return True if not hm else False