class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        l1=[]
        for digits in nums:
            dict1[digits]=dict1.get(digits,0)+1
        sortedd=dict(sorted(dict1.items(),key=lambda items:items[1],reverse=True))
        keylist=list(sortedd.keys())
        for i in range(k):
            l1.append(keylist[i])
        return l1
            

        