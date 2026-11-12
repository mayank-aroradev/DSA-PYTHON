class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 0
        maxlen=0
        nums.sort()
        for i in range(0,len(nums)-1):
            diff=abs(nums[i]-nums[i+1])
            maxlen=max(maxlen,diff)
        return maxlen