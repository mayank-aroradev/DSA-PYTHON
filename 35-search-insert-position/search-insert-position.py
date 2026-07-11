class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lb=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        if lb==-1:
            lb=n
        return lb


        