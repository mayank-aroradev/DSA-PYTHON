class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sumi=sum(weights)
        maxi=max(weights)
        low=maxi
        high=sumi
        while low<=high:
            mid=(low+high)//2
            noofdays=self.daysb(weights,mid)
            if noofdays<=days:
                high=mid-1
            else:
                low=mid+1
        return low
    
    def daysb(self,weights,capacity):
        n=len(weights)
        daysl=1
        load=0
        for i in range(n):
            if (load+weights[i]>capacity):
                daysl+=1
                load=weights[i]
            else:
                load+=weights[i]
        return daysl
        