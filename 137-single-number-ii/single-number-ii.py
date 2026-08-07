class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map={}
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
            
        for key in hash_map:
            if hash_map[key]==1:
                return key
        