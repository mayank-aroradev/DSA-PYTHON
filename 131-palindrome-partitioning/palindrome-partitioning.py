class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        path=[]
        n=len(s)

        def function(ind,s,path,ans):
            if ind==n:
                ans.append(path[:])
                return 

            for i in range(ind,n):
                if ispalindrom(s,ind,i):
                    path.append(s[ind:i+1])
                    function(i+1,s,path,ans)
                    path.pop()
        
        def ispalindrom(s,start,end):
            while start<end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True

        function(0,s,path,ans)
        return ans

                