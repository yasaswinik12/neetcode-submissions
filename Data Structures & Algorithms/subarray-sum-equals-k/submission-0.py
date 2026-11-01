class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hm = {0:1}
        res = 0
        for num in nums:
            prefix_sum += num
            subarray_sum = prefix_sum - k
            if subarray_sum in hm:
                res += hm[subarray_sum]
            if prefix_sum in hm:
                hm[prefix_sum] += 1
            else:
                hm[prefix_sum] = 1
        return res 