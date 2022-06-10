# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = deque()
        
        def req(head):
            if head == None:
                return
            
            q.append(head.val)
            req(head.next)
            head.val = q.popleft()
        
        req(head)
        
        return head