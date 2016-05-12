'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the 
order red, white and blue. 

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively. 

Note:
 You are not suppose to use the library's sort function for this problem

'''

'''
M1: O(n) time O(1) space
1) three ptrs, zero means all nums before zero ptr are zeros, two means all nums after two are twos 
2) ptr start traverses from left to right, it exchange with zero ptr or two ptr if 0 or 2 find and they are not overlap
3) ptr start moves on if overlapped or 1 found
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        zero = -1
        two = len(nums)
        start = 0
        while start < two: # not <=, because if start reach two, we end the loop
            if nums[start] == 0:
                zero += 1
                if zero != start:
                    nums[start] = nums[zero]
                    nums[zero] = 0
                else:
                    start += 1
            elif nums[start] == 2:
                two -= 1
                if two != start:
                    nums[start] = nums[two]
                    nums[two] = 2
                else:
                    start += 1
            else:
                start += 1
