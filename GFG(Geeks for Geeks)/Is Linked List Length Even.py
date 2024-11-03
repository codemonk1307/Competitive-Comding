

"""
Is Linked List Length Even? -> Problem Statement(  )

Given a linked list, your task is to complete the function isLengthEven() which 
contains the head of the linked list, and check whether the length of the linked 
list is even or not. Return true if it is even, otherwise false.

Examples:

Input: Linked list: 12->52->10->47->95->0
Output: true
Explanation: The length of the linked list is 6 which is even, hence returned true.

Input: Linked list: 9->4->3
Output: false
Explanation: The length of the linked list is 3 which is odd, hence returned false.

Expected Time Complexity: O(n)
Expected Auxillary Space: O(1)

Constraints:
1 <= number of nodes <= 105
1 <= elements of the linked list <= 105
"""


class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        fast, slow = head, head
     
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return fast == None