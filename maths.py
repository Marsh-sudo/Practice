class Solution(object):
    def twoSum(self, nums, target):
        numbers = {}
        for i in range(len(nums)):
            if (target-nums[i]) in numbers :
                return [numbers[(target-nums[i])],i]
            else :
                numbers[nums[i]]=i