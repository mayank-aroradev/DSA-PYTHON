class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        for i in nums:
            map[i]=map.get(i,0)+1
        maxele=max(map,key=map.get)
        return maxele
