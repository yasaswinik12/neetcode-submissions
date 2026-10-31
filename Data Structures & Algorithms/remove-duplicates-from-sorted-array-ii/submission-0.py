class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        l = 0
        r = l + 1
        while r < len(nums):
            if nums[l] == nums[r]:
                count += 1
                if count == 2:
                    l += 1
                    nums[l] = nums[r]
            else:
                nums[l+1] = nums[r]
                l += 1
                count = 1
            r += 1
            # print(l, r, count, nums)
        return l+1