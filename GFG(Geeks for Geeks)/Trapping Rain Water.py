


'''
Trapping Rain Water -> Problem Statement( https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1 )


Given an array arr[] with non-negative integers representing the height of blocks. 
If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 


Examples:

Input: arr[] = [3, 0, 1, 0, 4, 0 2]
Output: 10
Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides.

Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
Output: 9
Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.


Constraints:
1 < arr.size() < 105
0 < arr[i] < 103
'''


class Solution:
    def maxWater(self, height):
        # code here
        n = len(height)
        # No water can be trapped if there are fewer than 2 bars
        if n <= 1:
            return 0  

        # Precompute left and right maximum heights
        left_max = [0] * n
        right_max = [0] * n

        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Fill right_max array
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # Calculate total water trapped
        amount = 0
        for i in range(n):
            # Water trapped at current index
            amount += max(0, min(left_max[i], right_max[i]) - height[i])

        return amount
    



"""
class Solution:
    def maxWater(self, height):
        # code here
        n = len(height)
        if n == 1 or n == 0:
            return 0

        else:
            amount = 0
            
            lmax = height[0]
            rmax = max(height[1:])

            for i in range(n):
                if height[i] >lmax:
                    lmax = height[i]
                if height[i] == rmax and i < n-1:
                    rmax = max(height[i+1:])

                h = min(lmax, rmax)
                amount += max(h - height[i], 0)

            return amount



The current implementation has a time complexity of 𝑂(𝑛2) due to recalculating the right 
maximum height for each index using slicing (max(height[i+1:])). This can be optimized by 
precomputing the left and right maximum heights for each position, 
which reduces the time complexity to 𝑂(𝑛)

Here's the optimized approach:

Optimized Solution
We use two auxiliary arrays:

left_max – stores the maximum height encountered from the left up to the current index.
right_max – stores the maximum height encountered from the right up to the current index.

This allows us to calculate the trapped water for each index in constant time.
This method is optimised for the time complexity of O(n)

Explanation of Optimizations
Precomputing Left and Right Maximum Heights:

left_max[i] contains the maximum height from the start of the array to index i.
right_max[i] contains the maximum height from index i to the end of the array.

This allows us to determine the height of water at any index without recalculating the max values repeatedly.

Single Pass to Calculate Water:
Using the precomputed arrays, we compute the trapped water in one pass, as the water level 
at any index is the minimum of left_max[i] and right_max[i] minus the height at that index.


Complexity Analysis
Time Complexity:

Filling left_max and right_max arrays: O(n).
Calculating water trapped: O(n).
Total: O(n).
Space Complexity:

Additional space for left_max and right_max: O(n).
Total: O(n).
"""