'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
'''
Method 1: Brute Force O(n^2) time O(1) space
for each number, check following numbers which will add up to target
'''
'''
Method 2: dictionary O(n) time O(n) space
for each number, if it is not in the dic, add it to dic as [target - nums[i], i] pair, else return [dic[nums[i]], i]
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in xrange(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]] + 1, i + 1] # return indices + 1, stupid title
            else:
                dic[target - nums[i]] = i
  '''
  Method 3: two pointers O(nlogn) time O(1) space
  '''
  class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        original = nums[:] # need [:] to copy rather than reference
        nums.sort()
        start = 0
        end = len(nums) - 1
        adder1 = None
        adder2 = None
        while start < end: 
            if nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] == target:
                adder1 = nums[start]
                adder2 = nums[end]
                break
            else:
                 end -= 1
        i1 = -1
        i2 = -1
        if adder1 != adder2:
            for i in xrange(len(original)):
                if original[i] == adder1:
                    i1 = i + 1
                if original[i] == adder2:
                    i2 = i + 1
            return [i1, i2] if i1 < i2 else [i2, i1]
        else: # if adder1 == adder2, then need two different indexes
            for i in xrange(len(original)):
                if i1 == -1 and original[i] == adder1:
                    i1 = i + 1
                if i1 != -1 and original[i] == adder1:
                    i2 = i + 1
            return [i1, i2]
                
