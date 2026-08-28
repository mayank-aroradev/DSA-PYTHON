class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # brute solution
        # nums=list(range(1,n+1))
        # used=[False]*n
        # result=[]
        # path=[]
        # count=[0]

        # def dfs(path):
        #     if count[0]>=k:
        #         return 
        #     if len(path)==n:
        #         count[0]+=1
        #         if count[0]==k:
        #             result.append("".join(map(str,path)))
        #         return 

        #     for i in range(n):
        #         if used[i]:
        #             continue
        #         used[i]=True
        #         path.append(nums[i])
        #         dfs(path)
        #         path.pop()
        #         used[i]=False

        #         if count[0]>=k:
        #             return 
        # dfs([])
        # return result[0]

        fact=1
        numbers=[]
        for i in range(1,n):
            fact*=i
            numbers.append(i)
        numbers.append(n)
        ans=''
        k-=1
        while True:
            index=k//fact
            ans+=str(numbers[index])
            numbers.pop(index)
            if not numbers:
                break

            k%=fact
            fact//=len(numbers)

        return ans
