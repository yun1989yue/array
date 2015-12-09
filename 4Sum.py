'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in xrange(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]:
                comb = self.threeSum(nums, target - nums[i], i + 1)
                if comb:
                    for c in comb:
                        c = [nums[i]] + c
                        res.append(c)
        return res
        
    def threeSum(self, nums, target, start):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        for i in xrange(start, len(nums)-2):
            if i == start or nums[i] != nums[i-1]:
                comb = self.helper(nums, i + 1, target - nums[i])
                if comb:
                    for c in comb:
                        c = [nums[i]] + c
                        res.append(c)
        return res
        
    def helper(self, nums, start, target):
        end = len(nums) - 1
        comb = []
        while start < end:
            if nums[start] + nums[end] == target:
                comb.append([nums[start], nums[end]])
                key = nums[start]
                while start < end and nums[start] == key:
                    start += 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                 end -= 1
        return comb
