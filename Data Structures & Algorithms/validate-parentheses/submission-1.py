class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for bracket in s:
            if bracket not in mapping:
                stack.append(bracket)
            else:
                if stack:
                    if stack[-1]!= mapping[bracket]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if len(stack):
            return False
        else:
            return True