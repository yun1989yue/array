'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''
'''
Math: O(n) time O(1) space
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        res.append(1)
        for i in xrange(1, len(nums)): # res[i] = nums[i-1]*nums[i-2]...*nums[0]
            key = nums[i-1]*res[i-1]
            res.append(key)
        right = 1
        for i in xrange(len(nums)-2, -1, -1): # multiple nums[i+1]*..nums[-1] to nums[i]
            right *= nums[i+1]
            res[i] *= right
        return res
