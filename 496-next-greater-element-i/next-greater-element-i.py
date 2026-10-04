class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nge={}
        stack=[]
        for num in reversed(nums2):
            while stack and stack[-1]<=num:
                stack.pop()
            if stack:
                nge[num]=stack[-1]
            else:
                nge[num]=-1
            stack.append(num)
        ans=[nge[num] for num in nums1]
        return ans