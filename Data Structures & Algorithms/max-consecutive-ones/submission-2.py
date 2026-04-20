class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur_res = 0
        for idx in range(len(nums)):
            if nums[idx]==1:
                cur_res += 1
            else:
                res = max(res, cur_res)
                cur_res = 0
        return max(res, cur_res)

            

                
        