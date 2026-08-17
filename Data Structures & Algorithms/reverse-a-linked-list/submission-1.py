# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev, cur = None, head
        while cur:
            temp = cur.next
            #temp = 0.next (1)
            cur.next = prev
            #None = 0
            prev = cur
            #None.next = cur (0)
            cur = temp
        return prev

            

            