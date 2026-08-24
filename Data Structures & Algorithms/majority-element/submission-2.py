class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # TC: O(nlogn)
        # nums.sort()
        # return nums[len(nums)//2]
        # TC: O(1)
        count = 0
        for num in nums:
            if count==0:
                res = num
            if res == num:
                count += 1
            else:
                count -= 1
        return res