class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        i=k-1
        nums.sort(reverse=True)
        return nums[i]
        