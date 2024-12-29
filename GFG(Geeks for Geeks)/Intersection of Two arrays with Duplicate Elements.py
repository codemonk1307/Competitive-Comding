


'''
Intersection of Two arrays with Duplicate Elements -> 
Problem Statement(https://www.geeksforgeeks.org/problems/intersection-of-two-arrays-with-duplicate-elements/1)

Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. 
Intersection of two arrays is said to be elements that are common in both arrays. 
The intersection should not have duplicate elements and the result should contain items in any order.

Note: The driver code will sort the resulting array in increasing order before printing.

Examples:

Input: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]
Output: [1, 3]
Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements.

Input: a[] = [1, 1, 1], b[] = [1, 1, 1, 1, 1]
Output: [1]
Explanation: 1 is the only common element present in both the arrays.

Input: a[] = [1, 2, 3], b[] = [4, 5, 6]
Output: []
Explanation: No common element in both the arrays.


Constraints:
1 ≤ a.size(), b.size() ≤ 105
1 ≤ a[i], b[i] ≤ 105
'''


class Solution:
    def intersectionWithDuplicates(self, a, b):
        #Make my own counter dictionary and don't 
        #consider the duplicates situation here then 
        #we'll always get only unique values count
        count_a = {}
        for element in a:
            #only add those elements which aren't present in counter already
            if element not in count_a:
                count_a[element] = 1
        #declare empty list to dump output responses
        res = []
        for element in b:
            #if element from b[arr] is present in counter of a[arr] elements
            #add it to the result list
            if count_a.get(element, 0) > 0:
                res.append(element)
                count_a[element] -= 1
        #return the final output list of intersection of elements from both arrays    
        return res