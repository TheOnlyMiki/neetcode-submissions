# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.output = ""

        def dfs(node):
            if not node:
                self.output += "?!"
                return 

            self.output += str(node.val) + '!'
            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)

        return self.output

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if not data:
            return ""

        data = data.split('!')

        self.i = 0

        def dfs():
            if self.i == len(data):
                return None

            val = data[self.i]
            self.i += 1

            if val == '?':
                return None

            node = TreeNode(val=int(val))

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
