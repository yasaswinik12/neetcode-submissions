class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = len(nums) 
        left_sum = []
        total = 0
        for n in nums:
            total += n
            left_sum.append(total)
        for i in range(len(nums)):
            right_sum = total - left_sum[i]
            if left_sum[i] - nums[i] == right_sum:
                return i
        return -1
        