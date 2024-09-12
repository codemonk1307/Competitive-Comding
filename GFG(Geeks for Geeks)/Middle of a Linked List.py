
"""
Middle of a Linked List -> Problem Statement( https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1 )

Given the head of a linked list, the task is to find the middle. For example, the middle of 1-> 2->3->4->5 is 3. If there are two middle nodes (even count), return the second middle. For example, middle of 1->2->3->4->5->6 is 4.

Examples:

Input: Linked list: 1->2->3->4->5
Output: 3
Explanation: The given linked list is 1->2->3->4->5 and its middle is 3.

Input: Linked list: 2->4->6->7->5->1
Output: 7 
Explanation: The given linked list is 2->4->6->7->5->1 and its middle is 7.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= no. of nodes <= 105
"""

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getMiddle(self, head):
        # return the value stored in the middle node
        # If the linked list is empty, return -1
        if head is None:
            return -1
        # Initialize slow and fast pointers
        slow = head
        fast = head
        # Traverse the list with two pointers
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
        # When fast reaches the end, slow is at the middle
        return slow.data