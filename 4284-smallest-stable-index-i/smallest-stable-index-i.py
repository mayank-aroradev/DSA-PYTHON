class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            e1 = max(nums[0:i+1])
            e2 = min(nums[i:n])

            t = e1 - e2

            if t <= k:
                return i

        return -1
        