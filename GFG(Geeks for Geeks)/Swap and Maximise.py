


'''
Swap and Maximize -> Problem Statement ( https://www.geeksforgeeks.org/problems/swap-and-maximize5859/1 )

Given an array arr[ ] of positive elements. Consider the array as a circular array 
meaning the element after the last element is the first element of the array.

The task is to find the maximum sum of the absolute differences between consecutive 
elements with shuffling of array elements allowed i.e. shuffle the array elements and 
make [a1..an] such order that  |a1 – a2| + |a2 – a3| + …… + |an-1 – an| + |an – a1| is maximized.


Examples:
Input: arr[] = [4, 2, 1, 8]
Output: 18
Explanation: After Shuffling, we get [1, 8, 2, 4]. Sum of absolute difference between 
consecutive elements after rearrangement = |1 - 8| + |8 - 2| + |2 - 4| + |4 - 1| = 7 + 6 + 2 + 3 = 18

Input: arr[] = [10, 12]
Output: 4
Explanation: No need of rearrangement. Sum of absolute difference between consecutive 
elements = |10 - 12| + |12 - 10| = 2 + 2 = 4

Constraints:
2 ≤ arr.size()≤ 105
1 <= arr[i] <= 105
'''


class Solution:
    def maxSum(self,arr):
        n = len(arr)
        sum = 0
        arr.sort()
        #
        for i in range(n//2):
            sum -= (2 * arr[i])
            sum += (2 * arr[n - i - 1])
        #    
        return sum
