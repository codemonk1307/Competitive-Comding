

"""
Find position of set bit -> Problem Statement( https://www.geeksforgeeks.org/problems/find-position-of-set-bit3706/1 )

Given a number N having only one ‘1’ and all other ’0’s in its binary representation, 
find position of the only set bit. If there are 0 or more than 1 set bit the answer should be -1.
Position of  set bit '1' should be counted starting with 1 from LSB side in binary representation of the number.

Example 1:
Input:
N = 2
Output:
2
Explanation:
2 is represented as "10" in Binary.
As we see there's only one set bit
and it's in Position 2 and thus the
Output 2.

Example 2:
Input:
N = 5
Output:
-1
Explanation:
5 is represented as "101" in Binary.
As we see there's two set bits
and thus the Output -1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function 
findPosition() which takes an integer N as input and returns the answer.

Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)

Constraints:
0 <= N <= 108
"""


class Solution:
    def findPosition(self, n):
        binary = ""
        while n != 0:
            rem = n % 2
            #store the binary representation  in it's reverse order
            binary += str(rem)  
            n = n // 2
        count = 0
        for i in binary:
            #count the occurence of set bit '1'
            if i == '1':         
                count += 1
                #mark the index based on '1' index
                index_set_bit = binary.index(i) + 1  
        #if only one set bit 
        if count == 1:        
            #return it's index from LSB side
            return (index_set_bit)      
        #if more than one set bit occurs
        else:            
            return("-1")