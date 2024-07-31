

'''
Longest Common Prefix of Strings -> Problem Statement ( https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1 )

Given an array of strings arr. Return the longest common prefix among all strings present in the array. If there's no prefix common in all the strings, return "-1".


Examples :
Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
Output: gee
Explanation: "gee" is the longest common prefix in all the given strings.

Input: arr[] = ["hello", "world"]
Output: -1
Explanation: There's no common prefix in the given strings.

Expected Time Complexity: O(n*min(|arri|))
Expected Space Complexity: O(min(|arri|))

Constraints:
1 ≤ |arr| ≤ 103
1 ≤ |arr[i]| ≤ 103
'''


class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        # Check if the array is empty
        if not arr:
            return "-1"
    
        # Sort the array
        arr.sort()
        
        # Compare the first and the last string in the sorted array
        first = arr[0]
        last = arr[-1]
        i = 0
        
        # Find the common prefix between the first and last string
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        # If there is no common prefix
        if i == 0:
            return "-1"
        
        # Return the longest common prefix
        return first[:i]

