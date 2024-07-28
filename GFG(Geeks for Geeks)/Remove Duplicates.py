

'''
Remove Duplicates -> Problem Statement (https://www.geeksforgeeks.org/problems/remove-duplicates3034/1)

Difficulty: EasyAccuracy: 52.35%Submissions: 126K+Points: 2
Given a string str without spaces, the task is to remove all duplicate characters from it, keeping only the first occurrence.

Note: The original order of characters must be kept the same. 

Examples :
Input: str = "zvvo"
Output: "zvo"
Explanation: Only keep the first occurrence

Input: str = "gfg"
Output: "gf"
Explanation: Only keep the first occurrence

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= |str| <= 105
str contains lowercase English alphabets
'''

class Solution:
	def removeDups(self, str):
		isPresent=[False]*26
        ans=""
        for val in str:
            i=ord(val)-ord("a")
            if not isPresent[i]:
                ans+=val
                isPresent[i]=True
        return ans

