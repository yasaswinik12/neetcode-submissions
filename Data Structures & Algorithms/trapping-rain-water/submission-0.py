class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = [0]*len(height), [0]*len(height)
        cur_max = 0 
        for i in range(1, len(height)):
            left_max[i] = max(height[i-1], left_max[i-1])
        cur_max = 0
        for j in range(len(height)-2, -1, -1):
            right_max[j] = max(height[j+1], right_max[j+1])
        res = 0
        for k in range(len(height)):
            water = min(left_max[k], right_max[k])
            if water > height[k]:
                trapped_water = water - height[k]
                res += trapped_water
        return res        