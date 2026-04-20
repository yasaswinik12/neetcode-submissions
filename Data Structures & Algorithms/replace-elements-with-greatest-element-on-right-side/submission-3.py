class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        res = [0]*len(arr)
        for i in range(len(arr)-1, -1, -1):
            res[i] = right_max
            right_max = max(right_max, arr[i])
        return res
        