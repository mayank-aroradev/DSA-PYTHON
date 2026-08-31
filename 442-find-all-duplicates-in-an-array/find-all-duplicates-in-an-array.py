class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        lt=[]
        seen=set()
        for num in nums:
            if num in seen:
                lt.append(num)
            else:
                seen.add(num)
        return lt        