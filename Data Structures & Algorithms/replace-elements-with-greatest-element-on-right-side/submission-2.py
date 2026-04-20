class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        res = [-1]*len(arr)
        for idx in range(len(arr)-2, -1, -1):
            if arr[idx+1] > right_max:
                res[idx] = arr[idx+1]
                right_max = arr[idx+1]
            else:
                res[idx] = right_max
        return res
        