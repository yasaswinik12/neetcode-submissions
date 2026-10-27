class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # kadane's alogorithm
        curMin, curMax = 0, 0
        globalMin, globalMax = nums[0], nums[0]
        total = 0
        for n in nums:
            curMax = max(curMax, 0)
            curMax += n
            globalMax = max(globalMax, curMax)

            curMin = min(curMin, 0)
            curMin += n
            globalMin = min(globalMin, curMin)

            total += n

        if globalMax < 0:
            return globalMax
        else:
            return max(globalMax, total-globalMin)
