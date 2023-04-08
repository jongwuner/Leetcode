"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:    
            return node
        deq = deque([node])
        nodes = {node.val: Node(node.val)}
        
        while len(deq) > 0:
            nowNode = deq.popleft()
            clonedNode = nodes[nowNode.val]
            
            for neigh in nowNode.neighbors:
                if neigh.val not in nodes:
                    nodes[neigh.val] = Node(neigh.val)
                    deq.append(neigh)
                
                clonedNode.neighbors.append(nodes[neigh.val])
            
        return nodes[node.val]