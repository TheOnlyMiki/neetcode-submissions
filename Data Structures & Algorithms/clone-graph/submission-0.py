"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        record = {node.val:Node(val=node.val)}
        visit = set()

        def dfs(node, next_node):
            if not next_node:
                return

            visit.add(node.val)

            current = record[node.val]

            for neighbor in next_node:
                if neighbor.val not in record:
                    record[neighbor.val] = Node(val=neighbor.val)
                
                current.neighbors.append(record[neighbor.val])

                if neighbor.val not in visit:
                    dfs(neighbor, neighbor.neighbors)

        dfs(node, node.neighbors)
            
        return record[node.val]