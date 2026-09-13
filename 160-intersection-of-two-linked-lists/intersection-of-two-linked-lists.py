# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # pointer trick tc-> O(n*m)
                        # sc->O(1)
        # if headA is None or headB is None:
        #     return None
        # pA=headA
        # pB=headB
        # while pA != pB:
        #     pA=headB if pA is None else pA.next
        #     pB=headA if pB is None else pB.next

        # return pA
        
        # hashtable

        visited_set=set()
        current=headA
        while current:
            visited_set.add(current)
            current=current.next
        current=headB
        while current:
            if current in visited_set:
                return current
            current=current.next
        return None
            

        