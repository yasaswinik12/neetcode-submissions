class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        if len(strs[0])>=1:
                prefix_char = strs[0][0]
                prefix_idx = 0
        else:
            return output
        while True:
            common = False
            for word in strs:
                if prefix_idx >= len(word):
                    return output
                if word[prefix_idx] == prefix_char:
                    common = True
                else:
                    common = False
                    break
            if common:
                output= output+prefix_char
                if prefix_idx+1 < len(strs[0]):
                    prefix_char = strs[0][prefix_idx+1]
                    prefix_idx = prefix_idx+1
                else:
                    break
            else:
                break

        return output
                