'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start = 0
        end = len(nums)-1
        while start <= end:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            if nums[start] < nums[end]: # if subarray is increasing, do binary search
                while start <= end:
                    mid = (end - start) / 2 + start
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        end = mid - 1
                    else:
                        start = mid + 1
                return -1
            mid = (end - start) / 2 + start
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] > nums[start]:
                    if nums[start] > target:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    end = mid - 1
            else:
                if nums[end] > nums[mid]:
                    if nums[end] > target:
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    start = mid + 1
        return -1
                    
