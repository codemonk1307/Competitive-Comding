

'''
Count distinct elements in every window -> 
Problem Statement(https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1)


Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.


Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output:  [3, 4, 4, 3]

Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.

Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]

Explanation: Window 1 of size k = 2 is 4 1. Number of distinct elements in this window are 2. 
Window 2 of size k = 2 is 1 1. Number of distinct elements in this window is 1. 


Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]


Constraints:
1 <= k <= arr.size() <= 105
1 <= arr[i] <= 105
'''



class Solution:
    def countDistinct(self, arr, k):
        # Code here
        start = 0
        end = 0
        n = len(arr)
        mp = {}
        res = []
        while end < n:
            mp[arr[end]] = mp.get(arr[end], 0) + 1
            if ((end - start) + 1) == k:
                res.append(len(mp.keys()))
                mp[arr[start]] -= 1
                if mp[arr[start]] <= 0:
                    del mp[arr[start]]
                start += 1
            end += 1
        return res