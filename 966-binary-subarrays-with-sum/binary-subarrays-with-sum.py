class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMost(target):
            if target < 0:
                return 0
            l = 0
            r = 0
            currentsum = 0
            cnt = 0
            while r < len(nums):
                currentsum += nums[r]
                while currentsum > target:
                    currentsum -= nums[l]
                    l += 1
                cnt += r - l + 1
                r += 1
            return cnt

        return atMost(goal) - atMost(goal - 1)