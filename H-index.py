'''
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index
'''
'''
Math: O(nlogn) time O(1) space
1) Sort the arr
2) Consider the case, 0,...i,...n-1, assume k = N-i（if sort in descending order, just use i）, there are i(N-k) items at left side of i 
and N-i(k) items at right side(include ith item), 
3) if nums[i-1] <= k and nums[]
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        for i in xrange(len(citations)):
            if i == 0:
                if citations[0] >= len(citations):
                    return len(citations)
            else:
                if citations[i - 1] <= len(citations) - i and citations[i] >= len(citations) - i:
                    return len(citations) - i
        return 0
