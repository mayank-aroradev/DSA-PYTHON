class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lit=[]
        result_string = "".join(map(str, digits))
        dum=int(result_string)+1
        num=[int(char) for char in str(dum)]
        return num
