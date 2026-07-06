# Problem 1: Rotting Oranges(https://leetcode.com/problems/rotting-oranges)
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)
# Approach:
# First we scan the whole grid once to collect all rotten oranges into a queue and count how many fresh oranges exist.
# Then we do BFS minute by minute. In each minute we only process the oranges that were rotten at the start of that minute and rot their fresh neighbors, adding them to the queue for the next minute.
# If the fresh count reaches zero we return the current time right away. If the queue empties out before that happens, some oranges were unreachable, so we return minus one.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # these are the four possible moves from any cell, up down right left, used to check all four neighbors without writing four separate conditions
        self.directions = [[-1,0],[1,0],[0,1],[0,-1]]

        
        self.m = len(grid)          # m is the number of rows in the grid    
        self.n = len(grid[0])       # n is the number of columns in the grid
   
        queue = []      # queue will hold the positions of rotten oranges that still need to spread their rot   
        fresh = 0       # fresh keeps a running count of how many fresh oranges are still left in the grid

        # this loop goes through every single cell in the grid exactly once
        for i in range(self.m):
            for j in range(self.n):
                # if this cell is rotten, we add its position to the queue since it will spread rot from here
                if grid[i][j] == 2:
                    queue.append((i, j))
                # if this cell is fresh, we simply increase our fresh counter
                if grid[i][j] == 1:
                    fresh += 1

        # time tracks how many minutes have passed
        time = 0
        # if there were no fresh oranges to begin with, no rotting needs to happen, so we return zero right away
        if fresh == 0:
            return time

        # this loop keeps running as long as there are rotten oranges waiting to spread their rot
        while queue:
            # size captures exactly how many rotten oranges are in the queue at the start of this minute
            # this is important because it tells us where one minute ends and the next minute begins
            size = len(queue)
            # one full minute is about to pass for all these oranges together, so we increase time now
            time += 1

            # we only loop size times so we only process oranges that belong to this exact minute, not oranges added during this same minute
            for i in range(size):
                # we take the orange that has been waiting the longest, since we want first in first out order
                current = queue.pop(0)

                # we check all four neighbors of this rotten orange one by one
                for dir in self.directions:
                    # row is the neighbor's row, found by adding the row change to the current row
                    row = current[0] + dir[0]
                    # column is the neighbor's column, found by adding the column change to the current column
                    column = current[1] + dir[1]

                    # we only continue if the neighbor is inside the grid boundaries and the neighbor is currently a fresh orange
                    if row >= 0 and column >= 0 and row < self.m and column < self.n and grid[row][column] == 1:
                        # we mark this neighbor as rotten directly on the grid so it is never processed again
                        grid[row][column] = 2
                        # we add this newly rotten orange to the queue so it can spread rot in the next minute
                        queue.append((row, column))
                        # one less fresh orange remains now
                        fresh -= 1
                        # if there are no fresh oranges left at all, we are done, so we return the current time immediately
                        if fresh == 0:
                            return time

        # if we reach here, the queue became empty but some fresh oranges never got rotten, meaning they were unreachable
        return -1
