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

        output = []

        level = [root]

        while level:
            next_level = []

            for node in level:
                if not node:
                    output.append("N")
                else:
                    output.append(str(node.val))
                    next_level.append(node.left)
                    next_level.append(node.right)

            level = next_level

        return ",".join(output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")

        if data[0] == "N":
            return None

        root = TreeNode(int(data[0]))

        level = [root]

        i = 1

        while level:
            next_level = []

            for node in level:
                if data[i] != "N":
                    node.left = TreeNode(int(data[i]))
                    next_level.append(node.left)

                i += 1

                if data[i] != "N":
                    node.right = TreeNode(int(data[i]))
                    next_level.append(node.right)

                i += 1

            level = next_level

        return root
