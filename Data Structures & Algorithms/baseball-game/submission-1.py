class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total_score = 0
        for operation in operations:
            if operation == "+":
                score = record[-1] + record[-2]
                record.append(score)
                total_score += score
            elif operation == "D":
                score = record[-1]*2
                record.append(score)
                total_score += score
            elif operation == "C":
                score = record.pop()
                total_score -= score
            else:
                record.append(int(operation))
                total_score += int(operation)
        return total_score
            