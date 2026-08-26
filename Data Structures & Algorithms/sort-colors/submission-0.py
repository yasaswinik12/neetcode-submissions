class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hm = {0: 0, 1: 0, 2: 0}
        for num in nums:
            hm[num] += 1
        stack = []
        stack.append(hm[2])
        stack.append(hm[1])
        stack.append(hm[0])
        i = 0
        color = 0
        while stack:
            count = stack.pop()
            while count != 0:
                nums[i] = color
                i += 1
                count -= 1
            color += 1

        
            
