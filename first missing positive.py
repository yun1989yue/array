'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''
'''
put i to nums[i-1] if nums[i-1] != i, return i if nums[i-1] != i
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) + 1 and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                key = nums[i]
                nums[i] = nums[key - 1]
                nums[key - 1] = key
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
