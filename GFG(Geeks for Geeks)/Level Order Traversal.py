

"""
Level order traversal -> Problem Statement( geeksforgeeks.org/problems/level-order-traversal/1 )


Given a root of a binary tree with n nodes, the task is to find its level order traversal. 
Level order traversal of a tree is breadth-first traversal for the tree.

Examples:

Input: root[] = [1, 2, 3]
Output: [[1], [2, 3]]

Input: root[] = [10, 20, 30, 40, 50]
Output: [[10], [20, 30], [40, 50]]

Input: root[] = [1, 3, 2, N, N, N, 4, 6, 5]
Output: [[1], [3, 2], [4], [6, 5]]


Constraints
1 ≤ number of nodes ≤ 105
0 ≤ node->data ≤ 109
"""




"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        #edgecase when root is - []
        if root is None: return []
        
        binaryTreeLevelOrderBFSTraversal = [[root.data]]
        listOfNodes = [root]
        
        while len(listOfNodes) > 0:
            
            currentNode = []
            
            for node in listOfNodes:
                if node.left:
                    currentNode.append(node.left)
                if node.right:
                    currentNode.append(node.right)
                    
            listOfNodes = currentNode
            
            if currentNode != []:
                binaryTreeLevelOrderBFSTraversal.append([node.data for node in currentNode])
                
        return binaryTreeLevelOrderBFSTraversal
        