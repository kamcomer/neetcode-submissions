# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexes = {v: i for i, v in enumerate(inorder)}

        preIndex = inIndex = 0
        def dfs(limit):
            nonlocal preIndex, inIndex
            if preIndex >= len(preorder):
                return None
            if inorder[inIndex] == limit:
                inIndex += 1
                return None
            
            root = TreeNode(preorder[preIndex])
            preIndex += 1

            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root

        return dfs(float('inf'))
