

"""
Mirror Tree -> Prooblem Statement ( https://www.geeksforgeeks.org/problems/mirror-tree/1 )
Given a Binary Tree, convert it into its mirror.            

Examples:

Input:
      1
    /  \
   2    3
Output: 3 1 2
Explanation: The tree is
   1    (mirror)  1
 /  \    =>      /  \
2    3          3    2
The inorder of mirror is 3 1 2

Input:
      10
     /  \
    20   30
   /  \
  40  60
Output: 30 10 60 20 40
Explanation: The tree is
      10               10
    /    \  (mirror) /    \
   20    30    =>   30    20
  /  \                   /   \
 40  60                 60   40
The inroder traversal of mirror is
30 10 60 20 40.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105
"""


'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        if not root:
            return None
        left = self.mirror(root.left)
        right = self.mirror(root.right)
        root.left, root.right = right, left
        return root