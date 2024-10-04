

"""
2491. Divide Players Into Teams of Equal Skill -> Problem Statement (https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/)

You are given a positive integer array skill of even length n where skill[i] denotes the skill of the
ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players 
into teams such that the total skill of each team is equal.

Example 1:
Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

Example 2:
Input: skill = [3,4]
Output: 12
Explanation: 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.

Example 3:
Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.

Constraints:
2 <= skill.length <= 105
skill.length is even.
1 <= skill[i] <= 100
"""


from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Sort the array first
        skill.sort()
        # Total number of players
        n = len(skill)
        # Calculate the total skill sum
        total_skill_sum = sum(skill)
        # Check if the sum is divisible by n // 2 (number of teams)
        expected_team_skill = total_skill_sum // (n // 2)
        
        # If the total skill sum is not divisible, return -1
        if total_skill_sum % (n // 2) != 0:
            return -1
        
        total_chemistry = 0
        # Now, try to form teams by pairing smallest and largest values
        left, right = 0, n - 1
        
        while left < right:
            # The sum of current pair
            current_sum = skill[left] + skill[right]
            # If the sum of the current pair doesn't match the expected team skill, return -1
            if current_sum != expected_team_skill:
                return -1          
            # Calculate the chemistry (product of the skills)
            total_chemistry += skill[left] * skill[right]
            # Move to the next pair
            left += 1
            right -= 1
        
        return total_chemistry