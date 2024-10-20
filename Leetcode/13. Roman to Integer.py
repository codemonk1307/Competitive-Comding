


class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        n = len(s)
        result = roman[s[n - 1]]
        for i in range(n - 1, 0, -1):
            current_index = roman[s[i]]
            previous = roman[s[i - 1]]
            if previous >= current_index:
                result += previous 
            else:
                result -= previous 
        return result