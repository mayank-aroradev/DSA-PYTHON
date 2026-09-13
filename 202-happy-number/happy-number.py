class Solution:
    def isHappy(self, n: int) -> bool:
        # def check(n):
        #     if n==1:
        #         return True
        #     if n==4:
        #         return False
        #     sum_d=sum(int(digit)**2 for digit in str(n))

        #     return check(sum_d)
        
        # return check(n)
        # O(logn)
        # O(log(n))
        seen=set()

        while n!=1 and n not in seen:
            seen.add(n)
            n=sum(int(digit)**2 for digit in str(n))
            
        return n==1

        # O(log(n))
        # O(1) beacuse it will not hold more than 729

        

            
            