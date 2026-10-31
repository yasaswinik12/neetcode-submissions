class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = [[0] *len(matrix[0])for _ in range(len(matrix))]
        for row in range(len(matrix)):
            total = 0
            for col in range(len(matrix[row])):
                total += matrix[row][col]
                self.prefix_sum[row][col] = total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2+1):
            prefix_sum_left = self.prefix_sum[row][col1-1]  if col1 > 0 else 0
            prefix_sum_right = self.prefix_sum[row][col2]
            row_sum = prefix_sum_right - prefix_sum_left
            res += row_sum
        return res



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)