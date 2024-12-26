

'''
Two Sum - Pair with Given Sum -> Problem Statement( https://www.geeksforgeeks.org/problems/key-pair5616/1 )

Given an array arr[] of positive integers and another integer target. 
Determine if there exists two distinct indices such that the sum of there elements is equals to target.

Examples:

Input: arr[] = [1, 4, 45, 6, 10, 8], target = 16
Output: true
Explanation: arr[3] + arr[4] = 6 + 10 = 16.

Input: arr[] = [1, 2, 4, 3, 6], target = 11
Output: false
Explanation: None of the pair makes a sum of 11.

Constraints:
1 ≤ arr.size ≤ 105
1 ≤ arr[i] ≤ 105
1 ≤ target ≤ 2*105
'''


#User function Template for python3
class Solution:
	def twoSum(self, nums, target):
		# code here
		required_two_integers = {}
        #
        for i in range(len(nums)):
            if target - nums[i] in required_two_integers:
                return [required_two_integers[target - nums[i]],i]
            else:
                required_two_integers[nums[i]] = i