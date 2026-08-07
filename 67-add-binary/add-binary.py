class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result=""
        num=(int(a,2)+int(b,2))
        if num == 0:
            return "0"
        while num>0:
            if num%2==1:
                result+="1"
            else:
                result+="0"
            num=num//2
        
        return result[::-1]
                