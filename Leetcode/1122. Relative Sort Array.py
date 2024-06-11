


'''
1122. Relative Sort Array => Problem Statement

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]

Constraints:
1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1
'''



from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #Initialize an empty array
        sortedRes = []
        #Iterate over each of the elements present in arr2
        for ele in arr2:
            #Iterate over each of the values of arr1 respective to arr2's elements
            for idx in range(len(arr1)):
                #If value of element of arr1 is equals to the element of arr2 
                if arr1[idx] == ele:
                    #Add it to the result array
                    sortedRes.append(arr1[idx])
                    #Also mark the token up as sign of that particular value of arr1 is visited 
                    arr1[idx] = -1  
        #Sort the array
        arr1.sort()
        #Iterate over the arr1 again to fetch non visited elements
        for ele in arr1:
            if ele != -1:
                #Add the non-visited, unseen elements to the result of sorted array
                sortedRes.append(ele)
        return sortedRes