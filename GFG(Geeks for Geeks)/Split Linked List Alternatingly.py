

"""
Split Linked List Alternatingly -> Problem Statement( https://www.geeksforgeeks.org/problems/split-singly-linked-list-alternatingly/1 )

Given a singly linked list's head. Your task is to complete the function alternatingSplitList()
that splits the given linked list into two smaller lists. The sublists should be made from ]
alternating elements from the original list.

Note: 
The sublist should be in the order with respect to the original list.
Your have to return an array containing the both sub-linked lists.

Examples:

Input: LinkedList = 0->1->0->1->0->1
Output: 0->0->0 , 1->1->1
Explanation: After forming two sublists of the given list as required, we have two lists as: 0->0->0 and 1->1->1.

Input: LinkedList = 2->5->8->9->6
Output: 2->8->6 , 5->9
Explanation: After forming two sublists of the given list as required, we have two lists as: 2->8->6 and 5->9.

Input: LinkedList: 7 
Output: 7 , <empty linked list>

Constraints:
1 <= number of nodes <= 100
1 <= node -> data <= 104
"""



class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        if not head:
            return [None, None]  # If the original list is empty, return two empty lists.
        # Dummy nodes to represent the start of the two sublists
        list1_head = Node(0)
        list2_head = Node(0)
        
        list1 = list1_head
        list2 = list2_head
        
        current = head
        is_list1_turn = True  # To alternate between list1 and list2
    
        # Traverse the original list
        while current:
            if is_list1_turn:
                list1.next = current  # Attach current node to list1
                list1 = list1.next  # Move the list1 pointer forward
            else:
                list2.next = current  # Attach current node to list2
                list2 = list2.next  # Move the list2 pointer forward
            
            # Toggle between list1 and list2
            is_list1_turn = not is_list1_turn
            
            # Move to the next node in the original list
            current = current.next
        
        # Terminate both lists properly
        list1.next = None
        list2.next = None
        
        # Return the heads of the two new lists (ignoring the dummy nodes)
        return [list1_head.next, list2_head.next]

