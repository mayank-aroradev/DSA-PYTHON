class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash_map={}
        # for i in nums:
        #     hash_map[i]=hash_map.get(i,0)+1
            
        # for key in hash_map:
        #     if hash_map[key]==1:
        #         return key
        

        nums.sort()
        n=len(nums)
        for i in range(1,n,3):
            if nums[i]!=nums[i-1]:
                return nums[i-1]
        return nums[n-1]