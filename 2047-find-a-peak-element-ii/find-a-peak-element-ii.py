class Solution:
    def maxind(self,mat,cols):
        maxval=-1
        maxindex=-1
        m=len(mat)

        for i in  range (m):
            if mat[i][cols]>maxval:
                maxval=mat[i][cols]
                maxindex=i
        
        return maxindex


    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            maxrow=self.maxind(mat,mid)
            left = mat[maxrow][mid - 1] if mid - 1 >= 0 else -1
            right = mat[maxrow][mid + 1] if mid + 1 < n else -1 
            if mat[maxrow][mid]>left and mat[maxrow][mid]>right:
                return [maxrow,mid]
            elif mat[maxrow][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return[-1,-1]



        