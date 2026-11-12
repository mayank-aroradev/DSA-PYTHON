class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxnum=max(nums)
        cnt=0
        for i in range(len(nums)):
            if nums[i]!=maxnum:
                sum1=maxnum-nums[i]
                cnt+=sum1
        return cnt
        