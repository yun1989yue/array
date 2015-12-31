'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''
'''
In-Place O(mn) time O(1) space
1) if 1 -> 0 assign it as 2
2) if 0 -> 1 assign it as 3
'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return 
        dire = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                tmp = 0
                for d in dire:
                    x = i + d[0]
                    y = j + d[1]
                    if x > -1 and x < m and y > -1 and y < n and (board[x][y] == 1 or board[x][y] == 2):
                        tmp += 1
                if board[i][j] == 1 and (tmp < 2 or tmp > 3):
                    board[i][j] = 2 # if 1 -> 0 in next interval, set it to 2
                elif board[i][j] == 0 and tmp == 3:
                    board[i][j] = 3 # if 0 -> 1 in next interval, set it to 3
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
  '''
  Brute Force O(mn) time O(mn) space
  for each elems, count its live number and update its next value to the res
  '''
