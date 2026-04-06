class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        for i in range(len(nums)):
            if (target - nums[i]) in (nums[:i] + nums[i+1:]):
                return [i, (nums[:i] + nums[i+1:]).index(target - nums[i])+1]