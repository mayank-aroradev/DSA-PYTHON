class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        deen=set()
        for num in nums:
            if num in deen:
                return True
            else:
                deen.add(num)
        return False
                

            
            
        