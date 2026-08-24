class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        candidates.sort()
        n=len(candidates)


        def func(ind,candidates,target,ans,ds,n):
            if target==0:
                ans.append(ds[:])

                return 
            for i in range (ind,n):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                ds.append(candidates[i])
                func(i+1,candidates,target-candidates[i],ans,ds,n)
                ds.pop()

        func(0,candidates,target,ans,ds,n)
        return ans
            
