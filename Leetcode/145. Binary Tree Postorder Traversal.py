


'''
145. Binary Tree Postorder Traversal -> Problem Statement (https://leetcode.com/problems/binary-tree-postorder-traversal/description/)

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Postorder Traversal is a DFS Depth First Search Traversal 
        # left  ->  right  ->  root 
        res = []
        def dfs(root):
            #
            if root == None:
                return
            #
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
            #
            return res
        #
        return dfs(root)