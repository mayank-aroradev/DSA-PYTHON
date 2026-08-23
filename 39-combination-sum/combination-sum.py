class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        ds=[]
        ans=[]

        def func(candidates,ind,n,ds,s,target):

            if s > target:
                return
                
            if ind==n:
                if s==target:
                    ans.append(list(ds))
                return 
            

            ds.append(candidates[ind])
            s+=candidates[ind]
            func(candidates,ind,n,ds,s,target)

            ds.pop()
            s-=candidates[ind]
            func(candidates,ind+1,n,ds,s,target)

        func(candidates,0,n,ds,0,target)
        return ans



                
        