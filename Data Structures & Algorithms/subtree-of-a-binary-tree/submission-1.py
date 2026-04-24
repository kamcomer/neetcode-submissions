# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def rec(root: TreeNode):
            if not root:
                return None

            l = rec(root.left)
            r = rec(root.right)

            if not l:
                l = "n"
            
            if not r:
                r = "n"
            
            return str(root.val) + l + r

        tree = rec(root)
        sub_tree = rec(subRoot)

        print(tree)
        print(sub_tree)

        return True if sub_tree in tree else False
