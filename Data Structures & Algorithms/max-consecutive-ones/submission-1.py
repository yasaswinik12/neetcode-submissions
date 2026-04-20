class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur_res = 0
        prev = -1
        for idx in range(len(nums)):
            if nums[idx]==1:
                # if prev==-1:
                #     prev = idx
                cur_res += 1
            else:
                # prev = -1
                res = max(res, cur_res)
                cur_res = 0
        return max(res, cur_res)

            

                
        