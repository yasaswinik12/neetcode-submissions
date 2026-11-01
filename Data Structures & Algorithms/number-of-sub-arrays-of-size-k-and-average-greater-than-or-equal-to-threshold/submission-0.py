from collections import deque
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        hashset = deque([])
        res = 0
        for r in range(len(arr)+1):
            if r - l == k:
                # calculate the sum of hashset
                total = 0
                for num in hashset:
                    total+=num
                avg = total/k
                if avg >= threshold:
                    res += 1
                hashset.popleft()
                l+=1
            if r >= len(arr):
                continue
            hashset.append(arr[r])
        return res
