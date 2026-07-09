class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        rowtract=[0]*r
        coltract=[0]*c
        for i in range (0,r):
            for j in range(0,c):
                if matrix[i][j]==0:
                    rowtract[i]=-1 
                    coltract[j]=-1
            

        for i in range (0,r):
            for j in range(0,c):
                if rowtract[i]==-1 or coltract[j]==-1:
                    matrix[i][j]=0

        