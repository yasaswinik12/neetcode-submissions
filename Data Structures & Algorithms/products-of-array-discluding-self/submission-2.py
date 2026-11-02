class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]*len(nums)
        right_product = [1]*len(nums)
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1]*nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            right_product[j] = right_product[j+1]*nums[j+1]
        res = []
        for k in range(len(nums)):
            prod = left_product[k]*right_product[k]
            res.append(prod)
        return res
            