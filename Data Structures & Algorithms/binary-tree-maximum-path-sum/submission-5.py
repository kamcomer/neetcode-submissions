# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = root.val
        
        def dfs(root):
            nonlocal max_path
            if root is None:
                return 0
            
            lmax = dfs(root.left)
            rmax = dfs(root.right)
            lmax = max(lmax, 0)
            rmax = max(rmax, 0)

            max_path = max(max_path, lmax + root.val + rmax)
            return root.val + max(lmax, rmax)

        dfs(root)
        return max_path
