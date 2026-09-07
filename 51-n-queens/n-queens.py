class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=[["." for _ in range(n)]for _ in range(n) ]
        
        def check(row,col):
            r,c=row,col
            while r>=0 and c>=0: 
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            r,c=row,col
            while  c>=0: 
                if board[r][c]=='Q':
                    return False
                c-=1
            r,c=row,col
            while r<n and c>=0: 
                if board[r][c]=='Q':
                    return False
                r+=1
                c-=1
            return True
        
        def solve(col):
            if col==n:
                ans.append(["".join(r) for r in board])
                return 
            for row in range(n):
                if check(row,col):
                    board[row][col]='Q'
                    solve(col+1)
                    board[row][col]='.'
        solve(0)
        return ans


            

                
            
            
        