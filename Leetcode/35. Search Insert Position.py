

"""
35. Search Insert Position -> Problem Statement( https://leetcode.com/problems/search-insert-position/ )

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: 
        # brute force approach
        low = 0
        high = len(nums)-1
        index = 0
        #Binary Search Implementation
        while low <= high:
            mid = low + ((high - low)//2)
            #
            if nums[mid] == target: 
                return mid
            #
            elif nums[mid] < target: 
                low = index = mid + 1 
            else:
                high, index = mid - 1, mid
        #
        return index