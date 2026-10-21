class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans=[]
        q=deque()
        for i,time in enumerate(nums):
            if q and q[0]<i-k+1:
                q.popleft()
            while q and nums[q[-1]]<time:
                q.pop()
            q.append(i)
            if i>=k-1:
                ans.append(nums[q[0]])
        return ans


        # O(n)
        # O(K)