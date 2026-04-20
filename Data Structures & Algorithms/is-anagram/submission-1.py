
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = defaultdict()
        for c in s:
            if c not in hm:
                hm[c] = 1
            else:
                hm[c]+=1
        for c in t:
            if c in hm:
                hm[c] -=1
                if hm[c] == 0:
                    del hm[c]
            else:
                return False
        if len(hm):
            return False
        else:
            return True