# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = l = ListNode(0, head)
        r = head
        
        while r and r.next:       
            if r.val == r.next.val:
                while r and r.next and r.val == r.next.val:
                    r = r.next
                r = r.next
                l.next = r
            else:
                l = l.next
                r = r.next
        
        return ans.next
            
      
 