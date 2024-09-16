

"""
539. Minimum Time Difference -> Problem Statement( https://leetcode.com/problems/minimum-time-difference/ )

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time from "HH:MM" to total minutes
        def time_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        # Convert all time points to minutes
        minutes_list = [time_to_minutes(time) for time in timePoints]
        # Sort the list of minutes
        minutes_list.sort()
        # Initialize the minimum difference as large as possible
        min_diff = float('inf')
        # Compare each consecutive time point in the sorted list
        for i in range(1, len(minutes_list)):
            diff = minutes_list[i] - minutes_list[i - 1]
            min_diff = min(min_diff, diff)
        # Also compare the first and last time points considering the circular clock
        circular_diff = (1440 - minutes_list[-1] + minutes_list[0])
        min_diff = min(min_diff, circular_diff)
        #
        return min_diff