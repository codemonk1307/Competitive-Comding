

'''
1002. Find Common Characters - Problem Statement

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''


from typing import List
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        commonLetters = list(A[0])
        for words in A:
            commonCharCheck = []
            for char in words:
                if char in commonLetters:
                    commonCharCheck.append(char)
                    commonLetters.remove(char)
            commonLetters = commonCharCheck
        return commonLetters