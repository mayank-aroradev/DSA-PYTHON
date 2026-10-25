class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # cnt=0
        # n=len(s)
        # d=len(t)
        # if n!=d:
        #     return False
        # for i in range(n):
        #     if s[i] in t:
        #         cnt+=1
        #     else:
        #         return False
        # if cnt==n:
        #     return True
        

        n=len(s)
        d=len(t)
        if n!=d:
            return False
        sorteds=sorted(s)
        sortedt=sorted(t)
        if sorteds!=sortedt:
            return False
        else:
            return True