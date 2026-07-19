class Solution:
    def lowerbound(self,arr,n,x):
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        cnt_max = -1
        index = 0
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            sorted_row = sorted(mat[i])  
            cnt_ones = n - self.lowerbound(sorted_row, n, 1)
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i

        return [index, cnt_max]
        