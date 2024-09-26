

"""
20. Valid Parentheses -> Problem Statement ( https://leetcode.com/problems/valid-parentheses/ )

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

 

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""


class Solution:
    def isValid(self, s: str) -> bool:
        #
        stack = []
        dictionary = {"]":"[", "}":"{", ")":"("}
        #
        for c in s:
            if c in dictionary.values():
                stack.append(c)
            elif c in dictionary.keys():
                if stack == [] or dictionary[c] != stack.pop():
                    return False
            else:
                return False
        #
        return stack == []