class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        st=[]
        max_area=0
        n=len(heights)
        for i in range (n):
            while st and heights[st[-1]]>heights[i]:
                element_arr=st.pop()
                nse=i
                pse=st[-1 ] if st else -1
                current_area=heights[element_arr]*(nse-pse-1)
                max_area=max(current_area,max_area)
            st.append(i)
        while st:
            element_arr=st.pop()
            nse=n
            pse=st[-1] if st else -1
            current_area=heights[element_arr]*(nse-pse-1)
            max_area=max(current_area,max_area)
        return max_area