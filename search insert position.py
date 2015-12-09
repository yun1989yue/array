'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''
'''
Brute Force O(n) time O(1) space
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        while res < len(nums) and nums[res] < target:
            res += 1
        return res
'''
binary search O(logn) tiem O(1) space
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end: # find the 1st element >= target, if not, insert at len(nums)
            mid = (end - start) / 2 + start # using this will prevent overflow, suppose start and end will be really large
            if nums[mid] < target:
                start = mid + 1
            else:
                #if end == 0 or nums[end - 1] < target: # check whether it is the 1st element >= target, no need, we just need to find last element < target
                    #return end
                end = mid - 1
        return start
