

# Problem Statement -> https://codeforces.com/problemset/problem/1650/A
# Logic -> if the c - string's char is occuring at even indx in s - string's then conversion possible yes or else not possible no

for _ in range(int(input())):
    
    s = input()
    c = input()
    
    for i in range(len(s)):
        if c == s[i] and i % 2 == 0:
            print("YES")
            break  
    else:
        print("NO")

# Input -                              Output -

# 5
# abcde            s - string
# c                c - string           YES

# abcde
# b                                     NO

# x
# y                                     NO

# aaaaaaaaaaaaaaa
# a                                     YES

# contest
# t                                     YES