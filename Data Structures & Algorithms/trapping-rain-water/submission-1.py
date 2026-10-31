class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = [0]*len(height), [0]*len(height)
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
        for j in range(len(height)-2, -1, -1):
            right_max[j] = max(right_max[j+1], height[j+1])
        area = 0
        for k in range(len(height)):
            trapped_area = min(left_max[k], right_max[k]) - height[k]
            if trapped_area > 0:
                area += trapped_area
        return area