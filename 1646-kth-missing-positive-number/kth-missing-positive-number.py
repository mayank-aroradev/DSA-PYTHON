class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        for i in range(n):
            if k>=arr[i]:
                k+=1
            else:
                break

        return k
        

        