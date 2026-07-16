class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        
        
        high=max(nums)
        low=1
        ans=high
        cnt=0
        while low<=high:
            mid=(low+high)//2
            cnt=0
            for i in range(n):
                cnt+=(nums[i]+mid-1)//mid
            if cnt<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
                
        