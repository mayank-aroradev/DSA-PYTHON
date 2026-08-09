class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash_map={}
        
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
            list=[]
            for key in hash_map:
                if hash_map[key]==1:
                    list.append(key)
        return list

        