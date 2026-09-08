class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # ans=[]
        # board=[["." for _ in range(n)]for _ in range(n) ]
        
        # def check(row,col):
        #     r,c=row,col
        #     while r>=0 and c>=0: 
        #         if board[r][c]=='Q':
        #             return False
        #         r-=1
        #         c-=1
        #     r,c=row,col
        #     while  c>=0: 
        #         if board[r][c]=='Q':
        #             return False
        #         c-=1
        #     r,c=row,col
        #     while r<n and c>=0: 
        #         if board[r][c]=='Q':
        #             return False
        #         r+=1
        #         c-=1
        #     return True
        
        # def solve(col):
        #     if col==n:
        #         ans.append(["".join(r) for r in board])
        #         return 
        #     for row in range(n):
        #         if check(row,col):
        #             board[row][col]='Q'
        #             solve(col+1)
        #             board[row][col]='.'
        # solve(0)
        # return ans

        # O(N!) and O(N^2)

        # HASHING METHOD

        ans=[]
        board=[["." for _ in range(n)]for _ in range(n)]
        LR=[0]*n
        UD=[0]*(2*n-1)
        LD=[0]*(2*n-1)

        def solve(col,board,ans,LR,UD,LD):
            if col==n:
                ans.append(["".join(row) for row in board ])
                return 
            for row in range(n):
                if LR[row]==0 and UD[row+col]==0 and LD[n-1+col-row]==0:
                    board[row][col]='Q'
                    LR[row]=1
                    UD[row+col]=1
                    LD[n-1+col-row]=1

                    solve(col+1,board,ans,LR,UD,LD)

                    board[row][col]='.'
                    LR[row]=0
                    UD[row+col]=0
                    LD[n-1+col-row]=0

        solve(0,board,ans,LR,UD,LD)
        return ans
        

        


            

                
            
            
        