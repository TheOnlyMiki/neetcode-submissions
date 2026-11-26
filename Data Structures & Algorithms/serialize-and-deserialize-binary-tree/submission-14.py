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
            return "N"
        res = []
        level = [root]
        while level:
            next_level = []

            for node in level:
                if not node:
                    res.append("N")
                else:
                    res.append(str(node.val))
                    next_level.append(node.left)
                    next_level.append(node.right)

            level = next_level

        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        level = [root]
        index = 1
        while level:
            next_level = []

            for node in level:
                if vals[index] != "N":
                    node.left = TreeNode(int(vals[index]))
                    next_level.append(node.left)
                index += 1
                if vals[index] != "N":
                    node.right = TreeNode(int(vals[index]))
                    next_level.append(node.right)
                index += 1

            level = next_level

        return root
