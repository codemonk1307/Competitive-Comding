


"""
Equilibrium Point -> Problem Statement( https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1 )


Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements
 before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2 
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 0 + 3 = 3.

Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.

Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1.

Constraints:
3 <= arr.size() <= 106
-109 <= arr[i] <= 109
"""


class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        right_sum = sum(arr)  # Total sum of the array
        left_sum = 0          # Initial left sum is 0
        
        for i, num in enumerate(arr):
            # Calculate right sum by subtracting current element from total sum
            right_sum -= num
            
            # Check if left sum equals right sum
            if left_sum == right_sum:
                return i
            
            # Update left sum for the next iteration
            left_sum += num
        
        return -1  # No equilibrium index found
        