class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        n=len(nums)
        total_sum=0
        for i in range(n):
            largest=nums[i]
            smallest=nums[i]
            for j in range (i+1,n):
                largest=max(largest,nums[j])
                smallest=min(smallest,nums[j])
                total_sum=total_sum+(largest-smallest)

        return total_sum
        