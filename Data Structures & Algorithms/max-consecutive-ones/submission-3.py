class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, cur_max = 0, 0
        for num in nums:
            if num == 1:
                cur_max += 1
            else:
                res = max(res, cur_max)
                cur_max = 0
        res = max(res, cur_max)
        return res