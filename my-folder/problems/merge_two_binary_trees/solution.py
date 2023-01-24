# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         def new_node(node1=Null, node2=Null):
#             value = TreeNode()
#             if node1 and node2:
#                 value.val = node1.val + node2.val
#             elif node1:
#                 value = node1
#             elif node2:
#                 value = node2
#             return value
            
#         if not root1 and not root2:
#             return
        
#         nodes = [root1, root2]
#         root = TreeNode()
#         i = 0
#         while True:
#             root1, root2 = nodes[i]
#             root.val = new_node(root1,root2)
#             root.left  = new_node(root1.left, root2.left)
#             root.right = new_node(root1.right, root2.right)

#             i+=1
            
#         return root
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def next_node(node1:None, node2:None):
            if not node1 and not node2:
                return
            if node1 and not node2:
                return node1
            elif node2 and not node1:
                return node2
            
            node = TreeNode()
            node.left = next_node(node1.left, node2.left)
            node.right = next_node(node1.right, node2.right)
            node.val = node1.val + node2.val

            return node
        
        full_tree = next_node(root1, root2)
        return full_tree
