class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setme=set()
        list1=[]
        for num in nums1:
            setme.add(num)
        for numb in nums2:
            if numb in setme and numb not in list1:
                list1.append(numb)
        return list1

