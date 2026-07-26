class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        firstmax=float('-inf')
        secondmax=float('-inf')
        thirdmax=float('-inf')

        # Initialize two minimums
        firstmin = float('inf')
        secondmin = float('inf')

        for i in nums:
            if i>firstmax:
                thirdmax=secondmax
                secondmax=firstmax
                firstmax=i
            elif i>secondmax:
                thirdmax=secondmax
                secondmax=i
            elif thirdmax<i:

                thirdmax=i

            if i < firstmin:
                secondmin = firstmin
                firstmin = i
            elif i < secondmin:
                secondmin = i

        return max(firstmax*secondmax*thirdmax, firstmin*secondmin*firstmax
        
        )
            
                