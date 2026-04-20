class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for idx in range(len(nums)):
            num = nums[idx]
            diff = target - num
            if num in hm:
                return [hm[num], idx]
            else:
                hm[diff] = idx
        