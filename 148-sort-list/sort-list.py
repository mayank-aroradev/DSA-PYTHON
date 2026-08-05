# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        curr= head
        val=[]
        while curr :
            val.append(curr.val)
            curr=curr.next

        val.sort()

        curr=head
        for va in val:
            curr.val=va
            curr=curr.next

        return head
            
            
        