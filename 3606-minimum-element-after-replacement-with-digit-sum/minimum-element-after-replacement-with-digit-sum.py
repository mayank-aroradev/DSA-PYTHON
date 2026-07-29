class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val=float("inf")
        for num in nums:
            digit_sum=0
            while num>0:
                digit_sum+=num%10
                num=num//10
            if digit_sum<min_val:
                min_val=digit_sum
        return min_val
        