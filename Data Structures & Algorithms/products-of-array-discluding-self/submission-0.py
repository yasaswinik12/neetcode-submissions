class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]*len(nums)
        right_prod = [1]*len(nums)
        # compute left product
        for i in range(1, len(nums)):
            left_prod[i] = nums[i-1]*left_prod[i-1]
        # compute right product
        for j in range(len(nums)-2, -1, -1):
            right_prod[j] = nums[j+1]*right_prod[j+1]
        # compute output
        output = [1]*len(nums)
        for k in range(len(nums)):
            output[k] = left_prod[k]*right_prod[k]
        return output
