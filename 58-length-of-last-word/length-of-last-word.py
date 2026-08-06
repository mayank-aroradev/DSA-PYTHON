class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        re=s.split()
        return len(re[-1])
        