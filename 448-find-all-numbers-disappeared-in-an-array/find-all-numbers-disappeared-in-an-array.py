class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        st=set(nums)
        n=len(nums)
        lt=[]
        for i in range(1,n+1):
            if i not in st:
                lt.append(i)
        return lt
        