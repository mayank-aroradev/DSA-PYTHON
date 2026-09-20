class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
    #     ans=[]
    #     def permutations(index,nums,ans):
    #         if index==len(nums):
    #             ds=[]
    #             for i in range(len(nums)):
    #                 ds.append(nums[i])
    #             if ds not in ans:
    #                 ans.append(ds)
    #             return 
    #         for i in range (index,len(nums)):
    #             swap(i,index,nums)
    #             permutations(index+1,nums,ans)
    #             swap(i,index,nums)
        
    #     def swap(i,j,nums):
    #         nums[i],nums[j]=nums[j],nums[i]
        
    #     permutations(0,nums,ans)
    #     return ans

    # tc-O(n!*n^2)
    # sc-O(n!*n)

        ans=[]
        ds=[]
        freq=[False]*len(nums)
        nums.sort()
        
        
        def recruteperm(nums,ds,ans,freq):
            if len(ds)==len(nums):
                ans.append(ds[:])
                return 

            for i in range(len(nums)):
                if  freq[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not freq[i-1]:
                    continue
                freq[i]=True
                ds.append(nums[i])
                recruteperm(nums,ds,ans,freq)
                ds.pop()
                freq[i]=False
        
        recruteperm(nums,ds,ans,freq)
        return ans