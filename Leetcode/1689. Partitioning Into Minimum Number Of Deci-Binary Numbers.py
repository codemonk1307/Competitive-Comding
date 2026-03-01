

'''
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
Problem Statement : https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/

A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. 
For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, 
return the minimum number of positive deci-binary numbers needed so that they sum up to n.


Example 1:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:
Input: n = "82734"
Output: 8

Example 3:
Input: n = "27346209830709182346"
Output: 9

Constraints:

1 <= n.length <= 105
n consists of only digits.
n does not contain any leading zeros and represents a positive integer.
'''


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(map(int, n))
    


'''
Approach: 
Each deci-binary number contains only digits 0 or 1.
To build the number n, think digit-by-digit:
If a digit in n is 7, that means at least 7 deci-binary numbers must contribute a 1 in that position.
Since each deci-binary number can contribute at most one 1 per digit position, the minimum count required is simply:
The maximum digit in n
'''


'''
Complexity
Time: O(len(n))
Space: O(1)
'''