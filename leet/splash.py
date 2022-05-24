from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        z=0
        o=0
        t=0
        for i in nums:
            if i==0:
                z+=1
            elif i==1:
                o+=1
            else:
                t+=1
        o+=z
        t+=o
        for i in range(len(nums)):
            if i<z:
                nums[i]=0
            elif i<o and i>=z:
                nums[i]=1
            elif i<t and i>=o:
                nums[i]=2