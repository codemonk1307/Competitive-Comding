

"""
Parenthesis Checker -> Problem Statement ( https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1 )

Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".

Examples :

Input: {([])}
Output: true
Explanation: { ( [ ] ) }. Same colored brackets can form balanced pairs, with 0 number of unbalanced bracket.

Input: ()
Output: true
Explanation: (). Same bracket can form balanced pairs,and here only 1 type of bracket is present and in balanced way.

Input: ([]
Output: false
Explanation: ([]. Here square bracket is balanced but the small bracket is not balanced and Hence , the output will be unbalanced.

Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)

Constraints:
1 ≤ |x| ≤ 105
"""

class Solution:
    #Function to check if brackets are balanced or not.
    def ispar(self, exp):
        # Stack to store opening brackets
        stack = []
        # Dictionary to match corresponding brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
    
        # Traverse through the expression
        for char in exp:
            # If the character is an opening bracket, push it to the stack
            if char in bracket_map.values():
                stack.append(char)
            # If it's a closing bracket, check for matching opening bracket
            elif char in bracket_map:
                # Stack should not be empty and top of stack should match
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False  # Mismatch found
            else:
                continue  # Ignore other characters
    
        # If stack is empty, all brackets were matched
        return len(stack) == 0