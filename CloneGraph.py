"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        clonedNodeDict = {}
        
        def clone(node):
            if node in clonedNodeDict:
                return clonedNodeDict[node]
            
            cloned = Node(node.val)
            clonedNodeDict[node] = cloned   
            for n in node.neighbors:
                cloned.neighbors.append(clone(n))
            return cloned
        return clone(node) if node else None
        