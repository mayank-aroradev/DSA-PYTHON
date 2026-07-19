class Solution:
    
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        n=len(nums)
        if k>n:
            return -1

        while low<=high:
            mid=(low+high)//2
            cnt1=self.func(nums,mid)
            if cnt1>k:
                low=mid+1
            else:
                high=mid-1
        return low

    
    def func(self,nums,amount):
        n=len(nums)
        cnt2=0
        cnt=1
        for i in range(n):
            if cnt2+nums[i]<=amount:
                cnt2+=nums[i]
            else:

                cnt2=nums[i]
                cnt+=1
        return cnt

    
            