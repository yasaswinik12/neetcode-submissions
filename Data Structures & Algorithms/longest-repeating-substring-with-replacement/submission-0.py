class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        cur_freq = 0
        count_hm = {}
        res = 0
        for r in range(len(s)):
            if s[r] in count_hm:
                count_hm[s[r]] +=1
            else:
                count_hm[s[r]] = 1
            cur_freq = max(cur_freq, count_hm[s[r]])
            while r-l+1 - cur_freq > k:
                count_hm[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res

        