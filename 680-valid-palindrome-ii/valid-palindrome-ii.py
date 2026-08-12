class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(left,right):
            while left<right:
                if cleaned[left]!=cleaned[right]:
                    return False
                left+=1
                right-=1
            
            return True
        
        cleaned= "".join(c.lower() for c in s if c.isalnum())
        left=0
        right=len(cleaned)-1
        
        while left<right:
            if cleaned[left]!=cleaned[right]:
                return ispalindrome(left+1,right) or ispalindrome(left,right-1)

            left+=1
            right-=1
        return True


        
        