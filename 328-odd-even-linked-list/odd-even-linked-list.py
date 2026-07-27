# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[]
        temp=head
        if not head or not head.next:
            return head
            
        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next.next if temp.next else None
            
        temp = head.next
        while temp:
            values.append(temp.val)
            temp = temp.next.next if temp.next else None



        temp=head
        index=0
        while temp is not None:
            temp.val=values[index]
            index+=1
            temp=temp.next
        return head
        