class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=high
        while low<=high:
            mid=(low+high)//2
            if (self.possible(bloomDay,mid,m,k)==True):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def possible(self,arr,day,m,k):
        n=len(arr)
        cnt=0
        bou=0
        for i in range(0,n):
            if arr[i]<=day:
                cnt+=1
            else:
                bou+=(cnt//k)
                cnt=0
        bou+=(cnt//k)
        if bou>=m:
            return True
        else:
            return False


