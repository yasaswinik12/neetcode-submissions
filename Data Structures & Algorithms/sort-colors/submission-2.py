class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for color in nums:
            counts[color] += 1
        i = 0
        for color in range(3):
            count = counts[color]
            for _ in range(count):
                nums[i] = color
                i+=1
        
        