class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        def permutations(index,nums,ans):
            if index==len(nums):
                ds=[]
                for i in range(len(nums)):
                    ds.append(nums[i])
                if ds not in ans:
                    ans.append(ds)
                return 
            for i in range (index,len(nums)):
                swap(i,index,nums)
                permutations(index+1,nums,ans)
                swap(i,index,nums)
        
        def swap(i,j,nums):
            nums[i],nums[j]=nums[j],nums[i]
        
        permutations(0,nums,ans)
        return ans