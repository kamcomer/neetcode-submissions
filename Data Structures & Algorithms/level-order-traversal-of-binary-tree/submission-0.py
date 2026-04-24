# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])

        res = []
        nodes = []
        while q:
            nodes.append(q.popleft())
            if not q:
                res.append([x.val for x in nodes])
                for node in nodes:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                nodes = []
        return res
            



            