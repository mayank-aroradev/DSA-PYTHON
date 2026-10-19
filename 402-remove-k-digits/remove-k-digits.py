class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for char in num :
            while st and k>0 and st[-1]>char:
                st.pop()
                k-=1
            st.append(char)
        if k>0:
            st=st[:-k]
        res="".join(st).lstrip("0")

        return res if res else "0"
        