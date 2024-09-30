

"""
Merge two BST 's -> Problem Statement( https://www.geeksforgeeks.org/problems/merge-two-bst-s/1 )

Given two BSTs, return elements of merged BSTs in sorted form.

Examples :

Input:
BST1:
       5
     /   \
    3     6
   / \
  2   4  
BST2:
        2
      /   \
     1     3
            \
             7
            /
           6
Output: 1 2 2 3 3 4 5 6 6 7
Explanation: After merging and sorting the two BST we get 1 2 2 3 3 4 5 6 6 7.

Input:
BST1:
       12
     /   
    9
   / \    
  6   11
BST2:
      8
    /  \
   5    10
  /
 2
Output: 2 5 6 8 9 10 11 12
Explanation: After merging and sorting the two BST we get 2 5 6 8 9 10 11 12.

Expected Time Complexity: O((m+n)*log(m+n))
Expected Auxiliary Space: O(Height of BST1 + Height of BST2 + m + n)

Constraints:
1 ≤ Number of Nodes, value of nodes ≤ 105
"""


class Solution:
    def inorder(self, root, ans):
        # code here
        # If the current node is None, return
        if root is None:
            return 
        # Recursively traverse the left subtree
        self.inorder(root.left, ans)
        # Add the current node's data to the answer list
        ans.append(root.data)
        # Recursively traverse the right subtree
        self.inorder(root.right, ans)

    def merge(self, root1, root2):
        # Initialize an empty list to hold the inorder traversal results
        ans = []
        # Perform inorder traversal on the first tree and store the results in ans
        self.inorder(root1, ans)
        # Perform inorder traversal on the second tree and store the results in ans
        self.inorder(root2, ans)
        # Sort the combined results from both trees
        ans.sort()
        # Return the sorted list
        return ans