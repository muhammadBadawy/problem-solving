# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def DFS(l_node, r_node):
            if not l_node:
                return r_node
            if not r_node:
                return l_node
            
            l_node.val = l_node.val + r_node.val
            
            l_node.left = DFS(l_node.left, r_node.left)
            l_node.right = DFS(l_node.right, r_node.right)
            
            return l_node
        
        return DFS(root1, root2)