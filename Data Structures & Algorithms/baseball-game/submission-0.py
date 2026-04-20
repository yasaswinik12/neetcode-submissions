class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for operation in operations:
            if operation == '+':
                score = stack[-1] + stack[-2]
                stack.append(score)
                res += score
            elif operation == 'D':
                score = stack[-1]*2
                stack.append(score)
                res += score
            elif operation == 'C':
                score = stack.pop()
                res -= score
            else:
                score = int(operation)
                stack.append(score)
                res += score
        return res

        