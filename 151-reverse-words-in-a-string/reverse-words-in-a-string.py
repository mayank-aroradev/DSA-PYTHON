class Solution:
    def reverseWords(self, s: str) -> str:
        word_list=s.split()
        reversed_list = word_list[::-1]
        rs=" ".join(reversed_list)
        return rs
        