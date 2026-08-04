# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        while list1 is not None and list2 is not None:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0
            currmin=0
            if val1<val2:
                
                curr.next=list1
                list1=list1.next
                
            else:
                
                curr.next=list2
                list2=list2.next
            curr=curr.next
        
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2

            
        
        return dummy.next
