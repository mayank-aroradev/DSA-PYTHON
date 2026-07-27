class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        firstmax=float('-inf')
        secondmax=float('-inf')
        
        for i in range (len(nums)):
            if nums[i] >firstmax:
                secondmax=firstmax
                firstmax=nums[i]
            elif nums[i]>secondmax:
                secondmax=nums[i]

        return (firstmax-1)*(secondmax-1)
        