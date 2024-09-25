

"""
Palindrome Linked List -> Problem Statement( https://www.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1 )

Given a singly linked list of integers. The task is to check if the given linked list is palindrome or not.

Examples:

Input: LinkedList: 1->2->1->1->2->1
Output: true
Explanation: The given linked list is 1->2->1->1->2->1 , which is a palindrome and Hence, the output is true.

Input: LinkedList: 1->2->3->4
Output: false
Explanation: The given linked list is 1->2->3->4, which is not a palindrome and Hence, the output is false.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1) 

Note: You should not use the recursive stack space as well

Constraints:
1 <= number of nodes <= 105
1 ≤ node->data ≤ 103
"""


#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Step 3: Compare the first half and the reversed second half
        first_half, second_half = head, prev
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        # Step 4: Optional, restore the list by reversing the second half back
        # (Not implemented here but can be done similarly to Step 2)
        
        return True