class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[-1]*n
        stack=[]
        for i in range (2*n-1,-1,-1):
            actual_index=i%n
            while stack and nums[stack[-1]]<=nums[actual_index]:
                stack.pop()
            if i < n and stack :
                ans[actual_index]=nums[stack[-1]]

            stack.append(actual_index)
        return ans                    