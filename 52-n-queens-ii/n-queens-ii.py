class Solution:
    def totalNQueens(self, n: int) -> int:
        cnt=[0]
        board=[["." for _ in range(n)]for _ in range(n)]
        LR=[0]*n
        UD=[0]*(2*n-1)
        LD=[0]*(2*n-1)

        def solve(col,board,cnt,LR,UD,LD):
            if col==n:
                cnt[0]+=1
                return 
            for row in range(n):
                if LR[row]==0 and UD[row+col]==0 and LD[n-1+col-row]==0:
                    board[row][col]='Q'
                    LR[row]=1
                    UD[row+col]=1
                    LD[n-1+col-row]=1

                    solve(col+1,board,cnt,LR,UD,LD)

                    board[row][col]='.'
                    LR[row]=0
                    UD[row+col]=0
                    LD[n-1+col-row]=0

        solve(0,board,cnt,LR,UD,LD)
        ans=cnt[0]
        return ans
        
        