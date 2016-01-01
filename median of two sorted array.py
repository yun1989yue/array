'''
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''
'''
Binary search O(log(min(m,n))) time O(1) space
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return self.median(nums2)
        elif n == 0:
            return self.median(nums1)
        elif m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        res = 0
        left = 0
        right = len(nums1)
        while left <= right: 
        '''
        if nums1, nums2, i and j satisfies:
          1) i + j = (m+n) / 2( i + j <= m + n - i - j)
          2) nums1[i-1] < nums2[j]
          3) nums2[j-1] < nums1[i]
          then we found the median
        notice that 
          1) if A[i-1] > B[j], for all i0 > i, A[i0-1] > A[i-1]>B[j]>B[j0]
          2) if B[j-1] > A[i], for all i0 < i, B[j0-1] > B[j-1]>A[i]>A[i0]
        '''
            i = (left + right) / 2
            j = (m+n)/2 - i
            if (i == 0 or nums1[i-1] <= nums2[j] or j == n) & (i == m or nums2[j-1] <= nums1[i] or j == 0): # i == m means left part has m elems, not m - 1
            # consider boundary cases: i == 0, i == m, j == 0, j == n
            # the basic if condition is:
            # if A and B:
              elif A:
              elif B:
              else:
                if m + n == 2*(i + j) + 1:
                    if i == m:
                        return nums2[j]*1.0
                    elif j == n:
                        return nums1[i]*1.0
                    else:
                        return min(nums1[i], nums2[j])*1.0
                else:
                    if i == 0:
                        left = nums2[j-1]
                    elif j == 0:
                        left = nums1[i-1]
                    else:
                        left = max(nums1[i-1], nums2[j-1])
                    if i == m:
                        right = nums2[j]
                    elif j == n:
                        right = nums1[i]
                    else:
                        right = min(nums1[i], nums2[j])
                    return (left+right)*1.0/2 # need to multiple 1.0 1st, else, it will be rounded before changed to float
            elif i == 0 or nums1[i-1] <= nums2[j] or j == n: # if this statement is satisfied, condition 3 is violated
                left = i + 1
            else:
                right = i - 1
                    
    def median(self, nums):
        if len(nums) % 2 == 1:
            return nums[len(nums)/2]*1.0
        else:
            return (nums[len(nums)/2] + nums[len(nums)/2-1])*1.0/2
