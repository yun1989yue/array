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
        while min(nums) < amount: # it is correct, because if amount is 1st reached, it will be returned as smallest comb, but same value smaller than amount may appear more than once with different numbers comb, e.g. [1,2,5] 5 will appeared twice with comb 1 and 3
            temp = {}
            for n in nums:
                for c in coins:
                    if n + c not in nums:
                        if n + c == amount:
                            return nums[n] + 1
                        elif n + c < amount:
                            temp[n + c] = nums[n] + 1
            nums = temp
        return -1
'''
Improved, BFS O(max(mn, nlogn) time O(m) space)
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount < 0: # boundart cases, 1) coins = [] 2) amount < 0 3) amount = 0
            return -1
        if amount == 0:
            return 0
        coins.sort() 
        used = {} # explored numbers comb with least coins
        level = {} # numbers can be reached by current number of coins
        for c in coins: # base cases
            if c == amount:
                return 1
            elif c < amount:
                used[c] = 1
                level[c] = 1
        times = 1
        while times <= amount/coins[0]: # at most amount/coins[0] can be used to combine amount
            times += 1
            temp = {}
            for l in level:
                for c in coins:
                    if l + c < amount and l+c not in used and l+c not in temp: # find smallest number of coins
                        temp[l+c] = times
                        used[l+c] = times
                    elif l + c == amount:
                        return times
                    elif l + c > amount:
                        break
            level = temp
        return -1
