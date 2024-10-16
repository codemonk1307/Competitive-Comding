

"""
Two Swaps -> Problem Statement( https://www.geeksforgeeks.org/problems/two-swaps--155623/1 )

Given a permutation of some of the first natural numbers in an array arr[], determine if the 
array can be sorted in exactly two swaps. A swap can involve the same pair of indices twice.

Return true if it is possible to sort the array with exactly two swaps, otherwise return false.

Examples:

Input: arr = [4, 3, 2, 1]
Output: true
Explanation: First, swap arr[0] and arr[3]. The array becomes [1, 3, 2, 4]. 
Then, swap arr[1] and arr[2]. The array becomes [1, 2, 3, 4], which is sorted.

Input: arr = [4, 3, 1, 2]
Output: false
Explanation: It is not possible to sort the array with exactly two swaps.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ arr.size()
"""


class Solution:

    def checkSorted(self, arr):
        #code here
        n = len(arr)
        ans = sorted(arr)
        i = 1
        cnt = 0
        if arr == ans:
            return True
        while i<=n and cnt <= 2:
            if i != arr[i-1]:
                in1 = arr[i-1]-1
                arr[i-1],arr[in1] = arr[in1],arr[i-1]
                cnt += 1
            i += 1
            if arr[:] == ans[:] and cnt == 2:
                return True      
        if arr == ans and cnt == 2:
                return True
        else:
            return False
