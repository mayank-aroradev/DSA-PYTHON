class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result=[]
        n=len(nums)
        nums.sort()
        def backtrack(start,currentsubset):
            result.append(list(currentsubset))
            for i in range (start,n):
                if i>start and nums[i]==nums[i-1]:
                    continue
                currentsubset.append(nums[i])
                backtrack(i+1,currentsubset)
                currentsubset.pop()
        backtrack(0,[])
        return result

# 𝑂(n*2^n)
# O(n)