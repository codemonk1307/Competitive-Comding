

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bitFlip = 0 
        while start or goal:
            if start%2 != goal%2: 
                bitFlip += 1
            start, goal = start//2, goal//2
        return bitFlip