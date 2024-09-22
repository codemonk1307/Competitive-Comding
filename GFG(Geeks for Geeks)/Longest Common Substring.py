

"""
Longest Common Substring -> Problem Statement( https://www.geeksforgeeks.org/problems/longest-common-substring1452/1 )

You are given two strings str1 and str2. Your task is to find the length of the 
longest common substring among the given strings.

Examples:

Input: str1 = "ABCDGH", str2 = "ACDGHR"
Output: 4
Explanation: The longest common substring is "CDGH" which has length 4.

Input: str1 = "ABC", str2 = "ACB"
Output: 1
Explanation: The longest common substrings are "A", "B", "C" all having length 1.

Expected Time Complexity: O(n*m).
Expected Auxiliary Space: O(n*m).

Constraints:
1<= str1.size(), str2.size()<=1000
Both strings may contain upper and lower case alphabets.
"""


class Solution:
    def longestCommonSubstr(self, str1, str2):
        m, n = 0, 0
        # 2d array column pahle likhna hamesha(m) 
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        #
        res = 0
        # maximum length common substring ki store karte chalo res me
        for i in range(1, n+1):             # row
            for j in range(1, m+1):         # column
                #
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
                # jaise hi mismatch hua dono str me common substr ka count 0 kar do
                # coz discontinuous nahi ho sakti substring
                else:
                    dp[i][j] = 0
        #      
        return res