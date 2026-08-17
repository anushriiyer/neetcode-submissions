"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        cur = head
        old_to_new = {}
        new_head = Node(cur.val)
        old_to_new[cur] = new_head
        new_prev = new_head
        cur = cur.next
        

        while cur:
            new = Node(cur.val)
            old_to_new[cur] = new
            new_prev.next = new
            new_prev = new_prev.next
            cur = cur.next
        

        cur = head
        new_cur = new_head
        while cur:
            new_cur.random = old_to_new.get(cur.random)
            new_cur = new_cur.next
            cur = cur.next
        
        return new_head


