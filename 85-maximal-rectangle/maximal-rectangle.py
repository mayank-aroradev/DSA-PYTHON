class Solution:
    def maxhisto(self,arr):
        st=[]
        maxarea=0
        index=0
        while index<len(arr):
            if not st or arr[index]>=arr[st[-1]]:
                st.append(index)
                index+=1
            else:
                top_st=st.pop()
                area=arr[top_st]*((index-st[-1]-1)  if st else index)
                maxarea=max(maxarea,area)
        while st:
            top_st=st.pop()
            area=arr[top_st]*((index-st[-1]-1)  if st else index)
            maxarea=max(maxarea,area)
        return maxarea

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n=len(matrix)
        m=len(matrix[0])
        max_area=0
        p_sum=[[0]*m for _ in range (n)]
        for j in range(m):
            running_sum=0
            for i in range(n):
                if matrix[i][j] == "1":
                    running_sum += 1
                else:
                    running_sum = 0
                p_sum[i][j] = running_sum
        
        for i in range (n):
            area=self.maxhisto(p_sum[i])
            max_area=max(max_area,area)
        return max_area


    # O(N*m)+O(n*2M)
    # O(n*m)+O(n)

   

        
                



        