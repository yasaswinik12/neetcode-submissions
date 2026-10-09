class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #traversal 1 - whenever val is found,replace with -1
        # traversal 2 - swap -1 with next non -1 element whose value is not val
        # return 
        flag = 0
        for idx, num in enumerate(nums):
            if num == val:
                nums[idx] = -1
                flag += 1
        k  = len(nums) - flag
        i = 0
        j = i+1
        while j < len(nums):
            while nums[i] == -1:
                while j < len(nums) and nums[j] == -1:
                    j += 1
                if j >= len(nums):
                    return k
                nums[i] = nums[j]
                nums[j] = -1
            i += 1
            j += 1
        return k