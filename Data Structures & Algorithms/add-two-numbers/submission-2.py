# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry = 0

        if not cur1:
            return cur2
        if not cur2:
            return cur1
        
        carry = (cur1.val + cur2.val)//10
        head = ListNode((cur1.val + cur2.val)%10)
        cur = head
        cur1 = cur1.next
        cur2 = cur2.next

        while cur1 or cur2:
            if not cur2:
                while cur1:
                    new_node = ListNode((cur1.val+carry)%10)
                    carry = (cur1.val+carry)//10
                    cur.next = new_node
                    cur = cur.next
                    cur1 = cur1.next
                if carry:
                    cur.next = ListNode(1)
                return head
            
            if not cur1:
                while cur2:
                    new_node = ListNode((cur2.val+carry)%10)
                    carry = (cur2.val+carry)//10
                    cur.next = new_node
                    cur = cur.next
                    cur2 = cur2.next
                
                if carry:
                    cur.next = ListNode(1)
                return head

            sum_val = cur1.val + cur2.val
            new_node = ListNode((sum_val+carry)%10)
            carry = sum_val//10
            cur.next = new_node
            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next
        
        if carry:
            cur.next = ListNode(1)
        
        return head
            
            




        