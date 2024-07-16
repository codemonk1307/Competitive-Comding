

'''
Remaining String -> Problem Statement (https://www.geeksforgeeks.org/problems/remaining-string3515/1)

Given a string s without spaces, a character ch and an integer count. Your task is to return the substring that remains after the 
character ch has appeared count number of times.
Note:  Assume upper case and lower case alphabets are different. “”(Empty string) should be returned if it is not possible, 
or the remaining substring is empty.

Examples:

Input: s = "Thisisdemostring", ch = 'i', count = 3
Output: ng
Explanation: The remaining substring of s after the 3rd
occurrence of 'i' is "ng", hence the output is ng

Input: s = "Thisisdemostri", ch = 'i', count = 3
Output: ""
Explanation: The 3rd occurence of 'i' is at the last index. In this case the remaining substring is empty, hence we return empty string.

Input: s = "abcd", ch = 'x', count = 2
Output: ""
Explanation: The character x is not present in the string, hence we return empty string.

Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(1)

Constraints:
1<= s.length()<=105
1<=count<=s.length()
s[i] is both upper case and lower case
'''

#User function Template for python3
class Solution:
	def printString( self, s, ch, count ):
		k = 0
		m = ""
		for i in range( len(s) ):
			if s[i] == ch:
				k += 1
            if k == count:
                m = s[i + 1:]
				break
        else:
            m = ""
        return m

