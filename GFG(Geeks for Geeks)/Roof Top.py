

"""
Roof Top -> Problem Statement( https://www.geeksforgeeks.org/problems/roof-top-1587115621/1 ) 

You are given the heights of consecutive buildings. You can move from the roof of a building 
to the roof of the next adjacent building. You need to find the maximum number of consecutive 
steps you can put forward such that you gain an increase in altitude with each step.

Examples:

Input: arr[] = [1, 2, 2, 3, 2]
Output: 1
Explanation: 1, 2, or 2, 3 are the only consecutive buildings with increasing heights thus 
maximum number of consecutive steps with an increase in gain in altitude would be 1 in both cases.

Input: arr[] = [1, 2, 3, 4]
Output: 3
Explanation: 1 to 2 to 3 to 4 is the jump of length 3 to have a maximum number of buildings 
with increasing heights, so maximum steps with increasing altitude becomes 3.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 105
"""


class Solution:
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, heights):
        #Your code here
        max_steps = 0
        current_steps = 0
        #
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                current_steps += 1
                max_steps = max(max_steps, current_steps)
            else:
                current_steps = 0  # Reset if the next building is not taller
        #
        return max_steps