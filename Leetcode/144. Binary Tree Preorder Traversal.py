

'''
144. Binary Tree Preorder Traversal -> Problem Statement (https://leetcode.com/problems/binary-tree-preorder-traversal/description/)

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#--- APPROACH - 1 ------- Recursive Approach ---------APPROACH - 1 ------- Recursive Approach-------------- STARTS
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive Approach
        res = []
        def dfs(root):
            #
            if root == None:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
            #
            return res
        #
        return dfs(root)
#--- APPROACH - 1 ------- Recursive Approach ---------APPROACH - 1 ------- Recursive Approach-------------- ENDS



#--- APPROACH - 2 ------- Iterative Approach ---------APPROACH - 2 ------- Iterative Approach-------------- STARTS

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative Preorder -> DFS Traversal ||  Root  ->   left    ->   right
        if not root:
            return []
        #
        res, stack = [], [root]
        while stack:
            currNode = stack.pop()
            if currNode:
                res.append(currNode.val)
                stack.append(currNode.right)
                stack.append(currNode.left)
        #        
        return res

#--- APPROACH - 2 ------- Iterative Approach ---------APPROACH - 2 ------- Iterative Approach-------------- ENDS