class Solution:
    def trap(self, height: list[int]) -> int:
        # if not height:
        #     return 0
        # total_water=0
        # n=len(height)
        # for i in range(n):
        #     max_right=0
        #     max_left=0
        #     for j in range(i,-1,-1):
        #         max_left=max(max_left,height[j])
        #     for j in range(i,n):
        #         max_right=max(max_right,height[j])
        #     total_water+=min(max_left,max_right)-height[i]
        # return total_water

        # O(N^2)
        # O(1)

        if not height:
            return 0
        left,right=0,len(height)-1
        max_left,max_right=height[left],height[right]
        total_water=0
        while left<right:
            if max_left<max_right:
                left+=1
                max_left=max(max_left,height[left])
                total_water+=max_left-height[left]

            else:
                right-=1
                max_right=max(max_right,height[right])
                total_water+=max_right-height[right]

        return total_water
            

        