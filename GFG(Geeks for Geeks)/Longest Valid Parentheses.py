

"""
Longest valid Parentheses -> Problem Statement( https://www.geeksforgeeks.org/problems/longest-valid-parentheses5657/1 )

Given a string str consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.

A parenthesis string is valid if:
For every opening parenthesis, there is a closing parenthesis.
Opening parenthesis must be closed in the correct order.

Examples :

Input: str = ((()
Output: 2
Explaination: The longest valid parenthesis substring is "()".

Input: str = )()())
Output: 4
Explaination: The longest valid parenthesis substring is "()()".

Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(|str|)

Constraints:
1 ≤ |str| ≤ 105  
"""


class Solution:
    def maxLength(self, s):
        #Initialize the stack with base index
        stack = [-1]  
        max_len = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else: # char == ')'
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len