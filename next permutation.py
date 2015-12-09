'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
'''
Method: Brute Force O(n) time O(1) space
* consider two cases, with a certain number of digits [1,2,3,1,4,2], the smallest number is acending [1,1,2,2,3,4] and biggest is 
decreasing [4,3,2,2,1,1]
Base on the consideration, find decreasing part from the end(interrupt at index rev), then exchange rev and bigger digits in the decreasing 
part, reverse the decreasing part, we will find the answer
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        rev = len(nums) - 2
        while rev > -1 and nums[rev] >= nums[rev+1]: # rev is then the digit not in decreasing order
            rev -= 1
        if rev == -1: # the number is largest, just reverse it to smallest
            self.reverse(nums, 0, len(nums) - 1)
        else:
            exc = len(nums) - 1
            while nums[exc] <= nums[rev]: # need to find a digit just bigger than nums[rev], can use binary search to reduce running time
                exc -= 1
            key = nums[rev]
            nums[rev] = nums[exc]
            nums[exc] = key
            self.reverse(nums, rev + 1, len(nums) - 1)
        
    def reverse(self, nums, start , end):
        while start < end:
            key = nums[start]
            nums[start] = nums[end]
            nums[end] = key
            start += 1
            end -= 1
