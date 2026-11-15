class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            left=0
            odd_count=0
            total_subarray=0

            for right in range(len(nums)):
                if nums[right]%2==1:
                    odd_count+=1
                
                while odd_count>k:
                    if nums[left]%2==1:
                        odd_count-=1
                    left+=1
                total_subarray+=(right-left+1)
            return total_subarray
        return atmost(k)-atmost(k-1)
        