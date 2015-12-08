'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''
'''
Method: two pointers O(n^2) time O(n) space for comb
for each DISTINCT number, find all the pairs of numbers add up to -nums[i]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in xrange(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]: # only find for distinct numbers
                comb = self.helper(nums, i + 1, -nums[i])
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
                while start < end and nums[start] == key: # avoid repeating
                    start += 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                 end -= 1
        return comb
