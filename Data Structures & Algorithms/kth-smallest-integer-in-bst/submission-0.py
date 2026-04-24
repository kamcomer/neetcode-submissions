# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree = []
        def serialize(root):
            if not root:
                return None

            serialize(root.left)
            tree.append(root.val)
            serialize(root.right)
            return
        
        serialize(root)
        return tree[k-1]


        
