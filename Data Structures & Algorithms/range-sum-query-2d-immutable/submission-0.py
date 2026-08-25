class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        # print(m, n)
        self.sm = [[0]*(n+1) for _ in range(m)]
        # print(self.sm, len(self.sm), len(self.sm[0]))
        for i in range(m):
            for j in range(1, n+1):
                self.sm[i][j] = self.sm[i][j-1] + self.matrix[i][j-1]
            #     print("self.sm, i, j", self.sm[i][j], i, j)
            # print(self.sm)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for p in range(row1, row2+1, 1):
            row_sum = self.sm[p][col2+1] - self.sm[p][col1] 
            res += row_sum
        return res   


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)