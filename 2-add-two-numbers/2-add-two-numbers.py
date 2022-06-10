# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = pos = ListNode()
        carry = 0
        
        while l1 != None or l2 != None:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            
            summ = l1_value + l2_value + carry
            
            carry = int(summ / 10)
            pos.next = ListNode(summ%10)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            pos = pos.next
            
            if l1 == None and l2 == None and carry == 1:
                pos.next = ListNode(1)
            
        return head.next
            