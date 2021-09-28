
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        reqIdx = {}

        for i in range(len(nums)):
            des = target - nums[i]

            if des in reqIdx:
                return [reqIdx[des], i]
            else:
                req[nums[i]] = i 

