

"""
Multiply two linked lists

Given elements as nodes of the two singly linked lists. The task is to multiply these two linked lists, say L1 and L2.
Note: The output could be large take modulo 109+7.

Examples :

Input: LinkedList L1 : 3->2 , LinkedList L2 : 2
Output: 64
Explanation: 
Multiplication of 32 and 2 gives 64.

Input: LinkedList L1: 1->0->0 , LinkedList L2 : 1->0
Output: 1000
Explanation: 
Multiplication of 100 and 10 gives 1000.

Expected Time Complexity: O(max(n,m))
Expected Auxilliary Space: O(1)
where n is the size of L1 and m is the size of L2

Constraints:
1 <= number of nodes <= 9
0 <= node->data <= 9
"""


# Node definition for a singly linked list
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def multiply_two_lists(self, first: ListNode, second: ListNode) -> int:
        # Define modulo as 10^9 + 7
        MOD = 10**9 + 7
        # Step 1: Convert the first linked list to a number
        num1 = 0
        while first:
            num1 = (num1 * 10 + first.data) % MOD
            first = first.next
        # Step 2: Convert the second linked list to a number
        num2 = 0
        while second:
            num2 = (num2 * 10 + second.data) % MOD
            second = second.next
        # Step 3: Multiply the two numbers and take modulo MOD
        result = (num1 * num2) % MOD
        # Step 4: Return the result
        return result

# Helper function to create a linked list from a list of digits
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head