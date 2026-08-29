# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy = ListNode(next=head)
        # current = dummy
        
        # # 2. Traverse the list checking the next node's value
        # while current.next:
        #     if current.next.val == val:
        #         # Bypass the matching node
        #         current.next = current.next.next
        #     else:
        #         # Only move forward if we didn't delete a node
        #         current = current.next
                
        
        # return dummy.next
        

        if not head :
            return None

        head.next=self.removeElements(head.next,val)

        if head.val==val:
            return head.next

        return head

        