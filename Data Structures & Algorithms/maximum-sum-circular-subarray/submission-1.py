class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max, cur_min = 0, 0
        global_max, global_min = nums[0], nums[0]
        total = 0
        for n in nums:
            cur_max = max(cur_max, 0)
            cur_max += n
            global_max = max(cur_max, global_max)
            if cur_min == 0:
                cur_min += n
            else:
                cur_min = min(cur_min + n, n)
            global_min = min(cur_min, global_min)
            total += n
        print(global_min, global_max, total)
        if global_max < 0:
            return global_max
        else:
            return max(global_max, total - global_min )