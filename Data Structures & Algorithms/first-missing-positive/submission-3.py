class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # turn -ve numbers to 0 since they are not relevant
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for j in range(len(nums)):
            val = abs(nums[j])
            if 1 <= val <=len(nums):
                if nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums) + 1)
                elif nums[val - 1] > 0:
                    nums[val - 1] *= -1
        print(nums)
        for cur in range(1, len(nums)+1):
            if nums[cur-1] >= 0 :
                return cur
        return len(nums)+1