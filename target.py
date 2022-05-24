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