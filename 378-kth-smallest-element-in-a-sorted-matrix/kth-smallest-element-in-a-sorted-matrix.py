class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat=[element for row in matrix for element in row]
        flat.sort()
        return flat[k-1]
        