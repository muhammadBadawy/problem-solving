"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        q = deque()
        
        q.append(root)
        
        while q:
            tmp = deque()
            for i in range(len(q)):
                node = q.popleft()
                
                if q:
                    node.next = q[0]
                else:
                    node.next = None
                
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            q = tmp
        
        return root