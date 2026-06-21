class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i,n in enumerate(nums):
            if n not in pairs.keys():
                pairs[target - n] = i
            else:
                return [pairs[n],i]
        