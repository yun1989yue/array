'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
'''
two pointers O(n) time O(1) space
'''
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        start = 0
        end = len(nums) - 1
        while start != end:
            if nums[start] != val:
                start += 1
            else:
                nums[start] = nums[end]
                end -= 1
        if nums[start] == val: # at the end of the exchange, need to check whether val is exchanged
            return start
        else:
            return start + 1
