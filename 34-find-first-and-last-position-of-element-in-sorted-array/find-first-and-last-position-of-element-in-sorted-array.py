class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def lowerbound(nums,target):
            low=0
            high=n-1
            lb=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]>=target:
                    lb=mid
                    high=mid-1
                else:
                    low=mid+1
            return lb

        def highbound(nums,target):
            low=0
            high=n-1
            hb=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]<=target:
                    hb=mid
                    low=mid+1
                else:
                    high=mid-1
            return hb

        lb=lowerbound(nums,target)
        if lb==-1 or nums[lb]!=target:
            return [-1,-1]
        hb=highbound(nums,target)
        return [lb,hb]


    

        

        # first=-1
        # last=-1
        # for i in range(0,n):
        #     if nums[i]==target:
        #         if first==-1:
        #             first=i
        #         last=i
        # return [first,last]


        