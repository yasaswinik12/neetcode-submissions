class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_arr = [0]*3
        for num in nums:
            count_arr[num] += 1
        i = 0
        color = 0
        for count in count_arr:
            while count != 0:
                nums[i] = color
                i += 1
                count -= 1
            color += 1


            
