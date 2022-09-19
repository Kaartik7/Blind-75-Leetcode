from typing import List
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(0, len(nums)):
            lst.append(nums[nums[i]])
        return lst
