'''
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required. 

Example 1:
nums = [1, 3], n = 6
 Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
 Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
 Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
 So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
 Return 2.
 The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
 Return 0.

'''
'''
Idea: Dynamic Programming O(n) time O(1) space
1) start from beginning of nums, each interval makes sure that 1 -> far can be reached
2) for nums[cur], patches and nums before cur reach all numbers from 1 -> far
  if nums[cur] <= far + 1, we can reach all numbers from 1 -> far + nums[cur]
  if not, we need to add patch far + 1 iteratively until nums[cur] is reached
3) each patch is chosen as far + 1, because we need to add patch p <= far + 1 to make sure far + 1 can be reached and p = far + 1 can max
next max value to be reached, hence to minimize patches needed to be added
notice that if nums contains N ones, need O(N) time, if nums is empty, need O(logN) time, patches = 1,2,4,8,16
'''
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        count = 0 # number of patched need to be added
        far = 0 # max value that can be reached with added pathes and nums before current pointer(excluding)
        cur = 0 # current pointer
        while far < n:
            if cur >= len(nums):
                count += 1
                far = 2 * far + 1
            else:
                if nums[cur] <= far + 1:
                    far += nums[cur]
                    cur += 1
                else:
                    count += 1
                    far += far + 1
        return count
