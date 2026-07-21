class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
    #     if not matrix or not matrix:
    #         return False
    #     for i in range(m):
    #         index=self.bs(matrix,i,target)
    #         if index!=-1:
    #             return True
            
    #     return False


    # def bs(self,matrix,i,target):
    #     n=len(matrix[0])
    #     low=0
    #     high=n-1
    #     while low<=high:
    #         mid=(low+high)//2
    #         if matrix[i][mid]==target:
    #             return mid
    #         elif matrix[i][mid]<target:
    #             low=mid+1
    #         else:
    #             high=mid-1
    #     return -1

#  optimal sol

        row=0
        col=n-1
        while row<m and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False


        