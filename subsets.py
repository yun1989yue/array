'''
Given a set of distinct integers, nums, return all possible subsets. 

Note:

•Elements in a subset must be in non-descending order.
•The solution set must not contain duplicate subsets.


For example,
 If nums = [1,2,3], a solution is: 
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''
'''
M1: Iteration O(2**n) time O(2**n) space
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        for i in xrange(len(nums)):
            temp = [] # if temp = res[:], all elems of temp belongs to res too, need to copy every array
            for r in res:
                key = r[:]
                key.append(nums[i]) # key = r[:].append(nums[i]) is wrong, because we will assign r[:] to key before append
                temp.append(key)
            res += temp # not res.append(temp), you wanna add all elems of temp to res, not temp as a whole elem
        return res
        
  '''
  M2: another iteration
  '''
  def subsets(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res] # this is correct, although item belongs res, item+[] is a new array, notice that 
        #item.append() is wrong
    return res
    
'''
M3: bit manipulation
'''
def subsets2(self, nums):
    res = []
    nums.sort()
    for i in xrange(1<<len(nums)):
        tmp = []
        for j in xrange(len(nums)):
            if i & 1 << j:  # 1<<j can detect whether i is 1 at the position j (from right to left) in binary mode, hence this condition
            # can be seen as finding combination of 1s of i, e.g. 6 = 110 -> [2, 1] 9 = 1001 -> [3, 0]
            # since 0 -> 2**n -1 are 2**n different combination of 1 and 0, we can use it to combine 2**n different num combination too
                tmp.append(nums[j])
        res.append(tmp)
    return res
'''
M4: recursion
'''
def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res

def dfs(self, nums, index, path, res):
    res.append(path)
    for i in xrange(index, len(nums)):
        self.dfs(nums, i+1, path+[nums[i]], res)
