class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==divisor :
            return 1
        sign = True
        if dividend>=0 and divisor<0:
            sign=False
        if dividend<0 and divisor>0:
            sign=False
        n=abs(dividend)
        d=abs(divisor)
        ans=0
        while n>=d:
            cnt=0
            while n>=(d<<(cnt+1)):
                cnt+=1
            ans+=(1<<cnt)
            n=n-(d<<cnt)
        
        if sign==False:
            ans=-ans
        

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX
        
        
            
        return ans

       


        

        