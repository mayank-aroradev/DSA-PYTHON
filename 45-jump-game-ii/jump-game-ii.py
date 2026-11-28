class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        l=0
        r=0
        jumps=0

        while r<n-1:
            farthest=0
            for ind in range(l,r+1):
                farthest=max(nums[ind]+ind,farthest)
            l=r+1
            r=farthest
            jumps+=1
        return jumps