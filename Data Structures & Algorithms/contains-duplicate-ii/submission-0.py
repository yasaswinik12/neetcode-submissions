class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        hashset = set()
        for r in range(len(nums)):
            if r - l > k:
                hashset.remove(nums[l])
                l += 1
            if nums[r] in hashset:
                return True
            hashset.add(nums[r])
        return False