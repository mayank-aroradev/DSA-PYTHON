class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        rightmin=[0]*n
        rightmin[-1]=nums[-1]


        if n==0:
            return -1
        for i in range(n-2,-1,-1):
            rightmin[i]=min(nums[i],rightmin[i+1])
        left_max=float("-inf")
        for i in range (n):
            left_max=max(left_max,nums[i])
            if left_max - rightmin[i]<=k:
                return i
        return -1    

        # tc-o(n)
        # sc-O(n)

        