'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = -1
        right = -1
        start = 0
        end = len(nums) - 1
        while start <= end: # search for the left bound
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                left = mid
                end = mid - 1
            else:
                end = mid - 1
        start = 0
        end = len(nums) - 1
        while start <= end: # search for the right bound
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                right = mid
                start = mid + 1
            else:
                end = mid - 1
        return [left, right]
