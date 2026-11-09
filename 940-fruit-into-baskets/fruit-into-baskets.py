class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l=0
        r=0
        maxlen=0
        k=2
        map1={}
        n=len(fruits)
        while r<n:
            map1[fruits[r]] = map1.get(fruits[r], 0) + 1
            if len(map1)>k:
                map1[fruits[l]]-=1
                if map1[fruits[l]]==0:
                    del map1[fruits[l]]
                l+=1
            if len(map1)<=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
