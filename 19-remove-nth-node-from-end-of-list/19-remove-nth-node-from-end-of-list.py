# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        head = ListNode(next=head)
        pos = ans = head
        
        while pos:
            if n < 0:
                ans = ans.next
            pos = pos.next
            n-=1
        ans.next = ans.next.next
        return head.next