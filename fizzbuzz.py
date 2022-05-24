class Solution(object):
    def twoSum(self, nums, target):
        numbers = {}
        for i in range(len(nums)):
            if (target-nums[i]) in numbers :
                print [numbers[(target-nums[i])],i]
            else :
                numbers[nums[i]]=i

# EXAMPLE OF RESULT.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].