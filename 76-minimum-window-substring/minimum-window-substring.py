class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)>len(s):
            return ""
        n=len(s)
        m=len(t)
        hash_map=[0]*256
        l=0
        r=0
        min_len=10**9
        s_index=-1
        cnt=0
        for i in range(m):
            hash_map[ord(t[i])]+=1
        while r<n:
            if hash_map[ord(s[r])]>0:
                cnt+=1
            hash_map[ord(s[r])]-=1
            while cnt==m:
                if (r-l+1)<min_len:
                    min_len=r-l+1
                    s_index=l
                hash_map[ord(s[l])]+=1
                if hash_map[ord(s[l])]>0:
                    cnt-=1
                l+=1
            r+=1
        return "" if s_index==-1 else s[s_index:s_index+min_len]
                

