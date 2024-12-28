

'''
689. Maximum Sum of 3 Non-Overlapping Subarrays
Problem Statement( https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/ )

Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.
Return the result as a list of indices representing the starting position of each interval (0-indexed). 
If there are multiple answers, return the lexicographically smallest one.

Example 1:
Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Example 2:
Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 
Constraints:
1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)
'''

from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Calculate the sum of all subarrays of size k
        window_sum = sum(nums[:k])
        sums = [0] * (n - k + 1)
        sums[0] = window_sum
        
        for i in range(1, n - k + 1):
            window_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = window_sum

        # Step 2: Find the best subarray indices from the left
        left = [0] * len(sums)
        best = 0
        for i in range(len(sums)):
            if sums[i] > sums[best]:
                best = i
            left[i] = best

        # Step 3: Find the best subarray indices from the right
        right = [0] * len(sums)
        best = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best

        # Step 4: Find the best combination of three subarrays
        max_sum = 0
        result = [-1, -1, -1]
        for mid in range(k, n - 2 * k + 1):
            l = left[mid - k]
            r = right[mid + k]
            total = sums[l] + sums[mid] + sums[r]
            if total > max_sum:
                max_sum = total
                result = [l, mid, r]

        return result