

'''
Union of Arrays with Duplicates -> Problem Statement( https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1 )


Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

The Union of the two arrays can be defined as the set containing distinct elements from both arrays. 
If there are repetitions, then only one element occurrence should be there in the union.

Note: Elements of a[] and b[] are not necessarily distinct.


Examples
Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3]
Output: 5
Explanation: Union set of both the arrays will be 1, 2, 3, 4 and 5. So count is 5.

Input: a[] = [85, 25, 1, 32, 54, 6], b[] = [85, 2] 
Output: 7
Explanation: Union set of both the arrays will be 85, 25, 1, 32, 54, 6, and 2. So count is 7.

Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
Output: 2
Explanation: We need to consider only distinct. So count of elements in union set will be 2.


Constraints:
1 ≤ a.size(), b.size() ≤ 106
0 ≤ a[i], b[i] ≤ 105
'''


class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        #Counter for counting each distinct element in array[a]
        count_a = {}
        unionCount = 0
        for element in a:
            if element not in count_a:
                count_a[element] = 1
                unionCount += 1
        #Counter for counting each distinct element in array[b]
        count_b = {}
        for element in b:
            if element not in count_b:
                count_b[element] = 1
                if element not in count_a:
                    unionCount += 1
        #Return the count of the total number of elements present in the union of both arrays        
        return unionCount