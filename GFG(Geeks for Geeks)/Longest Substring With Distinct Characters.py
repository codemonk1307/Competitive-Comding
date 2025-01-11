


'''
Longest substring with distinct characters -> 
Problem Statement ( https://www.geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1 )


Given a string s, find the length of the longest substring with all distinct characters. 


Examples:

Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.

Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.

Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.


Constraints:
1<= s.size()<=3*104
All the characters are in lowercase.
'''



class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        char_set = set()
        max_length = 0
        start = 0
        #
        for end in range(len(s)):
            # Remove characters from the set until there are no duplicates
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            # Add the current character to the set
            char_set.add(s[end])
            # Update the maximum length
            max_length = max(max_length, end - start + 1)
        #
        return max_length