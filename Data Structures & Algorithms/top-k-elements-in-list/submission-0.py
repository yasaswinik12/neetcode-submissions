from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            if num not in freq_map:
                freq_map[num]= 1
            else:
                freq_map[num]+=1
        num_freq = []
        for num in freq_map:
            num_freq.append([freq_map[num], num])
        num_freq.sort()
        res = []
        n = len(num_freq)
        while k > 0:
            res.append(num_freq[n - 1][1])
            k -= 1
            n -= 1
        return res


        