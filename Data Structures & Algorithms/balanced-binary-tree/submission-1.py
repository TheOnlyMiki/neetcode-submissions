# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        stack = [root] if root else []
        record = {None: 0}

        while stack:
            node = stack[-1]

            if node.left and node.left not in record:
                stack.append(node.left)
            elif node.right and node.right not in record:
                stack.append(node.right)
            else:
                node = stack.pop()

                left_height = record[node.left]
                right_height = record[node.right]

                if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                    return False

                record[node] = 1 + max(left_height, right_height)

        return True
