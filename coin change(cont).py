'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''
'''
Dictionary: O(mn) time O(m) space, m is amount, n is len(coins)
TLE!!!
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        if amount == 0:
            return 0
        nums = {} # least number of coins needed for possible amounts
        for c in coins:
            nums[c] = 1
        for i in xrange(min(coins) + 1, amount + 1): # min(coins) is smallest coin face in array coins
            if i not in nums:
                temp = i / min(coins) + 1
                for c in coins:
                    if c < i and i - c in nums:
                        temp = min(temp, nums[i-c] + 1)
                nums[i] = temp
        if amount in nums:
            return nums[amount]
        else:
            return -1
'''
bfs: o(mn) time O(n) space, while both time and space are less than dictionary
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        nums = {}
        for c in coins:
            nums[c] = 1
        while min(nums) < amount:
            temp = {}
            for n in nums:
                for c in coins:
                    if n + c not in nums:
                        if n + c == amount:
                            return nums[n] + 1
                        temp[n + c] = nums[n] + 1
            nums = temp
        return -1
