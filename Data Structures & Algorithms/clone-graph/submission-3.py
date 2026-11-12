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
        
        maps = {
            node : Node(val=node.val)
        }

        level = [node]

        while level:
            next_level = []

            for current in level:
                for next_node in current.neighbors:
                    if next_node not in maps:
                        maps[next_node] = Node(val=next_node.val)
                        next_level.append(next_node)

                    maps[current].neighbors.append(maps[next_node])

            level = next_level

        return maps[node]

        if not node:
            return None
        
        maps = {
            node : Node(val=node.val)
        }

        def dfs(node):
            for next_node in node.neighbors:
                if next_node not in maps:
                    maps[next_node] = Node(val=next_node.val)
                    
                    dfs(next_node)

                maps[node].neighbors.append(maps[next_node])

        dfs(node)

        return maps[node]

