class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # change all -ve numbers to 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for j in range(len(nums)):
            if nums[j] == 0 or abs(nums[j]) > len(nums):
                continue
            elif nums[abs(nums[j])-1] > 0:
                nums[abs(nums[j])-1] = -1 * nums[abs(nums[j])-1]
            elif nums[abs(nums[j])-1] == 0:
                nums[abs(nums[j])-1] = -1 * (len(nums)+1)
        for cur in range(1, len(nums)+1):
            if nums[cur-1] < 0:
                continue
            else:
                return cur
        return len(nums) + 1
                