# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        record = []

        def dfs(root):
            if root is None:
                record.append("!")
                return

            record.append(str(root.val))

            dfs(root.left)
            dfs(root.right)

            return

        dfs(root)

        output = "?".join(record)

        #print(output)

        return output
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        data = data.split('?')
        self.preorder_i = 0

        def dfs():
            if data[self.preorder_i] == '!':
                self.preorder_i += 1
                return None

            node = TreeNode(int(data[self.preorder_i]))

            self.preorder_i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

        self.preorder_i = 0

        def dfs():
            if data[self.preorder_i] == '!':
                self.preorder_i += 2
                return None

            length = 0
            while data[self.preorder_i + length] != '?':
                length += 1

            node = TreeNode(int(data[self.preorder_i : self.preorder_i + length]))

            self.preorder_i += length + 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()