class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stack = []
        for char in s:
            if char in ("{", "[", "("):
                stack.append(char)
            else:
                if stack and stack[-1] == mapper[char]:
                    stack.pop()
                else:
                    return False
        return False if stack else True