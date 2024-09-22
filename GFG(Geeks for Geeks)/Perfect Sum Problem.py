


"""
Perfect Sum Problem -> Problem Statement( https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1 )

Given an array arr of size n of non-negative integers and an integer sum, 
the task is to count all subsets of the given array with a sum equal to a given sum.
Note: Answer can be very large, so, output answer modulo 109+7.

Examples:

Input: 
n = 6, arr = [5, 2, 3, 10, 6, 8], sum = 10
Output: 
3
Explanation: 
{5, 2, 3}, {2, 8}, {10} are possible subsets.

Input: 
n = 5, arr = [2, 5, 1, 4, 3], sum = 10
Output: 
3
Explanation: 
{2, 1, 4, 3}, {5, 1, 4}, {2, 5, 3} are possible subsets.

Expected Time Complexity: O(n*sum)
Expected Auxiliary Space: O(n*sum)

Constraints:
1 ≤ n*sum ≤ 106
0 ≤ arr[i] ≤ 106
"""


class Solution:
    def perfectSum(self, arr, n, sum):
        t = [[0]*(sum+1) for _ in range(n+1)]
        mod = 10 ** 9 + 7
        for i in range(n+1):
            for j in range(sum+1):
                if i == 0:
                    t[i][j] = 0
                if j == 0:
                    t[i][j] = 1
        for i in range(1, n+1):
            for j in range(sum+1):
                if arr[i-1] <= j:
                    t[i][j] = (t[i-1][j-arr[i-1]] + t[i-1][j]) % mod
                else:
                    t[i][j] = (t[i-1][j]) % mod
        return t[n][sum] % mod