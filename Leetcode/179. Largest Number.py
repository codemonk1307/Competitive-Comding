

"""
179. Largest Number -> Problem Statement( https://leetcode.com/problems/largest-number/ )

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109
"""


from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert all integers to strings
        nums_str = list(map(str, nums))
        # Custom comparator: Compare concatenation of two numbers in both possible orders
        def compare(a, b):
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0   # a and b are equal in terms of order
        # Sort using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        # Join the sorted numbers into a single string
        largest_num = ''.join(nums_str)
        # Handle the edge case where the result is like '00...'
        return '0' if largest_num[0] == '0' else largest_num