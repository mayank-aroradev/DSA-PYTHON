class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        # n=len(nums)
        # total_sum=0
        # for i in range(n):
        #     largest=nums[i]
        #     smallest=nums[i]
        #     for j in range (i+1,n):
        #         largest=max(largest,nums[j])
        #         smallest=min(smallest,nums[j])
        #         total_sum=total_sum+(largest-smallest)

        # return total_sum

        # O(n^2)
        # O(1)

     
        return self.sumSubarrayMaxs(nums) - self.sumSubarrayMins(nums)

    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        psee = [-1] * n
        nse = [n] * n
        st = []

        # Find Previous Smaller or Equal Element
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            psee[i] = -1 if not st else st[-1]
            st.append(i)

        # Find Next Smaller Element
        st = []
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            nse[i] = n if not st else st[-1]
            st.append(i)

        # Calculate Min Contributions
        total_min = 0
        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            total_min += left * right * arr[i]
        return total_min

    def sumSubarrayMaxs(self, arr: list[int]) -> int:
        n = len(arr)
        pgee = [-1] * n
        nge = [n] * n
        st = []

        # Find Previous Greater or Equal Element
        for i in range(n):
            while st and arr[st[-1]] < arr[i]:  # Inverted logic: pop if strictly smaller
                st.pop()
            pgee[i] = -1 if not st else st[-1]
            st.append(i)

        # Find Next Greater Element
        st = []
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] <= arr[i]: # Inverted logic: pop if smaller or equal
                st.pop()
            nge[i] = n if not st else st[-1]
            st.append(i)

        # Calculate Max Contributions
        total_max = 0
        for i in range(n):
            left = i - pgee[i]
            right = nge[i] - i
            total_max += left * right * arr[i]
        return total_max



        

        # O(n)
        # O(n)