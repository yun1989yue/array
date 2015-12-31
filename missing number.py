'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example,
Given nums = [0, 1, 3] return 2.
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
'''
Rearrangement: O(n) time in place O(n) space
1) move number i to index i
2) return i if index i does not store i
* notice that answer will only betwenn 1 and n + 1
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)): # move i to nums[i], every updation means a number is filled to its position, hence O(n) times updation
            while nums[i] != len(nums) and nums[i] != i and nums[nums[i]] != nums[i]: # must make sure nums[i] != len(nums) for every 
            #exchange
                key = nums[i]
                nums[i] = nums[key]
                nums[key] = key
        for i in xrange(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        
'''
bit manipulation: O(n) time O(1) space
1) ^ all numbers from 0 to n
2) ^ all numbers in nums
3) if k is missing, res is k
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums) # if 0 to n - 1 is included or nums is None, ans is n
        for i in xrange(len(nums)): 
            res ^= i
            res ^= nums[i]
        return res

'''
bit manipulation: O(n) time O(1) space
1) sum all numbers from 0 to n
2) minus all numbers in nums
3) if k is missing, res is k
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in xrange(len(nums)):
            res += i
            res -= nums[i]
        return res
        
'''
sort and binary search
'''
