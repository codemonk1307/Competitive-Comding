

"""
Union of Two Sorted Arrays with Distinct Elements -> 
Problem Statement(https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-with-distinct-elements/1)

Given two sorted arrays a[] and b[], where each array contains distinct elements, 
the task is to return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements 
that are present in either of the arrays.

Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7

Input: a[] = [2, 3, 4, 5], b[] = [1, 2, 3, 4]
Output: 1 2 3 4 5
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5

Input: a[] = [1], b[] = [2]
Output: 1 2
Explanation: Distinct elements including both the arrays are: 1 2

Constraints:
1  <=  a.size(), b.size()  <=  105
-109  <=  a[i] , b[i]  <=  109
"""



class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        n1, n2=len(a), len(b)
        i,j=0,0
        ans=[]
        while i<n1 and j<n2:
            if a[i]==b[j]:
                ans.append(a[i])
                i+=1
                j+=1
            elif a[i]<b[j]:
                ans.append(a[i])
                i+=1
            else:
                ans.append(b[j])
                j+=1
        while i<n1:
            ans.append(a[i])
            i+=1
        while j<n2:
            ans.append(b[j])
            j+=1
        return ans