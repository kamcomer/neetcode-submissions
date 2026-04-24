# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        
        def dfs(root):
            if root is None:
                return None
            
            nonlocal max_path

            lb = dfs(root.left)
            rb = dfs(root.right)

            combo =float('-inf')
            end = float('-inf')
            if lb and rb:
                end = lb + root.val + rb

            if lb:
                combo = lb + root.val

            if rb:
                combo = max(combo, rb+root.val)

            max_path = max(combo, end, root.val, max_path)
            return max(combo, root.val)

        dfs(root)
        return max_path
