'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''
'''
Method: Binary search O(logN) time O(1) space
'''
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = start + (end - start) / 2 # prevent overflow
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        if isBadVersion(start): # since end = mid - 1, the last start may be true or false
            return start
        else:
            return start + 1
            
'''
Simplify
'''
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = start + (end - start) / 2
            if isBadVersion(mid): # if mid is false, it may be first bad and mid is always smaller than end, so while will end
                end = mid
            else:
                start = mid + 1 # if mid is true, start can not be 1st bad
        return start
