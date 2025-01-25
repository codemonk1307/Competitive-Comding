

"""
Find the first node of loop in linked list

Problem Statement(hhttps://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1)


Given a head of the singly linked list. If a loop is present in the list then return the first node of the loop 
else return NULL.

Custom Input format:
A head of a singly linked list and a pos (1-based index) which denotes the position of the node to which the last node points to. If pos = 0, it means the last node points to null, indicating there is no loop.


Examples:

Input: 
Output: 3
Explanation: We can see that there exists a loop in the given linked list and the first node of the loop is 3.

Input: 
Output: -1
Explanation: No loop exists in the above linked list.So the output is -1.


Constraints:
1 <= no. of nodes <= 106
1 <= node->data <= 106 
"""


#User function Template for python3
""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:
    def findFirstNode(self, head):
        # Initialize slow and fast pointers to the head
        slow, fast = head, head

        # Detect if a cycle exists in the linked list
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # If cycle is detected break out of the loop
            if slow == fast:
                # Find the start of the cycle using the Floyd's Cycle Detection Algorithm
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # The first node in the loop
        
        return None  # No cycle found