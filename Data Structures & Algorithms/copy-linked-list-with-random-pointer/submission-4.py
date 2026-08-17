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
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = cur.next.next
        
        new_head = head.next
        
        cur = head
        while cur:
            random_node = cur.random
            if random_node:
                cur.next.random = random_node.next
            cur = cur.next.next
        
        cur = new_head
        old_cur = head
        while cur and cur.next:
            old_cur.next = old_cur.next.next
            cur.next = cur.next.next
            cur = cur.next
            old_cur = old_cur.next
        
        if old_cur:
            old_cur.next = None
        
        return new_head



