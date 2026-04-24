# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque()
        q.append(root)
        ser_tree = [str(root.val)]
        ser_tree.append(",")
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                ser_tree.append(str(node.left.val))
            else:
                ser_tree.append("n")
            ser_tree.append(",")

            if node.right:
                q.append(node.right)
                ser_tree.append(str(node.right.val))
            else:
                ser_tree.append("n")
            ser_tree.append(",")
        
        ser_tree = "".join(ser_tree)
        print(ser_tree)
        return ser_tree


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not len(data):
            return None
        data = data.split(',')
        q = deque()
        root = TreeNode(data.pop(0))
        q.append(root)
        while q:
            node = q.popleft()

            if len(data):
                val = data.pop(0)
                if val != 'n':
                    node.left = TreeNode(val)
                    q.append(node.left)

            if len(data):
                val = data.pop(0)
                if val != 'n':
                    node.right = TreeNode(val)
                    q.append(node.right)

        return root
            

