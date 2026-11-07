class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row_start, row_end = 0, rows-1
        while row_start <= row_end:
            row_mid = (row_start+row_end)//2
            if target > matrix[row_mid][-1]:
                row_start = row_mid + 1
            elif target < matrix[row_mid][0]:
                row_end = row_mid - 1
            else:
                break
        if row_start > row_end:
            return False
        col_start, col_end = 0, cols-1
        while col_start <= col_end:
            col_mid = (col_start+col_end)//2
            if target > matrix[row_mid][col_mid]:
                col_start = col_mid + 1
            elif target < matrix[row_mid][col_mid]:
                col_end = col_mid - 1
            else:
                return True
        return False
        