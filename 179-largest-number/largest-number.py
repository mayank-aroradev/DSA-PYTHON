class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
    
            str_nums = list(map(str, nums))
            
            
            str_nums.sort(key=lambda x: x * 9, reverse=True)
            
        
            return str(int("".join(str_nums)))
