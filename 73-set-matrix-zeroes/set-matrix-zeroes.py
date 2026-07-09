from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        
        # Helper function must accept r and c, or be nested to access them
        def markInfinity(row: int, col: int):
            for i in range(0, r):
                if matrix[i][col] != 0:
                    matrix[i][col] = float('inf')
            for j in range(0, c):
                if matrix[row][j] != 0:
                    matrix[row][j] = float('inf')

        # Step 1: Mark rows and columns of 0s with infinity
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    markInfinity(i, j)
                    
        # Step 2: Replace all infinity markers with 0
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
