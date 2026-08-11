class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # for i in range(n):
        #     for j in range(0,n-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        # return nums

        def merge_sort(nums):
            if len(nums)<=1:
                return nums
            else:
                mid=len(nums)//2
                left_half=nums[:mid]
                right_half=nums[mid:]
                left_sr=merge_sort(left_half)
                right_sr=merge_sort(right_half)
                return mergeme(left_sr,right_sr)

        def mergeme(left_sr,right_sr):
            i=0
            j=0
            n=len(left_sr)
            m=len(right_sr)
            result=[]
            while i<n and j<m:
                if left_sr[i]<right_sr[j]:
                    result.append(left_sr[i])
                    i+=1
                else:
                    result.append(right_sr[j])
                    j+=1

            result.extend(left_sr[i:])
            result.extend(right_sr[j:])

            return result

        return merge_sort(nums)

                
                