class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)       # 4
        cols = len(matrix[0])    # 3
        for i in range(rows):
            if matrix[i][cols-1] < target:
                continue
            for j in range(cols):
                if matrix[i][j] == target:
                    return True
        return False            