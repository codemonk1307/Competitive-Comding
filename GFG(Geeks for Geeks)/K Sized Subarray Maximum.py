

"""
K Sized Subarray Maximum -> Problem Statement( https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1 )

Given an array arr[] and an integer k. Find the maximum for each and every contiguous subarray of size k.

Examples:

Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6]
Output: [3, 3, 4, 5, 5, 5, 6] 
Explanation: 
1st contiguous subarray = [1 2 3] max = 3
2nd contiguous subarray = [2 3 1] max = 3
3rd contiguous subarray = [3 1 4] max = 4
4th contiguous subarray = [1 4 5] max = 5
5th contiguous subarray = [4 5 2] max = 5
6th contiguous subarray = [5 2 3] max = 5
7th contiguous subarray = [2 3 6] max = 6

Input: k = 4, arr[] = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
Output: [10, 10, 10, 15, 15, 90, 90]
Explanation: 
1st contiguous subarray = [8 5 10 7], max = 10
2nd contiguous subarray = [5 10 7 9], max = 10
3rd contiguous subarray = [10 7 9 4], max = 10
4th contiguous subarray = [7 9 4 15], max = 15
5th contiguous subarray = [9 4 15 12], max = 15
6th contiguous subarray = [4 15 12 90], max = 90
7th contiguous subarray = {15 12 90 13}, max = 90

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(k)

Constraints:
1 ≤ sizeof(arr) ≤ 106
1 ≤ k ≤ sizeof(arr)
0 ≤ arr[i] ≤ 109
"""


class Solution:
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,lists):
        n = len(lists)
        # Initialize a deque to store indexes of array elements
        deq = deque()
        result = []
        # Process the first k elements (the first window)
        for i in range(k):
            # Remove elements smaller than the current element from the back of the deque
            while deq and arr[i] >= arr[deq[-1]]:
                deq.pop()
            # Add the current element's index at the back of the deque
            deq.append(i)
        # Process the rest of the elements
        for i in range(k, n):
            # The element at the front of the deque is the largest for the previous window
            result.append(arr[deq[0]])
            # Remove elements which are out of this window from the front
            while deq and deq[0] <= i - k:
                deq.popleft()
            # Remove elements smaller than the current element from the back of the deque
            while deq and arr[i] >= arr[deq[-1]]:
                deq.pop()
            # Add the current element's index at the back of the deque
            deq.append(i)
        # Add the maximum of the last window
        result.append(arr[deq[0]])
        #
        return result