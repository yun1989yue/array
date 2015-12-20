'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
'''
Method: two pointers O(n) time O(1) space
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonzero = -1 # how many nonzero numbers before pointer cur
        cur = 0 # current pointer to be explored
        while cur < len(nums):
            if nums[cur] != 0:
                nonzero += 1
                if cur != nonzero:
                    nums[nonzero] = nums[cur]
                    nums[cur] = 0
            cur += 1
