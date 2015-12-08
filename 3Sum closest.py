'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dif = float('Inf')
        res = 0
        for i in xrange(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    tempSum = nums[i] + nums[start] + nums[end]
                    if dif > abs(tempSum - target): # update res if smaller difference found
                        dif = abs(tempSum - target)
                        res = tempSum
                    if tempSum > target:
                        end -= 1
                    elif tempSum < target:
                        start += 1
                    else:
                        break
                if dif == 0: # dif >= 0
                    break
        return res
