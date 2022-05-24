class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        #print(candidates)
        ret = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            if candidates[i] == target:
                ret.append([candidates[i]])
            else:
                subs = self.combinationSum(candidates[i:], target - candidates[i])
                if subs:
                    for sub in subs:
                        sub.insert(0, candidates[i])
                        ret.append(sub)
        return ret

# Test case

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
