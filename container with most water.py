'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''
'''
Method: 2 pointers O(n) time O(1) space
* notice that for i and j, if h[i] < h[j] then for all index k between i and j, i and k contain less water than i and j
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxVol = 0
        start = 0
        end = len(height) - 1
        while start < end:
            tempVol = min(height[start], height[end]) * (end - start)
            if maxVol < tempVol:
                maxVol = tempVol
            if height[start] < height[end]:
                start += 1
            else:
                 end -= 1
        return maxVol
