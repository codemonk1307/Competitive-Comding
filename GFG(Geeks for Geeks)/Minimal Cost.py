

"""
Minimal Cost - Problem Statement (https://www.geeksforgeeks.org/problems/minimal-cost/1)

There is an array arr of heights of stone and Geek is standing at the first stone and can jump to
one of the following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that 
can be jumped and cost will be |hi-hj| is incurred, where j is the stone to land on. Find the
minimum possible total cost incurred before the Geek reaches the last stone.

Example:

Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum

Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be |10 - 20| + |20 - 10| = 20.

Expected Time Complexity: O(n*k)
Expected Auxilary Space: O(n)

Constraint:
1<= arr.size() <=104
1 <= k <= 100
1 <= arr[i] <= 104
"""


class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        # Initialize dp array with infinity
        dp = [float('inf')] * n
        dp[0] = 0  # No cost to stay on the first stone
        
        # Iterate through each stone
        for i in range(n):
            # Try to jump from stone i to any stone i+1 to i+k
            for j in range(i+1, min(i+k+1, n)):
                dp[j] = min(dp[j], dp[i] + abs(arr[i] - arr[j]))
        
        # The result will be the cost to reach the last stone
        return dp[n-1]
