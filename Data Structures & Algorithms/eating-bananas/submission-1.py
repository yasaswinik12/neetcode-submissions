class Solution:
    def totalEatingHours(self, piles: List[int], k: int) -> int:
        total_hours = 0
        for pile in piles:
            total_hours += -(-pile//k)
        return total_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # print("l, r", l, r)
        res = r
        while l <= r:
            mid = (l+r) // 2
            # print("mid", mid)
            total_hours = self.totalEatingHours(piles, mid)
            # print("total_hours", total_hours)
            if total_hours > h :
                l = mid + 1
            elif total_hours <= h:
                res = min(res, mid)
                r = mid - 1
            # else:
            #     res = min(res, mid)
            #     break
        return res

            
        