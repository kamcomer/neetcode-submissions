# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        vals = []
        def rec(root: TreeNode):
            if not root:
                vals.append("#n")
                return
            
            vals.append(f'#{root.val}')
            rec(root.left)
            rec(root.right)
            return

        rec(root)
        tree = "".join(vals)

        vals = []
        rec(subRoot)
        sub_tree = "".join(vals)

        return True if sub_tree in tree else False
