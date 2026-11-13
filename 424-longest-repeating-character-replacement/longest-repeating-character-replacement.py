class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0

        maxlen=0
        maxf=0
        hash_arr=[0]*26
        while r<len(s):
            hash_arr[ord(s[r])-ord('A')]+=1
            maxf=max(maxf,hash_arr[ord(s[r])-ord('A')])
            if (r-l+1)-maxf>k:
                hash_arr[ord(s[l])-ord('A')]-=1
                l=l+1
            if (r-l+1)-maxf<=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
       
    #    O(N)
    #    O(1)